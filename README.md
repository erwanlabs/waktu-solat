# Waktu Solat — paparan iPad

Paparan jam dan waktu solat untuk iPad lama (iOS 9). Zon JAKIM **NGS03** (Seremban & Port Dickson).

- Waktu solat rasmi JAKIM e-Solat disimpan terus dalam `index.html`, jadi paparan tak perlu internet untuk tarik waktu.
- JavaScript ES5 sahaja (serasi Safari iOS 9).
- Kad kiri: hari, tarikh Masihi dan kalendar Hijri. Kad kanan "Tarikh Penting": kira hari ke Awal Ramadan, Aidilfitri, Aidiladha, Awal Muharram, Maulidur Rasul dan lain-lain, ikut tarikh Hijri dalam data JAKIM.
- Kotak waktu semasa ditebalkan dengan lencana "SEKARANG".
- Saiz ikut skrin 4:3 (iPad) atau 16:9 (komputer/TV) tanpa terpotong.
- Mod iqamah (5 minit), skrin "matikan telefon" (15 minit) dan skrin Jumaat (45 minit).
- Font Cinzel (tajuk) dan Jost (nombor & teks) dibenamkan terus dalam `index.html` semasa bina (sumber dalam `fonts/`, lesen SIL OFL).
- **Mod ringan** automatik untuk iPhone/iPad iOS 12 ke bawah: tiada animasi, latar rata, font lebih tebal untuk skrin bukan Retina. Paksa dengan `?mod=ringan` atau `?mod=penuh` pada link.
- Animasi hanya guna transform & opacity. Set `ANIMASI_LATAR = false` untuk matikan cahaya bergerak di latar.

## Tetapan

Edit `build/template.html`, bahagian `TETAPAN` (nama, format jam, minit iqamah, animasi latar), kemudian bina semula.

## Kemas kini data tahunan

```bash
curl -sS -X POST "https://www.e-solat.gov.my/index.php?r=esolatApi/TakwimSolat&period=duration&zone=NGS03" \
  -d "datestart=2028-01-01&dateend=2028-12-31" -o build/data/ngs03-2028.json
python3 build/build.py build/template.html index.html build/data/ngs03-2027.json build/data/ngs03-2028.json
```

Data semasa sah hingga 31 Disember 2027.
