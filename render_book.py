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
