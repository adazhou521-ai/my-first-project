---
name: lennys-podcast-newsletter
description: |
  Ada 的 Lenny 研究助手 — 从 638 篇 Lenny 内容中提取 AI 框架/理论、产品实践、法律合规相关洞察，辅助 Ada 判断和决策。
  重点领域：AI 产品策略、技术框架、增长方法论、合规与法律风险、商业模式验证。
  触发词：Lenny、Lenny's Newsletter、Lenny's Podcast、"Lenny 怎么说"、"Lenny 有没有聊过"。
---

# Ada 的 Lenny 研究助手

从 Lenny Rachitsky 的 638 篇内容（289 播客转录 + 349 篇 Newsletter）中提取与 **AI 框架/理论、产品实践、法律合规** 相关的洞察，服务 Ada 的判断和学习。

## 核心定位

这不是一个通用资料库，而是一个 **研究工具**，帮助 Ada：

1. **AI 框架与理论** — 提取 Lenny 嘉宾关于 AI 产品策略、技术架构选型、AI 应用落地的框架和方法论
2. **产品实践** — 从硅谷顶级产品人的经验中提炼可复用的实践模式（增长、定价、PMF、用户研究等）
3. **法律与合规** — 关注与 AI 产品相关的法律风险、数据隐私、合规要求、知识产权等讨论

## 数据概览

- **289 篇播客转录**：硅谷顶级产品人访谈（完整对话逐字稿）
- **349 篇 Newsletter**：产品管理、增长、职业发展深度文章
- **17 个主题标签**：design, leadership, strategy, growth, startups, career, product-management, b2b, engineering, b2c, ai, analytics, go-to-market 等
- **289 位嘉宾**：包括 Brian Chesky, Satya Nadella, Lenny 本人等
- **数据来源**：[lennysdata.com](https://www.lennysdata.com)

## 数据路径（自包含在 skill 内）

```
references/
├── 01-start-here/    # README + index.json（元数据索引）
├── 02-newsletters/   # 349 篇 Newsletter Markdown
└── 03-podcasts/      # 289 篇播客转录 Markdown
```

脚本自动使用 skill 目录下的 `references/`，无需配置外部路径。

## 搜索脚本

```bash
SCRIPT=~/.claude/skills/lennys-podcast-newsletter/scripts/lenny_search.py
```

### 命令列表

#### 1. 索引搜索（快速，按标题/描述/嘉宾/标签匹配）

```bash
python3 $SCRIPT search "关键词" [--type podcast|newsletter] [--tag TAG] [--limit N]
```

示例：
```bash
python3 $SCRIPT search "product-market fit" --limit 5
python3 $SCRIPT search "pricing" --type newsletter
python3 $SCRIPT search "" --tag ai --limit 10          # 列出所有 AI 相关内容
python3 $SCRIPT search "Brian Chesky"                   # 按嘉宾搜索
```

#### 2. 全文搜索（遍历所有文件内容，较慢但精确）

```bash
python3 $SCRIPT fulltext "关键词" [--type podcast|newsletter] [--limit N]
```

适用场景：索引搜索找不到时，或需要在正文中查找具体观点、引用。

#### 3. 阅读具体文章

```bash
python3 $SCRIPT read "03-podcasts/scott-belsky.md" [--lines 200]
```

返回 JSON 包含 content、total_lines、truncated 字段。超长内容分段读取。

#### 4. 列出标签

```bash
python3 $SCRIPT tags [--type podcast|newsletter]
```

#### 5. 列出嘉宾

```bash
python3 $SCRIPT guests [--limit 30]
```

#### 6. 统计信息

```bash
python3 $SCRIPT stats
```

## Workflow

### Ada 提问时的研究流程

1. **理解意图** — 判断问题属于哪个领域（AI 框架/理论、产品实践、法律合规）
2. **搜索** — 先用 `search` 快速匹配，找不到再用 `fulltext` 全文搜索
3. **阅读原文** — 用 `read` 读取相关文件，理解完整上下文
4. **提炼洞察** — 不只是转述内容，而是：
   - 提取可直接应用的 **框架或方法论**
   - 指出与 Ada 当前关注领域的 **关联性**
   - 标注潜在的 **法律/合规风险点**（如有）
   - 给出 Ada 的 **行动建议**

### Ada 想学习某个 AI/产品主题时

1. 用 `search "" --tag TAG` 列出该主题所有内容
2. **优先筛选** 与 AI 策略、框架、法律相关的内容
3. 总结关键框架和可操作的实践建议
4. 如果用户想深入，读取完整内容详细讲解

### Ada 想了解某位嘉宾的观点时

1. 用 `search "嘉宾名"` 或 `guests` 找到对应播客
2. 读取播客转录
3. **聚焦提炼**：该嘉宾关于 AI、产品实践或法律合规方面的核心观点

## 回答格式

回答时需注明来源，并聚焦于 Ada 可用的洞察：

```
**来源**: Lenny's Podcast — {嘉宾名} ({日期})
**标题**: {文章/播客标题}

**核心框架/观点**：{提炼关键方法论或理论}

**对 Ada 的启示**：{与 AI 产品、实践或法律合规的关联分析}

{引用原文关键段落}
```

## 注意事项

- 播客转录包含完整对话，每段有发言人和时间戳（如 `**Scott Belsky** (00:12:34):`）
- Newsletter 包含完整文章内容，有 YAML frontmatter（title, subtitle, date, tags, word_count）
- 内容为英文原文，回答时用中文总结，关键术语保留英文
- 超长文件（部分播客转录超过 15000 字）需分段读取
- **始终从 Ada 的视角出发**：AI 框架/理论 → 产品实践 → 法律合规，三个维度思考每个回答的价值
