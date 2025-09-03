print("Ayo buat profil digitalmu!")
nama = input("Nama: ")
umur = int(input("Umur: "))

print("Pilih Hobi Anda:")
print("1. Gamer")
print("2. Wibu")
print("3. K-Popers")
print("4. Anak Konten")
print("5. Anak Nongki")
pilihan_hobi = input("Masukkan angka pilihan hobi pilih salah satu angka")

hobi = ""
detail_hobi = "" 

if pilihan_hobi == "1":
    hobi = "Gamer"
    detail_hobi = input("Apa game favoritmu? ")
elif pilihan_hobi == "2":
    hobi = "Wibu"
    detail_hobi = input("Siapa waifumu? ")
elif pilihan_hobi == "3":
    hobi = "K-Popers"
    detail_hobi = input ("siapa oshimu?")
elif pilihan_hobi == "4" :
    hobi = "Anak Konten" 
    detail_hobi = input ("Apa platform favorit mu??")
elif pilihan_hobi == "5" :
    hobi = "Anak Nongki" 
    detail_hobi = input ("Basecampmu dimana nih? ")
else:
    hobi = "Tidak Diketahui"
    detail_hobi = "Tidak ada detail spesifik karena pilihan tidak valid."

tahun_sekarang = 2025
tahun_lahir = tahun_sekarang - umur

print("\n--- Profil Digital Anda ---")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Perkiraan Tahun Lahir: {tahun_lahir}")
print(f"Hobi: {hobi}")
print(f"Detail Hobi: {detail_hobi}") 
print("----------------------------")