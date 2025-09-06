import requests

# Endpoint API
url_arab = "https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
url_en   = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"

try:
    # ====== Ambil Teks Arab ======
    res_arab = requests.get(url_arab, timeout=10)
    res_arab.raise_for_status()   # kalau status != 200 → lempar error
    data_arab = res_arab.json()   # hasil JSON → dict Python
    
    # Struktur: {"data": {"text": "...."}}
    teks_arab = data_arab["data"]["text"]

    # ====== Ambil Teks Inggris ======
    res_en = requests.get(url_en, timeout=10)
    res_en.raise_for_status()
    data_en = res_en.json()
    teks_en = data_en["data"]["text"]

    # ====== Output ======
    print("Ayat Al-Kursi (2:255) - Arab:")
    print(teks_arab)
    print("\nTerjemah (EN):")
    print(teks_en)

except requests.exceptions.RequestException as e:
    print("Terjadi error saat mengambil data API:", e)
except KeyError as e:
    print("Struktur respons tidak sesuai. Kunci tidak ditemukan:", e)
