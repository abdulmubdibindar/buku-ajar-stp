---
name: tinjau-bab
description: Meninjau satu bab buku ajar terhadap aturan penulisan dan render — linter otomatis lalu tinjauan kualitatif (studi kasus memperjelas konsep, meta-commentary, penjelasan berlebih). Pakai saat diminta meninjau, mengaudit, atau memeriksa bab sebelum commit/render.
---

# Tinjau Bab

Tinjauan **tidak mengedit** berkas kecuali pengguna memintanya.

## 1. Linter

```bash
python _scripts/lint_buku.py <berkas.qmd>
```

Laporkan semua galat. Galat bertanda dapat diperbaiki otomatis (daftar, BOM,
mojibake) cukup disebut jumlahnya beserta perintah `--fix`.

## 2. Tinjauan kualitatif

Baca bab dari awal sampai akhir. Untuk setiap temuan catat baris, kutipan, dan
usulan perbaikan. Acuan aturan: skill `menulis-bab`.

1. **Studi kasus ↔ konsep.** Untuk tiap `.kasus`: konsep apa yang dijelaskan
   tepat di atasnya? Apakah pembahasan kasus menyebut konsep itu dan menunjukkan
   di angka/langkah mana konsep bekerja? Kasus yang hanya hitungan = temuan.
2. **Meta-commentary.** Kalimat yang membicarakan teks itu sendiri, instruksi
   penulis yang bocor ("data fiktif ini akan kita gunakan untuk…", "bayangkan
   saya berbicara kepada Anda…"), atau pengumuman isi ("pada subbab ini kita
   akan…"). Peringatan `[meta]` dari linter hanyalah kandidat — nilai satu per satu.
3. **Penjelasan berlebih.** Konsep yang dijelaskan ulang dengan kata lain,
   kalimat pengisi, contoh yang tidak menambah pemahaman.
4. **Konsistensi.** Angka desimal koma, istilah asing miring, istilah kunci
   ditebalkan saat pertama didefinisikan, judul callout bermakna.
5. **Soal latihan.** Tiap soal punya kode capaian `[STP-x.y]{.capaian}` yang
   sesuai dengan capaian bab.

## 3. Keluaran

```markdown
## Tinjauan <berkas>

Linter: N galat (rincian…)

| Baris | Aturan | Kutipan | Usulan |
|---|---|---|---|
```

Akhiri dengan 3 perbaikan paling berdampak.
