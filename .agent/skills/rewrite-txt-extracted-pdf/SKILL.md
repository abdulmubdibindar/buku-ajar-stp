---
name: rewrite-txt-extracted
description: Cleans and converts raw text extracted from a Statistics in Planning PDF textbook into R Markdown (Rmd) files for compilation.
---

# TXT to Rmd Book Rewriter

This skill cleans and converts raw text extracted from the _Statistics in Planning_ textbook into structured R Markdown (Rmd) files for HTML or PDF book compilation.

## Workflow

1. **Check Encoding**: Check the encoding of the `.txt` files. If the encoding is not UTF-8, convert it to UTF-8.
2. **Read & Parse**: Read the encoded `.txt` files and parse according to these rules:
   1. check if it is a chapter or subchapter heading. Indicated by _Bab_ for chaptersor _<number>.<number>_ for subchapters.
   2. check if there is an intercepting page number. Indicated by number in one line appear between two lines of text. If found, remove it.
   3. check if there is table or picture.
3. **Verify Against PDF**: Compare the extracted text with the original PDF. Correct any errors to ensure an accurate representation.
4. **Write to Rmd**: Update the specified existing R Markdown file. Modify its contents as needed to faithfully reflect the PDF.

## Formatting Rules

- Prioritize Bahasa Indonesia; _italicize_ non-Indonesian words.
- Use a comma (`,`) for decimals and a period (`.`) for thousands separators.
- Use custom blocks:
  - `rmdcapaian` for "Capaian Pembelajaran"
  - `rmdnote` for "Catatan"
  - `rmdexercise` for "Soal Latihan"
  - `rmdkasus` for "Studi Kasus"
- Use code chunks for tables and figures.
- Recreate mathematical figures using `ggplot2` whenever possible and save them in the `figures/` folder.
- For external images, insert a `FIXME` placeholder in the Rmd file and save the image in `figures/`.
- Use cross-references: `\@ref(fig:label)`, `\@ref(tab:label)`, or `\@ref(eq:label)`.

## Coding Rules

- Use `tidyverse` (including `ggplot2`) for data manipulation and visualization.
- Use the base R pipe operator `|>`.
- Use `knitr::include_graphics` for figures, applying `out.width = '60%'` and `fig.align = "center"`.
- Use `kbl` for formatting tables.
- Hide non-essential source code with `echo=FALSE` in chunks.

## Reference

Match text citations with the PDF's Reference section and use `referensi.bib` for the correct citation keys.

## Equations

Refer to `@equation_guide.md` for rules on formatting equations.

## Documentation

Refer to `@official_documentations.md` for information not covered here.
