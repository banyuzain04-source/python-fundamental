# set -> {} -> tidak berurutan, berubah, tidak duplikat
print("==============================")

game_azka = {"valorant", "dark soul"}
game_evan = {"genshin impact", ""}

print("evans game: ", game_evan)
print("azka games: ", game_azka)

# add untuk menambah item baru 
game_azka.add("zzz")
game_evan.add("valorant")

# len() untuk menghitung jumlah item
print("azka ada:", len(game_azka), "games:", game_azka)
print("evan ada:", len(game_evan), "games:", game_evan)

# .union() = menggabungkan 2 set berbeda
game_berdua = game_azka.union(game_evan)
total_game = len(game_berdua)
print('semua game yang ada:', total_game, 'games:', game_berdua)

# .intersection() = item yang sama di kedua set
game_yang_kembar = game_azka.intersection(game_evan)
total_game_kembar = len(game_yang_kembar)
print("game sama:", total_game_kembar, 'games:', game_yang_kembar)

# .difference() = item yang ada di azka tapi tidak di evan
game_yang_beda = game_azka.difference(game_evan)
total_game_beda = len(game_yang_beda)
print("game beda:", total_game_beda, 'games:', game_yang_beda)
#dict(dictionary) -> {key:value} / {kunci:isinya}
#key tidak boleh duplikat
koleksi_anime = {
    're_zero':'subaru',
    'wind_breaker':'sakura',
    'waifu':{
        're_zero':'Azuka',
        'oshinoko':'akane'
    }
}
print('koleksi Anime:', koleksi_anime)
print('mc re:zero:',koleksi_anime['re_zero'])

#menambah / mengubah data dict
koleksi_anime['jujutsu kaisen']= 'Yuuta'
koleksi_anime['wind breaker']= 'kaji'
koleksi_anime['waifu']['re_zero']='ram'
print('koleksi anime skrg: ',koleksi_anime)