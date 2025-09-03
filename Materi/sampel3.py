teks= 'halo semua nya apa kalian sehat atau kalian sakit , apa jawaban kalian tulis di kolom apa saja ya'
x = teks.count('apa')
print(x)

a= 'halo guys'
b= 'Halo guys'
print(a.islower())
print(b.islower())

# Ambil nama peserta dari input pengguna
peserta = []

for i in range(3):
    nama = input(f"Masukkan nama peserta ke-{i+1}: ")
    peserta.append(nama)

# Tampilkan hasil dengan index
print("\nDaftar Peserta:")
for i in range(len(peserta)):
    print(f"{i}. {peserta[i]}")
peserta = []

for i in range(3):
    nama = input(f"Masukkan nama peserta ke-{i+1}: ")
    peserta.append(nama)

# Tampilkan hasil dalam satu baris dengan index
print("\nDaftar Peserta:")
print(', '.join([f"{i}. {nama}" for i, nama in enumerate(peserta)]))

#menambah / mengubah data dict
