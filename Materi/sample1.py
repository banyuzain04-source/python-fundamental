# len     \\untuk ngitung yaa ges
data_nama = ["azka","evan","ali"]
print(len(data_nama))

# inseret      \\untuk nambah ya ges sesuai yg kita inginkan (sesuai indek yaaa)
data_nama.insert(0, "hamka")
print(data_nama)

# aappend  \\ menambah di akhir yaaa..
data_nama.append("mahiru")
print(data_nama)

# Remove 
data_nama.remove("ali")
print(data_nama)

# POP \\ untk menghapus paling belakang

data_nama.pop()
print(data_nama)

#tuple = gak bisa diubah data nya
my_tuple= ('daffa','fawwwaz','yanto','ridho')
my_tuple.append('hamka') = #bakalan error


# Ambil nama peserta dari input pengguna
peserta = []

for i in range(3):
    nama = input(f"Masukkan nama peserta ke-{i+1}: ")
    peserta.append(nama)

# Tampilkan hasil dengan index
print("\nDaftar Peserta:")
for i in range(len(peserta)):
    print(f"{i}. {peserta[i]}")
