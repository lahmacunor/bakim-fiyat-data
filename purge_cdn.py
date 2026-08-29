"""
fiyat.json'u push ettikten SONRA calistir.

jsDelivr, main dalindaki dosyalari agresif onbellekliyor (saatlerce eski
veri donebiliyor). Bu script jsDelivr'in resmi purge endpoint'ine istek
atarak cache'i hemen temizler - app bir sonraki acilista guncel fiyati ceker.

Kullanim:  python purge_cdn.py
"""
import json
import urllib.request

PURGE_URL = "https://purge.jsdelivr.net/gh/lahmacunor/bakim-fiyat-data@main/fiyat.json"


def purge():
    with urllib.request.urlopen(PURGE_URL, timeout=15) as resp:
        sonuc = json.loads(resp.read().decode("utf-8"))
    if sonuc.get("state") == "finished" or resp.status == 200:
        print(f"jsDelivr cache temizlendi: {PURGE_URL}")
    else:
        print(f"Beklenmeyen yanit: {sonuc}")
    return sonuc


if __name__ == "__main__":
    purge()
