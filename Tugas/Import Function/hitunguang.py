def tambah_bonus(uang_list):
    tambah_uang = list(map(lambda uang: uang + 5000, uang_list))

    return tambah_uang


def filter_boros(uang_list):
    uang_boros = list(filter(lambda boros: boros >= 50000, uang_list))

    return uang_boros
