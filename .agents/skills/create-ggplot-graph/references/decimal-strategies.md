# Complex Strategies for Decimal Markers in ggplot2

This document details advanced scenarios where `options(OutDec = ",")` might interfere with `ggplot2` rendering and how to resolve them.

## Scenario: Dynamic Mathematical Labels

When labels are generated dynamically based on calculated statistics (e.g., p-values, Z-scores), the risk of "comma-parsing" errors is highest.

### Problematic Pattern
```r
z_score <- 1.96
# If OutDec = ",", this becomes "Z == 1,96"
label_str <- paste0("Z == ", z_score)
# Fails because R parser doesn't like 1,96
p <- p + annotate("text", label = parse(text = label_str))
```

### Recommended Solution: `sub()` or `format()`
```r
z_score <- 1.96
# Method A: Use format to force the marker
label_str <- paste0("Z == ", format(z_score, decimal.mark = "."))

# Method B: Global Replacement (safest if you have many numbers)
label_str <- gsub(",", ".", paste0("Z == ", z_score))

p <- p + annotate("text", label = parse(text = label_str))
```

## Scenario: Combining Math and Text with Commas

If your label contains *both* a math expression and a descriptive text where the user *wants* a comma (e.g., "Rata-rata = 2,5"), use `paste()` inside `expression()` carefully.

```r
val <- 2.5
# Use a string literal for the part that should display a comma
p + annotate("text", x = 0, y = 0, 
             label = bquote(mu == .(format(val, decimal.mark = ","))))
```

## Scenario: Rendering in RMarkdown

In `.Rmd` files, if the setup chunk has `options(OutDec = ",")`, every subsequent chunk is affected. 

1. **Inline R**: `r round(2.5, 1)` will show `2,5`.
2. **Knitr Tables**: Numbers will have commas.
3. **Plots**: Axes will have commas, but `annotate` expressions MUST use periods for logic/constants.

### Tip: Helper Function
If your plot has many annotations, define a small helper:

```r
math_val <- function(x) format(x, decimal.mark = ".")

annotate("text", label = parse(text = paste0("sigma == ", math_val(sd_val))))
```

## Troubleshooting
If you see the error:
`Error in parse(text = text) : <text>:1:10: unexpected ','`

It almost certainly means a number like `0,05` was passed to `parse()` instead of `0.05`. Use `math_val` or `gsub` as shown above.
