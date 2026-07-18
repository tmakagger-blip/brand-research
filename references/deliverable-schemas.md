# Deliverable schemas

## Executive brief

1. Scope, market, period, research date
2. Five decision-relevant findings
3. Brand position in one paragraph
4. Three opportunities
5. Three risks
6. Priority actions with confidence
7. Critical evidence gaps

## Brand research report

1. Executive summary
2. Scope, methods, sample, and limitations
3. Company and brand
4. Products, services, channels, and business model
5. Apparent objectives and current problems
6. Audiences, Jobs to Be Done, occasions, and journey
7. Market, category, and macro environment
8. Competitors, POP/POD, positioning, and white space
9. Brand identity, equity, associations, and distinctive assets
10. Historical communications and PESO/channel patterns
11. Social listening and cultural signals
12. Reputation, regulatory, operational, and communications risks
13. Diagnosis: strengths, tensions, contradictions, and root causes
14. Prioritized opportunities and actions
15. Client-only information request
16. Sources and methodological notes

### Depth and composition standard

The executive summary is a front section, not the report itself. A standard full report should normally contain 18,000-30,000 Chinese characters of substantive narrative (excluding sources and evidence tables) when the public evidence is sufficient.

For chapters 3-14, include:

1. current state and relevant context;
2. dated evidence and any contradiction;
3. analysis using the selected framework;
4. business and brand implications;
5. recommended response or experiment;
6. confidence and the internal data needed to validate it.

Use prose as the primary analytical form. Reserve tables for comparisons, matrices, timelines, repeated metrics, and implementation plans. Do not let tables replace explanation.

Competitor analysis must include a standalone profile for every principal competitor. Audience analysis must include Jobs to Be Done, category entry points, barriers, switching triggers, journey moments, and evidence limitations. Communications analysis must cover message evolution, PESO roles, content architecture, channel coherence, and measurement gaps.
For every major finding use: **Evidence ? Interpretation ? Implication ? Recommended action ? Confidence**.

## User-provided materials in the report

When user materials are supplied, add a methodology subsection named `User-provided materials and limitations` (or the Chinese equivalent). List the U-IDs used, material type/date, confidentiality class, role in the analysis, excluded or unreadable items, and any unresolved conflict with public evidence. Do not embed or redistribute raw confidential files.

## Evidence data

Use the following logical tables in the research content. Create an XLSX workbook or CSV files only when the user selects one of those formats:

- `user_materials`: `material_id,file_name,material_type,provided_by,document_date,received_at,confidentiality,evidence_status,summary,supports,limitations,usage_restrictions,confidence,source_path_or_url` (include when materials are supplied)
- `sources`: `source_id,title,publisher,source_type,tier,published_at,accessed_at,geography,url,supports,limitations,confidence`
- `claims`: `claim_id,claim,state,report_section,source_ids,confidence,contradiction,notes` (`source_ids` may contain public `S...` IDs and user-material `U...` IDs)
- `social_sample`: `platform,query,post_id,canonical_url,author,account_type,published_at,collected_at,geography,title,summary,topic,sentiment,likes,saves,comments,shares,age_hours,relevance,sponsored_status,hot_score,exclusion_reason`
- `competitors`: `brand,product_scope,price_position,audience,occasions,functional_benefits,emotional_benefits,positioning,distinctive_assets,channels,recent_moves,evidence_ids,confidence`
- `risks`: `risk,category,evidence_ids,probability,impact,velocity,stakeholder,current_response,recommended_monitoring,confidence`
- `gaps`: `information_needed,why_needed,likely_owner,public_proxy,decision_blocked`

## Optional output formats

Do not create files by default. First complete and present the research content. If the user has not already selected formats, ask after delivery whether they want any of the following:

- HTML: self-contained responsive report for convenient reading;
- PDF: fixed-layout report for circulation or archiving;
- DOCX: editable Word report;
- Markdown: portable source document;
- XLSX or CSV: structured evidence data;
- PPTX: presentation-oriented summary, which must not replace the full report.

Generate only the selected formats. Preserve the same claims, evidence IDs, confidence, contradictions, and limitations across formats.

## HTML requirements

When HTML is selected, create a self-contained `.html` report. Preserve the full evidence-backed narrative rather than creating a shorter duplicate.

- Include a sticky table of contents with anchors for every H1 section.
- Use responsive typography, cards, and horizontally scrollable tables so the report works on desktop and mobile.
- Preserve evidence labels, source identifiers, confidence language, limitations, and source URLs.
- Use semantic HTML, sufficient contrast, visible focus states, and a print stylesheet.
- Do not require a web server, external JavaScript, a CDN, remote fonts, or external CSS.
- Generate directly from the finalized research content. Use `scripts/docx_to_html_report.py` only when the user selected DOCX as well and it is the chosen conversion source.
- Open or render the resulting page and verify the title, navigation, all sections, tables, URLs, and narrow-screen layout.
## File naming

When the user selects file output, use `<brand>-brand-research-YYYY-MM-DD/` and include only the requested files, using these names where applicable:

- `<brand>-brand-research-report.docx`, `.pdf`, or `.md`
- `<brand>-brand-research-report.html`
- `<brand>-evidence-workbook.xlsx` or CSV files
- `<brand>-executive-brief.md`
- `<brand>-brand-research-presentation.pptx`

Do not create files that merely repeat the same narrative.

