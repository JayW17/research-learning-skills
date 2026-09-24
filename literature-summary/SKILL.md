---
name: literature-summary
description: Generate a compact, source-grounded Chinese literature-summary note from one Zotero paper and its PDF, crop cited paper figures into summary-specific assets, and save it to an Obsidian vault. Use when the user wants a structured paper summary or literature card, not a full bilingual reader or a reviewer-style deep analysis.
metadata:
  version: "1.3.0"
---

# Literature Summary

Create a reliable, reusable literature card for exactly one paper. The outcome is a concise Chinese Markdown note that lets the user recall the research question, method, evidence, contribution, and boundary without reopening the paper.

## Required inputs and safe defaults

The user may identify the paper with a Zotero item key, DOI, exact title, an unambiguous Zotero search query, or a local PDF path. Resolve the Obsidian vault from a user-supplied vault or note path, or from the nearest `.obsidian` ancestor of a supplied source path. If no unique vault can be identified, ask for its absolute path. Use `20_文献` as the literature root within the selected vault unless the user specifies another root.

- Do not guess a Zotero item or a PDF attachment.
- If a Zotero search has multiple plausible papers, present a compact candidate list with title, year, creator, and item key; wait for a selection.
- If an item has multiple plausible primary PDFs, ask the user which attachment to use. Do not silently pick the first attachment.
- If the target note already exists, do not overwrite it or its assets without the user's explicit instruction to replace or update it.
- Write the normal bundle below `20_文献`. When the user explicitly requests direction classification, infer one concise, source-grounded Chinese research-direction label and write below `20_文献/<direction>/` instead. State the chosen direction in frontmatter and the delivery report.

Use the Zotero skill only for Zotero Desktop readiness, bibliographic metadata, and attachment discovery. This workflow is read-only toward Zotero: never create, edit, delete, or link Zotero notes or items.

## Source hierarchy

Treat sources in this strict order:

1. The selected PDF is authoritative for the paper's claims, numbers, formulas, figures, tables, and conclusions.
2. Zotero supplies bibliographic metadata and attachment location; resolve conflicts in paper content in favor of the PDF and flag metadata conflicts.
3. A MinerU parse, when already supplied or available in the environment, is an optional extraction aid only. Cross-check its central claims, equations, and figure references against the PDF. If it disagrees with the PDF, correct it from the PDF and record the discrepancy in the note.
4. Do not introduce outside knowledge unless the user explicitly asks for it. Mark it as 【外部】 and link or cite the source.

Never promote an abstract, title, caption, OCR fragment, or MinerU output into a claim that the PDF does not support. If no PDF is available, offer a clearly marked metadata/abstract-only card; do not present it as a full-paper summary.

## Workflow

1. Resolve one Zotero item and its primary PDF. Capture title, creators, venue, year, DOI/URL, item key, attachment key, and the chosen PDF path.
2. Reuse an existing paper.md, source_map.json, source_bundle.json, or paper-card.md within the paper's target folder when they match the same Zotero item and PDF. Otherwise read enough of the full PDF to map the abstract, introduction, method, results, discussion/conclusion, main figures, main tables, and essential equations. Follow nature-reader's source-grounding, figure-crop, and equation-confidence conventions without creating an unnecessary full bilingual reader.
3. Build a compact evidence inventory before drafting: research question, gap, approach, data/setting, main results, author-stated limitations, and the figures/tables that support the important conclusions.
4. Crop every main-paper visual that the note discusses. Make tight, individual crops; do not use full-page screenshots when a figure or table can be isolated. Store them under the note folder's `assets/summary-figures/` directory. Never write summary assets into a deep-reading asset directory. Preserve figure/table numbers and page references. Put a compact image index at the end for main figures that are not otherwise discussed.
5. Draft the note with the summary template in references/obsidian-output.md. Use Chinese by default while preserving canonical terms, model names, variables, units, and abbreviations.
6. Validate the completed note and its relative image links:

    py -3 scripts/validate_note.py "PATH_TO_NOTE" --mode summary

   Resolve every reported error before delivery.
7. Report the generated Obsidian note path, asset directory, Zotero item key for traceability, source coverage, and any source limitations. Do not claim the note was imported into Obsidian; writing it under the configured vault is the import mechanism. Do not create, update, or link any Zotero note.

## Grounding and writing rules

- Put a traceable paper pointer beside every major result, numerical value, figure/table interpretation, central method statement, and limitation. Use forms such as [论文：PDF p. 4，Fig. 2] or [论文：结果部分，Table 1].
- Separate source classes visibly: direct paper facts use paper pointers; use 【推断】 for a reasonable but unstated inference; use 【分析】 for the agent's judgment; use 【外部】 only after the user requests external material.
- State 原文未说明, 论文未提供, or 当前材料不足以判断 rather than filling a template field speculatively.
- Distinguish author-claimed innovation from 【分析】实际创新. Do not inflate novelty.
- Keep author-acknowledged limitations separate from 【分析】可能局限.
- Include only formulas essential to understanding the paper. Preserve symbols, subscripts, units, and equation numbers. A display formula must use one complete $$...$$ pair on one physical Markdown line for Better Notes and Obsidian compatibility. If a formula cannot be transcribed confidently, insert a tight PDF crop and state that the image is authoritative.
- Never infer a plot trend solely from a caption. When a visual cannot be inspected, state that the caption or nearby text is all that can be grounded.

## Delivery layout

Read references/obsidian-output.md before creating the note. The normal destination is:

    VAULT_ROOT/20_文献/SAFE_PAPER_TITLE/总结—SAFE_PAPER_TITLE.md

with associated crops in:

    VAULT_ROOT/20_文献/SAFE_PAPER_TITLE/assets/summary-figures/

Use the target title exactly for the readable heading. For Windows path components, remove invalid characters, collapse whitespace, remove trailing dots/spaces, and shorten only the filesystem-safe name when necessary. Preserve a Zotero item key in frontmatter so a shortened folder remains traceable. Honor the user's stated `20_文献` root or requested `20_文献/<direction>` root rather than silently switching to an integration-specific subfolder such as 课题组文献.

## Scope boundary

This skill creates a compact evidence-backed literature summary, not:

- a full paragraph-by-paragraph bilingual translation (use nature-reader);
- a full Sections 01-16 Paper Card or extended critical audit (use paper-deep-reading and nature-paper-card);
- a multi-paper review or bibliography search. Zotero is used only as a read-only source for the resolved paper and its attachment.
