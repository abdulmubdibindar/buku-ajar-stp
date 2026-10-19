# Callout

Diproses oleh `callout-buku.lua`. Judul dan nomor dibuat otomatis — jangan
menulis "Studi Kasus 6.3" atau "Soal Latihan" secara manual.

| Kelas | Judul hasil | Nomor | Masuk TOC kanan | `id` | `title` |
|---|---|---|---|---|---|
| `.capaian` | Capaian Pembelajaran Bab X | per bab | ya | `#capaian-…` | tidak dipakai |
| `.kasus` | Studi Kasus X.n: *title* | per bab | ya | `#kasus-…` wajib | wajib |
| `.latihan` | Soal Latihan X.n[: *title*] | per bab | ya | `#latihan-…` wajib | opsional |
| `.penting` | Penting[: *title*] | — | tidak | opsional | opsional |
| `.catatan` | Catatan[: *title*] | — | tidak | opsional | opsional |

## Contoh

```markdown
::: {#capaian-estimasi .capaian}
Setelah mempelajari bab ini, Anda diharapkan mampu memaknai interval
kepercayaan estimasi sebuah parameter [STP-5.1]{.capaian}.
:::

::: {#kasus-jarak-hunian .kasus title="Rata-rata Jarak Tempat Tinggal per Jenis Hunian"}
Isi studi kasus…
:::

::: {#latihan-ci-usia-dosen .latihan title="Rentang Usia Dosen"}
Soal… [STP-5.1]{.capaian}
:::

::: {.penting title="Tingkat kepercayaan bukan peluang"}
Isi…
:::
```

## Aturan

- `id` diawali nama jenis dan unik di seluruh buku: `kasus-<topik-singkat>`.
- `title` boleh memuat math (`$\bar{x}$`) dan *miring*.
- Rujukan dari mana pun di buku: `@kasus-jarak-hunian` → "Studi Kasus 6.3" bertaut.
- Soal Latihan: jangan mengarang soal sendiri bila tidak diminta; cukup siapkan
  callout dan kode capaian `[STP-x.y]{.capaian}` yang relevan.
- Isi callout boleh panjang; di PDF kotaknya otomatis terpotong antarhalaman.
