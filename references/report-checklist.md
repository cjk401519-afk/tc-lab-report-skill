# TC Lab Report Checklist

Use this checklist for every German Technische Chemie or chemistry lab report produced with `$tc-lab-report-skill`.

## Intake

- Identify the current authoritative DOCX if multiple versions exist.
- Record which files are raw data, which are Skript/Lernstoff, which are Vorgaben, and which are only style references.
- If an older student report is provided, use only writing/formatting style unless the user explicitly authorizes scientific reuse.
- Compare the report content against the teaching PDF tasks before finalizing. Do not add unsupported formulas, diagrams, plots, models, or tasks.
- If a reference report and the teaching PDF both contain the same required figure, table, or evaluation step, include the corresponding item for the user's report. Do not create extra figures or analysis sections that are unsupported by the teaching PDF or the user's data.
- Use the word `Skript` only as an internal source label. Do not write `Skript` in the final report body, captions, appendix, or reference list unless the user explicitly requests it; use natural terms such as `Versuchsanleitung`, `theoretische Grundlage`, or simply present the method.

## Vorgaben Compliance

- Body: Arial 12, 1.5 line spacing, justified.
- Main headings: 14 pt, bold. Default spacing for this user's reports is three blank lines before and two blank lines after, unless the heading begins at the top of a page or the specific Vorgaben state otherwise.
- Subheadings: 12 pt, bold. Default spacing for this user's reports is two blank lines before and one blank line after, unless the heading begins at the top of a page or the specific Vorgaben state otherwise.
- Bold text only where required by the Vorgaben or normal report hierarchy. Remove accidental bold from body paragraphs, formula explanations, and ordinary discussion text.
- Tables: caption above, numbered consistently.
- Tables must never exceed the Word/PDF text block or page margins. Before rendering, check the sum of explicit column widths against the available body width; if a table is too wide, restructure it, split it, abbreviate headers, or use a suitable landscape/appendix layout instead of letting Word crop it.
- Main data and calculation tables should use the available page width generously. Avoid tiny, preview-like tables; adjust column widths, font size, spacing, or split/landscape layout when necessary.
- Tables that technically fit the width but look compressed or miniature are still a QA failure. Increase row height, cell padding, font size, and caption/table spacing, or redesign the table so it reads like a formal report table at normal Word zoom.
- Short formal result tables must not break across pages. If a table is only a few rows, keep it on one page by reducing excessive header wrapping, using compact but readable font size, explicit column widths, cell margins, and row `cantSplit`; move the whole table to the next page if needed.
- Figures: caption below, numbered consistently.
- Figures and tables should not look narrow or thumbnail-like. Use the available page width generously where readability benefits, and keep visible spacing between body text, the graphic/table, its caption/title, and any following figure/table or paragraph.
- Figure legends, labels, annotations, and inset text must not overlap or cover data points, curves, bars, axes, tick labels, titles, captions, or each other. Treat any overlap as a render-QA failure, not a cosmetic preference. If a legend would cover data, move it outside the plotting area, split it, shrink it modestly, or reserve extra margin before exporting.
- For shaded-area plots, labels and operating-condition annotations must not sit on top of the shaded areas. Put conditions in a white margin above the axes, and put A1/A2 explanations in a separate legend or note box instead of printing text over the filled regions.
- If a legend is placed below the axes, keep it visually close enough to belong to the figure. Do not leave a large empty gap between plot body, x-axis label, and legend; reserve just enough margin to prevent overlap.
- Page numbers: present through the document, including pages added late.
- Table of contents: own page, clickable entries, correct page numbers, no unrelated content on TOC page.
- Appendix: use "Anhang 1", "Anhang 2", etc.; if multi-page, use the Vorgaben style such as "Anhang 1 (1/3)".
- Watch for Word artifacts such as black dots or square bullets before headings and TOC entries. They are not acceptable and must be fixed at the XML/style source, not hidden visually.

## Formula And Calculation Blocks

For each important calculated quantity:

1. Introduce the formula in prose before displaying it.
2. Insert the pure formula as a native Word equation when possible.
3. Right-align the equation number in parentheses; check that the closing parenthesis is not clipped.
   Equation numbers such as `(1)` must use one consistent right-side alignment position across the document. Never leave numbering immediately next to the formula body; use a two-column equation layout or a fixed right tab stop so all numbers align vertically.
4. Add a "mit" block directly after the formula.
5. Use a borderless aligned "mit" block, not a formal table: `mit` at the left, then symbol, meaning, and unit columns. Give the meaning column enough width so natural one-line descriptions do not wrap unnecessarily.
   All unit cells in a single `mit` block must share the same alignment, font family, font size, weight, and math rendering. A single unit that appears shifted right/left, bold, larger, or visually different from the other units is a QA failure. Fix the whole `mit` block/table geometry and unit-cell run formatting, not only the visible row.
6. Italicize physical variables; keep units upright.
7. Use SI-compatible units and nonbreaking spaces inside units where Word/PDF might split them, for example `mL min^-1`, `S m^-1`, `s`, `mL`.
8. Add a "Beispielrechnung" using real values from the report.
9. In the `Beispielrechnung ...` sentence, explicitly list the numerical values that will be substituted, including variables and units, e.g. `mit r = 0,04 m, l = 2 m und p = 100 Pa:`. Do not rely on the displayed substitution alone to reveal the input values.
10. Do not put substitutions only as ordinary prose sentences. After the `Beispielrechnung ...` sentence, put the substituted arithmetic as a separate centered formula/display line when it contains a real calculation.
11. Keep substitutions and arithmetic on one line when they fit; do not split every addition, subtraction, multiplication, or unit into separate lines.
12. Avoid visible artificial line-break clutter around formulas.
13. Add enough vertical spacing before and after display formulas so consecutive equations do not look compressed.
14. Render inline mathematical symbols and units professionally as Word math or rich math-styled runs wherever they appear in body text, tables, symbol lists, and example calculations.
15. This is a hard gate, not a style preference: after formula formatting, audit the complete DOCX at least three separate times for plain-text math leftovers. Search body text, tables, `mit` blocks, captions, headers, symbol lists, appendix labels, and generated table cells. Reject the report if any variable/unit is still typed like `m^2`, `m^3`, `s^-1`, `h^-1`, `L^-1`, `R^2`, `Dax`, `uG`, `VG`, `VL`, `EA`, `LF`, `hS`, `epsilon_g`, `εg`, or `εg,lok` instead of being rendered with true superscript/subscript/math styling.
16. If the apparatus records non-SI operating values, convert them for the main report tables, figures, equations, and example calculations. Mention the original instrument reading only when needed for reproducibility, and give the SI conversion directly next to it.
17. For ReportLab/PDF generation, do not hard-code Unicode superscript exponents such as `10⁻⁵` in body/table strings because some bundled fonts render them as square boxes. Keep source text as `10^-5` and let the PDF/math markup convert it to true superscript during rendering.

Common symbols to format carefully:

- `c_T,aus`, `c_T^0`, `E(t)`, `F(t)`, `V_R`, `Vdot`, `tbar`, `t_tot`, `sigma^2`, `tau`, `K`, `RMSE`.
- For fitted model values, explain how the fit was performed and what was minimized.
- When a calculated quantity comes from fitting, interpolation, regression, or numerical integration rather than direct substitution, state the method and show at least one traceable example or intermediate result.

## Figures

- Use Origin-like scientific styling: clean white background, black axes, readable tick labels, meaningful legend, restrained colors.
- For Nature-style report figures, avoid dense minor gridlines or background line patterns that look like noise or moire artifacts in Word/PDF. Prefer a clean white plotting area, restrained palette, readable markers, high-DPI export, and only the minimal grid/axis aids needed for interpretation.
- Axis labels must include SI units.
- When axes logically start at zero, set both axes to show the same origin at `(0, 0)`.
- Remove vertical guide lines unless they are explicitly needed and explained.
- For diagrams based on separate operating points, do not connect data points with lines unless the teaching PDF, a fitted model, or a physically justified interpolation explicitly requires it. Use marker-only scatter plots for discrete measurements and explain trends from point distributions.
- If tau and experimental mean residence time are part of the interpretation, show both or state why one is omitted.
- After each figure, write a focused trend explanation:
  - What does the curve do over time?
  - How do apparatus variants compare?
  - What physical transport, mixing, dead volume, dispersion, or model limitation explains the trend?
  - Does the observation match the teaching PDF or theoretical expectation?
- Keep figure/table layout calm: add breathing room before the item, between image/table and caption/title, after the caption/title, and between consecutive figures/tables.
- Before final delivery, visually inspect every exported figure at the exact size used in the Word/PDF. Reject and redraw any figure where the legend, title, annotation, label, or caption overlaps data marks, curves, bars, tick labels, axis labels, titles, or captions. If needed, use a figure-level legend outside the axes and reserve canvas margin so the plot remains readable.

## Content Quality

- Experimental section: factual, passive Prateritum, no casual process narration.
- Motivation und Zielsetzung must be written as the student's own framing and should not carry literature citations unless the user explicitly asks for them.
- For this user's Technische Chemie reports, the final report should have a comparable substantive volume to the provided senior reports, usually around 20+ pages when the reference reports are that long. Expand with required theory, formula explanations, symbol lists, example calculations, tables, discussion, error analysis, and appendix material; do not pad with unrelated plots or invented tasks.
- Keep theory proportional and task-linked. It should explain only the concepts needed for the experiment, formulas, figures, and interpretation; do not let a long generic theory section crowd out Auswertung, Diskussion, and Fehleranalyse.
- Put more substantive effort into the results/discussion sections than into background theory. Discussion should compare operating conditions, explain mechanisms, and state limitations, not merely repeat table values.
- Results/discussion: interpret rather than recite numbers.
- Error analysis: connect deviations to the real setup and calculation chain. Do not only list possible sources; identify which source likely has the largest influence, whether it is systematic or random, and how it changes the main calculated quantities.
- Prefer a clearly numbered Fehleranalyse when multiple sources are discussed. Each item should have a short label, then 2-4 sentences covering cause, direction of influence, affected calculated quantities, and whether the effect is likely systematic or random.
- Avoid generic AI phrasing, overlong transitions, and unsupported claims.
- If the report uses a model that was not in the teaching PDF, add a verified source and clearly separate it from course-derived content.
- Write the report for the assistant/reader, not for the user. Do not include private rationale or meta-comments about why the group chose an order, saved time, or followed a prompt.

## Style Calibration

When the user provides senior/student reports as style examples:

- Treat them as style references only, not as scientific sources.
- Extract recurring writing traits:
  - section opening style,
  - length and density of paragraphs,
  - how equations are introduced,
  - how "mit" symbol blocks and Beispielrechnungen are phrased,
  - how figures and tables are discussed,
  - how uncertainty/error analysis is worded,
  - how direct and formal the German tone is.
- Do not copy distinctive sentences, uncommon turns of phrase, or experiment-specific content.
- Convert the extracted traits into a short style profile before drafting.
- Use the profile to make the report sound like a real German student lab report: precise, slightly restrained, evidence-led, and not over-polished.
- Add new stable style preferences below when the user explicitly asks to remember them.

Current style profile:

- Calibrated from four Gruppe-8 reference reports on Waermeuebertragung, Mischen und Ruehren, Rohrstroemung/Druckverlust, and Umsatzverhalten.
- Overall voice: formal student-lab German, direct and evidence-led, not journal-polished. Paragraphs are usually medium length and focus on one concrete point rather than a broad rhetorical arc.
- Motivation/Zielsetzung: begin with `Ziel dieses Versuchs ist es ...` or `Im Rahmen des Versuchs wird ...`; then state why the phenomenon matters in technical chemistry and which measured quantities or dimensionless numbers are evaluated.
- Apparatus description: use present-tense factual description for equipment, geometry, sensors, feeds, flow paths, and relevant dimensions. Keep it concrete: what is connected to what, what is measured, and which variants are compared.
- Versuchsdurchfuehrung: use chronological passive Prateritum with connectors such as `Zuerst`, `Danach`, `Anschliessend`, `Nach der Stabilisierung`, `Zum Schluss`. Include operating values and waiting/stabilization times when relevant. Avoid storytelling; write as a lab log converted into prose.
- Auswertung: introduce formulas with short sentences such as `... ergibt sich aus`, `... wird nach Gleichung (...) berechnet`, or `Mithilfe der gemessenen Werte ...`. Then show formula, symbol explanation, example calculation, and resulting table/figure.
- Results/discussion paragraphs usually start from evidence: `Aus Tabelle ... ist erkennbar`, `Aus Abbildung ... geht hervor`, `Im Vergleich ...`. Then state the trend, give one physical reason, and mention exceptions or deviations only when they are visible in the data.
- Trend explanation style: explain mechanisms with direct cause-effect wording (`Dies liegt daran, dass ...`, `Der Grund dafuer liegt darin, dass ...`, `Ein moeglicher Grund ist ...`). Prefer apparatus- and process-specific causes over generic uncertainty language.
- Figure discussion: describe what changes with time or operating condition, compare variants, and connect the shape/trend to theory or measurement conditions. Do not over-describe obvious plotted values.
- Error/deviation analysis: link deviations to unstable readings, sensor response, delayed stabilization, subjective endpoint recognition, air bubbles, flow fluctuations, heat loss, wall roughness, non-ideal mixing, or model assumptions. Keep the explanation plausible and tied to the setup. Do not only list error sources; state which source likely has the largest influence on the calculated results, whether it is systematic or random, and how it changes the key quantities.
- Conclusion: compactly restate the main experimental findings, then one practical/technical implication. Avoid a marketing-like ending.
- Humanization guardrail: imitate the restrained student rhythm, not the reference reports' grammar or typography mistakes. Correct spacing, units, word endings, figure/table numbering, and punctuation while keeping the prose slightly plain and not over-polished.

Reusable pattern from the Adsorption report:

- Motivation can be concise but specific: state the investigated phenomenon, the measured curve/quantity, the two or three comparisons that structure the report, and any special measured condition that later matters for interpretation.
- The experimental part should first anchor the apparatus with concrete components and required setup figures, then describe the real procedure in reproducible chronological paragraphs. For repeated runs, fully describe the first run and then shorten later runs by naming only changed settings and confirming that the same procedure was followed.
- Theory should be modular and short: define only the process concepts needed later, place required teaching figures close to the relevant concept, and bridge immediately to how the quantities are evaluated.
- Auswertungsmethodik should read like a calculation chain: data selection/preprocessing, normalization or correction, characteristic times or variables, then derived quantities. Each formula should have a purpose sentence before it and one traceable example calculation after the symbol block.
- Results and discussion work well when separated by comparison logic: first describe the overall curve behavior, then compare pairs or groups of operating conditions, then connect the trend to transport, residence time, concentration/partial pressure, temperature, or apparatus effects.
- Avoid vague curve labels. Use concrete descriptors such as early/late breakthrough, steeper/flatter rise, wider/narrower transfer zone, plateau deviation, delayed stabilization, or asymmetric tailing, and link each descriptor to a physical reason.
- Good discussion paragraphs follow the rhythm: evidence from table/figure, observed trend, mechanism, caveat. This sounds more student-like than a long abstract explanation.
- Schlussfolgerung should be compact: summarize the main measured trends, state the most reliable evaluation method or comparison, and mention the dominant remaining uncertainty without reopening the whole discussion.
- Appendix material is strongest when it supports traceability without bloating the main text: raw-data previews, original-file links, symbol list, and complete curves belong there when they are useful but not central to the argument.

## References

- Verify every external reference. Prefer DOI/publisher/CrossRef/library sources.
- Do not keep references that cannot be confirmed.
- Numeric citation groups such as `[1, 4, 5]` are allowed if the combined statement is supported by those sources.
- Add citations where theory, external formulae, physical interpretations, or data-processing methods need support.
- Do not cite Motivation und Zielsetzung unless the user explicitly asks; these sections should be written as the student's own framing.

## Appendix And Raw Data

- Do not label every preview internally as "Tabelle 1" or "Abb. A1" unless the Vorgaben require it.
- Prefer appendix headings: `Anhang 1: Rohdaten ...`.
- In each raw-data preview, state file name, experiment mapping, number of measurements, number of columns, and whether only start/end rows are shown.
- Add a clickable link to the original Excel file below each preview when possible.
- Keep previews large enough to read but compact enough not to consume excessive pages.

## Final Render QA

Render DOCX to PDF and PNGs, then inspect:

- Cover page alignment, especially date labels and values.
- TOC page isolation, links, and page numbers.
- Formula layout, variable styling, unit styling, and equation-number alignment.
- Unit columns and symbol lists for unwanted wrapping such as `mL` split from `min^-1`.
- Page numbers after section breaks and appendices.
- Figure captions below and table captions above.
- Main tables should look like formal report tables, not compressed thumbnails; check readability of headers, units, and numbers after rendering.
- Appendix numbering and raw-data links.
- No unexpected blank pages, cropped images, clipped parentheses, black bullets before headings, or text overflow.
- If clickable TOC bookmarks are added manually in OOXML, `w:bookmarkStart` must come after `w:pPr`, not before it; invalid ordering can show black dots or repair artifacts in Word.

## User-Specific Refinements

- Prefer final deliverables as exactly one current DOCX and one PDF when the user asks to reduce clutter.
- After a final DOCX/PDF is accepted, do not keep producing numbered near-duplicate reports. Use `scripts/sync_final_report.py` first in dry-run mode, then with `--commit`, to overwrite same-topic DOCX/PDF copies with the accepted pair and remove obvious intermediate reports such as backups, audit renders, layout-fix drafts, and proposal copies.
- Final-version cleanup must only target same-topic report `.docx` and `.pdf` files. Do not delete or overwrite raw data, Versuchsanleitung/Vorgaben PDFs, images, figures, plotting scripts, or unrelated experiment reports.
- Same-topic report copies may exist in Desktop folders, WeChat received/temp folders, Documents, and iCloud/Obsidian folders. Synchronize all found copies so there is no stale imperfect version that can be submitted accidentally.
- Some WeChat received files are read-only. A sync helper should attempt to make targets writable, continue past individual failures, and print a failure summary instead of stopping halfway.
- When the user provides a screenshot of a Word/PDF issue, inspect the rendered document, find the source in DOCX/XML or build script, fix the generator/source, and re-render.
- In this user's reports, Beispielformel blocks should match the demonstrated style: formula, "mit" symbol list, then concrete Beispielrechnung.
- The required pattern is: formal displayed formula with right-aligned number, directly followed by a `mit` symbol/unit block, then a left-aligned `Beispielrechnung ...` sentence, then the substituted arithmetic as a separate centered formula/display line. Apply this to every important calculated quantity, not only the first one.
- The `Beispielrechnung ...` sentence must name the substituted values before the arithmetic line, including variable symbols and units, like the Vorgaben example `mit r = 0,04 m, l = 2 m und p = 100 Pa:`. Never write only `für denselben Messpunkt` without the actual values.
- When a senior/student report is the requested style and content frame, keep its section logic, figure selection, and report rhythm, but paraphrase the prose. Do not invent a new framework; do not copy sentences. Calculations and data-driven sections must use the user's own data. Fehleranalyse should be based primarily on the user's actual experiment and measurements, with the senior report used only as a style and plausibility reference.
- When the user provides a teammate-revised DOCX, preserve that new framework unless the user explicitly asks for a restructure. Apply corrections locally to calculations, figures, formula rendering, wording, and error analysis instead of rebuilding the report from an older generated structure.
- When the user uploads a newer target DOCX after earlier generated versions, treat the uploaded file as the only source of truth. Before saving, compare embedded media counts and captions against the incoming file; never replace the target with an older generated document or accidentally drop later-inserted figures such as Zeitpunkts-/Rohdaten-/appendix graphics.
- Before recalculating or redrawing any figure, make a small explicit data map from each raw-data file to the actual operating condition. Re-check totals, component ratios, units, and any handwritten/user-corrected settings against the teaching PDF tasks; one wrong raw-data mapping can invalidate all downstream tables, figures, and conclusions.
- Keep theory sections proportionate to the framework in the current report and the reference style. For many TC reports, apparatus/setup and procedure belong early, while detailed Auswertung theory should appear near the results/calculation section and should not overwhelm the experimental narrative.
- For sensor or analyzer plateaus, distinguish the physical set point (`Sollwert`) from the measured/displayed plateau (`Messwert`). Use the measured plateau only when a teaching-PDF method requires normalization of a measured curve; use the actual set flow/composition for mass-flow and loading calculations unless a verified calibration correction is explicitly applied.
- In Fehleranalyse, connect unexpected measured plateaus or offsets to concrete apparatus elements such as flow controllers, bypass/three-way valve switching, gas mixing zone, analyzer calibration/range, leaks, dead volume, or delayed desorption. State how the error propagates into normalized curves, times, loadings, and theory comparisons.
- Versuchsdurchführung must be written for an assistant/reader who needs reproducibility, not as an explanation to the user. Describe concrete operations, apparatus numbers from the setup figure, connection changes, valves/switches, waiting/stabilization steps, measurement points, flow settings, and the real measurement order. Do not include private rationale such as `aus Zeitgründen`; simply state the performed sequence.
- Keep calculations readable and student-like: not too terse, not padded, and no obviously machine-generated line breaks.
- For future reports, allocate page budget deliberately: concise required theory, fuller Auswertung/Diskussion, and a clear Fehleranalyse. Do not compensate for weak analysis by adding generic theory.
- When the same experiment has several runs or parameter settings, build the narrative around comparisons that a reader can follow: same total flow but different composition, same composition but different flow, different temperature, different reactor/geometry, etc. Use these comparison pairs consistently in Motivation, Durchführung, tables, figures, discussion, and conclusion.
- Put actual operating conditions into a compact early table when they determine later calculations or interpretation. Include set values, measured deviations, important temperatures, real file mapping, and any nonstandard operational note that affects reproducibility.
- Fehleranalyse should normally be a numbered list with meaningful mini-headings, not one dense paragraph. Start with the largest or most direct uncertainty, then secondary apparatus/data-processing effects. Each point should say how the error would shift times, slopes, normalized curves, calculated loadings/yields, or model comparison.
- Do not over-cite or over-theorize. Motivation/Zielsetzung remain uncited unless requested; references should support theory, formulas, methods, and physical interpretation, while the student's own data discussion should lead.
- Recurring Word issue: black square/dot artifacts before headings or TOC lines are not acceptable. Check heading paragraphs and manually inserted bookmarks/list metadata in OOXML and rebuild until the artifact source is removed. In Word this is often caused by paragraph pagination flags such as `w:keepNext`, `w:keepLines`, `w:pageBreakBefore`, or `w:suppressLineNumbers`; remove these from heading styles and heading paragraphs, then audit that all counts are zero.
- Recurring table issue: when the user says tables are too narrow/small, do not only change font size. Write explicit table geometry (`tblGrid`, `tblW`, per-cell `tcW`, and cell margins), use nearly the full text width for formal data tables, and re-render representative pages before delivery.
- Recurring table spacing issue: table captions, tables, and following body text must never look glued together. For every formal table, set a small caption-to-table gap and a clearly visible post-table gap before the next paragraph. Verify this visually in the Word/PDF render, especially after compact tables that fit within one page.
- Recurring formula issue: never leave physical quantities as plain concatenated text such as `tD,korr`, `ttot`, `VCO2`, `mCO2`, `XCO2,D`, `hZ`, `Vtot`, `pnorm`, or `Tnorm`. In display equations, rebuild them as native Word math with true subscripts/superscripts/overdots; in body text, symbol lists, and tables, use Word rich-text subscript/superscript formatting or native inline math. Overdotted quantities such as `Vdot` and `mdot` should use a real Word math accent, not a fragile precomposed or combining Unicode dot. After every formula pass, audit the whole DOCX text/XML for these plain patterns and fix all remaining occurrences before delivery.
- Recurring unit-rendering issue: units are formulas too. Never leave caret notation such as `[m^2]`, `[m^3 s^-1]`, `L h^-1`, `cm^2 s^-1`, `mol L^-1`, or `R^2` visible in Word/PDF. Superscripts must be real superscripts, units upright, and variables italic/subscripted. Perform three passes: (1) XML/text search for caret patterns and concatenated symbols, (2) visual PDF page check around every formula/table/symbol list, (3) final grep after Word export to confirm no known leftover patterns remain.
- Recurring `mit`-block issue: do not mix ordinary text runs and Word math runs in the unit column in a way that changes weight, size, or baseline. Standardize every unit cell in a `mit` block as non-bold Arial 12 with native math/rich superscripts, equal cell margins, vertical centering, and one consistent unit-column width. Scan all formula explanation blocks, not only the screenshot location.
- Recurring abbreviation/data-table issue: any abbreviated entry such as `n. b.` must be explained directly below the table and tied to the calculation logic. State whether values were excluded from later evaluation and why, for example a near-zero/negative denominator, unstable back-calculation, or physically meaningless result.
- Recurring source-of-truth issue: when a teammate has reinserted figures, Zeitpunkts tables, raw-data images, or appendix material into a newer DOCX, preserve them. Before and after editing, compare media count, captions, and appendix headings; never replace the target with an older generated document that drops these materials.
- Teacher-comment pattern from Waermeuebertragung: apparatus descriptions should not be a loose component list. Explain the functional chain so the reader understands how the setup works, preferably in active factual wording where appropriate: which component heats, pumps, measures, transfers, returns, or controls which stream.
- Teacher-comment pattern: every vague operating phrase such as `moeglichst konstant`, `schwankt`, `gering`, `hoeher`, `deutlich`, or `unterschiedlich` must answer: what exactly varies, over what range, why it matters for the calculation, and whether it changes the comparison.
- Teacher-comment pattern: when measurement locations matter, name them. For each temperature, pressure, concentration, level, or flow value used in calculations, state where it was measured and which physical loss or delay can occur between that point and the ideal balance boundary.
- Teacher-comment pattern: tables and figures used for comparison must contain the variables needed for that comparison. If the discussion compares Gleichstrom/Gegenstrom, temperatures, or volume flows, the relevant flow rates/temperatures must be visible in the same table or figure, not hidden pages away.
- Teacher-comment pattern: if data points or operating cases are indexed, the same index must be used consistently in raw data, tables, figures, captions, and text. Do not introduce point labels that cannot be found in the original measurement table or appendix.
- Teacher-comment pattern: figure axes must name the real independent variable. Do not use a physical surface or object name as an axis label when the plotted coordinate is actually an axial position, measuring point, time, flow rate, or another derived coordinate.
- Teacher-comment pattern: discussion must state the actual dependency, not only that there is an influence. Write whether the quantity increases, decreases, saturates, changes sign, becomes less reliable, or is indistinguishable within uncertainty. Avoid `schwammig` claims.
- Teacher-comment pattern: when comparing two operating modes, explicitly judge whether the observed difference is larger than the estimated measurement uncertainty. If uncertainty was recorded, do at least a rough plausibility estimate before claiming a meaningful difference.
- Teacher-comment pattern: calculated loss terms such as heat loss, mass loss, or deviation balances require their own short evaluation. State sign convention, what positive/negative means, likely physical path such as tubing, wall, sensor position, environment, bypass, or storage, and how the term depends on flow rate or temperature.
- Teacher-comment pattern: not every possible error source is relevant. Before listing effects such as metal-wall heat capacity, tubing losses, or sensor delay, ask whether the effect can realistically be observed in the recorded steady-state data and whether it affects the main comparison.
