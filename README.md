# Waktu Solat — paparan iPad

Paparan jam dan waktu solat untuk iPad lama (iOS 9). Zon JAKIM **NGS03** (Seremban & Port Dickson).

- Waktu solat rasmi JAKIM e-Solat disimpan terus dalam `index.html`, jadi paparan tak perlu internet untuk tarik waktu.
- JavaScript ES5 sahaja (serasi Safari iOS 9).
- Mod iqamah (5 minit), skrin "matikan telefon" (15 minit) dan skrin Jumaat (45 minit).
- Font Poppins disimpan dalam `fonts/` (lesen SIL OFL, lihat `fonts/OFL.txt`).
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
