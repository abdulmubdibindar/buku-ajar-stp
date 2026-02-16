# Panduan Penulisan Kutipan dan Referensi dalam RMarkdown

Panduan ini mencakup langkah-langkah teknis untuk mengelola daftar
pustaka, kutipan dalam teks (*in-text citation*), serta integrasi
workflow modern menggunakan **Google Antigravity**.

## 1. Persiapan Database Bibliografi (`.bib`)

Langkah pertama adalah membuat file database referensi (biasanya format
BibTeX).

**Implementasi:** Buat file teks bernama `referensi.bib` (atau nama lain
yang relevan) di direktori root proyek Anda. Isi dengan format BibTeX
standar:

``` bibtex
@book{xie2016bookdown,
  title={Bookdown: Authoring Books and Technical Documents with R Markdown},
  author={Xie, Yihui},
  year={2016},
  publisher={Chapman and Hall/CRC},
  url={https://bookdown.org/yihui/bookdown/}
}

@article{wickham2014tidy,
  title={Tidy Data},
  author={Wickham, Hadley},
  journal={Journal of Statistical Software},
  volume={59},
  number={10},
  year={2014}
}
```

## 2. Konfigurasi YAML Header

Anda harus mendeklarasikan file bibliografi di dalam YAML header dokumen
`.Rmd` Anda agar Pandoc dapat memprosesnya.

**Implementasi:** Tambahkan baris `bibliography` di bagian atas file
`.Rmd` atau `index.Rmd`:

``` yaml
---
title: "Laporan Analisis Data"
output: html_document
bibliography: referensi.bib
link-citations: true
---
```

## 3. Format Penulisan Kutipan (In-text Citation)

R Markdown menggunakan sintaks standar Pandoc. Gunakan *citation key*
(misal: `xie2016bookdown`) yang telah didefinisikan di file `.bib`.

**Tabel Referensi Sintaks:**

| Tipe Kutipan | Sintaks Markdown | Output Hasil Render |
|:---|:---|:---|
| **Kutipan Standar** | `[@wickham2014tidy]` | (Wickham, 2014) |
| **Kutipan Naratif** | `@wickham2014tidy` menyatakan... | Wickham (2014) menyatakan... |
| **Tanpa Penulis** | `[-@wickham2014tidy]` | (2014) |
| **Multiple Kutipan** | `[@xie2016bookdown; @wickham2014tidy]` | (Xie, 2016; Wickham, 2014) |
| **Prefix/Suffix** | `[lihat @xie2016bookdown, hlm. 33]` | (lihat Xie, 2016, hlm. 33) |

> **Pro Tip:** Secara default, daftar pustaka akan muncul di akhir
> dokumen. Jika Anda ingin menempatkannya di lokasi spesifik (misalnya
> sebelum lampiran), sisipkan kode HTML berikut di dalam body teks
> RMarkdown Anda:
>
> ``` html
> <div id="refs"></div>
> ```

## 4. Mengatur Style Kutipan dengan CSL

Secara default, R Markdown menggunakan format Chicago Author-Date. Untuk
mengubahnya (misalnya ke APA, IEEE, atau Harvard), Anda memerlukan file
CSL (*Citation Style Language*).

**Implementasi:**

1.  Unduh file style yang diinginkan (misal `apa.csl`) dari [Zotero
    Style Repository](https://www.zotero.org/styles).
2.  Simpan file tersebut di direktori proyek.
3.  Update YAML header:

``` yaml
---
title: "Laporan Teknis"
bibliography: referensi.bib
csl: apa.csl
---
```

## 5. Workflow Modern: Google Antigravity & Agentic Orchestration

Berdasarkan literatur "Creating Books With Bookdown (R-based Package),
Enhanced by Antigravity", Anda dapat mengotomatisasi manajemen sitasi
yang kompleks dengan bantuan AI Agent.

### A. Konfigurasi `AGENTS.md`

Buat file `AGENTS.md` di root repositori Anda untuk memberikan instruksi
persisten bagi AI Agent.

**Contoh Aturan untuk Sitasi:**

``` markdown
# Bibliographic Rules

- Style Guide: Gunakan APA 7th edition untuk semua sitasi.
- Source Integrity: Pastikan semua entry di `referensi.bib` memiliki field DOI atau URL yang valid.
- Formatting: Saat melakukan refactoring teks, pertahankan sintaks citation keys (`@key`). Jangan ubah menjadi teks statis.
- Safety: Jangan pernah menghapus entry dari `referensi.bib` tanpa persetujuan eksplisit.
```

### B. Validasi Otomatis

Manfaatkan kemampuan agen untuk memvalidasi integritas referensi:

1.  **Scan Broken Links:** Minta agen untuk memindai file `.bib` dan
    memeriksa ketersediaan URL/DOI.
2.  **Cross-Check:** Minta agen untuk memastikan semua kutipan dalam
    teks (`@key`) memiliki entri yang sesuai di `referensi.bib`.
