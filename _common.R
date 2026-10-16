# Opsi bersama untuk semua bab. Quarto me-render tiap bab dalam sesi R
# terpisah, jadi berkas ini di-source() dari chunk setup di setiap bab:
#
#   ```{r}
#   #| label: setup
#   #| include: false
#   source("_common.R")
#   ```

options(cli.hyperlink = FALSE)
options(OutDec = ",")

knitr::opts_chunk$set(
  echo = FALSE,
  message = FALSE,
  warning = FALSE
)

# Mengamankan karakter < dan > agar tidak merusak sidebar HTML
safe_html <- function(x) {
  if (knitr::is_html_output()) {
    x <- gsub("<", "&lt;", x)
    x <- gsub(">", "&gt;", x)
  }
  x
}
