---
name: reflow-text
description: Reorganizes the chapter presentation flow to match concept-case-exercise structure
---

# Chapter Text Reflow

This skill reorganizes the presentation flow of a chapter to follow a **Concept → Case → Exercise** structure, improving clarity and pedagogical effectiveness.

## Workflow

1.  **Read & Parse**: Read the existing R Markdown chapter file.
2.  **Identify Sections**: Recognize and separate the following components:
    - **Concept Section**: Theoretical explanation of the topic.
    - **Case Section**: Real-world application or study case.
    - **Exercise Section**: Practice problems for the reader.
3.  **Reorder**: Rearrange the content into the standard order: Concept → Case → Exercise.
4.  **Update Rmd**: Write the reorganized content back into the R Markdown file.

## Best Practices

- The files `01-konsep-dasar.Rmd` through `05-pengantar-inferensial.Rmd` serve as reference examples for the intended presentation flow.

## Formatting Rules

- Maintain the use of Bahasa Indonesia for all text.
- Italicize non-Indonesian words.
- Use comma (`,`) for decimal separators and period (`.`) for thousands separators.
- Use custom blocks as defined in the original file:
  - `rmdcapaian` for "Capaian Pembelajaran"
  - `rmdnote` for "Catatan"
  - `rmdexercise` for "Soal Latihan"
  - `rmdkasus` for "Studi Kasus"
- Use code chunks for tables and figures.
- Recreate mathematical figures using `ggplot2` and save them in the `figures/` folder.
- For external images, insert a `FIXME` placeholder in the Rmd file and save the image in `figures/`.
- Use cross-references: `\@ref(fig:label)`, `\@ref(tab:label)`, or `\@ref(eq:label)`.

## Coding Rules

- Use `tidyverse` (including `ggplot2`) for data manipulation and visualization.
- Use the base R pipe operator `|>`.
- Use `knitr::include_graphics` for figures with `out.width = '60%'` and `fig.align = "center"`.
- Use `kbl` for formatting tables.
- Hide non-essential source code with `echo=FALSE` in chunks.

## Equations

Refer to `@equation_guide.md` for rules on formatting equations.

## Documentation

Refer to `@official_documentations.md` for information not covered here.
