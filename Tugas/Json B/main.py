import json

with open("peminjaman_buku.json" , "r" , encoding="utf-8") as f:
    data = json.load(f)

print ("belum kembali")

total_dipinjamkan = 0
total_belum = 0

for anggota in data["anggota"]:
    nama=anggota["nama"]
    for buku in anggota ["pinjam"]:
        total_dipinjamkan += 1
        if not buku ["kembali"]:
            total_belum += 1
        print(f"- {nama:6} : {buku['judul']} ({buku['tanggal']})")

print (f"\nTotal dipinjam: {total_dipinjamkan} | Belum kembali: {total_belum}")