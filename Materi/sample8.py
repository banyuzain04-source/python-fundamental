print('MATERI 8 - Function')
print('===================')

def halo_dunia():
    print('hello world')
    print('halo dunia')

#cara akses function, sertakan nama dan () -nya
halo_dunia()

#fungsi dengan parameter (variebel di fungsi)
def sapa_sapa_gan(nama):
    print('halo', nama,'Selamat datamg di Isekai')

def sapa_waifuku(waifu):
    print('konbawa' ,(waifu),'-chan aishteru yo')
sapa_sapa_gan('Azuka')
sapa_waifuku('Rem')
sapa_waifuku('Akane')
sapa_waifuku('Aira')
sapa_waifuku('Komi')
sapa_waifuku('Sisei')
sapa_waifuku('Nano')

def rumus_luas_segitiga(alas, tinggi):
    print('alas',alas)
    print('tinggi',tinggi)
    rumusan=1/2*(alas*tinggi)
    print('Hasil',rumusan)
rumus_luas_segitiga(10, 30)

def filter_teman_toxix(nama, sifat):
    #ciri-ciri toxic
    sifat_toxic = [
     "julid",
     "baperan",
     "manipulatif", 
     "drama",
     "sombong"   
    ]

    # deteksi parameter sifat toxic dari pada parameter sifat
    if any(kata in sifat for kata in sifat_toxic):
        print(nama, "itu org gabaek jgn ditemenin")
    else:
        print(nama, "oohhhh dia org baik kok gpp")

