# 科研与学习 Codex Skills

本仓库收录六个作者自建的 Codex skills，覆盖课程学习、文献解析、文献总结、精读和知识同步。仓库只包含技能说明与配套脚本，不包含论文、PDF、Zotero 导出或 Obsidian 笔记。

| Skill | 用途 |
| --- | --- |
| `course-learning` | 整理课程资料，保存带来源定位的学习笔记与可检查练习。 |
| `paper-ingestion` | 使用 MinerU 解析论文，完成独立逐页复核后归档全文。 |
| `paper-parse-review` | 对照原 PDF 复核 MinerU 文字、图表与公式，记录校验结果。准确的图片和 Obsidian Markdown 表格/公式保持原样；仅在发现问题时修正。 |
| `literature-summary` | 为单篇论文生成简洁、可追溯的中文总结。 |
| `paper-deep-reading` | 分析单篇核心论文的论证、方法、证据、局限和研究启发。 |
| `knowledge-sync` | 将有长期价值的课程、文献或项目知识增量写入知识库。 |

## 安装

将需要的整个 skill 文件夹复制到 Codex skills 目录，并保留 `SKILL.md`、`agents/`、`references/` 和 `scripts/` 等配套文件。复制后刷新 Codex，使其重新加载技能。

需要访问 Obsidian 的流程应使用用户指定或当前环境唯一识别的 Vault，并遵循该 Vault 自身的说明和模板。论文解析与复核以原 PDF 为事实依据；表格和公式以 Markdown/LaTeX 表达，只有内容有误或格式不适用时才修改。图像内容准确时保留原图；仅当图像缺失、残缺、错误或无法使用时才从 PDF 裁切替换。

## 依赖与边界

- `paper-ingestion` 依赖 MinerU 与 `$paper-parse-review`。
- `literature-summary` 和 `paper-deep-reading` 可通过 Zotero 定位书目信息与 PDF，也可以使用用户提供的本地 PDF。
- 每个 skill 只处理用户明确提供或选定的资料；不会自动上传原文、批量复制资料或覆盖已有笔记。
