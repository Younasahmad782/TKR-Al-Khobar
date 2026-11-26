#!/usr/bin/env python3
"""Build the TKR Al Khobar bilingual menu page from the verified transcription.
Data sources (Nov 2026):
 1. The printed menu as photographed on Google Maps (Menu tab, 13 photos, Nov 2026)
    — the primary source; high-resolution, read in full.
 2. The same printed menu filmed in a YouTube review inside the branch
    (transcription: ~/workspace/tkr-alkhobar-media/menu-hunt/menu-transcription.md).
    Video-frame prices that disagreed with the menu photos were corrected to the
    photos; calories are kept ONLY where the video price matched the photo price
    (where the price differed, the row was misread, so its calorie is dropped).
 3. A customer bill from the branch (13 Nov 2026, Table H-17) — confirms prices
    and the Half/Full meaning of dual prices (Namkeen Karahi HALF = 35 SAR).
Nothing is invented. Anything unclear is flagged, never guessed.
"""
import json, os

OUT = os.path.expanduser("~/workspace/tkr-alkhobar-menu")
ASSETS = os.path.join(OUT, "assets")
os.makedirs(ASSETS, exist_ok=True)

# price: None = not printed / not visible -> "price to confirm"
# prices: list of numbers as printed (dual prices = Half / Full, confirmed by the bill)
# ar_printed: True when the Arabic name was read off the printed menu or the bill
def item(en, ar, ar_printed, cal, prices, note=None, photo=None):
    return {"en": en, "ar": ar, "ar_printed": ar_printed, "cal": cal,
            "prices": prices, "note": note, "photo": photo}

SECTIONS = [
    {"id": "signature", "en": "Signature Dishes", "ar": "الأطباق المميزة",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("2 KG Dum Pukht (Served with Rice)", "دم بخت 2 كجم (يُقدم مع الأرز)", False, None, [189], note="2 KG, served with rice"),
        item("Namkeen Lamb Rosh", "روش لحم الضأن المملح", False, None, [118]),
        item("Matka Gosht", "ماتكا جوشت", False, None, [118]),
    ]},
    {"id": "platters", "en": "Platters / Dum Pukht", "ar": "الأطباق العائلية / دم بخت",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("TKR Special Platter", "طبق تي كي آر الخاص", False, None, [199], note="3/4 Persons"),
        item("Qandhari Platter", "طبق قندهاري", False, None, [275], note="4 Persons"),
        item("Chef's Special Platter", "طبق الشيف الخاص", False, None, [119], note="2 Persons"),
        item("TKR Special Dum Pukht per KG", "دم بخت الخاص بتي كي آر للكيلو", False, None, [99], note="Per KG — minimum order 10 KG, order at least 5 hours in advance"),
    ]},
    {"id": "starters", "en": "Mouth-Watering Appetizers", "ar": "مقبلات شهية",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("French Fries", "بطاطس مقلية", True, None, [15]),
        item("Finger Fish", "أصابع السمك", False, None, [40], note="6 Pieces, served with Tartar Sauce"),
        item("Honey Sesame Wings", "أجنحة العسل والسمسم", False, None, [22], note="6 Pieces"),
        item("Drumsticks", "أفخاذ دجاج", False, None, [40], note="4 Pieces"),
        item("Korean Cheese Balls", "كرات الجبن الكورية", False, None, [30]),
        item("Cheese Naan", "نان بالجبن", False, None, [10]),
        item("Dynamite Chicken", "دجاج ديناميت", False, None, [42], note="12 Pieces"),
        item("Dynamite Prawns", "جمبري ديناميت", False, None, [58], note="12 Pieces"),
        item("Tempura Prawns", "جمبري تمبورا", False, 700, [55], note="5 Pieces"),
    ]},
    {"id": "soup", "en": "Soup (Bowls of Comfort)", "ar": "الشوربة",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("TKR Special Soup", "شوربة تي كي آر الخاصة", False, 220, [20]),
        item("Chicken Corn Soup", "شوربة الذرة بالدجاج", False, 180, [18], note="Single", photo="soup.jpg"),
        item("Hot & Sour Soup", "شوربة حارة وحامضة", False, 180, [18], note="Single"),
        item("Cream of Mushroom Soup", "شوربة كريمة الفطر", False, 210, [20], note="Single"),
        item("Chef Signature Soup", "شوربة الشيف الخاصة", False, 260, [18], note="Single"),
    ]},
    {"id": "garden", "en": "Garden (Fresh Bowl Salads)", "ar": "سلطات طازجة",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Hummus", "حمص", True, 35, [15]),
        item("Lahori Green Salad", "سلطة خضار مشكلة", True, 45, [18]),
        item("Russian Salad", "سلطة روسية", True, 50, [28]),
        item("Fattoush Salad", "سلطة الفتوش", True, 140, [25]),
        item("TKR Special Salad", "سلطة تي كي آر الخاصة", True, 180, [35]),
        item("Mint Raita", "رايتا بالنعناع", True, 220, [8]),
        item("Zeera Raita", "رايتا بالكمون", True, 250, [8]),
    ]},
    {"id": "bbq", "en": "BBQ Section", "ar": "قسم المشويات",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Shinwari Lamb Tikka", "تيكا لحم الضأن الشينواري", False, None, [99], note="1 KG"),
        item("Mutton Chops", "شرحات لحم الضأن", False, None, [65], note="4 Pieces"),
        item("Chicken Chatkhara Boti", "بوتي الدجاج تشاتخارا", False, None, [44], note="8 Pieces"),
        item("Chicken Afghani Boti", "بوتي الدجاج الأفغاني", False, None, [40], note="8 Pieces"),
        item("Chicken Malai Boti", "بوتي الدجاج مالاي", False, None, [48], note="8 Pieces"),
        item("Chicken Seekh Kabab", "كباب سيخ الدجاج", False, None, [35], note="4 Pieces"),
        item("Beef Seekh Kabab", "كباب سيخ اللحم البقري", False, None, [38], note="4 Pieces"),
        item("Turkish Beef Kabab", "كباب بقري تركي", False, None, [48], note="4 Pieces"),
        item("Chicken Tikka 2 Pieces (Leg & Chest)", "دجاج تيكا", True, None, [38], note="2 Pieces (Leg & Chest) — price confirmed by branch bill, 13 Nov 2026"),
        item("Fish Tikka", "تيكا السمك", False, None, [58], note="8 Pieces"),
    ]},
    {"id": "shinwari", "en": "Shinwari Section", "ar": "قسم شينواري",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Special Sulemani Karahi", "كراهي سليماني الخاص", False, 850, [65, 118]),
        item("Lamb Karahi", "كراهي لحم الضأن", False, 950, [65, 125]),
        item("Chicken Namkeen Karahi", "دجاج نمكين كراهي", True, 950, [35, 65]),
        item("Chicken White Karahi", "كراهي الدجاج الأبيض", False, 1050, [35, 70]),
        item("Beef Seekh Kabab Karahi", "كراهي كباب سيخ اللحم البقري", False, 1190, [55]),
        item("Chicken Seekh Kabab Karahi", "كراهي كباب سيخ الدجاج", False, None, [45]),
    ]},
    {"id": "pakistani", "en": "Pakistani Section", "ar": "القسم الباكستاني",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Lahori Chicken Karahi", "كراهي الدجاج اللاهوري", False, 850, [35, 65]),
        item("Lahori Mutton Karahi", "كراهي لحم الضأن اللاهوري", False, 1150, [65, 118]),
        item("Chicken Makhni Karahi", "كراهي الدجاج ماخني", False, None, [40, 70]),
        item("Hyderabadi Chicken Handi", "هاندي الدجاج الحيدر أبادي", False, None, [55]),
        item("Mughlai Murgh Handi", "هاندي المرغ المغولي", False, None, [55]),
        item("Butter Chicken", "دجاج بالزبدة", False, 1000, [60]),
        item("Lakshami Tawa Chicken", "دجاج تاوا لاكشمي", False, 850, [45]),
        item("Daal Maharani", "دال مهاراني", False, None, [30]),
        item("Mix Vegetables", "خضار مشكلة", False, None, [25]),
        item("Palak Paneer", "بالاك بانير", False, None, [35]),
    ]},
    {"id": "chapli", "en": "Chapli Kabab Section", "ar": "قسم تشابلي كباب",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Chapli Kabab Simple", "تشابلي كباب عادي", False, None, [26, 46]),
        item("Chapli Kabab Special", "تشابلي كباب خاص", False, None, [28, 48]),
    ]},
    {"id": "sea", "en": "Dive Into The Sea", "ar": "من البحر",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Lahori Fried Fish (Whole)", "سمك لاهوري مقلي (كامل)", False, None, [78]),
        item("BBQ Grill Fish (Whole)", "سمك مشوي على الفحم (كامل)", False, None, [78]),
    ]},
    {"id": "rice", "en": "Rice Corner", "ar": "ركن الأرز",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Hyderabadi Biryani (Chicken)", "برياني حيدر أباد (دجاج)", False, None, [39]),
        item("Matka Biryani (Mutton)", "برياني المطكا (لحم ضأن)", False, None, [55]),
        item("TKR Special Kabuli Pulao (Beef)", "بولو كابلي الخاص بتي كي آر (لحم بقري)", False, None, [45]),
        item("Vegetable Fried Rice", "أرز مقلي بالخضار", False, None, [30]),
        item("Chicken Fried Rice", "أرز مقلي بالدجاج", False, None, [35]),
        item("Steam Rice", "أرز على البخار", False, None, [15]),
    ]},
    {"id": "tandoor", "en": "Tandoor Section", "ar": "قسم التنور",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Roghni Naan", "نان روغني", True, None, [4]),
        item("Garlic Naan", "نان بالثوم", False, None, [4]),
        item("Qandhari Naan", "نان قندهاري", False, None, [7]),
        item("Kalonji Naan", "نان كالونجي", True, None, [4]),
        item("Cheese Naan", "نان بالجبن", False, None, [10]),
        item("Roti", "روتي", True, None, [1]),
    ]},
    {"id": "continental", "en": "The Continental Kitchen", "ar": "المطبخ القاري",
     "ar_printed": True, "note_en": None, "note_ar": None, "items": [
        item("Flame Grill Chicken", "دجاج مشوي على اللهب", False, None, [68]),
        item("Beef Steak", "ستيك لحم بقري", False, None, [80]),
        item("Tarragon Sauce", "صلصة الطرخون", True, None, None),
        item("Morrocan Sauce", "صلصة مغربية", False, None, None),
        item("Mushroom Sauce", "صلصة الفطر", False, None, None),
        item("Pepper Sauce", "صلصة الفلفل", False, None, None),
        item("French Fries", "بطاطس مقلية", True, None, [15], note="Side Order"),
        item("Mash Potato", "بطاطس مهروسة", False, None, None, note="Side Order"),
        item("Sauteed Vegetable", "خضار سوتيه", False, None, None, note="Side Order"),
        item("Penne Arrabiata Pasta", "باستا بيني أرابياتا", False, 480, [45]),
        item("Fettuccine Alfredo Pasta", "باستا فيتوتشيني ألفريدو", False, 750, [55]),
    ]},
    {"id": "china", "en": "Welcome to the China", "ar": "المطبخ الصيني",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Chilli Dry With Rice (Chicken)", "دجاج جاف حار مع الأرز", False, 580, [45]),
        item("Chilli Dry With Rice (Fish)", "سمك جاف حار مع الأرز", False, 520, [55]),
        item("Chilli Dry With Rice (Prawn)", "جمبري جاف حار مع الأرز", False, 540, [58]),
        item("Basil Curry With Rice (Chicken)", "كاري الريحان مع الأرز (دجاج)", False, 680, [45]),
        item("Basil Curry With Rice (Fish)", "كاري الريحان مع الأرز (سمك)", False, 600, [55]),
        item("Basil Curry With Rice (Prawn)", "كاري الريحان مع الأرز (جمبري)", False, 820, [58]),
        item("Chicken Manchurian With Rice", "دجاج مانشوري مع الأرز", False, 850, [45]),
        item("Chicken Chow Mein", "تشاو مين بالدجاج", False, None, [45]),
    ]},
    {"id": "desserts", "en": "Desserts Section", "ar": "قسم الحلويات",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("TKR Special Kheer", "خير الخاص بتي كي آر", False, None, [18]),
        item("Gulab Jamun", "جولاب جامون", False, None, [18]),
        item("Fruit Trifle", "ترايفل الفواكه", False, None, [18]),
        item("Shahi Tukra", "شاهي توكرا", False, None, [18]),
    ]},
    {"id": "hotbev", "en": "Hot Beverages", "ar": "مشروبات ساخنة",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Doodh Patti", "دود باتي", False, None, [5]),
        item("Peshawari Kehwa", "قهوة بيشاوري", False, None, [3]),
        item("Sulemani Tea", "شاي سليماني", False, None, [4]),
        item("Cafe Mocha", "كافيه موكا", False, None, [16]),
        item("Espresso (Single)", "إسبريسو (فردي)", False, None, [10]),
        item("Espresso (Double)", "إسبريسو (مزدوج)", False, None, [14]),
        item("Cappuccino Coffee", "كابتشينو", False, None, [15]),
        item("Cafe Latte", "كافيه لاتيه", False, None, [15]),
        item("Hot Chocolate", "شوكولاتة ساخنة", False, None, [16]),
    ]},
    {"id": "coldbev", "en": "Cold Beverages", "ar": "مشروبات باردة",
     "ar_printed": False, "note_en": None, "note_ar": None, "items": [
        item("Saudi Cocktail (Glass)", "كوكتيل سعودي (كأس)", False, None, [16]),
        item("Saudi Cocktail (Jug)", "كوكتيل سعودي (إبريق)", False, None, [45]),
        item("TKR Delight", "ديلايت تي كي آر", False, None, [18]),
        item("Lassi (Sweet/Salted)", "لاسي (حلو/مالح)", False, None, [8]),
        item("Peach Ice Tea", "شاي مثلج بالخوخ", False, None, [14]),
        item("Lemon Ice Tea", "شاي مثلج بالليمون", False, None, [14]),
        item("Fresh Lime", "ليمون طازج", False, None, [8]),
        item("Fresh seasonal (Juice & Shakes)", "عصائر وميلك شيك موسمية طازجة", False, None, [18]),
        item("Cold Coffee", "قهوة باردة", False, None, [18]),
        item("Iced Americano", "أمريكانو مثلج", False, None, [14]),
        item("Iced Latte (Caramel/Vanilla/Hazelnuts)", "لاتيه مثلج (كراميل/فانيليا/بندق)", False, None, [18]),
        item("Smoothie (Strawberry/Mango/Banana/Vanilla)", "سموثي (فراولة/مانجو/موز/فانيليا)", False, None, [16]),
        item("Mojito (Strawberry/Mint/Orange/Lemon)", "موهيتو (فراولة/نعناع/برتقال/ليمون)", False, None, [17]),
        item("Margarita (Strawberry/Mint/Orange/Lemon)", "مارغريتا (فراولة/نعناع/برتقال/ليمون)", False, None, [15]),
        item("Mineral Water (Small)", "مياه معدنية (صغيرة)", False, None, [3]),
        item("Mineral Water (Large)", "مياه معدنية (كبيرة)", False, None, [5]),
        item("Soft Drink Can", "مشروب غازي (علبة)", False, None, [4]),
    ]},
]

total_items = sum(len(s["items"]) for s in SECTIONS)
priced = sum(1 for s in SECTIONS for i in s["items"] if i["prices"])
print(f"sections={len(SECTIONS)} items={total_items} priced={priced} unpriced={total_items-priced}")

DATA_JSON = json.dumps(SECTIONS, ensure_ascii=False)

HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TKR Al Khobar — Menu | قائمة طعام مطعم طاهر خان الخبر</title>
<meta name="description" content="The real menu of Tahir Khan Restaurant, Al Khobar branch — dishes and prices in SAR, in English and Arabic.">
<style>
:root{--red:#d21f2c;--dark:#12291f;--green:#0f5257;--cream:#faf6ef;--card:#fff;--ink:#1d1d1d;--muted:#6b6b6b;--line:#e8e0d2;--gold:#c9a227}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI",system-ui,-apple-system,Arial,sans-serif;background:var(--cream);color:var(--ink);line-height:1.5}
[dir=rtl] body{font-family:"Segoe UI",Tahoma,Arial,sans-serif}
header.top{background:var(--dark);color:#fff;padding:14px 16px;position:sticky;top:0;z-index:50;box-shadow:0 2px 10px rgba(0,0,0,.25)}
.top-inner{max-width:1060px;margin:0 auto;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.logo{height:54px;width:auto;border-radius:8px;background:#0a1f18}
.brand{flex:1;min-width:200px}
.brand h1{font-size:20px;line-height:1.2}
.brand p{font-size:13px;opacity:.85}
.lang-btn{border:1px solid #fff;background:transparent;color:#fff;border-radius:20px;padding:8px 16px;font-size:14px;cursor:pointer}
.lang-btn:hover{background:rgba(255,255,255,.15)}
.hero{max-width:1060px;margin:0 auto;padding:18px 16px 6px}
.hero img{width:100%;border-radius:14px;display:block;box-shadow:0 4px 18px rgba(0,0,0,.15)}
.hero-cap{font-size:13px;color:var(--muted);margin-top:8px}
.info-bar{max-width:1060px;margin:10px auto 0;padding:0 16px;display:flex;gap:10px;flex-wrap:wrap}
.info-chip{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px;font-size:14px;flex:1;min-width:200px}
.info-chip b{display:block;font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
.call-btn{display:inline-block;background:var(--red);color:#fff;text-decoration:none;font-weight:700;border-radius:10px;padding:10px 18px;font-size:15px}
.call-btn:hover{filter:brightness(1.08)}
.wa-btn{display:inline-block;background:#1faa53;color:#fff;text-decoration:none;font-weight:700;border-radius:10px;padding:10px 18px;font-size:15px;margin-inline-start:8px}
.wa-btn:hover{filter:brightness(1.08)}
.controls{max-width:1060px;margin:16px auto 0;padding:0 16px;position:sticky;top:82px;z-index:40;background:var(--cream);padding-top:10px;padding-bottom:10px}
.search{width:100%;padding:12px 16px;font-size:16px;border:1.5px solid var(--line);border-radius:12px;background:#fff;outline:none}
.search:focus{border-color:var(--green)}
.chips{display:flex;gap:8px;overflow-x:auto;padding:12px 2px 4px;scrollbar-width:thin}
.chip{flex:0 0 auto;border:1.5px solid var(--green);background:#fff;color:var(--green);border-radius:20px;padding:7px 14px;font-size:14px;cursor:pointer;white-space:nowrap}
.chip.active{background:var(--green);color:#fff}
main{max-width:1060px;margin:0 auto;padding:8px 16px 30px}
section.menu-sec{margin-top:26px}
.sec-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;border-bottom:3px solid var(--red);padding-bottom:6px}
.sec-head h2{font-size:22px}
.sec-head .ar{font-size:20px;color:var(--green)}
.sec-note{font-size:13px;color:#8a6d00;background:#fff8dd;border:1px solid #f0dfa0;border-radius:8px;padding:8px 10px;margin-top:8px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin-top:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:6px}
.card img.dish{width:100%;height:180px;object-fit:cover;border-radius:8px;margin-bottom:4px}
.card .name{font-weight:700;font-size:17px}
.card .name-ar{font-size:16px;color:var(--green)}
.card .meta{font-size:13px;color:var(--muted);display:flex;gap:12px;flex-wrap:wrap}
.price{margin-top:auto;font-size:18px;font-weight:800;color:var(--red)}
.price small{font-size:12px;font-weight:600;color:var(--muted)}
.badge{display:inline-block;font-size:12px;font-weight:700;background:#fff3cd;color:#7a5b00;border:1px solid #f0dfa0;border-radius:6px;padding:2px 8px;margin-top:6px}
.badge.red{background:#fde8e8;color:#8f1d24;border-color:#f5c2c2}
.gallery{margin-top:34px}
.gallery h2{font-size:22px;border-bottom:3px solid var(--red);padding-bottom:6px}
.g-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px;margin-top:14px}
.g-grid figure{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.g-grid img{width:100%;height:190px;object-fit:cover;display:block}
.g-grid figcaption{padding:10px 12px;font-size:13.5px}
.missing{margin-top:34px;background:#fff;border:1px dashed #c9a227;border-radius:12px;padding:18px}
.missing h2{font-size:20px;margin-bottom:8px}
.missing ul{margin-inline-start:20px;font-size:15px}
.missing li{margin:4px 0}
footer{max-width:1060px;margin:0 auto;padding:0 16px 40px;font-size:13px;color:var(--muted)}
.no-results{display:none;text-align:center;padding:30px 10px;color:var(--muted);font-size:16px}
@media(max-width:640px){.brand h1{font-size:17px}.logo{height:44px}.controls{top:76px}.cards{grid-template-columns:1fr}.sec-head h2{font-size:19px}}
</style>
</head>
<body>
<header class="top">
  <div class="top-inner">
    <img class="logo" src="assets/logo.jpg" alt="TKR — Tahir Khan Restaurant logo">
    <div class="brand">
      <h1 data-i18n="title">Tahir Khan Restaurant — Al Khobar</h1>
      <p data-i18n="subtitle">Real branch menu · Prices in Saudi Riyals (SAR) · القائمة الحقيقية للفرع</p>
    </div>
    <button class="lang-btn" id="langBtn" type="button">العربية</button>
  </div>
</header>

<div class="hero">
  <img src="assets/menu-cover.jpg" alt="The printed TKR Al Khobar menu cover">
  <p class="hero-cap" data-i18n="heroCap">The printed menu of the Al Khobar branch, photographed on Google Maps and filmed inside the restaurant. Every dish and price on this page was read from that menu.</p>
</div>

<div class="info-bar">
  <div class="info-chip"><b data-i18n="addrB">Address</b><span data-i18n="addr">7th Cross, Prince Majid Street, Al Khobar Al Shamalia, Al Khobar 34427</span></div>
  <div class="info-chip"><b data-i18n="hoursB">Hours</b><span data-i18n="hours">Daily 12:00 PM – 1:00 AM</span></div>
  <div class="info-chip"><b data-i18n="orderB">Reservations — as printed on the menu</b><a class="call-btn" href="tel:+966509009474" data-i18n="call">Call 050 900 9474</a><a class="wa-btn" href="https://wa.me/966509009474" data-i18n="waBtn">WhatsApp 050 900 9474</a>
  <div style="font-size:12px;color:var(--muted);margin-top:6px" data-i18n="waNote">No online ordering is listed for this branch — order by phone or WhatsApp.</div></div>
  <div class="info-chip"><b data-i18n="mapsPhoneB">Branch phone (Google Maps)</b><a class="call-btn" href="tel:+966545990754" data-i18n="mapsPhone">Call +966 54 599 0754</a></div>
</div>

<div class="controls">
  <input class="search" id="search" type="search" placeholder="Search dishes… / ابحث عن طبق…" aria-label="Search dishes">
  <div class="chips" id="chips"></div>
</div>

<main id="menu"></main>
<div class="no-results" id="noResults" data-i18n="noResults">No dishes match your search.</div>

<section class="gallery" style="max-width:1060px;margin:0 auto;padding:0 16px">
  <h2 data-i18n="galH">Inside the Al Khobar branch</h2>
  <div class="g-grid">
    <figure><img src="assets/dining-hall.jpg" alt="Dining hall, TKR Al Khobar"><figcaption data-i18n="g1">The dining hall — red and blue chairs, crystal chandeliers</figcaption></figure>
    <figure><img src="assets/platter.jpg" alt="Giant roasted lamb rice platter, TKR Al Khobar"><figcaption data-i18n="g2">The giant roasted-lamb rice platter at the opening — a branch speciality, not a priced menu item</figcaption></figure>
    <figure><img src="assets/opening-night.jpg" alt="Opening night at TKR Al Khobar"><figcaption data-i18n="g3">Opening night, 12 November 2026</figcaption></figure>
  </div>
</section>

<section class="missing" style="max-width:1060px;margin:26px auto;padding:18px">
  <h2 data-i18n="missH">Not on this page yet — needs the restaurant's confirmation</h2>
  <p style="font-size:14px;margin-bottom:8px" data-i18n="missP">Only a few prices could not be read from the menu. Nothing here is guessed — please confirm with the branch:</p>
  <ul>
    <li data-i18n="m1">Sauce prices — Tarragon, Morrocan, Mushroom and Pepper are listed on the menu without prices</li>
    <li data-i18n="m2">Mash Potato and Sauteed Vegetable (side orders) — no prices on the menu</li>
    <li data-i18n="m3">HungerStation — the branch could not be checked there; the site blocks every restaurant page, even from the user's own Chrome</li>
  </ul>
</section>

<footer>
  <p data-i18n="src">Source: the branch's printed menu as photographed on Google Maps (Menu tab, Nov 2026), cross-checked against the same menu filmed in a customer review video and a customer bill from the branch (13 Nov 2026). Prices are as printed. Where two prices are shown (e.g. 35 / 65 SAR), the first is the half portion and the second the full — confirmed by the bill, which charges Chicken Namkeen Karahi (HALF) at 35 SAR. The 360p video frames had misread several BBQ and Rice Corner prices; those are corrected here from the high-resolution menu photos, and Chicken Tikka is listed at 38 SAR from the bill. Arabic names marked as translated were translated from the English names where the printed Arabic text was not legible — the restaurant's own Arabic wording may differ.</p>
</footer>

<script>
const MENU = __DATA__;
const I18N = {
  en: {title:"Tahir Khan Restaurant — Al Khobar", subtitle:"Real branch menu · Prices in Saudi Riyals (SAR) · القائمة الحقيقية للفرع",
    heroCap:"The printed menu of the Al Khobar branch, photographed on Google Maps and filmed inside the restaurant. Every dish and price on this page was read from that menu.",
    addrB:"Address", addr:"7th Cross, Prince Majid Street, Al Khobar Al Shamalia, Al Khobar 34427",
    hoursB:"Hours", hours:"Daily 12:00 PM – 1:00 AM", orderB:"Reservations — as printed on the menu", call:"Call 050 900 9474",
    waBtn:"WhatsApp 050 900 9474", mapsPhoneB:"Branch phone (Google Maps)", mapsPhone:"Call +966 54 599 0754",
    waNote:"No online ordering is listed for this branch — order by phone or WhatsApp.",
    noResults:"No dishes match your search.", galH:"Inside the Al Khobar branch",
    g1:"The dining hall — red and blue chairs, crystal chandeliers",
    g2:"The giant roasted-lamb rice platter at the opening — a branch speciality, not a priced menu item",
    g3:"Opening night, 12 November 2026",
    missH:"Not on this page yet — needs the restaurant's confirmation",
    missP:"Only a few prices could not be read from the menu. Nothing here is guessed — please confirm with the branch:",
    m1:"Sauce prices — Tarragon, Morrocan, Mushroom and Pepper are listed on the menu without prices",
    m2:"Mash Potato and Sauteed Vegetable (side orders) — no prices on the menu",
    m3:"HungerStation — the branch could not be checked there; the site blocks every restaurant page, even from the user's own Chrome",
    src:"Source: the branch's printed menu as photographed on Google Maps (Menu tab, Nov 2026), cross-checked against the same menu filmed in a customer review video and a customer bill from the branch (13 Nov 2026). Prices are as printed. Where two prices are shown (e.g. 35 / 65 SAR), the first is the half portion and the second the full — confirmed by the bill, which charges Chicken Namkeen Karahi (HALF) at 35 SAR. The 360p video frames had misread several BBQ and Rice Corner prices; those are corrected here from the high-resolution menu photos, and Chicken Tikka is listed at 38 SAR from the bill. Arabic names marked as translated were translated from the English names where the printed Arabic text was not legible — the restaurant's own Arabic wording may differ.",
    all:"All", cal:"Cal.", toConfirm:"Price to confirm", twoSizes:"Half / Full"},
  ar: {title:"مطعم طاهر خان — الخبر", subtitle:"القائمة الحقيقية للفرع · الأسعار بالريال السعودي",
    heroCap:"القائمة المطبوعة لفرع الخبر كما صُوّرت في خرائط جوجل وكما ظهرت في فيديو داخل المطعم. كل طبق وسعر في هذه الصفحة مأخوذ من تلك القائمة.",
    addrB:"العنوان", addr:"التقاطع السابع، شارع الأمير ماجد، الخبر الشمالية، الخبر 34427",
    hoursB:"أوقات العمل", hours:"يومياً 12:00 ظهراً – 1:00 بعد منتصف الليل", orderB:"الحجوزات — كما هو مطبوع على القائمة", call:"اتصل على 0509009474",
    waBtn:"واتساب 0509009474", mapsPhoneB:"هاتف الفرع (خرائط جوجل)", mapsPhone:"اتصل على ‎+966 54 599 0754",
    waNote:"لا يوجد طلب إلكتروني مسجّل لهذا الفرع — اطلب عبر الهاتف أو واتساب.",
    noResults:"لا توجد أطباق مطابقة لبحثك.", galH:"داخل فرع الخبر",
    g1:"صالة الطعام — كراسٍ حمراء وزرقاء وثريات كريستالية",
    g2:"طبق الأرز بلحم الضأن المشوي العملاق في الافتتاح — من تخصصات الفرع، وليس بنداً مسعّراً في القائمة",
    g3:"ليلة الافتتاح، 12 نوفمبر 2026",
    missH:"ليست في هذه الصفحة بعد — تحتاج تأكيد المطعم",
    missP:"لم تُقرأ سوى أسعار قليلة من القائمة. لا شيء هنا مُخمَّن — يرجى التأكيد مع الفرع:",
    m1:"أسعار الصلصات — الطرخون والمغربية والفطر والفلفل مذكورة في القائمة دون أسعار",
    m2:"البطاطس المهروسة والخضار السوتيه (أطباق جانبية) — بلا أسعار في القائمة",
    m3:"هنقرستيشن — لم يمكن التحقق من الفرع هناك؛ الموقع يحجب كل صفحات المطاعم حتى من متصفح المستخدم نفسه",
    src:"المصدر: القائمة المطبوعة للفرع كما صُوّرت في خرائط جوجل (تبويب القائمة، نوفمبر 2026)، وقورنت بنفس القائمة المصوّرة في فيديو مراجعة لأحد الزبائن وفاتورة زبون من الفرع (13 نوفمبر 2026). الأسعار كما هي مطبوعة. وعند ظهور سعرين (مثل 35 / 65 ريال)، الأول للنصف والثاني للكامل — تأكد ذلك من الفاتورة التي تحسب كراهي الدجاج النمكين (نصف) بـ 35 ريالاً. إطارات الفيديو منخفضة الدقة قرأت بعض أسعار المشويات والأرز خطأً؛ وقد صُححت هنا من صور القائمة عالية الدقة، وتيكا الدجاج مسعّرة بـ 38 ريالاً من الفاتورة. الأسماء العربية المترجمة تُرجمت من الأسماء الإنجليزية حيث لم يكن النص العربي المطبوع مقروءاً — وقد تختلف صياغة المطعم نفسه.",
    all:"الكل", cal:"سعرة", toConfirm:"السعر للتأكيد", twoSizes:"نصف / كامل"}
};
let lang = "en";
const $ = s => document.querySelector(s);
function priceHTML(it){
  if(!it.prices) return '<div class="price"><span class="badge">'+I18N[lang].toConfirm+'</span></div>';
  const p = it.prices.map(n=>n).join(" / ");
  const extra = it.prices.length>1 ? ' <small>'+I18N[lang].twoSizes+'</small>' : '';
  return '<div class="price">'+p+' SAR'+extra+'</div>';
}
function render(){
  const q = ($("#search").value||"").trim().toLowerCase();
  const active = document.querySelector(".chip.active");
  const cat = active ? active.dataset.cat : "all";
  const menu = $("#menu"); menu.innerHTML = "";
  let any = false;
  MENU.forEach(sec=>{
    if(cat!=="all" && cat!==sec.id) return;
    const items = sec.items.filter(it=>{
      if(!q) return true;
      return it.en.toLowerCase().includes(q) || it.ar.includes(q);
    });
    if(!items.length) return;
    any = true;
    const s = document.createElement("section"); s.className="menu-sec"; s.id="sec-"+sec.id;
    const head = '<div class="sec-head"><h2>'+(lang==="ar"?sec.ar:sec.en)+'</h2><span class="ar">'+(lang==="ar"?sec.en:sec.ar)+'</span></div>';
    const note = sec["note_"+lang] ? '<div class="sec-note">'+sec["note_"+lang]+'</div>' : '';
    let cards = '<div class="cards">';
    items.forEach(it=>{
      const name = lang==="ar" ? it.ar : it.en;
      const sub = lang==="ar" ? it.en : it.ar;
      const cal = it.cal ? '<span>'+I18N[lang].cal+' '+it.cal+'</span>' : '';
      const note = it.note ? '<span>'+it.note+'</span>' : '';
      const img = it.photo ? '<img class="dish" src="assets/'+it.photo+'" alt="'+it.en+'">' : '';
      cards += '<article class="card">'+img+'<div class="name">'+name+'</div><div class="name-ar">'+sub+'</div><div class="meta">'+cal+note+'</div>'+priceHTML(it)+'</article>';
    });
    cards += '</div>';
    s.innerHTML = head + note + cards;
    menu.appendChild(s);
  });
  $("#noResults").style.display = any ? "none" : "block";
}
function buildChips(){
  const c = $("#chips"); c.innerHTML = "";
  const mk = (id,label)=>{const b=document.createElement("button");b.type="button";b.className="chip"+(id==="all"?" active":"");b.dataset.cat=id;b.textContent=label;b.onclick=()=>{document.querySelectorAll(".chip").forEach(x=>x.classList.remove("active"));b.classList.add("active");render();document.querySelector("main").scrollIntoView({behavior:"smooth"});};c.appendChild(b);};
  mk("all", I18N[lang].all);
  MENU.forEach(s=>mk(s.id, lang==="ar"?s.ar:s.en));
}
function applyLang(){
  document.documentElement.lang = lang;
  document.documentElement.dir = lang==="ar" ? "rtl" : "ltr";
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const k = el.dataset.i18n;
    if(I18N[lang][k]) el.textContent = I18N[lang][k];
  });
  $("#langBtn").textContent = lang==="ar" ? "English" : "العربية";
  $("#search").placeholder = lang==="ar" ? "ابحث عن طبق…" : "Search dishes… / ابحث عن طبق…";
  buildChips(); render();
}
$("#langBtn").onclick = ()=>{ lang = lang==="ar" ? "en" : "ar"; applyLang(); };
$("#search").addEventListener("input", render);
applyLang();
</script>
</body>
</html>
"""

html_out = HTML.replace("__DATA__", DATA_JSON)
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_out)
print("wrote", os.path.join(OUT, "index.html"), len(html_out), "bytes")
