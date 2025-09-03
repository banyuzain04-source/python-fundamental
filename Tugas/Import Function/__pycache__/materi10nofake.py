print ('materi 10 - file handling')
print('--------------------------')

#cari posisi file note.txt  
file_path = r"C:\Project Python\materi-10-file\note.txt"
#open() -> buka file
#mode r -> read only (hanya baca)
file_catatan = open(file_path, 'r')
#read() -> baca isi file notr.txt
catatan = file_catatan.read()
print(f'isi catatan: {catatan}')
#tutup file note.txt
file_catatan.close
print("---------- OPEN CSV ---------")
file_json_path = r"C:\Project Python\materi-10-file\rukun_islam.json"
# with ... as -> agar file otomatis ter close 
with open(file_json_path, "r") as file_rukun_islam:
  # gunakan fungsi reader() dari module csv
  data_rukun_islam = json.load(file_rukun_islam)
  print(f"Judul:{data_rukun_islam['judul']}")
  print(f"Jumalah rukun:{data_rukun_islam}")
  # keluarkan seluruh data dengan for loop
  for rukun in data_rukun_islam:
    print(rukun)    
print('>> proses baca file anime.csv selesai')
print("---------- ADD CSV ---------")
anime_baru = [6, "Evan", "Kaijuu no-8", 10.0]
print(f"Anime baru: {anime_baru}")
