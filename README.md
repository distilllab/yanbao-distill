# yanbao-distill · 研报蒸馏四分身流水线

**中文** | [English](#english)

把没人读的 PDF 研报，蒸成**带源页码、过核验、可迁移**的知识卡。

> **适用范围**：任何"来源权威、结构完整的长 PDF"——研报、书籍、政策文件/白皮书、年报/招股书/合同/论文、设备手册、视频字幕转写稿。"研报"只是第一个实战场景（两单 31/31 核验），换内容只换模板，不换流水线骨架。

这不是又一个"AI 总结工具"。它是一套经过实战验证的**知识加工纪律**，核心是三条反共识的设计：

1. **审校分身独立核验，不带病放行**——每张卡对照原文核验四项（数字/页码/口径/原话），核验表随单留档。两单实战 31 个关键数字全部命中（11/11、20/20）。**没有核验记录的知识卡不是资产，是负债。**
2. **时效警示必填**——旧样本因子只写"怎么验证"，不写"直接上线"。
3. **三块结构 + 迁移注记**——核心结论/可复用方法/关键数据每条标源页码；至少一张卡回答"能否搬到用户自己的场景、怎么验证"。

## 快速开始

```bash
# 1. 克隆到你的技能目录（Claude Code / WorkBuddy / 其他兼容 agentskills 标准的平台）
git clone <repo> ~/.claude/skills/yanbao-distill

# 2. 配置你的库路径
export YANBAO_LIBRARY="/path/to/your/pdf-library"

# 3. 跑一单
#    对你的 AI 助手说：
"跑一单研报，关键词：高频因子"
```

流程自动走：检索定位 → 结构遍（出精读页清单）→ 精读遍（逐页出卡）→ **核验遍（对照原文打回不合格卡）** → 归档 → 复盘。

## 目录结构

```
yanbao-distill/
├── SKILL.md                  # 技能主文件：方法+流程+Gotchas+红线
├── scripts/find_reports.py   # 关键词检索（只读，自动标重复件）
└── references/card-template.md  # 知识卡模板+落盘规则+核验表
```

## 设计哲学

- **四分身不是营销话术**：选题/蒸馏/审校/归档四个角色对应四种不同的注意力——尤其"审校"必须独立于"蒸馏"，自查不叫审校。
- **AI 不用记住所有细节，但要知道去哪找**：卡片是索引化的知识，源页码保证可回溯。
- **坑清单是护城河**：SKILL.md 里每条 Gotcha 都是真实失败换来的，欢迎 PR 补充你的坑。

## 实战记录

| 单 | 研报 | 页数 | 产出 | 核验命中 |
|---|---|---|---|---|
| 1 | 海通证券·高频因子的现实与幻想 (2020) | 30 | 1 主卡 + 3 专题卡 | 11/11 |
| 2 | 华泰证券·微软AI量化平台Qlib体验 (2020) | 34 | 1 主卡 + 3 专题卡 | 20/20 |

## License

MIT。金融场景使用注意：本工具只做知识蒸馏，产出物不含投资建议。

---

<a name="english"></a>
# yanbao-distill · Research Report Distillation Pipeline

Turn unread PDF research reports into **source-paginated, verified, transferable** knowledge cards.

> **Scope**: any long-form PDF with an authoritative source — research reports, books, policy papers/white papers, annual reports/prospectuses/contracts/papers, equipment manuals, video transcripts. "Research reports" is just the first battle-tested scenario (two runs, 31/31 verified); swapping content means swapping templates, not the pipeline.

Not another "AI summarizer" — a battle-tested **knowledge-processing discipline** with three contrarian designs:

1. **Independent review agent, no defective cards ship** — every card is verified against the source PDF on four axes (numbers / page refs / metric basis / actual wording). Two production runs: 31/31 key figures verified.
2. **Mandatory freshness warning** — factors from old samples get "how to validate", never "use directly".
3. **Three-block structure + migration note** — Core findings / Reusable methods / Key data, each with source page; at least one card answers "can this transfer to *my* dataset, and how would I test it".

## Quick start

```bash
git clone <repo> ~/.claude/skills/yanbao-distill
export YANBAO_LIBRARY="/path/to/your/pdf-library"
# Then tell your agent: "run a batch, keyword: high-frequency factors"
```

## Philosophy

- The four roles (topic-selection / distillation / **review** / archiving) map to four different kinds of attention. Review must be independent from distillation — self-checking is not review.
- Agents don't need to remember everything; they need to know where to find it. Cards are indexed knowledge; source pages guarantee traceability.
- The gotcha list is the moat. Every entry was paid for with a real failure. PRs welcome.
