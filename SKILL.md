---
name: tc-lab-report-skill
description: Write, revise, format, and QA German Technische Chemie lab reports from Excel/raw data, Skript/Lernstoff PDFs, Vorgaben PDFs, DOCX drafts, and reference reports. Use when the user asks for a full Versuchsauswertung, German lab report text, DOCX/PDF delivery, formula professionalization, Origin-like academic plots, appendix/raw-data previews, citation verification, TOC/page-number fixes, teacher-comment revision, or when the user asks to remember/refine TC lab-report preferences for future reports.
---

# TC Lab Report Skill

## Purpose

Create German Technische-Chemie university lab reports that are scientifically grounded, Word/PDF-ready, and aligned with the user's local Vorgaben. Treat this as a full report-production workflow, not just text generation.

Before writing or editing a report, load `references/report-checklist.md`. Use it as the standing checklist and update it when the user explicitly says a new preference should be remembered or the skill should be refined.

## Source Priority

1. Use the user's experiment data, existing draft, Skript/Lernstoff PDF, and Vorgaben PDF as primary sources.
2. Use older/senior reports only for structure, tone, and formatting patterns unless the user explicitly says their scientific content is relevant.
3. Do not invent formulas, tasks, theory, or citations. If a formula or task is not in the Skript, mark it as an external model and cite a verified source, or remove it.
4. Preserve the user's scientific results unless the user asks for recalculation or the numbers are demonstrably inconsistent.
5. When the user provides a newer DOCX, treat it as the current source of truth and build on it instead of reverting to older generated versions.

## Workflow

1. Inspect inputs first.
   - Read PDFs for required report structure, evaluation tasks, formulas, appendix rules, citation expectations, and formatting rules.
   - Read Excel files with a structured parser. Map each file to the corresponding experiment before plotting or calculating.
   - Inspect existing DOCX structure and rendered pages before making layout-sensitive edits.

2. Build or revise the analysis.
   - Reproduce calculations from the raw data where needed.
   - Keep a transparent chain from formula to symbol explanation to example calculation to result.
   - For fitted quantities such as equivalent tank number K, state that K comes from fitting/minimizing the deviation between measured response and model response, not from a single substituted point.

3. Write in report style.
   - Use natural German suitable for a real student lab report.
   - If the user provides senior/student reports for style calibration, extract only reusable style traits: sentence length, paragraph rhythm, section transitions, formula-explanation pattern, discussion depth, and typical German phrasing. Do not copy distinctive wording or scientific content.
   - Use passive Prateritum for the experimental procedure.
   - Write discussion paragraphs that explain trends mechanistically and compare experiment with theory. Avoid filler such as calling a curve "S-shaped" unless that is technically the point.
   - After each important figure, add a compact interpretation: what changes over time, what differs between apparatus variants, and what physical/theoretical reason explains it.

4. Format formulas and calculations.
   - Use native Word equations for numbered display formulas whenever possible.
   - Keep equation numbers fixed and right-aligned in parentheses, with the closing parenthesis fully visible in Word and PDF.
   - Use the required calculation block pattern: pure formula, then "mit" symbol list with units, then "Beispielrechnung" with actual values and final result.
   - Keep arithmetic on one line when it fits. Do not split every addition/subtraction or unit into separate lines.
   - Italicize physical variables, render subscripts/superscripts/dots/bars professionally, and keep units upright.

5. Make academic figures.
   - Prefer clean Origin-like plots: white background, black axes, subtle grid if helpful, readable legends, SI units on axes, synchronized zero origin where relevant.
   - Remove unnecessary guide lines. Add tau and experimental mean residence time markers only when they serve the analysis or the user asks for them.
   - Include diagrams required by Skript tasks, including supplementary Aufgaben when requested.

6. Assemble the DOCX.
   - Apply the Vorgaben formatting: Arial 12 body, 1.5 line spacing, justified body text, main headings 14 bold, subheadings 12 bold.
   - Keep tables captioned above and figures captioned below unless the local Vorgaben state otherwise.
   - Put the table of contents on its own page, with page numbers and clickable internal links.
   - Preserve page numbering through all sections after content changes.
   - Use appendix titles such as "Anhang 1", "Anhang 2"; if a single appendix spans multiple pages, use "Anhang 1 (1/3)" style when required.
   - For raw-data previews, make them compact but readable, state data volume plainly, and provide clickable links to the original Excel files.

7. Verify references.
   - Use the provided Skript and Vorgaben as local sources where appropriate.
   - Verify all external references through a real source such as DOI/CrossRef, publisher pages, library catalogues, PubMed, or official documentation.
   - Do not include any citation that cannot be verified.
   - Numeric grouped citations such as "[1, 4, 5]" are acceptable when all cited sources support the same statement.

8. Render and QA before final delivery.
   - Use the documents skill and its DOCX render workflow when editing `.docx`.
   - Render DOCX to PDF and page PNGs after layout-sensitive changes.
   - Inspect every page for formula clipping, equation-number alignment, unit wrapping, TOC links/page numbers, page numbers, captions, image placement, appendix labeling, cover-page alignment, blank pages, and overflow.
   - Deliver both DOCX and PDF when the user asks for final output.

## Iteration Rule

When the user says that a correction should be remembered for future lab reports, update this skill before or after completing the requested report change. Put recurring preferences and failure modes in `references/report-checklist.md` under "User-Specific Refinements"; edit `SKILL.md` only when the workflow itself changes.

When the user provides senior/student reports to reduce AI-like writing, summarize the style profile in `references/report-checklist.md` under "Style Calibration". Update that profile as more examples arrive.
