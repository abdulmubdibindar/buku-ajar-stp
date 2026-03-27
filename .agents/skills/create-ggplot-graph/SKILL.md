---
name: create-ggplot-graph
description: Guide for creating ggplot2 graphs in R while handling locale-specific decimal markers (commas). Use this skill when generating plots that use mathematical expressions, annotations, or labels in a workspace where `options(OutDec = ",")` is set to ensure R's parser does not fail on comma decimals.
---

# Create ggplot Graph (with Decimal Handling)

This skill provides instructions for creating `ggplot2` visualizations in an environment where `options(OutDec = ",")` is active. This global R option can break mathematical parsing in plots if not handled correctly.

## The Decimal Issue

When `options(OutDec = ",")` is set:
- Numeric values converted to strings (via `format`, `as.character`, or `paste`) use a comma as the decimal separator (e.g., `2,5` instead of `2.5`).
- R's mathematical parser (used by `expression()`, `parse(text=...)`, and `bquote()`) **requires a period** for decimals in code-like syntax.
- **Error Example**: `annotate("text", label = parse(text = "mu == 2,5"))` will throw a syntax error.

## Best Practices & Strategies

### 1. Use `bquote()` for Expressions
Instead of `parse(text = paste0(...))`, use `bquote()`. It handles the insertion of values more cleanly. However, if the value itself is formatted with a comma by R's global state, you may still need to be careful.

```r
# Safe way to insert a value into a math expression
val <- 2.5
annotate("text", x = 0, y = 0, 
         label = bquote(mu == .(val))) 
```

### 2. Force Period in Strings for Parsing
If you must use `parse(text = ...)`, always force the decimal marker to be a period.

```r
val <- 2.5
# Force period for the parser
val_str <- format(val, decimal.mark = ".")
annotate("text", x = 0, y = 0, 
         label = parse(text = paste0("mu == ", val_str)))
```

### 3. Handling Axis Labels
`options(OutDec = ",")` will automatically make `ggplot2` use commas for numeric axis labels. To be explicit or to override this:

```r
library(scales)
scale_x_continuous(labels = label_number(decimal.mark = ","))
```

### 4. Direct Expression Usage
When the decimal is a constant, just hardcode it with a period inside the `expression`.

```r
annotate("text", x = 0, y = 0, label = expression(mu == 2.5))
```

## Safe Use of `paste()` with `OutDec = ","`

When `options(OutDec = ",")` is active, `paste()` and `paste0()` auto-coerce numbers using `format()` internally, which respects `OutDec`. This means:

| Value type | `paste()` output | Safe? |
|---|---|---|
| Integer (`nrow()`, `length()`) | `"25"` (no decimal) | ✅ Always safe |
| Decimal in plain text/footnote | `"3,14"` | ✅ OK for HTML; risky in PDF LaTeX body text |
| Decimal inside `$...$` math | `"3,14"` → LaTeX parse error | ❌ Breaks PDF |

### Rule: Use `format()` with explicit `decimal.mark`

Rather than relying on `OutDec` autocorrection, be explicit:

```r
# For display in plain text (e.g., kableExtra footnote, body text):
paste0("Rata-rata: ", format(mean(x), decimal.mark = ",", big.mark = "."))

# For use inside LaTeX math expressions (fig.cap, equation labels):
paste0("$\\bar{x} = ", format(mean(x), decimal.mark = "."), "$")
```

### kableExtra `footnote()` with integers

`nrow()` and similar integer-returning functions are always safe inside `paste()` — no decimal point means `OutDec` has no effect:

```r
footnote(
  general = paste0("Menampilkan 6 dari ", nrow(tabel), " baris"),
  ...
)
```

## Workflows

1. **Check for OutDec**: Verify if `getOption("OutDec")` is `","`.
2. **Identify Annotations**: Find all `annotate()`, `labs()`, or `geom_text()` calls using mathematical expressions.
3. **Apply Fix**: Use one of the strategies above (preferably `bquote` or forced `decimal.mark = "."`).
4. **Test Render**: Run the code locally to ensure no "unexpected ','" errors occur.

For more detailed examples and troubleshooting, see [decimal-strategies.md](references/decimal-strategies.md).
