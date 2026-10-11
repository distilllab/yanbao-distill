# yanbao-distill · 研报蒸馏四分身流水线

**中文** | [English](#english)

把没人读的 PDF 研报，蒸成**带源页码、过核验、可迁移**的知识卡。

> **适用范围**：任何"来源权威、结构完整的长 PDF"——研报、书籍、政策文件/白皮书、年报/招股书/合同/论文、设备手册、视频字幕转写稿。"研报"只是第一个实战场景（两单 31/31 核验），换内容只换模板，不换流水线骨架。

这不是又一个"AI 总结工具"。它是一套经过实战验证的**知识加工纪律**，核心是三条反共识的设计：

1. **审校分身独立核验，不带病放行**——每张卡对照原文核验四项（数字/页码/口径/原话），核验表随单留档。两单实战 31 个关键数字全部命中（11/11、20/20）。**没有核验记录的知识卡不是资产，是负债。**
2. **时效警示必填**——旧样本因子只写"怎么验证"，不写"直接上线"。
3. **三块结构 + 迁移注记**——核心结论/可复用方法/关键数据每条标源页码；至少一张卡回答"能否搬到用户自己的场景、怎么验证"。

## 关于 DistillLab 蒸馏研究室

这套流水线来自 **[DistillLab 蒸馏研究室](https://distilllab.cn/)**（distilllab.cn）——一家知识蒸馏工作室，把"厚资料"和"人的经验"蒸成可复用的知识资产：

- **研报蒸馏 / 深度研究 / 书籍蒸馏**：百页资料蒸成一页干货，附核验记录
- **老师傅经验萃取 / 企业知识资产整理**：结构化访谈 → 案例卡 + 排查决策树 + 问答助手
- **创业之路 / 口述家史 / 真人分身复刻**：让创始人的来时路、家族的记忆留下来、问得着

每单交付附核验记录——数字带来源，结论可复核。业务合作：hello@distilllab.cn

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

## 一单完整示例 / Walkthrough

```text
输入  "跑一单研报，关键词：高频因子"

第一步 选题  在 475 份 PDF 库中命中 3 份，1 份标 [DUP] 跳过，
            锁定《高频因子的现实与幻想》(海通证券，30 页)，
            输出精读页清单 8-12 页
第二步 蒸馏  逐页精读 → 产出 1 张主卡 + 3 张专题卡（草稿）
第三步 核验  对照原文逐卡核验：数字抄行 / 页码 / 费前费后口径 / 原话属实
            ↓ 发现 1 处夏普比率页码标错 → 打回重写
            （同一张卡累计打回 ≥2 次即停单报告，不许第三次盲改）
第四步 归档  核验表 11/11 命中 → 卡片落库 → 档案目录登记 → 复盘一句话
```

产出的知识卡长这样（骨架）：

```markdown
# 高频因子衰减速度：alpha 半衰期不足一日
**时效警示**：样本期 2016-2019 A 股；当时 T+1 环境、无程序化降频新规
## 核心结论
- 高频因子的预测力随持有期拉长快速衰减，日频调仓下 IC 衰减 60%+（源 p.12）
## 可复用方法
- 因子有效性必须分持仓期分层检验，全期平均 IC 会掩盖衰减（源 p.13）
## 关键数据
- 日频 IC 0.052 → 周频 0.021 → 月频 0.008（源 p.12 表 3）
## 迁移注记
- 可迁移至可转债 5 分钟库重测：同因子分频率切窗口验证；T+0 环境衰减斜率应更缓
```

核验表随单留档（这是"知识卡 vs AI 直接总结"的差别所在）：

```text
| 卡 | 项目 | 原文页 | 核验 |
| 1 | IC 0.052 | p.12 表3 | ✓ |
| 1 | 衰减 60%+ | p.12 换算 | ✓ |
| 2 | 检验方法 | p.13 §4.2 | ✓ |  → 11/11 命中
```

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

## End-to-end walkthrough

```text
Input   "run a batch, keyword: high-frequency factors"

Step 1  Select   3 hits in a 475-PDF library, 1 marked [DUP] and skipped;
                 locks onto "The Reality and Illusion of High-Frequency Factors"
                 (Haitong Securities, 30 pages); outputs an 8-12 page reading list
Step 2  Distill  page-by-page close reading -> 1 master card + 3 topic cards (drafts)
Step 3  Verify   four-axis check against the source PDF: numbers / page refs /
                 metric basis / wording
                 ↓ 1 Sharpe-ratio page reference wrong -> card sent back for rewrite
                 (>=2 rejections on the same card halts the run for human review)
Step 4  Archive  verification table 11/11 hits -> cards filed -> catalog updated -> one-line retrospective
```

What a knowledge card looks like:

```markdown
# High-frequency factor decay: alpha half-life under one day
**Freshness warning**: sample 2016-2019 A-shares; T+1 regime, no programmatic-trading throttle
## Core findings
- Factor predictive power decays fast with holding period; daily-rebalance IC drops 60%+ (source p.12)
## Reusable method
- Factor validity must be tested per holding-period layer; full-period average IC masks decay (source p.13)
## Key data
- Daily IC 0.052 -> weekly 0.021 -> monthly 0.008 (source p.12 table 3)
## Migration note
- Re-test on a 5-minute convertible-bond library: same factor, frequency-split windows;
  decay slope should flatten under T+0
```

The verification table ships with every run — this is the difference between a knowledge card and an AI summary.

## Philosophy

- The four roles (topic-selection / distillation / **review** / archiving) map to four different kinds of attention. Review must be independent from distillation — self-checking is not review.
- Agents don't need to remember everything; they need to know where to find it. Cards are indexed knowledge; source pages guarantee traceability.
- The gotcha list is the moat. Every entry was paid for with a real failure. PRs welcome.
