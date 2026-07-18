# Source and evidence protocol

## Source hierarchy

| Tier | Source | Best use | Caution |
|---|---|---|---|
| A | Filings, regulators, official datasets, audited reports | Entity, financials, operations, formal claims | Company framing and definitions |
| A- | Official site, product pages, releases, official accounts | Current offers, stated strategy, campaigns | Promotional bias |
| B | Industry bodies, academic work, established research firms | Category, trends, methods | Modeled estimates and definitions |
| B- | Reputable news and attributable interviews | Events and context | May repeat unverified claims |
| C | Retail listings, reviews, complaints, search trends, social posts | Availability, language, perceptions, issues | Selection, algorithms, fraud, sponsorship |
| D | Aggregators, anonymous reposts, unsourced summaries | Leads only | Never sole support for a material claim |

## Confidence

- **High:** primary evidence plus independent corroboration, or multiple strong independent sources with consistent definitions.
- **Medium:** one strong source, or several weaker consistent sources with known limitations.
- **Low:** anecdote, inferred objective, opaque model, contradiction, or unstable social signal.

## Claim states

Use **Fact**, **Perception**, **Inference**, **Hypothesis**, or **Gap**. Never silently convert one state into another.

## Query design

Combine brand variants with corporate terms; products and services; audience needs and occasions; competitor comparisons; campaigns and collaborations; and risk terms such as complaint, recall, safety, discrimination, labor, closure, lawsuit, and regulator. Record exact social queries and collection timestamps.

## Standard coverage targets

Targets control coverage; they are not quotas to pad:

- at least 3 current primary/official sources;
- at least 5 independent authoritative sources across 2 publishers;
- at least 3 sources per principal competitor;
- at least 30 deduplicated social/review items across query families when access permits;
- detail validation of the 5 highest-scoring relevant items and material risk/anomaly items;
- explicit sample and access limitations.

Reduce targets for niche or inaccessible brands and state why. Increase them for high-stakes claims.

## Social controls

1. Deduplicate by canonical URL or post ID.
2. Separate organic, official, employee, media, influencer, and suspected sponsored content.
3. Normalize labels such as `1.2?` before ranking.
4. Retain relevance-ranked and recent samples.
5. Exclude false-positive keyword matches and record exclusion rules.
6. Do not compare raw engagement across platforms without normalization.
7. Treat visible engagement as a dated snapshot.
