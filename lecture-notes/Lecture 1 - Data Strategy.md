---
title: Lecture 1 - Data Strategy
type: lecture
course: Strategic Business Analytics
lecture: 1
date: 2026-09-10
publish: true
tags: [data-strategy, ssot, mvot, data-governance, sba]
---

<!--
Cornell method (Pauk, "How to Study in College"):
  Record  - during lecture, fill the Notes column. Short phrases, abbreviations, examples.
  Reduce  - within 24h, write cues in the left column: questions, keywords, prompts.
            Turn each block of notes into a question - Who / What / When / Where / Why / How
            (5W1H). If a block yields no question, it is probably not worth keeping.
  Recite  - hide the Notes column, answer each cue aloud from memory.
            Feynman check: could you explain this answer to a friend outside the course?
            If not, the gap goes in Reflection.
  Reflect - add your own connections / questions under Reflection.
  Review  - re-read weekly; keep the Summary to 3-5 sentences.
  Sources - name + link, nothing else: slides, textbook chapter, papers the lecturer cited.
            No files in the vault; it is all online anyway.
  Related - link every idea that deserves its own note: [[Topics]], [[Companies]], [[Media]].
            Links are what make the graph useful; folders and tags do not.
-->

## Notes

| Cues | Notes |
| :--- | :--- |
| Why is data strategy a problem? | Cross-industry stats: <50% of structured data used in decisions; <1% of unstructured data analysed; >70% of employees can access data they shouldn't; 80% of analysts' time = finding and preparing data. Breaches common, rogue datasets in silos, tech can't keep up. |
| Is a CDO alone enough? | No. Need a coherent strategy for organising, governing, analysing, deploying data. Whole C-suite is responsible, starting with the CEO. Framework built from AIG (DalleMule = CDO) plus ~6 other large firms. |
| What is **data defense**? | Minimise downside risk: regulatory compliance (privacy, financial reporting), fraud detection, preventing data theft. Governs authoritative sources, so it owns the **SSOT**. Concerns: legal, finance, compliance, IT. Day-to-day, operational (P&G: permanent IT teams for MDM and infosec). Exception: fraud protection needs real-time analytics. |
| What is **data offense**? | Support business objectives: revenue, profit, customer satisfaction. Customer insights (analysis, modelling), dashboards integrating market and customer data. Sales and marketing, often real-time. Partners with business leaders on tactical and strategic initiatives. |
| What shifts the offense vs defense balance? | They compete for the same finite resources. Heavy regulation (finance, healthcare) pushes defense. Strong competition for customers pushes offense. Uniform data = easier defense; flexible data = more useful for offense. **Balancing offense/defense = balancing control/flexibility.** |
| How does Drucker separate data from information? | Information = "data endowed with relevance and purpose". Raw sales figures have limited value; in historical or market context they become meaningful. |
| Data architecture vs information architecture? | *Data arch*: how data is collected, stored, transformed, distributed, consumed (databases, file systems, links to processes). *Info arch*: processes and rules converting data into information (eg marketing dashboards fed by raw ad and sales data). |
| What is an **SSOT**? | Single source of truth: logical, often virtual or cloud repository with one authoritative copy of crucial data (customer, supplier, product). Needs provenance, governance controls and a common language (one definition of revenue, customer, product). AI can assemble an SSOT from chaos. Eg industrial firm shut redundant systems, spotted suppliers selling to multiple BUs, $75M savings in year 1. |
| What are **MVOTs**? | Multiple versions of the truth: business-specific transformations of SSOT data into information; controlled, consistent, customised. Eg marketing reports TV ad spend when ads air; finance reports when invoices paid. Different numbers, both correct. |
| Who governs SSOT and MVOTs? | Needs strong controls, standards, governance, tech. CDO/CTO lead governance; business and tech managers in units participate. |
| How does CIBC apply it? | SSOT = client profile and preference data. MVOTs for loan origination and CRM. Automated sync between SSOT and MVOTs, nightly exception handling for integrity issues (CDO Jose Ribau). |
| Data lake vs data warehouse? | *Warehouse*: structured data in hierarchical files; tight security and access control; still used for production apps (general ledger, order mgmt). *Lake*: cheap, agile, scalable; structured and unstructured; ideal home for SSOT (granular, to transaction level) and MVOTs (aggregations). Trend: more data moving to the lake; many firms run both. |
| Who owns data strategy? | CIO ultimately responsible; CDO conceives, develops, executes and adjusts the trade-offs. |
| What sets a firm's position on the offense-defense spectrum? | Overall strategy, regulatory environment, competitors' data capabilities, maturity of data-mgmt practices, data budget. Position is dynamic (insurer moves to offense under competition; hedge fund moves to defense under regulation). |
| Centralised vs decentralised data mgmt? | *Centralised*: one enterprise CDO, consistent policy and standards, suits **defense**; larger budget, less tangible ROI. *Decentralised*: unit CDOs (matrix report to enterprise CDO) own their MVOTs, enterprise CDO owns SSOT, suits **offense**; budgets closer to users, tangible ROI. Matrix prevents silos and duplicate systems. |
| What is the future outlook? | ML already helps build SSOTs; cheaper, more dynamic SSOT/MVOTs coming; blockchain makes the framework more relevant. Still no substitute for a well-run data function. Internet traffic passed 1 ZB/yr in Sept 2016 (Cisco), doubling in 4 years. Firms without a data strategy must catch up fast "or plan their exit". |

## Reflection

- Offense/defense maps neatly onto control/flexibility. Does every architecture decision (lake vs warehouse, central vs unit CDO) reduce to that one axis?
- The MVOT ad-spend example shows "conflicting" numbers can both be right. The key is that the *definition* is documented. Link to data-dictionary and metadata ideas later in the course.
- How does a small company without a CDO apply this? Who plays the enterprise-CDO role?

## Summary

Data strategy is a C-suite concern, not just the CDO's. The DalleMule and Davenport framework frames it as a trade-off between **defense** (control, compliance, risk, SSOT) and **offense** (flexibility, insight, revenue, MVOTs), with the right balance set by regulation, competition, maturity and budget. Architecturally this is delivered by a single source of truth feeding multiple controlled versions of the truth, increasingly hosted in a data lake alongside traditional warehouses. Organisationally, centralised data management favours defense while decentralised unit CDOs favour offense.

## Sources

- Slides: Lecture 1 - Data Strategy (Dr Francis)
- Reading: [What's Your Data Strategy?](https://hbr.org/2017/05/whats-your-data-strategy) - Leandro DalleMule and Thomas H. Davenport, HBR May-June 2017

## Related

- [[Single Source of Truth]]
- [[Data Governance]]
- [[Data Lake vs Data Warehouse]]
- [[AIG]]
- [[CIBC]]
