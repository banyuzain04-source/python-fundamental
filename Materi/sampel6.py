print('materi 6 data structure')
print('=======================')
#list = [] = berurutan , berubah , duplikat
daftar_belanjaan= ['es teh desa',
                   'gorengan'
                   ,'gabin']
print ('daftar brlanjaan',daftar_belanjaan)
print(daftar_belanjaan[0])
#append() menambh item ke akhir list
daftar_belanjaan.append('boba')
print('daftar belanjaan skrg', daftar_belanjaan)
#renove / menghapus item berdasarkan index
daftar_belanjaan.remove('gabin')
#insert menambah item ke spesifik index
daftar_belanjaan.insert(0,'action figure')
print('potong list',daftar_belanjaan[1:3])
#menggabungkan list
jajan_zaki=['basreng']
jajan_bilal=['apel']
jajan_ku=['melon']
gabungan_jajanan=jajan_bilal+jajan_zaki
print('gabungan jajanan:', gabungan_jajanan)
#tuple () berurutan, berubah, tidak duplikat
ttl= ("depok",10, 'july', 2001)
print('TTL Hamka:',ttl)
print('tgl lahir',ttl[1])
#unpacking tuple ke variable baru
#harus berurutan sesuai value nya
tempat_lahir, bln_lahir, bln_lahir, thn_lahir= ttl
print('tempat lahir', tempat_lahir)
print('tahun lahir', thn_lahir)
#list multi dimensi
daftar_hobi=[
    ['action fiqure','nodroid'],
    ['baju clb','makanan clb'],
    ['poto ama cosplayer', 'nge event']
]
print(daftar_hobi)
print('yg paling utama', daftar_hobi[2][1])