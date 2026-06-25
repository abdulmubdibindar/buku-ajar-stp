---
name: setup-quarto-multiformat
description: Panduan setup konfigurasi Quarto book project agar dapat diekspor ke HTML dan PDF secara aman tanpa konflik cache, menggunakan skrip otomatisasi Python yang agnostik terhadap bahasa pemrograman buku.
---

# Panduan Setup Konfigurasi Quarto Book Multi-Format (HTML & PDF)

Dokumen ini berisi panduan bagi Agen untuk menyiapkan konfigurasi proyek Quarto Book agar bisa diekspor ke format HTML dan PDF (menggunakan Typst sebagai mesin PDF agnostik) secara aman. Alur ini menggunakan skrip Python otomatis untuk mengelola cache (`_freeze`) agar tidak terjadi konflik antar format.

---

## Langkah 1: Konfigurasi `_quarto.yml`
Pastikan format output `html` dan `typst` didefinisikan dalam berkas `_quarto.yml`. Format `typst` direkomendasikan karena menghasilkan PDF berkualitas tinggi secara cepat tanpa ketergantungan pada LaTeX.

Contoh konfigurasi minimum `_quarto.yml`:
```yaml
project:
  type: book

execute:
  freeze: auto # Mengaktifkan caching otomatis

format:
  html:
    theme: cosmo
    # ... konfigurasi html lainnya ...
  typst:
    toc: true
    number-sections: true
    # ... konfigurasi pdf/typst lainnya ...
```

---

## Langkah 2: Konfigurasi `.gitignore`
Pastikan cache sementara Quarto dan cache per format diabaikan oleh Git agar repositori tetap bersih. Tambahkan baris berikut ke berkas `.gitignore`:

```text
# Quarto output & cache
/_book/
/_freeze/
/.quarto/
/html_freeze/
/typst_freeze/
```

---

## Langkah 3: Skrip Otomatisasi Agnostik (`render_book.py`)
Gunakan skrip Python berikut untuk merender buku. Python dipilih karena terpasang secara bawaan di hampir semua sistem developer modern dan sepenuhnya agnostik terhadap bahasa pemrograman yang digunakan di dalam dokumen Quarto (baik R, Python, Julia, dll.).

Buat berkas `render_book.py` di direktori root proyek:

```python
import os
import shutil
import subprocess
import sys

def run_command(command):
    """Menjalankan perintah terminal dan menampilkan outputnya secara realtime."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc

def clean_dir(path):
    """Menghapus direktori jika ada."""
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def swap_freeze(target_freeze):
    """Mengganti folder _freeze utama dengan cache khusus format."""
    clean_dir("_freeze")
    if os.path.exists(target_freeze):
        shutil.copytree(target_freeze, "_freeze")
        print(f"-> Menggunakan cache dari '{target_freeze}'")
    else:
        print(f"-> Tidak ada cache sebelumnya untuk '{target_freeze}'. Memulai cache baru.")

def save_freeze(target_freeze):
    """Menyimpan cache dari _freeze ke folder khusus format."""
    clean_dir(target_freeze)
    if os.path.exists("_freeze"):
        shutil.copytree("_freeze", target_freeze)
        print(f"-> Menyimpan cache ke '{target_freeze}'")
    clean_dir("_freeze")

def render_html():
    print("\n=== MERENDER FORMAT HTML ===")
    swap_freeze("html_freeze")
    
    # Render ke html
    exit_code = run_command("quarto render --to html")
    if exit_code != 0:
        print("Error saat merender HTML!")
        sys.exit(exit_code)
        
    # Pindahkan output ke folder khusus html agar tidak tertumpuk format lain
    dest_dir = "_book_html"
    clean_dir(dest_dir)
    if os.path.exists("_book"):
        shutil.move("_book", dest_dir)
        print(f"-> Output HTML berhasil disimpan di '{dest_dir}'")
        
    save_freeze("html_freeze")

def render_pdf():
    print("\n=== MERENDER FORMAT PDF (TYPST) ===")
    swap_freeze("typst_freeze")
    
    # Render ke typst (menghasilkan file .pdf)
    exit_code = run_command("quarto render --to typst")
    if exit_code != 0:
        print("Error saat merender PDF/Typst!")
        sys.exit(exit_code)
        
    # Pindahkan file pdf hasil render ke direktori root utama
    if os.path.exists("_book"):
        for file in os.listdir("_book"):
            if file.endswith(".pdf"):
                src_path = os.path.join("_book", file)
                shutil.copy2(src_path, file)
                print(f"-> File PDF berhasil disalin ke root: {file}")
        shutil.rmtree("_book")
        
    save_freeze("typst_freeze")

if __name__ == "__main__":
    # Jalankan render untuk kedua format
    render_html()
    render_pdf()
    print("\nProses render selesai dengan sukses!")
```

---

## Langkah 4: Cara Menjalankan
Jalankan skrip di atas melalui terminal di root proyek:
```bash
python render_book.py
```

Skrip ini akan secara otomatis:
1. Menukar cache `_freeze` agar format HTML dan PDF tidak saling menimpa hasil kompilasi kode pemrograman.
2. Memanggil CLI `quarto` langsung dari sistem.
3. Merapikan folder keluaran (`_book_html` untuk website HTML, dan file `.pdf` langsung di folder root).
