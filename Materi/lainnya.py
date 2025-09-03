from PIL import Image
import os

def buat_gif_dari_file(
    paths,                # list path gambar
    output_path="hasil.gif",
    duration=200          # lama tiap frame (ms)
):
    # pastikan semua file ada
    paths = [p for p in paths if os.path.exists(p)]
    if not paths:
        print("Tidak ada file valid.")
        return

    # buka semua gambar
    frames = [Image.open(p) for p in paths]

    # simpan sebagai GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )
    print(f"GIF berhasil dibuat: {output_path}")


# --- Contoh pemakaian ---
# Tinggal copy path gambar kamu ke list di bawah
gambar_list = [
    r"C:\Project Python\sampel python\Cuplikan layar 2025-08-12 195032.png"
]

buat_gif_dari_file(gambar_list, "gabungan.gif")
