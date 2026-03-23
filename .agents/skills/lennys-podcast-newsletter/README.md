# lennys-podcast-newsletter

> Ada 的 Lenny 研究助手 — 从 638 篇 Lenny 内容中提取 AI 框架/理论、产品实践、法律合规洞察

> Lenny research skill for Ada — Extract AI frameworks, product practices, and legal insights from 638 Lenny articles

**[English](#english) | [中文](#中文)**

---

<a name="english"></a>
## English

### What This Does

A research skill that helps Ada extract actionable insights from Lenny Rachitsky's content archive, focused on **AI frameworks/theories, product practices, and legal/compliance topics**. Claude searches through 289 podcast transcripts and 349 newsletter articles, then synthesizes findings from Ada's perspective.

### Content Overview

| Content | Count | Format |
|---------|-------|--------|
| Podcast transcripts | 289 | Full conversation with speaker names & timestamps |
| Newsletter articles | 349 | Complete articles with frontmatter metadata |
| Topic tags | 17 | design, leadership, strategy, growth, ai, startups, etc. |
| Unique guests | 289 | Brian Chesky, Satya Nadella, and many more |

### Prerequisites

- [ ] [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- [ ] Python 3.8+ (built-in on macOS)
- [ ] Lenny's data archive (from [lennysdata.com](https://www.lennysdata.com) paid subscription)
  - Place the extracted data at: `~/乔木新知识库/20-29 学习/23 播客转录/lennys-data/`
  - Or modify the `DATA_DIR` path in `scripts/lenny_search.py`

### Installation

```bash
npx skills add joeseesun/lennys-podcast-newsletter
```

Verify:
```bash
ls ~/.claude/skills/lennys-podcast-newsletter/SKILL.md
```

### Usage

Just ask Claude naturally:

- "Lenny 有没有聊过 product-market fit？"
- "Lenny's podcast about pricing strategy"
- "What did Brian Chesky say on Lenny's podcast?"
- "Summarize Lenny's newsletters about growth"
- "Search Lenny for AI product management"

### Search Commands (used by Claude internally)

| Command | Description |
|---------|-------------|
| `search <query>` | Fast index search by title/description/guest/tags |
| `fulltext <query>` | Deep full-text search across all content |
| `read <filename>` | Read specific article or transcript |
| `tags` | List all topic tags with counts |
| `guests` | List podcast guests |
| `stats` | Show archive statistics |

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "File not found" errors | Check data path in `scripts/lenny_search.py`, update `DATA_DIR` |
| Search returns empty | Try `fulltext` instead of `search` for exact phrases |
| Content too long | Script auto-truncates at 200 lines, use `--lines N` for more |

### Credits

- [Lenny Rachitsky](https://www.lennysnewsletter.com/) — Original content creator
- [lennysdata.com](https://www.lennysdata.com) — Data archive for paid subscribers

---

<a name="中文"></a>
## 中文

### 功能

Ada 的 Lenny 研究助手 — 从 638 篇 Lenny 内容中提取与 **AI 框架/理论、产品实践、法律合规** 相关的洞察，辅助 Ada 的判断和学习。不是通用资料库，而是聚焦于 AI 产品策略、方法论和法律风险的研究工具。

### 内容概览

| 内容类型 | 数量 | 格式 |
|---------|------|------|
| 播客转录 | 289 篇 | 完整对话逐字稿（含发言人和时间戳） |
| Newsletter 文章 | 349 篇 | 完整文章（含 YAML frontmatter 元数据） |
| 主题标签 | 17 个 | design, leadership, strategy, growth, ai, startups 等 |
| 独立嘉宾 | 289 位 | Brian Chesky, Satya Nadella 等 |

### 前置条件

- [ ] 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [ ] Python 3.8+（macOS 自带）
- [ ] Lenny 数据存档（来自 [lennysdata.com](https://www.lennysdata.com) 付费订阅）
  - 将解压的数据放在：`~/乔木新知识库/20-29 学习/23 播客转录/lennys-data/`
  - 或修改 `scripts/lenny_search.py` 中的 `DATA_DIR` 路径

### 安装

```bash
npx skills add joeseesun/lennys-podcast-newsletter
```

验证：
```bash
ls ~/.claude/skills/lennys-podcast-newsletter/SKILL.md
```

### 使用示例

直接用自然语言问 Claude：

- "Lenny 有没有聊过 product-market fit？"
- "Lenny 播客里谁讲过定价策略？"
- "Brian Chesky 在 Lenny 播客上说了什么？"
- "总结一下 Lenny 关于增长的 Newsletter"
- "搜一下 Lenny 关于 AI 产品管理的内容"

### 常见问题

| 问题 | 解决方法 |
|------|----------|
| 文件找不到 | 检查 `scripts/lenny_search.py` 中的 `DATA_DIR` 路径是否正确 |
| 搜索结果为空 | 索引搜索找不到时会自动降级到全文搜索 |
| 内容太长 | 脚本默认截取前 200 行，可用 `--lines N` 读取更多 |

### 致谢

- [Lenny Rachitsky](https://www.lennysnewsletter.com/) — 原始内容创作者
- [lennysdata.com](https://www.lennysdata.com) — 付费订阅者数据存档

---

## 关注作者

- **X (Twitter)**: [@vista8](https://x.com/vista8)
- **微信公众号「向阳乔木推荐看」**

<p align="center">
  <img src="https://github.com/joeseesun/terminal-boost/raw/main/assets/wechat-qr.jpg?raw=true" alt="向阳乔木推荐看公众号二维码" width="300">
</p>
