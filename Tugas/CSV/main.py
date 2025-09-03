import csv

#Baca semua data dari csv
with open ("keuangan.csv", newline="",encoding="utf-8") as f:
    reader= csv.DictReader(f)
    data= list(reader)
print(data)

print("\n")
#Tampilkan semua data
print("📌 Semua data:")
for row in data:
    print(
        f"{row["Tanggal"]} | {row["Keterangan"]} | {row["Kategori"]} | Rp{row["Jumlah"]} |")

# 2. Hitung Semua Pengeluaran
total= sum(int(row["Jumlah"])for row in data)
print (f"Total pengeluaran: Rp.{total}")

# 3. Hitung total per kategori
ketegori_total= {} 

for row in data:
    kategori = row["Kategori"]
    jumlah = int(row["Jumlah"])
    if kategori not in ketegori_total:
        ketegori_total[kategori] = 0
    ketegori_total[kategori] += jumlah

print('Pengeluaran Per Kategori :')
for kategori, jumlah in ketegori_total.items():
    print(f"{kategori} : Rp.{jumlah}")

