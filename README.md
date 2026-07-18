# Brand Research Skill｜品牌研究 Skill

一套用于 Codex 的系统化品牌研究工作流：整合公开资料与用户已有资料，形成可追溯、可判断、可直接用于策略工作的完整品牌研究报告。

A systematic brand-research workflow for Codex. It combines public evidence with user-provided materials to produce a traceable, decision-ready report for strategy, marketing, and communications work.

[中文](#中文) · [English](#english)

---

## 中文

### 简介

`brand-research` 适用于品牌营销公司、公关公司、咨询团队、企业品牌部及独立研究者。输入品牌名后，Skill 会按照统一的方法论研究品牌、市场、用户、竞争、传播、舆情与风险，并对事实、公众认知和分析推断进行区分。

它不是简单的资料汇总器，也不以“搜索结果越多越好”为目标。它强调：

- 研究问题与商业决策相关；
- 重要结论有来源、有时间、有证据等级；
- 多来源交叉验证，不把品牌自述直接当作市场事实；
- 明确区分事实、公众认知与推断；
- 在证据不足时主动标注缺口与不确定性；
- 把研究结果转化为可行动的策略启示。

### 核心能力

Skill 可覆盖以下九类信息：

1. 品牌与企业基础：发展历程、业务结构、所有权、管理与关键里程碑。
2. 产品与服务：产品线、价格带、渠道、卖点、体验与创新动作。
3. 商业目标与核心问题：增长命题、挑战、机会、研究假设与优先问题。
4. 用户与需求：目标人群、行为、场景、痛点、动机、JTBD 与认知差异。
5. 市场与竞争：市场结构、趋势、竞品、替代方案、竞争维度与相对位置。
6. 品牌定位与资产：价值主张、个性、语调、视觉和语言资产、差异化线索。
7. 传播与内容：自有、赢得、社交与付费传播，议题、内容支柱和平台表现。
8. 口碑、舆情与风险：正负面议题、事件、争议、监管、运营和传播风险。
9. 结论与行动：关键发现、证据强度、机会空间、策略建议和待验证问题。

### 安装

将整个仓库克隆到 Codex 的个人 Skills 目录，确保 `SKILL.md` 位于 `brand-research` 文件夹根目录。

Windows PowerShell：

```powershell
git clone https://github.com/tmakagger-blip/brand-research "$env:USERPROFILE\.codex\skills\brand-research"
```

macOS / Linux：

```bash
git clone https://github.com/tmakagger-blip/brand-research ~/.codex/skills/brand-research
```

安装后新建一个 Codex 任务。如果已经存在同名目录，请先自行备份或更新该目录，不要直接覆盖其中的个人修改。

关于 Codex Skills 的机制与使用方式，可参考 [OpenAI Codex 官方文档](https://developers.openai.com/codex/)。

### 快速开始

使用品牌中文名：

```text
@brand-research #星巴克
```

也可以使用 `$skill-name` 形式或自然语言：

```text
$brand-research Starbucks
```

```text
请使用 brand-research 对宝莹洗衣液进行完整品牌研究。
```

如果一开始就确定需要文件格式，可以直接说明：

```text
@brand-research #星巴克，研究完成后生成可直接浏览的 HTML 完整报告和 PDF 正式报告。
```

### 添加已有资料

Skill 支持把用户已有资料作为正式研究证据纳入分析。可以：

- 直接附加文件；
- 提供本地文件或文件夹路径；
- 提供已授权访问的网页或在线资料；
- 在提示中粘贴访谈、会议纪要、调研结果或业务背景。

示例：

```text
@brand-research #星巴克 --materials "D:\项目资料\星巴克"
```

```text
@brand-research #星巴克
请结合我附上的品牌手册、消费者访谈、历史提案和销售复盘完成研究。
```

用户资料会使用 `U001`、`U002` 等独立编号；公开来源使用 `S001`、`S002` 等编号。两类证据不会被混为一谈。当内部资料与公开资料冲突时，报告会说明冲突、时间范围和可能原因，而不是静默选择其中一方。

除非用户明确授权，已有资料默认按保密材料处理，不应用作公开搜索词，也不应被上传到第三方服务。

### 默认交付方式

默认情况下，Skill 会先在对话中呈现完整研究内容，不自动创建 Word 或其他文件。内容完成后，再由用户选择是否需要：

- 可直接浏览的 HTML 完整报告；
- PDF 正式报告；
- Markdown 研究底稿；
- DOCX 可编辑文档；
- XLSX / CSV 证据表、竞品表或内容样本表；
- PPTX 汇报版。

如果用户在最初指令中已经指定格式，则只生成指定格式。报告篇幅由问题和证据决定；在证据充分时，完整中文报告通常以深度报告而非简报为目标。

### 方法与证据原则

#### 来源优先级

一般优先使用：

1. 监管文件、公司公告、财报、政府和统计机构资料；
2. 品牌及企业官方渠道、产品页、新闻稿和公开演讲；
3. 可靠媒体、行业机构、研究报告和学术资料；
4. 电商、应用商店、门店与平台公开页面；
5. 小红书、X、微博、抖音、论坛等社交内容；
6. 搜索摘要、聚合页和线索型来源。

来源等级不等于结论自动成立。品牌官方资料适合确认“品牌说了什么”，消费者资料适合观察“人们如何理解和体验”，市场结论通常需要多类证据共同支持。

#### 结论类型

- **Fact｜事实**：可被可靠来源直接核实的信息。
- **Perception｜认知**：消费者、媒体或社群表达的看法与体验。
- **Inference｜推断**：研究者基于多项证据形成的分析判断。

重要判断会标记高、中、低置信度，并说明证据缺口。

#### 社交媒体研究

社交平台内容可用于发现话题、语言、使用场景、口碑和新兴问题，但公开搜索结果通常只是样本，不代表平台全量数据。动态页面、登录限制、个性化推荐、地区差异和删除内容都会影响覆盖范围。因此报告应说明检索窗口、关键词、样本量、筛选方式与局限，不能把可见样本直接外推为总体比例。

### 典型工作流

1. 确认品牌、市场范围、时间范围和决策目标。
2. 接收并登记用户已有资料。
3. 建立研究问题、关键词和证据计划。
4. 收集官方、行业、媒体、渠道和社交来源。
5. 去重、核验、交叉验证并标记证据等级。
6. 完成九类研究模块和跨模块分析。
7. 提炼关键发现、风险、机会与建议。
8. 先交付完整内容，再按用户选择生成文件。

### 项目结构

```text
brand-research/
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── deliverable-schemas.md
│   ├── methodology-selection.md
│   ├── source-and-evidence.md
│   ├── user-material-intake.md
│   └── starbucks-seed-2026-07-16.md
└── scripts/
    ├── docx_to_html_report.py
    └── rank_social_posts.py
```

- `SKILL.md`：主工作流、触发条件、研究标准和交付规则。
- `references/`：方法选择、证据规范、资料接收和交付结构。
- `scripts/`：特定格式转换和社交样本排序辅助脚本。
- `agents/openai.yaml`：Skill 的展示名称、简介和默认提示。

### 使用边界

- 研究质量取决于资料的可获得性、可信度与时间范围。
- 本 Skill 不是各社交平台的官方全量数据接口，也不承诺绕过登录、权限、付费墙或反自动化机制。
- 涉及实时舆情、销量、财务、法规或重大决策时，应使用最新的一手资料并进行人工复核。
- 社交媒体样本适合做定性洞察和假设生成；除非采样设计支持，否则不应被表述为总体统计结论。
- 报告中的建议是基于可见证据形成的研究判断，不替代法律、财务或合规意见。

---

## English

### Overview

`brand-research` is designed for brand agencies, PR firms, consulting teams, in-house brand departments, and independent researchers. Given a brand name, it applies a consistent methodology to investigate the company, products, market, audiences, competition, communications, reputation, and risks.

It is not a simple search-results summarizer. The workflow is designed to:

- connect research questions to business decisions;
- keep major conclusions traceable to dated sources;
- triangulate important claims across source types;
- separate facts, public perceptions, and analytical inferences;
- disclose uncertainty and evidence gaps;
- translate findings into actionable strategic implications.

### Core coverage

The Skill covers nine research areas:

1. Brand and company fundamentals: history, ownership, business structure, management, and milestones.
2. Products and services: portfolio, pricing, channels, propositions, experience, and innovation.
3. Business objectives and key problems: growth agenda, challenges, opportunities, and research hypotheses.
4. Audiences and needs: segments, behaviors, occasions, pain points, motivations, and jobs to be done.
5. Market and competition: category structure, trends, competitors, substitutes, and relative position.
6. Positioning and brand assets: value proposition, personality, tone, visual and verbal assets, and differentiation.
7. Communications and content: owned, earned, social, and paid activity, themes, content pillars, and platform signals.
8. Reputation and risk: positive and negative topics, incidents, controversies, regulatory, operational, and communications risks.
9. Conclusions and action: findings, evidence strength, opportunity spaces, recommendations, and open questions.

### Installation

Clone the complete repository into your personal Codex Skills directory. `SKILL.md` must remain at the root of the `brand-research` folder.

Windows PowerShell:

```powershell
git clone https://github.com/tmakagger-blip/brand-research "$env:USERPROFILE\.codex\skills\brand-research"
```

macOS / Linux:

```bash
git clone https://github.com/tmakagger-blip/brand-research ~/.codex/skills/brand-research
```

Start a new Codex task after installation. If a folder with the same name already exists, back it up or update it carefully instead of overwriting local changes.

See the [official OpenAI Codex documentation](https://developers.openai.com/codex/) for general information about Codex and Skills.

### Quick start

Invoke the Skill with a brand name:

```text
@brand-research #Starbucks
```

The `$skill-name` form and natural-language requests are also supported:

```text
$brand-research Starbucks
```

```text
Use brand-research to conduct a complete study of Starbucks in China.
```

If you already know the required output formats, specify them in the initial request:

```text
@brand-research #Starbucks. After completing the research, generate a browsable HTML report and a formal PDF report.
```

### Adding existing materials

User-provided materials can be incorporated as first-class research evidence. You may:

- attach files directly;
- provide a local file or folder path;
- provide an authorized URL or online resource;
- paste interviews, meeting notes, survey findings, or business context into the prompt.

Examples:

```text
@brand-research #Starbucks --materials "D:\Brand Projects\Starbucks"
```

```text
@brand-research #Starbucks
Use the attached brand book, consumer interviews, previous proposals, and sales review.
```

User materials receive identifiers such as `U001` and `U002`; public sources receive identifiers such as `S001` and `S002`. If internal and public evidence conflict, the report should describe the discrepancy, dates, and plausible reasons rather than silently choosing one source.

Unless explicitly authorized otherwise, user materials are treated as confidential. They should not be uploaded to third-party services or reused as public search queries.

### Default delivery behavior

By default, the Skill presents the complete research content in the conversation and does not automatically create Word or other files. After the content is complete, the user can choose whether to generate:

- a browsable HTML report;
- a formal PDF report;
- a Markdown research master;
- an editable DOCX document;
- XLSX / CSV evidence, competitor, or content-sample tables;
- a PPTX presentation.

If formats are specified in the initial request, only those formats are generated. Report length follows the research question and available evidence; when evidence supports it, the target is a full decision-grade report rather than a short briefing.

### Method and evidence principles

#### Source hierarchy

The workflow generally prioritizes:

1. regulatory filings, company disclosures, financial reports, government and statistical sources;
2. official brand channels, product pages, press releases, and public speeches;
3. reputable media, industry bodies, research reports, and academic sources;
4. e-commerce, app-store, retail, and platform pages;
5. social content from platforms such as Xiaohongshu, X, Weibo, Douyin, and forums;
6. search snippets, aggregators, and lead-only sources.

Source rank does not make a conclusion automatically true. Official sources are useful for establishing what a brand claims; audience sources reveal how people interpret or experience it; market conclusions normally require triangulation across several source types.

#### Claim types

- **Fact**: information directly verifiable from a reliable source.
- **Perception**: an opinion or experience expressed by consumers, media, or communities.
- **Inference**: an analytical judgment derived from multiple pieces of evidence.

Important conclusions should include High, Medium, or Low confidence and disclose material evidence gaps.

#### Social-media research

Social content is valuable for discovering topics, language, occasions, reputation signals, and emerging issues. Publicly visible results are usually a sample, not a complete platform census. Dynamic pages, login restrictions, personalized feeds, regional differences, and deleted posts all affect coverage. Reports should therefore disclose the query window, keywords, sample size, selection method, and limitations. Visible samples must not be presented as population-level statistics without a defensible sampling design.

### Typical workflow

1. Define the brand, market, time window, and decision objective.
2. Receive and register user-provided materials.
3. Build research questions, search terms, and an evidence plan.
4. Collect official, industry, media, channel, and social evidence.
5. Deduplicate, verify, triangulate, and grade the evidence.
6. Complete the nine research modules and cross-module analysis.
7. Synthesize findings, risks, opportunities, and recommendations.
8. Present the full content first, then generate only the file formats requested by the user.

### Repository structure

```text
brand-research/
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── deliverable-schemas.md
│   ├── methodology-selection.md
│   ├── source-and-evidence.md
│   ├── user-material-intake.md
│   └── starbucks-seed-2026-07-16.md
└── scripts/
    ├── docx_to_html_report.py
    └── rank_social_posts.py
```

- `SKILL.md`: core workflow, triggers, research standards, and delivery rules.
- `references/`: method selection, evidence rules, material intake, and deliverable schemas.
- `scripts/`: helpers for selected format conversion and social-sample ranking.
- `agents/openai.yaml`: display name, description, and default prompt metadata.

### Limitations

- Research quality depends on source availability, reliability, and the selected time window.
- This Skill is not an official full-data API for any social platform and does not promise to bypass logins, permissions, paywalls, or anti-automation controls.
- Real-time reputation, sales, finance, regulation, and other high-impact conclusions require current primary sources and human review.
- Social samples are useful for qualitative insight and hypothesis generation. They should not be presented as population statistics unless the sampling design supports that claim.
- Strategic recommendations are research judgments based on visible evidence and do not replace legal, financial, or compliance advice.
