# bakim-fiyat-data

[Bakım Proforma App](https://github.com/lahmacunor) için fiyat verisi. Bu
repo sadece veri barındırır, kod/mantık içermez.

## Nasıl kullanılıyor

App bu repodaki `fiyat.json`'u [jsDelivr CDN](https://www.jsdelivr.com/)
üzerinden çekiyor:

```
https://cdn.jsdelivr.net/gh/lahmacunor/bakim-fiyat-data@main/fiyat.json
```

Yerelde bir cache tutuluyor (offline fallback için) — app her açılışta
yeniden çekmeye çalışır, başarısız olursa son bilinen veriyi kullanır.

## Güncelleme

Kaynak veri, Fiat bayiindeki BOS sisteminden aylık indirilen fiyat
listesinden üretiliyor (bkz. ana proje: `Bakim-Fiyat-Otomasyonu`). `fiyat.json`
şu an için elle güncelleniyor; `guncelle.py`'ye otomatik export adımı
eklenmesi backlog'da.

**`git push`'tan hemen sonra mutlaka `python purge_cdn.py` çalıştır.**
jsDelivr push edilen dosyayı saatlerce eski haliyle servis etmeye devam
edebiliyor, bu script jsDelivr'in resmi purge endpoint'ine istek atıp
cache'i anında temizliyor.

Bu repo **public** — fiyat listesi zaten müşteriye proformada gösterilen bir
veri, gizli değil. jsDelivr private repo'yu desteklemediği için bu tercih
edildi (bkz. `Bakim-Proforma-App/decisions.md`, 2026-08-23).

## Format

Henüz kesinleşmedi — şu an placeholder. Gerçek şema, `guncelle.py` export
adımı tasarlanırken netleşecek.
