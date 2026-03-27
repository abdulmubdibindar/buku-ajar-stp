---
name: write-tables
description: Guide for creating responsive and properly formatted tables in R Markdown for both HTML and PDF output, incorporating troubleshooting fixes for page margin breaks, OutDec interactions, and responsive wrappers. Use this skill when generating or modifying tables (`kableExtra` or `flextable`).
---

# Write Tables Skill

This project uses `kableExtra` (`kbl()`) as the primary engine for creating tables, with occasional use of `flextable` (e.g., when converting model summaries). This guide documents critical workarounds discovered to ensure tables render flawlessly without breaking page margins in either HTML or PDF (LaTeX) formats.

## 1. Primary Rule: Use `kableExtra`
By default, all custom tables should use the `kbl()` function from `kableExtra`, supplemented by `dplyr` for data manipulation.

### Standard Bulletproof Template
```r
library(knitr)
library(kableExtra)

tbl_out <- kbl(df, 
    caption = "Judul Tabel",
    format.args = list(big.mark = ".", decimal.mark = ","),
    escape = FALSE) |>
  kable_styling(
    bootstrap_options = c("striped", "hover", "responsive"), 
    full_width = FALSE, 
    latex_options = c("scale_down", "HOLD_position")
  ) |>
  # Optional: Forcing text wrapping on long columns to improve scaling
  column_spec(2:4, width = "1.5cm")

# HTML-only Overflow Protection
if (knitr::is_html_output()) {
  tbl_out <- tbl_out |> scroll_box(width = "100%", box_css = "border: 0px;")
}
tbl_out
```

## 2. Preventing Margin Breaks (HTML & PDF)

When tables have many columns or long headers (e.g., "Rumah ngontrak bersama-sama"), they often break out of their parent containers (like `::: rmdkasus` blocks), getting abruptly cut off in HTML or pushed off the page in PDF.

### PDF (LaTeX) Strategy
- **`scale_down`**: Adding `latex_options = c("scale_down", "HOLD_position")` shrinks the entire table proportionately to fit the page width.
- **`column_spec()`**: If `scale_down` makes the text microscopic (because the table is infinitely wide), use `column_spec(..., width = "...")` to explicitly cap column widths. This forces LaTeX to wrap long headers natively, resulting in a much taller but narrower table that doesn't need scaling down aggressively.

### HTML Strategy
- **`scroll_box()` via Conditional Logic**: `kableExtra`'s built-in "responsive" modes often fail when the table sits inside custom CSS blocks with strict boundaries. The most reliable fix is to wrap the finalized table in an explicit horizontal scroll container **only** for HTML output:
  ```r
  if (knitr::is_html_output()) {
    tbl_out <- tbl_out |> scroll_box(width = "100%", box_css = "border: 0px;")
  }
  ```
  *(Failure to use the boolean condition `if (knitr::is_html_output())` will break PDF LaTeX compilation, as `scroll_box()` injects raw HTML `<div style="...">` tags into the `.tex` output!).*

## 3. Working with `flextable`

If you are required to use `flextable` (e.g., via `gtsummary::as_flex_table()`), adhere to the following:

1. **Never use `width="60%"` as a Knitr chunk option!**
   - **Bad**: ````{r, width="60%"}` ➔ Triggers a `non-numeric argument to binary operator` error during rendering, because `knitr` evaluates the option alias `fig.width` expecting a clean numeric integer, completely dying on the string `"60%"`.
   - **Good**: ````{r, out.width="60%"}`
   
2. **Autofitting and Page Margins constraint**
   - Append `autofit()` at the end of the pipeline to shrink column widths perfectly to their contents.
   - If `autofit()` evaluates columns that are still collectively wider than the standard PDF text block geometry (usually 6.5 inches), `flextable` will just run off the page edge. Prevent this by supplementing it with a hard lock:
     ```r
     flextable_obj |>
       autofit() |>
       fit_to_width(max_width = 6.5)
     ```

## 4. Avoiding `paste()` Math Errors under `OutDec`

Be incredibly careful when generating footnotes or captions dynamically using `paste()` or `paste0()`. This project overrides decimal markers via `options(OutDec = ",")`. 

- **Integers are Safe**: Simple counting functions like `nrow(df)` do not contain decimals, so `paste0("Total mahasiswa ", nrow(df))` will process without incident.
- **Floating Decimals Break LaTeX Math**: If you execute `paste0(mean(x))` to render inline equations (like inside `$...$`), it automatically coerces it to a string `"3,14"`. That forced comma triggers crippling syntax errors in LaTeX's parser. Bypass `OutDec` globally on individual insertions using explicit formats:
  ```r
  # CORRECT:
  format(mean(x), decimal.mark = ".", big.mark = ",")
  ```
