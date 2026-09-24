# 科研学习与文献笔记 Codex Skills

这个仓库收录四个个人 Codex skill：课程学习入库、文献总结、文献精读、知识库同步。它们将来源、证据定位和分析边界写入 Obsidian 笔记。截图中的「通用文献下载与全文读取」不在本仓库中。

## 安装

将需要的整个 skill 文件夹复制到 Codex 的个人 skills 目录（通常是 `~/.codex/skills/`），保持 `SKILL.md`、`agents/`、`references/`、`scripts/` 的相对位置。重新启动或刷新 Codex 后，在对话中使用下表的调用名。只复制 `SKILL.md` 会使文献 skill 缺少模板与校验脚本。

这四个 skill 不包含论文、PDF、Zotero 库或 Obsidian 笔记。使用前提供资料路径或明确的文献标识，并给出 Obsidian Vault 的绝对路径（Vault 根目录含 `.obsidian`）；若当前路径能够唯一定位 Vault，skill 会尝试自动发现。Vault 内的 `AGENTS.md` 和模板决定实际写入约定。默认文献目录为所选 Vault 下的 `20_文献`，可以在请求中指定其他目录。

| Skill | 主要用途 | 需要的输入 | 产出 |
| --- | --- | --- | --- |
| [`course-learning`](course-learning/SKILL.md) | 整理课程材料、回答课程问题、记录可验证的学习进展 | 课件/PDF/教材/习题路径，课程或章节线索，Vault | 课程单元及相关概念、方法或问题笔记 |
| [`literature-summary`](literature-summary/SKILL.md) | 为单篇论文生成简洁的中文文献总结 | Zotero 条目键、DOI、准确题名或 PDF 路径；Vault | 带来源定位和独立图表裁剪的总结笔记 |
| [`paper-deep-reading`](paper-deep-reading/SKILL.md) | 对单篇核心论文重建论证与证据链 | 同上 | 包含方法、公式、图表、局限和研究启发的精读笔记 |
| [`knowledge-sync`](knowledge-sync/SKILL.md) | 将长期有用的知识增量写回知识库 | 本次学习成果、来源或现有笔记路径，Vault | 更新后的 Obsidian 卡片、链接和必要日志 |

## 1. 课程学习入库 `$course-learning`

**功能：** 首次接收课程资料时建立来源指针和课程单元；已有课程问题则先查现有笔记，再按需返回原文核对；对于核心知识点，留下推导、独立例题或最小计算等可检查工件。它区分资料内容、AI 解释、用户自己完成的推导和尚未解决的问题，不会把一份摘要当作已经掌握的证据。

**使用：** 提供课程材料和目标，例如：

> 使用 `$course-learning` 整理这份第 3 讲课件 `D:\Courses\Example\lecture-03.pdf`，将要点和页码写入我的 Vault `D:\MyVault`，并列出一个可验证的练习。

首次运行会定位课程主页、现有单元和模板。资料原件留在原位置，笔记保存精确的页、幻灯片或题号。若课程归属不明确，应先指定课程名称或目标笔记。

## 2. 文献总结 `$literature-summary`

**功能：** 针对一篇论文输出短而可追溯的中文卡片，覆盖研究问题、方法、主要结果、贡献及边界；对正文中讨论的图表单独裁剪，放到 `assets/summary-figures/`。结论和数字必须有 PDF 页码或章节、图表定位。PDF 不可用时只能生成明确标注的摘要/元数据卡片。

**使用：**

> 使用 `$literature-summary` 总结 DOI `10.xxxx/xxxxx` 对应的论文，PDF 在 Zotero 中，保存到 Vault `D:\MyVault` 的 `20_文献`。

也可以提供准确题名、Zotero 条目键或 PDF 路径。Zotero 用于定位书目信息和附件，论文 PDF 是科学内容的依据。运行完成后，可在该 skill 文件夹中执行 `py -3 scripts/validate_note.py "笔记绝对路径" --mode summary` 检查结构与本地图像链接。

## 3. 文献精读 `$paper-deep-reading`

**功能：** 为一篇核心论文建立“问题 → 现有局限 → 核心思路 → 方法 → 证据 → 有边界的结论”链条，逐项核对关键图表、必要公式与结论所依赖的比较条件，并区分作者局限、分析判断和研究假设。图表裁剪放到 `assets/deep-figures/`，不会与文献总结的资源混用。

**使用：**

> 使用 `$paper-deep-reading` 精读 Zotero 条目键 `ABCD1234`，输出到 Vault `D:\MyVault`，重点分析 Figure 2 和 Figure 4 能支持哪些结论。

如有多个同名条目或候选 PDF，需要明确选定一个。运行完成后，可在该 skill 文件夹中执行 `py -3 scripts/validate_note.py "笔记绝对路径" --mode deep` 检查笔记。

## 4. 知识库同步 `$knowledge-sync`

**功能：** 在文献、课程、项目或研究学习之后，更新值得长期保留的知识：来源定位、证据支持的结论、方法适用边界、未解问题与下一步行动。它优先增量更新已有卡片，核对 Obsidian 链接，遵守当前 Vault 的 `AGENTS.md`、模板与日志要求。

**使用：**

> 使用 `$knowledge-sync` 将刚才论文精读中关于模型适用条件的结论同步到 `D:\MyVault`，链接现有方法卡，并保留论文页码。

这是按次调用的 skill，不会在后台持续监控 Vault。一次性问答若无需保存，可不调用。

## 依赖与边界

- 四个 skill 均需要可读的资料或已有笔记；Obsidian Vault 由使用者提供或由当前路径唯一定位。
- 文献总结与文献精读可以使用 Zotero skill 获取元数据和 PDF 附件；它们不会修改 Zotero 条目。也可直接提供本地 PDF。
- 文献总结引用 `nature-reader` 的来源核对、公式和图表处理约定；文献精读还依赖 `nature-paper-card` 的论文预处理脚本，并可复用 `nature-reader` 的 source map。这些辅助 skill **不包含**在本仓库，使用对应流程时需另行安装。
- MinerU 解析可作为可选辅助，不能替代 PDF 核验。两个文献 skill 的 `validate_note.py` 使用 Python 3 标准库。
- 不会自动上传原文、批量复制课程资料或覆盖已有笔记。若目标已经存在，按 skill 规则明确要求更新或替换。

## 仓库结构

```text
course-learning/       SKILL.md + agents/openai.yaml
literature-summary/     SKILL.md + agents/ + references/ + scripts/
paper-deep-reading/     SKILL.md + agents/ + references/ + scripts/
knowledge-sync/         SKILL.md + agents/openai.yaml
```
