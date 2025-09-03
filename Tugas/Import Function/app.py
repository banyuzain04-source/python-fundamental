import doa
import hitunguang

print(doa.doa_sebelum_makan())
print(doa.doa_setelah_makan())
print(doa.doa_sebelum_tidur())
print(doa.doa_setelah_bangun())

jajan = [50000, 30000, 15000, 70000, 10000]
print("<<<<<<tambah bonus>>>>>>>>")
print(hitunguang.tambah_bonus (jajan))
print("<<<<<<<uang boros>>>>>>>>")
print(hitunguang.filter_boros(jajan))

