# Script untuk memperbaiki semua file Rmd yang memiliki "## Soal Evaluasi" tanpa custom block

# List file yang perlu diperbaiki
files_to_fix <- c(
    "04-visualisasi-data.Rmd",
    "05-pengantar-inferensial.Rmd",
    "06-estimasi-parameter.Rmd",
    "07-uji-hipotesis-satu-populasi.Rmd",
    "08-uji-hipotesis-dua-populasi.Rmd",
    "09-uji-hipotesis-lebih-dua-populasi.Rmd",
    "10-korelasi-nominal.Rmd",
    "11-korelasi-ordinal.Rmd",
    "12-korelasi-metrik.Rmd",
    "13-regresi-sederhana.Rmd",
    "14-regresi-berganda.Rmd",
    "15-multivariat-interdependensi.Rmd"
)

# Fungsi untuk memperbaiki satu file
fix_soal_evaluasi <- function(filename) {
    cat(sprintf("Processing: %s\n", filename))

    # Baca file
    content <- readLines(filename, warn = FALSE)

    # Cari line yang berisi "## Soal Evaluasi"
    soal_eval_line <- grep("^## Soal Evaluasi", content)

    if (length(soal_eval_line) == 0) {
        cat(sprintf("  - No '## Soal Evaluasi' found. Skipping.\n"))
        return(FALSE)
    }

    if (length(soal_eval_line) > 1) {
        cat(sprintf("  - WARNING: Multiple '## Soal Evaluasi' found. Skipping.\n"))
        return(FALSE)
    }

    # Extract nomor bab dari filename (e.g., "04" dari "04-visualisasi-data.Rmd")
    bab_num <- as.integer(substr(basename(filename), 1, 2))
    soal_num <- bab_num + 1 # Soal Evaluasi 5 untuk Bab 4, dst.

    # Ganti "## Soal Evaluasi" dengan custom block rmdexercise
    new_heading <- sprintf("::: rmdexercise\n### Soal Evaluasi %d {.unnumbered}", soal_num)
    content[soal_eval_line] <- new_heading

    # Ubah format capaian dari (STP-X.X) menjadi [STP-X.X]{.capaian}
    content <- gsub("\\(STP-([0-9]+\\.[0-9]+)\\)", "[STP-\\1]{.capaian}", content)

    # Tambahkan closing ::: di akhir file jika belum ada
    if (!grepl("^:::$", tail(content, 1))) {
        content <- c(content, "", ":::")
    }

    # Tulis kembali file
    writeLines(content, filename)

    cat(sprintf("  - Fixed! Changed line %d and added closing fence.\n", soal_eval_line))
    return(TRUE)
}

# Proses semua file
results <- sapply(files_to_fix, fix_soal_evaluasi)

# Summary
cat("\n=== SUMMARY ===\n")
cat(sprintf("Total files processed: %d\n", length(files_to_fix)))
cat(sprintf("Successfully fixed: %d\n", sum(results)))
cat(sprintf("Skipped: %d\n", sum(!results)))

if (sum(results) > 0) {
    cat("\nFiles fixed:\n")
    cat(paste0("  - ", files_to_fix[results], collapse = "\n"))
    cat("\n")
}
