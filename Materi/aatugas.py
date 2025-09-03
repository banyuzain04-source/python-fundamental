

print("<<<================<<<<>>>>================>>>")

#function 
print("--------------->contoh function<---------------")

def hello_world(nama):
    print("hai mas", nama)
    print("selamat datang di program ini")

hello_world("bilal")
hello_world("syahid")
hello_world("azmi")

print("<<<================<<<<>>>>================>>>")

#lambda
print("---------->Contoh penggunaan lambda<----------")

greeting = lambda name: f"hei, {name}!"
print(greeting("Bilal"))
print(greeting("Syahid"))
print(greeting("Azmi"))

print("<<<================<<<<>>>>================>>>")

#map()
print("------------>Conto penggunaan map<------------")
nilai_mentah = [19.8, 20.9, 32.9, 49.8, 97.9, 100.0, 88.9, 90.0, 99.55, 100.2]
nilai_dibulatkan = map(lambda x: round(x), nilai_mentah)
for nilai in nilai_dibulatkan:
    print(nilai)

print("<<<================<<<<>>>>================>>>")
#map() dengan input dari user
print("------------>Contoh penggunaan map dengan input dari user<------------")
nilai_mentah = input("Masukkan nilai-nilai (pisahkan dengan spasi): ").split()
nilai_dibulatkan = map(lambda x: round(float(x)), nilai_mentah) 
for nilai in nilai_dibulatkan:
    print(nilai)


print('Lagi Males...')

def doa():
    return 'bismillah'

def doa_ot():
    return'alhamdulillah kenyang'