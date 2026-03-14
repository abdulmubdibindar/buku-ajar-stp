---
name: add-block
description: Adds custom blocks (like rmdnote, rmdkasus, rmdexercise) to R Markdown files following specific formatting and content rules. Use this skill when asked to add a block to the document.
---

# Add Block Skill

Follow these instructions when asked to add a custom block to an R Markdown document.

## General Guidelines

- Add the custom block according to the prompt.
- **Do not add questions yourself**. Let the user add the questions. Instead, just add the corresponding learning outcome code.
- Place the block so there is a space (blank line) at the beginning and at the end of the fence to avoid HTML rendering errors.
- Be careful with the use of `>` or `<` signs as they can interfere with HTML rendering. Use them in a way that won't disrupt the output.
- **Clarification**: If you get confused, ask clarifying questions before proceeding to the next task.

## Formatting the Block Container

### Titles and Headings
- Inside each container (such as `rmdnote` or `rmdkasus`), format the first line of the container such that it becomes the appropriate heading for the title.
- Use `{.unnumbered}` at the end of the title of each block.
- For `rmdkasus` (cases), use a 3rd-level heading (`###`), and begin the title with "Studi Kasus: ". Modify details for the title based on the context of the case. 
- For `rmdnote` (notes), use a 3rd-level heading (`###`), and begin the title with "Catatan: ".
- For `rmdexercise` (exercises), use a 2nd-level heading (`##`).

### Exercises (`rmdexercise`)
- Add learning outcome code provided by `rmdcapaian` for each problem sentence.
- Add a sequential number that spans across all parts of the module. Be aware of the current order of the numbering.

### Cases (`rmdkasus`)
- Prioritize using datasets in the `datasets` folder as the foundation of the case.
- Prefer simpler, more concise, and more efficient language use.

## General R Markdown Formatting

### Text and Numbers
- Use `,` for decimal and `.` for thousand separator.

### Code Chunks
- Use single apostrophe for naming strings.
- Use `|>` for the pipe operator.

### Images
1. Create chunk id with "-" as separator, e.g. `fig-proses-perencanaan-rasional`.
2. Use `knitr::include_graphics()` to include images.
3. Use `out.width = '60%'` and `fig.align = "center"` to control image size and alignment.
4. Use `fig.cap` to add image caption.
5. Use `echo=FALSE` to hide code.
6. For data viz, use `ggplot2` mainly to construct the diagrams.

### Tables
1. Use function `kbl` to create tables.
2. Use `kable_styling` to style tables.
3. Use similar styling as in Images from number 3--5.
4. Use `dplyr` package mainly to process dataset.

### Equations
- Follow how to format equations from `@guides/equation_guide.md`.
