library(dplyr)
library(kableExtra)

dfb_vals <- c(1:30, 40, 60, 120, 1000)
dfw_vals <- c(1:30, 40, 60, 120, 1000)

fmt_f <- function(x) {
  formatC(x, digits = 2, format = 'f', decimal.mark = ',')
}

mat <- outer(dfw_vals, dfb_vals, function(dfw, dfb) {
  fmt_f(qf(0.95, dfb, dfw))
})

tbl <- as.data.frame(mat)
colnames(tbl) <- as.character(dfb_vals)
tbl <- cbind(`dfw` = c(as.character(1:30), '40', '60', '120', '\u221e'), tbl)

tbl |>
  kbl(
    caption = 'Tabel Distribusi F pada Tingkat Signifikansi $\\alpha = 5\\%$',
    align   = c('c', rep('c', length(dfb_vals))),
    escape  = FALSE,
    booktabs = TRUE
  ) |>
  kable_styling(
    full_width        = FALSE,
    bootstrap_options = c('striped', 'hover', 'condensed')
  ) |>
  add_header_above(c(' ' = 1, 'dfb' = length(dfb_vals))) |>
  column_spec(1, bold = TRUE)
