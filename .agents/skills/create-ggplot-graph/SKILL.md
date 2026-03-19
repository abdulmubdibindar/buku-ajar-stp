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

## Workflows

1. **Check for OutDec**: Verify if `getOption("OutDec")` is `","`.
2. **Identify Annotations**: Find all `annotate()`, `labs()`, or `geom_text()` calls using mathematical expressions.
3. **Apply Fix**: Use one of the strategies above (preferably `bquote` or forced `decimal.mark = "."`).
4. **Test Render**: Run the code locally to ensure no "unexpected ','" errors occur.

For more detailed examples and troubleshooting, see [decimal-strategies.md](references/decimal-strategies.md).
