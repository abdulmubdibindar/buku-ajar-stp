# render_book.R
# Skrip untuk merender buku ke berbagai format tanpa konflik cache

render_html <- function() {
  cat("Memulai render format HTML...\n")
  tmpdir <- tempfile()
  dir.create(tmpdir)
  
  # Copy file ke tempdir
  fs::dir_copy(".", tmpdir)
  
  # Bersihkan _freeze jika terbawa
  if (fs::dir_exists(file.path(tmpdir, "_freeze"))) {
    fs::dir_delete(file.path(tmpdir, "_freeze"))
  }
  
  # Gunakan cache khusus html
  if (fs::dir_exists(file.path(tmpdir, "html_freeze"))) {
    fs::dir_copy(file.path(tmpdir, "html_freeze"), file.path(tmpdir, "_freeze"))
  }
  
  # Eksekusi render
  quarto::quarto_render(tmpdir, output_format = "html", as_job = FALSE)
  
  # Pindahkan _book yang dihasilkan
  if (fs::dir_exists("_book_html")) fs::dir_delete("_book_html")
  fs::file_move(file.path(tmpdir, "_book"), "_book_html")
  
  # Simpan kembali cache
  if (fs::dir_exists("html_freeze")) fs::dir_delete("html_freeze")
  if (fs::dir_exists(file.path(tmpdir, "_freeze"))) {
    fs::file_move(file.path(tmpdir, "_freeze"), "html_freeze")
  }
  
  cat("Selesai render HTML. Hasil ada di folder '_book_html'.\n\n")
}

render_typst <- function() {
  cat("Memulai render format Typst...\n")
  tmpdir <- tempfile()
  dir.create(tmpdir)
  
  fs::dir_copy(".", tmpdir)
  
  if (fs::dir_exists(file.path(tmpdir, "_freeze"))) {
    fs::dir_delete(file.path(tmpdir, "_freeze"))
  }
  
  if (fs::dir_exists(file.path(tmpdir, "typst_freeze"))) {
    fs::dir_copy(file.path(tmpdir, "typst_freeze"), file.path(tmpdir, "_freeze"))
  }
  
  quarto::quarto_render(tmpdir, output_format = "typst", as_job = FALSE)
  
  # Cari file PDF hasil Typst
  pdf_files <- fs::dir_ls(file.path(tmpdir, "_book"), glob = "*.pdf")
  if (length(pdf_files) > 0) {
    # Pindahkan PDF ke root direktori kerja utama
    fs::file_copy(pdf_files[1], basename(pdf_files[1]), overwrite = TRUE)
    cat("File PDF berhasil disalin:", basename(pdf_files[1]), "\n")
  } else {
    cat("Peringatan: File PDF hasil render Typst tidak ditemukan.\n")
  }
  
  if (fs::dir_exists("typst_freeze")) fs::dir_delete("typst_freeze")
  if (fs::dir_exists(file.path(tmpdir, "_freeze"))) {
    fs::file_move(file.path(tmpdir, "_freeze"), "typst_freeze")
  }
  
  cat("Selesai render Typst.\n\n")
}

render_all <- function() {
  render_html()
  render_typst()
  cat("Semua format (HTML dan Typst) berhasil dirender.\n")
}
