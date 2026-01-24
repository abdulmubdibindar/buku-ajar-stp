---
trigger: always_on
---

## Formatting for R Markdown

### General blocks

- Use {.unnumbered} at the end of the title of each blocks

### General chunks

- Use single apostrophe for naming strings

### Images

1. Create chunk id with "-" as separator, e.g. `fig-proses-perencanaan-rasional`
2. Use knitr::include_graphics() to include images
3. Use out.width = '60%' and fig.align = "center" to control image size and alignment
4. Use fig.cap to add image caption
5. Use echo=FALSE to hide code

### Tables

1. Use function `kableExtra` or `kable` to create tables
2. Use `kable_styling` to style tables
3. Use similar styling as in Images from number 3--5

### Equations

1. Follow how to format equations from @guides/equation_guide.md
