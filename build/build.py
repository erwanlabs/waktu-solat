"""Bina index.html: gabung data JAKIM (JSON tahunan) ke dalam template."""
import base64
import json
import os
import re
import sys
from datetime import date, timedelta

BULAN_MS = {"Jan": 1, "Feb": 2, "Mac": 3, "Apr": 4, "Mei": 5, "Jun": 6, "Jul": 7,
            "Ogo": 8, "Sep": 9, "Okt": 10, "Nov": 11, "Dis": 12}
BULAN_PENUH = ["Januari", "Februari", "Mac", "April", "Mei", "Jun", "Julai", "Ogos",
               "September", "Oktober", "November", "Disember"]
KEYS = ["imsak", "fajr", "syuruk", "dhuhr", "asr", "maghrib", "isha"]


def parse_date(s):
    d, m, y = s.split("-")
    return date(int(y), BULAN_MS[m[:3]], int(d))  # JAKIM kadang tulis "Ogo", kadang "Ogos"


def hhmm(t):
    h, m, _ = t.split(":")
    return h.zfill(2) + m.zfill(2)


def main(template_path, out_path, *json_paths):
    rows = []
    for p in json_paths:
        rows += json.load(open(p))["prayerTime"]
    rows.sort(key=lambda r: parse_date(r["date"]))

    start = parse_date(rows[0]["date"])
    for i, r in enumerate(rows):
        expected = start + timedelta(days=i)
        if parse_date(r["date"]) != expected:
            sys.exit(f"Tarikh terputus: {r['date']} (jangka {expected})")

    data = [r["hijri"] + "|" + "|".join(hhmm(r[k]) for k in KEYS) for r in rows]
    end = start + timedelta(days=len(rows) - 1)

    html = open(template_path, encoding="utf-8").read()
    html = (html
            .replace("/*__DATA__*/", json.dumps(data, separators=(",", ":")))
            .replace("/*__START_UTC__*/", f"{start.year},{start.month - 1},{start.day}")
            .replace("/*__START_LABEL__*/", start.isoformat())
            .replace("/*__END_LABEL__*/", f"{end.day} {BULAN_PENUH[end.month - 1]} {end.year}"))
    # Benamkan font (woff, serasi Safari 9) terus dalam HTML: tiada muat turun berasingan
    font_dir = os.path.join(os.path.dirname(os.path.abspath(template_path)), "..", "fonts")
    for nama, w in re.findall(r"/\*__FONT_([a-z]+)-(\d+)__\*/", html):
        with open(os.path.join(font_dir, f"{nama}-latin-{w}-normal.woff"), "rb") as f:
            html = html.replace(f"/*__FONT_{nama}-{w}__*/", "data:font/woff;base64," + base64.b64encode(f.read()).decode())
    assert "/*__" not in html
    open(out_path, "w", encoding="utf-8").write(html)
    print(f"{len(rows)} hari, {start} hingga {end}, {len(html)} bait -> {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
