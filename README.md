# TC Lab Report Skill

Codex skill for German Technische-Chemie lab reports. It is built from repeated report revisions and teacher feedback across residence-time behavior, heat transfer, adsorption, mixing/stirring, and related TC practical reports.

The skill is intentionally strict: it should not only write text, but also inspect sources, calculate from raw data, build academic figures, format DOCX/PDF output, and catch the layout problems that repeatedly appeared during previous reports.

## What This Skill Does

- Reads raw data, Versuchsanleitung/Lernstoff PDFs, Vorgaben PDFs, existing DOCX drafts, and senior/student reference reports.
- Produces or revises German lab reports in a natural student style.
- Keeps the current DOCX framework when the user or teammate has already edited it.
- Recalculates data-driven sections when raw data mappings change.
- Builds Word-ready formulas, example calculations, tables, figures, references, appendix material, TOC, page numbers, and final PDF.
- Runs visual QA by rendering DOCX to PDF/PNGs and checking for layout defects.

## Installation

Copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R tc-lab-report-skill ~/.codex/skills/
```

Then invoke it with:

```text
$tc-lab-report-skill
```

## Source Priority

1. The user's raw data and newest DOCX are the source of truth.
2. The Versuchsanleitung/Lernstoff PDF defines required tasks, formulas, figures, and evaluation scope.
3. The Vorgaben PDF defines formatting.
4. Senior/student reports are style references only unless the user explicitly says their scientific content is relevant.
5. External references must be verified. No fabricated citations.

## Complete Problem Checklist From Previous Reports

For a Chinese full catalog of all recurring issues and failure modes, see `PROBLEM_CATALOG.zh-CN.md`.

### Source And Scope Problems

- Do not invent formulas, models, tasks, diagrams, or figures that are not required by the teaching PDF.
- If a formula is not in the teaching PDF, either remove it or clearly cite a verified external model.
- Compare the final report against every Aufgabe in the teaching PDF before delivery.
- Required figures from the teaching PDF must appear near the relevant theory, procedure, or Auswertung section.
- Do not add extra plots only because they look useful; every plot must support a required task or stated comparison.
- Never write the word `Skript` in the report body as a meta-source label; use natural phrasing such as `Versuchsanleitung`, `theoretische Grundlage`, or direct method description.

### Raw-Data And Calculation Problems

- Before plotting or calculating, map every raw-data file to the exact run, apparatus, flow, temperature, concentration, and measurement order.
- Re-check totals, ratios, units, and handwritten/user-corrected settings before calculations.
- When raw data are corrected later, recalculate all dependent figures, tables, formulas, and conclusions.
- Distinguish set points from measured plateaus. Use set flow/composition for mass-flow and loading calculations unless a verified calibration correction is required; use measured plateaus only for measured-curve normalization when appropriate.
- If apparatus records non-SI values, raw-data tables may keep original units, but calculation tables, formulas, and main report results should use SI-compatible units or give immediate conversions.
- Density, viscosity, and other material properties must come from the provided appendix/table or a verified reference, not guessed values.
- For fitted values such as `K`, state the fitting/minimization method and what was minimized. Do not present fitted values as if they came from one substituted point.
- When values are obtained by numerical integration, interpolation, regression, or graphical construction, state the program and method, e.g. Python/Origin/Matplotlib, trapezoidal rule, minimum area difference.
- If a teacher asks "und für Messung 2 und 3?", include the corresponding diagrams or results for all runs, not only a text sentence for the first run.

### Formula And Example-Calculation Problems

- Use native Word equations for display formulas whenever possible; do not insert formulas as screenshots.
- Equation numbers such as `(1)` must be right-aligned at one fixed position. Never leave the number glued to the formula body.
- Check that the closing parenthesis of every equation number is visible in Word and PDF.
- Physical variables must be italic; units must be upright.
- Render subscripts, superscripts, overdots, overbars, Greek letters, and fractions professionally.
- Do not leave plain text symbols such as `tD,korr`, `ttot`, `VCO2`, `mCO2`, `XCO2,D`, `hZ`, `Vtot`, `pnorm`, or `Tnorm`.
- Formula symbol lists, body text, tables, and example-calculation sentences must also format variables and units professionally.
- Keep arithmetic on one line when it fits; do not split every number, plus/minus sign, or unit into separate lines.
- Avoid visible artificial line-break clutter around formulas.
- Add enough vertical spacing before and after formulas so consecutive equations do not look compressed.
- Every important calculation must follow this pattern:
  1. prose introduction,
  2. pure formula,
  3. `mit` symbol/unit block,
  4. `Beispielrechnung ...` sentence naming the actual substituted values with units,
  5. substituted arithmetic line,
  6. result.
- The `Beispielrechnung` sentence must explicitly list values, e.g. `mit r = 0,04 m, l = 2 m und p = 100 Pa:`. Do not rely only on the arithmetic line.
- If a formula produces `K`, `F(t)`, `t_stoech`, `RMSE`, or another derived quantity, show enough intermediate calculation that the reader can trace where it came from.

### Word Formatting Problems

- Body text: Arial 12, 1.5 line spacing, justified.
- Main headings: 14 pt, bold, with required spacing before/after unless at page top.
- Subheadings: 12 pt, bold, with required spacing before/after unless at page top.
- Remove accidental bold from ordinary body text and formula explanations.
- Table of contents must be on its own page, have aligned page numbers, and be clickable.
- Page numbers must continue after added pages, section breaks, references, and appendices.
- Fix black square/dot artifacts before headings or TOC entries at the XML/style source. Do not hide them visually.
- Avoid Word repair artifacts from invalid bookmark placement, list metadata, or heading pagination flags.
- Cover-page metadata such as date and supervisor names must align cleanly.
- Do not allow units to split across lines, e.g. `mL` on one line and `min^-1` on the next.

### Table Problems

- Tables need captions above and consistent numbering.
- Formal result tables should use the page width generously; they must not look like tiny thumbnails.
- Tables must not exceed page width or be cropped by Word/PDF margins.
- Short tables should not split across two pages. Use explicit geometry, row `cantSplit`, or move the whole table to the next page.
- Tables that fit but look too compressed are still a failure: increase width, row height, padding, or split/landscape if necessary.
- Captions, tables, and following text need visible spacing; they must not look glued together.
- Headers and units must remain readable and not wrap into awkward fragments.
- Use explicit table geometry: `tblGrid`, `tblW`, per-cell `tcW`, cell margins, and intentional alignment.
- Raw-data previews should be readable but compact. State file name, run mapping, measurement count, column count, and whether only start/end rows are shown.

### Figure And Plot Problems

- Plots should look Origin-like or Nature-style: clean white background, black axes, readable ticks, restrained colors, high DPI.
- Avoid dense background grids that look like noise or moire in Word/PDF.
- Axis labels need units.
- If axes logically start at zero, show a clear `(0, 0)` origin.
- Remove unnecessary vertical guide lines unless they are needed and explained.
- Do not connect discrete operating points with lines unless physically justified or explicitly required.
- Legends, labels, annotations, and inset text must not overlap curves, points, shaded areas, axes, tick labels, titles, captions, or each other.
- For shaded-area plots, do not put labels or operating conditions on top of the shaded regions. Put conditions in a white margin above the axes and A1/A2 explanations in a legend or note box.
- If a legend covers data, move it outside the plot, split it, shrink it modestly, or reserve extra margin.
- If a legend is below the plot, keep it close enough to belong to the figure; avoid a large empty gap.
- Screenshots from the teaching PDF must be complete, not cropped. If needed, crop out the original figure number but keep the content intact.
- Figure captions go below figures. Leave clear spacing between text, image, caption, and following paragraphs.
- Figures and tables should not be narrow or too small. Use the available text width where readability benefits.
- After important figures, add a focused trend explanation: what changes, how variants compare, and what physical reason explains it.

### Content And Writing Problems

- Motivation und Zielsetzung should be written as the student's own framing and normally should not contain citations.
- Use senior/student reports only for style, structure, rhythm, and formatting patterns. Paraphrase; do not copy distinctive wording.
- Versuchsdurchfuehrung must be reproducible: apparatus numbers, valves, connections, measurement order, settings, waiting/stabilization steps, and the real workaround for broken equipment.
- Write procedure in passive Prateritum and avoid private rationale such as `aus Zeitgründen`.
- Theory should be concise and tied to the tasks. Do not let generic theory crowd out Auswertung and Diskussion.
- Results and discussion should interpret trends mechanistically, not merely recite table values.
- Avoid vague filler such as calling a curve "S-shaped" unless the shape itself is technically important.
- Compare runs using a clear logic: same total flow different composition, same composition different flow, different temperature, different geometry, etc.
- Explain unexpected results through apparatus and process mechanisms, not generic "device aging" alone.
- Reports should have a substantive volume comparable to provided senior reports when those are 20+ pages, but never pad with unrelated content.

### Fehleranalyse Problems

- Fehleranalyse should usually be a numbered list with meaningful mini-headings.
- Start with the largest or most direct uncertainty.
- Each item should describe cause, direction of influence, affected quantities, and whether the effect is systematic or random.
- Tie errors to concrete apparatus elements such as sensors, hoses, valves, flow controllers, gas mixing zone, dead volume, leaks, delayed desorption, heat loss, or unstable thermostat readings.
- Explain how errors propagate into normalized curves, times, slopes, loadings, yields, heat transfer coefficients, or model comparison.
- Do not make Fehleranalyse disproportionately long compared with the rest of the report.

### References Problems

- Verify every external source through DOI, publisher page, CrossRef, PubMed, library catalogue, or official documentation.
- Do not copy references from senior reports blindly.
- Every reference in the reference list must be cited in the text.
- Grouped citations such as `[1, 4, 5]` are acceptable when the statement is supported by all cited sources.
- Use about 5-8 references when the task calls for external references unless the user asks otherwise.

### Appendix Problems

- Use `Anhang 1`, `Anhang 2`, etc.; if one appendix spans pages, use the required style such as `Anhang 1 (1/3)`.
- Do not label raw-data previews as repeated `Tabelle 1` or unnecessary `Abb. A1` unless required.
- Include clickable links to original raw-data files when possible.
- Appendix material should support traceability without bloating the main text.

### Final QA Problems

- Render DOCX to PDF and page PNGs before delivery whenever layout matters.
- Inspect every page, not only the page just edited.
- Check formula clipping, equation-number alignment, unit wrapping, TOC links, page numbers, captions, image placement, appendix labels, cover alignment, blank pages, table size, and overlap.
- When a screenshot shows a Word/PDF issue, fix the source or generator and re-render; do not hide the symptom.
- If teacher comments exist, extract every comment first, rank by difficulty, and fix them without deleting material that should instead be cited or cross-referenced.

## Repository Contents

- `SKILL.md` - main skill workflow.
- `references/report-checklist.md` - detailed standing checklist and accumulated user preferences.
- `scripts/sync_final_report.py` - helper to overwrite same-topic old DOCX/PDF report copies with the accepted final pair and remove obvious intermediate drafts.
- `agents/openai.yaml` - display metadata.

## Final-Version Cleanup Helper

After a final report has been accepted, run a dry-run first:

```bash
python3 scripts/sync_final_report.py \
  --docx "/path/to/final.docx" \
  --pdf "/path/to/final.pdf" \
  --topic "stoff chemischer reaktion"
```

If the planned overwrite/delete list is correct, apply it:

```bash
python3 scripts/sync_final_report.py \
  --docx "/path/to/final.docx" \
  --pdf "/path/to/final.pdf" \
  --topic "stoff chemischer reaktion" \
  --commit
```

The helper only targets same-topic `.docx`/`.pdf` report files. It is not for raw data, teaching PDFs, images, or scripts.

## Maintenance Rule

When a new recurring issue appears, update `references/report-checklist.md`. Only edit `SKILL.md` when the overall workflow changes.
