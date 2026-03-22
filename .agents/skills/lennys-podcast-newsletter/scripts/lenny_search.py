#!/usr/bin/env python3
"""Search Lenny's Newsletter & Podcast archive by keyword, tag, guest, or date range."""

import json
import sys
import os
import re
from pathlib import Path

# Auto-detect: use skill's bundled references/ directory
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(SKILL_DIR, "references")
INDEX_FILE = os.path.join(DATA_DIR, "01-start-here/index.json")


def load_index():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def search_index(query, content_type=None, tag=None, limit=10):
    """Search index by keyword in title/description/guest, optionally filter by type and tag."""
    index = load_index()
    results = []

    sources = []
    if content_type in (None, "podcast"):
        sources.extend([(item, "podcast") for item in index.get("podcasts", [])])
    if content_type in (None, "newsletter"):
        sources.extend([(item, "newsletter") for item in index.get("newsletters", [])])

    query_lower = query.lower() if query else ""

    for item, item_type in sources:
        # Tag filter
        if tag and tag.lower() not in [t.lower() for t in item.get("tags", [])]:
            continue

        # Keyword search in title, description, guest
        if query_lower:
            searchable = " ".join([
                item.get("title", ""),
                item.get("description", ""),
                item.get("guest", ""),
                " ".join(item.get("tags", []))
            ]).lower()
            if query_lower not in searchable:
                continue

        results.append({**item, "type": item_type})

    # Sort by date descending
    results.sort(key=lambda x: x.get("date", ""), reverse=True)
    return results[:limit]


def list_tags(content_type=None):
    """List all unique tags with counts."""
    index = load_index()
    tag_counts = {}

    sources = []
    if content_type in (None, "podcast"):
        sources.extend(index.get("podcasts", []))
    if content_type in (None, "newsletter"):
        sources.extend(index.get("newsletters", []))

    for item in sources:
        for tag in item.get("tags", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    return sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)


def list_guests(limit=30):
    """List podcast guests."""
    index = load_index()
    guests = []
    for item in index.get("podcasts", []):
        guest = item.get("guest", "")
        if guest:
            guests.append({"guest": guest, "title": item.get("title", ""), "date": item.get("date", ""), "filename": item.get("filename", "")})
    guests.sort(key=lambda x: x.get("date", ""), reverse=True)
    return guests[:limit]


def read_content(filename, max_lines=200):
    """Read a specific file's content."""
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return {"error": f"File not found: {filename}"}

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total = len(lines)
    content = "".join(lines[:max_lines])
    truncated = total > max_lines

    return {
        "content": content,
        "total_lines": total,
        "truncated": truncated,
        "filename": filename
    }


def fulltext_search(query, content_type=None, limit=5):
    """Full-text search across all markdown files."""
    results = []
    query_lower = query.lower()

    search_dirs = []
    if content_type in (None, "podcast"):
        search_dirs.append(os.path.join(DATA_DIR, "03-podcasts"))
    if content_type in (None, "newsletter"):
        search_dirs.append(os.path.join(DATA_DIR, "02-newsletters"))

    for search_dir in search_dirs:
        if not os.path.exists(search_dir):
            continue
        for fname in os.listdir(search_dir):
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(search_dir, fname)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if query_lower in content.lower():
                # Extract title from frontmatter
                title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else fname

                # Find matching context
                lines = content.split("\n")
                snippets = []
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        start = max(0, i - 1)
                        end = min(len(lines), i + 2)
                        snippet = "\n".join(lines[start:end]).strip()
                        snippets.append(snippet)
                        if len(snippets) >= 2:
                            break

                rel_path = os.path.relpath(filepath, DATA_DIR)
                item_type = "podcast" if "03-podcasts" in rel_path else "newsletter"
                results.append({
                    "title": title,
                    "filename": rel_path,
                    "type": item_type,
                    "snippets": snippets
                })

                if len(results) >= limit:
                    break
        if len(results) >= limit:
            break

    return results


def print_help():
    print("""Usage: lenny_search.py <command> [options]

Commands:
  search <query> [--type podcast|newsletter] [--tag TAG] [--limit N]
      Search by keyword in title/description/guest/tags

  fulltext <query> [--type podcast|newsletter] [--limit N]
      Full-text search across all content

  read <filename> [--lines N]
      Read a specific file (e.g., 03-podcasts/scott-belsky.md)

  tags [--type podcast|newsletter]
      List all tags with counts

  guests [--limit N]
      List podcast guests

  stats
      Show archive statistics
""")


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    cmd = sys.argv[1]

    # Parse flags
    args = sys.argv[2:]
    flags = {}
    positional = []
    i = 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                flags[key] = args[i + 1]
                i += 2
            else:
                flags[key] = True
                i += 1
        else:
            positional.append(args[i])
            i += 1

    if cmd == "search":
        query = " ".join(positional) if positional else ""
        results = search_index(
            query,
            content_type=flags.get("type"),
            tag=flags.get("tag"),
            limit=int(flags.get("limit", 10))
        )
        print(json.dumps(results, ensure_ascii=False, indent=2))

    elif cmd == "fulltext":
        query = " ".join(positional)
        if not query:
            print("Error: fulltext requires a search query", file=sys.stderr)
            sys.exit(1)
        results = fulltext_search(
            query,
            content_type=flags.get("type"),
            limit=int(flags.get("limit", 5))
        )
        print(json.dumps(results, ensure_ascii=False, indent=2))

    elif cmd == "read":
        filename = " ".join(positional)
        if not filename:
            print("Error: read requires a filename", file=sys.stderr)
            sys.exit(1)
        result = read_content(filename, max_lines=int(flags.get("lines", 200)))
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif cmd == "tags":
        tags = list_tags(content_type=flags.get("type"))
        for tag, count in tags:
            print(f"  {tag}: {count}")

    elif cmd == "guests":
        guests = list_guests(limit=int(flags.get("limit", 30)))
        for g in guests:
            print(f"  [{g['date']}] {g['guest']} — {g['title']}")

    elif cmd == "stats":
        index = load_index()
        podcasts = index.get("podcasts", [])
        newsletters = index.get("newsletters", [])
        print(f"Podcasts: {len(podcasts)}")
        print(f"Newsletters: {len(newsletters)}")
        print(f"Total: {len(podcasts) + len(newsletters)}")
        all_tags = set()
        for item in podcasts + newsletters:
            all_tags.update(item.get("tags", []))
        print(f"Unique tags: {len(all_tags)}")
        all_guests = set(item.get("guest", "") for item in podcasts if item.get("guest"))
        print(f"Unique guests: {len(all_guests)}")

    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
