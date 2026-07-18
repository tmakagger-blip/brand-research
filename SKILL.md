---
name: brand-research
description: Research a brand from public and user-authorized sources, apply established brand, market, consumer, competitor, social-listening, communications, and risk methodologies, and produce complete cited brand-research content before letting the user choose any optional output files or formats. Use when the user invokes @brand-research or $brand-research with a brand such as #星巴克, or asks for comprehensive brand research, brand diagnosis, social listening, competitive analysis, public-information due diligence, or a client-ready brand research report.
---

# Brand Research

Turn a brand name into an evidence-backed public-information brand research pack. Optimize for useful coverage and traceability, not exhaustive scraping.

## Parse the request

1. Treat the first hashtag or explicit company/brand name as the target brand. Accept `@brand-research #星巴克`, `$brand-research Starbucks`, and natural-language equivalents.
2. Accept optional user materials through attached files, one or more local file/folder paths, or authorized URLs. Also accept `--materials "D:\项目资料\星巴克"` and natural-language instructions such as `使用我附上的品牌手册、访谈纪要和历史提案`.
3. Use explicit geography, category, period, competitors, language, and output format when supplied. Treat any format named in the initial request as an explicit selection.
4. Otherwise infer the primary market from the user's language and the brand's operations; state the inference. Default to the last 24 months for business and communications history, the last 30 days for social listening, and the last 7 days for emerging topics.
5. Run the complete research scope unless the user requests a narrower module. Do not ask about optional file formats before researching.
6. Describe the result as a public-information diagnosis. Never present inferred objectives, internal budgets, CRM data, approval processes, or unpublished risks as confirmed facts.
7. If the user explicitly mentions existing materials but has not attached them or supplied a path/URL, ask for them. Otherwise do not block: proceed with public sources and state that no user materials were supplied.

## Load only the needed references

- Read `references/methodology-selection.md` before selecting frameworks.
- Read `references/source-and-evidence.md` before research and source scoring.
- Read `references/deliverable-schemas.md` before writing outputs.
- Read `references/user-material-intake.md` whenever the user supplies attachments, file/folder paths, or URLs.
- When the target is Starbucks/星巴克, also read `references/starbucks-seed-2026-07-16.md`; treat it as a dated seed, refresh unstable facts, and do not treat the sample as platform-wide data.

## Research workflow

### 1. Establish the research contract

Record target brand, market, category, period, inferred competitors, output language, research date, and known limitations. Separate confirmed public facts, external stakeholder perceptions, analytical inferences, unresolved contradictions, and client-only information still required.

### 2. Register user-supplied materials

When materials are supplied, inventory them before public research, assign stable `U001...` IDs, record confidentiality and usage restrictions, and distinguish `Internal fact`, `Client assertion`, `Draft`, `Historical`, and `Reference`. User-provided does not mean independently verified. Map each material-derived claim to its U-ID, reconcile conflicts with public evidence explicitly, and follow `references/user-material-intake.md`.

### 3. Build the nine-part evidence matrix

Collect and analyze:

1. company and brand;
2. products and services;
3. apparent objectives and problems;
4. target audiences and demand occasions;
5. market and competitors;
6. historical communications;
7. public brand rules and distinctive assets;
8. observable project constraints and client-only gaps;
9. reputation, regulatory, operational, and communications risks.

Maintain a source register while researching. Attach every material claim to a source or mark it as an inference.

### 4. Collect efficiently

Use this order:

1. official sites, investor relations, filings, regulators, product pages, official accounts;
2. authoritative research, industry bodies, reputable news, interviews, and databases;
3. search trends, reviews, complaints, commerce listings, and social platforms;
4. authenticated browser sessions only when the needed content is unavailable through a connector, API, CLI, or ordinary web access.

Prefer batched search queries and bounded page extraction. On dynamic social platforms, extract visible result cards in one pass, deduplicate by note/post ID, and open only the top five high-score items plus up to five risk or anomaly items. Do not open every result.

### 5. Run social listening

Use brand/spelling variants, products/campaigns, usage occasions, positive/negative evaluation terms, competitors/comparisons, and risk terms. Sample both relevance-ranked and recent results. Preserve platform, query, URL, author, publication time, visible engagement, summary, sentiment, topic, geography when visible, relevance, and collection time. Use `scripts/rank_social_posts.py` when engagement fields are available.

Treat search results as an account-, location-, time-, and algorithm-dependent sample. Never label a sampled result set as a platform-wide census or official ranking.

### 6. Select and apply methods

Choose only methods that answer the research question. Always use triangulation and the Fact/Perception/Inference distinction. For the standard pack, normally combine PESTEL and category analysis; 3C, STP, Jobs to Be Done, and journey; competitor benchmarking, POP/POD, and perceptual mapping; Aaker or Keller brand equity, distinctive assets, and category entry points; social listening, netnography, content coding, and sentiment/topic analysis; PESO/message analysis; stakeholder mapping and a probability-impact risk assessment. Do not force a framework when the evidence cannot support it.

### 7. Validate

Triangulate important claims across source types. Prefer primary sources for facts, independent sources for verification, and natural consumer language for perception. Check dates, geography, definitions, sample bias, sponsored content, duplicate posts, and contradictory evidence. Mark confidence High, Medium, or Low using `references/source-and-evidence.md`.

### 8. Deliver the research content

Complete the executive brief and full brand-research report content; brand dossier; social-listening and consumer-insight analysis; competitor and positioning analysis; brand diagnosis, opportunities, risks, source register, social sample dataset, and client information request. The executive brief must summarize the full report and must never substitute for it.

Follow `references/deliverable-schemas.md`. Unless the user already selected a format, present the completed research content directly in the task and create no DOCX, HTML, PDF, Markdown, spreadsheet, slide, or other artifact file. After presenting the content, ask whether the user wants any files and offer format choices appropriate to the material, normally HTML, PDF, DOCX, Markdown, XLSX/CSV evidence data, or PPTX. Do not assume that Word is wanted.

If the user selected one or more formats in the initial request, generate only those formats after finalizing the content. If the user chooses formats in a follow-up, reuse the finalized research without repeating the research unless freshness or a material change requires it. Verify every generated artifact according to its format and save only user-facing files in the output directory.


### Full-report depth gate

Treat the standard pack as a decision-grade report, not a slide narrative or extended executive summary.

- Develop each substantive chapter with context, evidence, interpretation, implications, actions, confidence, contradictions, and validation needs.
- Explain the reasoning in prose. Use tables only for real comparisons or repeated records; do not compress most analysis into cells.
- Give every principal competitor a standalone profile covering business model, price/value, audience, occasions, product/innovation, channel/experience, brand assets, recent moves, strengths, vulnerabilities, and evidence limits.
- Develop audience segments through needs, Jobs to Be Done, category entry points, barriers, switching triggers, journey moments, and observable evidence. Do not rely on demographic labels alone.
- Distinguish diagnosis from recommendation. Show the causal or logical chain from evidence to root tension before proposing action.
- For Chinese-language standard reports, normally target 18,000-30,000 Chinese characters of substantive narrative excluding source lists and evidence data. This is a depth check, not a padding quota; reduce or exceed it when the evidence warrants it and state why.
- Fail the depth gate if any core chapter is only a table, a list of headlines, or fewer than two developed analytical paragraphs without a stated evidence limitation.
## Quality bar

- Lead with findings, not research narration.
- Cite every consequential factual claim near the claim.
- Include collection dates for unstable metrics.
- Quantify sample sizes and distinguish counts from interpretations.
- Report negative and contradictory evidence.
- Do not invent internal strategy, customer data, budgets, market share, or causality.
- End with prioritized implications: evidence, meaning, recommended action, confidence, and what would validate it.

