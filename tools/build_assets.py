#!/usr/bin/env python3
"""Builds data/menu.json and optimised images from the supplied data pack.
Usage: python3 tools/build_assets.py /path/to/tkr-alkhobar-data"""
import json, re, sys, os
from PIL import Image, ImageOps
SRC = sys.argv[1] if len(sys.argv) > 1 else "../tkr-alkhobar-data"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def out(*p): return os.path.join(ROOT, *p)

FIX = {"2 KG, served with rice": ("2 KG, served with rice", "2 كجم، يُقدم مع الأرز"),
 "Single": ("Single", "فردي"), "Side Order": ("Side Order", "طبق جانبي"),
 "3/4 Persons": ("3/4 Persons", "3 – 4 أشخاص"), "4 Persons": ("4 Persons", "4 أشخاص"),
 "2 Persons": ("2 Persons", "شخصان"), "1 KG": ("1 KG", "1 كجم"),
 "Per KG — minimum order 10 KG, order at least 5 hours in advance": (
   "Per KG — minimum order 10 KG, order at least 5 hours in advance",
   "للكيلو — الحد الأدنى للطلب 10 كجم، يُطلب قبل 5 ساعات على الأقل"),
 "6 Pieces, served with Tartar Sauce": ("6 Pieces, served with Tartar Sauce", "6 قطع، تُقدم مع صلصة التارتار")}
def note(n):
    if not n: return None, None
    if n.startswith("2 Pieces (Leg"): return "2 Pieces (Leg & Chest)", "قطعتان (فخذ وصدر)"
    if n in FIX: return FIX[n]
    m = re.fullmatch(r"(\d+) Pieces", n)
    if m: return n, f"{m.group(1)} قطع"
    raise SystemExit("untranslated note: " + n)
S = json.load(open(out("tools", "sections.source.json"), encoding="utf8"))
menu = []
for s in S:
    items = []
    for i in s["items"]:
        ne, na = note(i["note"])
        items.append({"en": i["en"], "ar": i["ar"], "arPrinted": i["ar_printed"],
                      "prices": i["prices"], "noteEn": ne, "noteAr": na})
    menu.append({"id": s["id"], "en": s["en"], "ar": s["ar"], "items": items})
json.dump(menu, open(out("data", "menu.json"), "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
print("sections", len(menu), "items", sum(len(m["items"]) for m in menu))

def save(src, dst, w, q=78):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(dst, "JPEG", quality=q, optimize=True, progressive=True); return im.size
G = {"hero": "photos/branch/maps-02.jpg", "platter": "photos/branch/maps-02.jpg",
     "pulao": "photos/branch/maps-07.jpg", "kabab": "photos/branch/maps-04.jpg",
     "rooftop-night": "photos/branch/maps-06.jpg", "rooftop-lights": "photos/branch/maps-01.jpg",
     "reception": "photos/branch/maps-05.jpg", "dining-hall": "photos/branch/maps-09.jpg",
     "hall-tour": "media/stills/fb-venue-tour-1.jpg", "hall-tables": "media/stills/fb-venue-tour-2.jpg",
     "hall-evening": "media/stills/fb-day3-house-full-1.jpg"}
for k, v in G.items(): print(k, save(os.path.join(SRC, v), out("img/gallery", k + ".jpg"), 1600 if k == "hero" else 1100))
for n in range(1, 14):
    f = [x for x in os.listdir(os.path.join(SRC, "photos/menu")) if x.startswith(f"menu-{n:02d}.")][0]
    save(os.path.join(SRC, "photos/menu", f), out("img/menu", f"menu-{n:02d}.jpg"), 1500, 74)
save(os.path.join(SRC, "media/TKR_Logo.jpg"), out("img/logo.jpg"), 600, 85)
