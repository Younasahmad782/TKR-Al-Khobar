(() => {
'use strict';
/* ---------- verified branch data (see README for sources) ---------- */
const B = { lat: 26.2861875, lng: 50.2184375, wa: '966509009474',
  maps: 'https://www.google.com/maps/place/TKR+Al+Khobar/@26.2861875,50.2184375,15z',
  reviewsUrl: 'https://www.google.com/maps/place/TKR+Al+Khobar/@26.2861875,50.2184375,17z/data=!4m7!3m6!1s0x3e49e9000d34ac7f:0xac0dfe2c15750478!8m2!3d26.2861875!4d50.2184375!9m1!1b1' };
B.dir = `https://www.google.com/maps/dir/?api=1&destination=${B.lat},${B.lng}`;
const RATING = { avg: 4.5, total: 346, dist: { 5: 278, 4: 15, 3: 17, 2: 7, 1: 29 } };
const REVIEWS = [
 { n: 'sara Ayesha', s: 5, en: '3 days before 26 Nov 2026', ar: 'قبل 3 أيام من 26 نوفمبر 2026', tag: 'Local Guide · 21 reviews',
   t: 'The food is super delicious! Kind and super active staff. I don\'t prefer soft drinks with food but I was asked 3 to 4 times by different staff member for it which I think that extra touch if we needed it. Wish you success.' },
 { n: 'sohaib khan', s: 5, en: 'A week before 26 Nov 2026', ar: 'قبل أسبوع من 26 نوفمبر 2026', tag: 'Local Guide · 22 reviews',
   t: 'Taste was nice hope they will Maintain the quality service was messy due to crowd cause of opening',
   own: 'Thanks for pointing out. We will get better inshaAllah' },
 { n: 'Salman Zahid', s: 2, en: 'A week before 26 Nov 2026', ar: 'قبل أسبوع من 26 نوفمبر 2026', tag: 'Local Guide · 11 reviews', more: true,
   t: 'Average experience. It\'s a good addition for Pakistani food in khobar but it was below expectation. They need to focus on the service as well as the food quality. It\'s the 2nd day of opening, no cheese nan was available although order was taken. Hummus didnt tasted like Hummus and was tasteless. Chicken karahi was bit cold and…' },
 { n: 'Anasullah Khan', s: 5, en: '2 weeks before 26 Nov 2026', ar: 'قبل أسبوعين من 26 نوفمبر 2026', tag: '7 reviews',
   t: 'Today is the soft opening of this restaurant. Reasonable price and good food.' },
 { n: 'tawsif Jan', s: 5, en: '2 weeks before 26 Nov 2026', ar: 'قبل أسبوعين من 26 نوفمبر 2026', tag: '10 reviews',
   t: 'Last night, I had the pleasure of visiting TKR Al Khobar for its soft opening. The food was absolutely delicious, the atmosphere was amazing, and the hospitality was outstanding. Everything was perfectly arranged, and I truly enjoyed the experience. Wishing TKR Al Khobar great success and many more milestones ahead.' }
];
const GAL = [
 ['platter', 'Rice platter with lamb and a naan', 'طبق أرز مع لحم الضأن ونان'],
 ['rooftop-night', 'The TKR sign and rooftop dining at night', 'لافتة TKR والجلسات على السطح ليلًا'],
 ['dining-hall', 'Indoor dining hall with teal chairs', 'قاعة الطعام الداخلية بكراسيها الفيروزية'],
 ['pulao', 'Pulao with carrots and raisins', 'أرز بولاو بالجزر والزبيب'],
 ['reception', 'TKR reception desk', 'مكتب الاستقبال في TKR'],
 ['kabab', 'Seekh kabab with naan', 'كباب سيخ مع الخبز'],
 ['rooftop-lights', 'Rooftop terrace under string lights', 'التراس العلوي تحت الأضواء المعلقة'],
 ['hall-tour', 'Main dining hall', 'قاعة الطعام الرئيسية'],
 ['hall-tables', 'Dining tables set for guests', 'طاولات الطعام جاهزة للضيوف'],
 ['hall-evening', 'Dining hall in the evening', 'قاعة الطعام في المساء']
];
/* ---------- translations ---------- */
const T = {
 en: { title: 'TKR – Tahir Khan Restaurant, Al Khobar | Pakistani & Afghan Restaurant',
  desc: 'TKR – Tahir Khan Restaurant, Al Khobar. Karahi, dum pukht, BBQ and more. 7th Cross, Prince Majid Street, Al Khobar Al Shamalia. Open daily 12 PM – 1 AM.',
  skip: 'Skip to content', branch: 'Al Khobar', menuBtn: 'Menu', navLabel: 'Main navigation', nMenu: 'Menu', nAbout: 'About', nGallery: 'Gallery', nReviews: 'Reviews', nReserve: 'Reserve', nVisit: 'Visit',
  heroAlt: 'A rice platter with lamb, served with naan at TKR Al Khobar',
  eyebrow: 'Tahir Khan Restaurant · Al Khobar', h1: 'Authentic Pakistani & Afghan flavours, now in Al Khobar', lead: 'Karahi, dum pukht, BBQ and more — served daily until 1 AM.',
  bMenu: 'View menu', bDir: 'Get directions', bReserve: 'Reserve a table', hoursL: 'Hours', hoursV: 'Daily 12:00 PM – 1:00 AM', addrL: 'Address', addrV: '7th Cross, Prince Majid St, Al Khobar Al Shamalia', resL: 'Reservations',
  tMenu: 'Our menu', menuSub: 'Prices in Saudi Riyals (SAR), from the branch’s printed menu.', searchL: 'Search the menu', searchPh: 'Search dishes in English or Arabic', printed: 'View printed menu', catLabel: 'Menu categories', loading: 'Loading menu…',
  menuFine: 'Dual prices are Half / Full portions. Items marked “price to be confirmed” have no price printed on the menu. Arabic names printed on the menu are used where available; the rest are translations pending the restaurant’s review. Prices and availability may change — please confirm with the restaurant.',
  half: 'Half', full: 'Full', cur: 'SAR', tbc: 'Price to be confirmed', items: n => `${n} dishes`, noRes: 'No dishes match your search.', menuErr: 'The menu could not be loaded. Please refresh the page, or call the restaurant.',
  tAbout: 'About TKR Al Khobar', a1: 'TKR — Tahir Khan Restaurant — brings its Pakistani and Afghan cooking to Al Khobar, on Prince Majid Street in Al Khobar Al Shamalia. The branch had its grand opening on Thursday 12 November 2026.',
  a2: 'The menu covers signature dum pukht and platters, Shinwari and Lahori karahi, BBQ, Chapli Kabab, rice, tandoor breads, seafood, soups, salads, Chinese and Continental dishes, desserts and hot and cold drinks.',
  a3: 'The restaurant is part of the TKR family founded by Tahir Khan, with branches in Pakistan, the UK and Saudi Arabia. The Al Khobar listing notes a wheelchair-accessible entrance and parking.', bChain: 'Visit the main TKR website', platterAlt: 'Pulao with carrots and raisins at TKR Al Khobar',
  tGallery: 'Gallery', galSub: 'Photos of the branch and its food. Tap a photo to view it full size.', tReviews: 'Google reviews', revCount: 'Google reviews', star: 'stars', rated: 'rating', ownerReply: 'Reply from the owner', readMore: 'Read the full review on Google', origReview: 'Original review',
  revFine: 'Showing the 5 reviews visible on the public Google Maps listing when collected on 26 November 2026; reviews are in the reviewers’ own words. Source: Google Maps.', bReadAll: 'Read all reviews on Google', bWrite: 'Write a review on Google',
  tReserve: 'Reserve a table', resP: 'Send your request to the restaurant on WhatsApp. This is a request only — your table is not booked until the restaurant confirms it.',
  resFine: 'Reservation number printed on the menu: <bdi dir="ltr">050 900 9474</bdi> (phone and WhatsApp). Online ordering is not set up on this website — please call or message to order.', bCallRes: 'Call to reserve',
  fName: 'Name', fPhone: 'Phone number', fDate: 'Date', fTime: 'Time', fGuests: 'Number of guests', fNotes: 'Special requests (optional)', fSend: 'Send request on WhatsApp',
  eName: 'Please enter your name.', ePhone: 'Please enter a valid phone number (at least 7 digits).', eDate: 'Please choose today’s date or a future date.', eTime: 'Please choose a time.', eGuests: 'Please enter between 1 and 50 guests.',
  fOk: 'WhatsApp has been opened with your request. It is not confirmed until the restaurant replies.', waMsg: (v) => `Hello TKR Al Khobar, I would like to request a table.\nName: ${v.n}\nPhone: ${v.p}\nDate: ${v.d}\nTime: ${v.t}\nGuests: ${v.g}${v.x ? '\nNotes: ' + v.x : ''}`,
  tVisit: 'Visit & contact', addrFull: 'TKR Al Khobar, 7th Cross, Prince Majid Street, Al Khobar Al Shamalia, Al Khobar 34427, Saudi Arabia', phoneL: 'Phone & WhatsApp', listingTag: '(Google Maps listing)', resTag: '(reservations — phone & WhatsApp)', bCall: 'Call', socialL: 'Follow',
  fIntro: 'Pakistani & Afghan cooking in Al Khobar.', fLinks: 'Explore', copy: '© 2026 TKR Al Khobar. Demo website prepared for the restaurant’s review — not yet an official TKR website.', close: 'Close', prev: 'Previous', next: 'Next', printedCap: n => `Printed menu — page ${n} of 13`,
  nf: 'Page not found', nfP: 'The page you are looking for does not exist.', nfB: 'Back to home' },
 ar: { title: 'مطعم طاهر خان (TKR) – فرع الخبر | مطعم باكستاني وأفغاني',
  desc: 'مطعم طاهر خان TKR فرع الخبر. كراهي ودم بخت ومشويات وأكثر. الشارع السابع، شارع الأمير ماجد، الخبر الشمالية. يعمل يوميًا من 12 ظهرًا حتى 1 بعد منتصف الليل.',
  skip: 'انتقل إلى المحتوى', branch: 'الخبر', menuBtn: 'القائمة', navLabel: 'التنقل الرئيسي', nMenu: 'قائمة الطعام', nAbout: 'من نحن', nGallery: 'الصور', nReviews: 'التقييمات', nReserve: 'احجز', nVisit: 'زورونا',
  heroAlt: 'طبق أرز مع لحم الضأن يُقدم مع النان في TKR الخبر',
  eyebrow: 'مطعم طاهر خان · الخبر', h1: 'نكهات باكستانية وأفغانية أصيلة، الآن في الخبر', lead: 'كراهي ودم بخت ومشويات وأكثر — نخدمكم يوميًا حتى الساعة 1 بعد منتصف الليل.',
  bMenu: 'عرض القائمة', bDir: 'الاتجاهات', bReserve: 'احجز طاولة', hoursL: 'ساعات العمل', hoursV: 'يوميًا من 12:00 ظهرًا حتى 1:00 بعد منتصف الليل', addrL: 'العنوان', addrV: 'الشارع السابع، شارع الأمير ماجد، الخبر الشمالية', resL: 'الحجوزات',
  tMenu: 'قائمة الطعام', menuSub: 'الأسعار بالريال السعودي، من قائمة الفرع المطبوعة.', searchL: 'ابحث في القائمة', searchPh: 'ابحث عن طبق بالعربية أو الإنجليزية', printed: 'عرض القائمة المطبوعة', catLabel: 'أقسام القائمة', loading: 'جارٍ تحميل القائمة…',
  menuFine: 'الأسعار المزدوجة تعني نصف / كامل. الأصناف المكتوب عليها «السعر يُؤكد لاحقًا» لا يوجد لها سعر مطبوع في القائمة. استُخدمت الأسماء العربية المطبوعة في القائمة حيثما وُجدت، وبقية الأسماء مترجمة بانتظار مراجعة المطعم. قد تتغير الأسعار والتوفر — يرجى التأكيد مع المطعم.',
  half: 'نصف', full: 'كامل', cur: 'ر.س', tbc: 'السعر يُؤكد لاحقًا', items: n => `${n} صنفًا`, noRes: 'لا توجد أطباق مطابقة لبحثك.', menuErr: 'تعذر تحميل القائمة. يرجى تحديث الصفحة أو الاتصال بالمطعم.',
  tAbout: 'عن TKR الخبر', a1: 'يقدم مطعم طاهر خان (TKR) مأكولاته الباكستانية والأفغانية في الخبر، على شارع الأمير ماجد في الخبر الشمالية. افتُتح الفرع رسميًا يوم الخميس 12 نوفمبر 2026.',
  a2: 'تشمل القائمة أطباق دم بخت المميزة والأطباق العائلية، وكراهي الشينواري واللاهوري، والمشويات، وتشابلي كباب، والأرز، وخبز التنور، والمأكولات البحرية، والشوربات، والسلطات، والأطباق الصينية والقارية، والحلويات، والمشروبات الساخنة والباردة.',
  a3: 'المطعم جزء من عائلة TKR التي أسسها طاهر خان، وله فروع في باكستان والمملكة المتحدة والمملكة العربية السعودية. وتشير صفحة فرع الخبر إلى وجود مدخل ومواقف مهيأة لذوي الاحتياجات الخاصة.', bChain: 'زيارة موقع TKR الرئيسي', platterAlt: 'أرز بولاو بالجزر والزبيب في TKR الخبر',
  tGallery: 'معرض الصور', galSub: 'صور من الفرع وأطباقه. اضغط على الصورة لعرضها بالحجم الكامل.', tReviews: 'تقييمات Google', revCount: 'تقييم على Google', star: 'نجوم', rated: 'التقييم', ownerReply: 'رد المالك', readMore: 'اقرأ التقييم كاملًا على Google', origReview: 'التقييم الأصلي',
  revFine: 'نعرض التقييمات الخمسة الظاهرة في صفحة Google Maps العامة عند جمعها في 26 نوفمبر 2026، وهي بكلمات أصحابها. المصدر: Google Maps.', bReadAll: 'اقرأ كل التقييمات على Google', bWrite: 'اكتب تقييمًا على Google',
  tReserve: 'احجز طاولة', resP: 'أرسل طلبك إلى المطعم عبر واتساب. هذا طلب فقط — لا يُعتبر الحجز مؤكدًا حتى يؤكده المطعم.',
  resFine: 'رقم الحجوزات المطبوع على القائمة: <bdi dir="ltr">050 900 9474</bdi> (اتصال وواتساب). الطلب عبر الإنترنت غير متاح في هذا الموقع — يرجى الاتصال أو المراسلة للطلب.', bCallRes: 'اتصل للحجز',
  fName: 'الاسم', fPhone: 'رقم الجوال', fDate: 'التاريخ', fTime: 'الوقت', fGuests: 'عدد الضيوف', fNotes: 'طلبات خاصة (اختياري)', fSend: 'أرسل الطلب عبر واتساب',
  eName: 'يرجى إدخال اسمك.', ePhone: 'يرجى إدخال رقم جوال صحيح (7 أرقام على الأقل).', eDate: 'يرجى اختيار تاريخ اليوم أو تاريخ لاحق.', eTime: 'يرجى اختيار الوقت.', eGuests: 'يرجى إدخال عدد ضيوف بين 1 و50.',
  fOk: 'تم فتح واتساب مع طلبك. لا يُعتبر الحجز مؤكدًا حتى يرد المطعم.', waMsg: (v) => `مرحبًا TKR الخبر، أرغب في طلب حجز طاولة.\nالاسم: ${v.n}\nالجوال: ${v.p}\nالتاريخ: ${v.d}\nالوقت: ${v.t}\nعدد الضيوف: ${v.g}${v.x ? '\nملاحظات: ' + v.x : ''}`,
  tVisit: 'زورونا وتواصلوا معنا', addrFull: 'TKR الخبر، الشارع السابع، شارع الأمير ماجد، الخبر الشمالية، الخبر 34427، المملكة العربية السعودية', phoneL: 'الهاتف وواتساب', listingTag: '(حسب صفحة Google Maps)', resTag: '(الحجوزات — اتصال وواتساب)', bCall: 'اتصل', socialL: 'تابعونا',
  fIntro: 'مأكولات باكستانية وأفغانية في الخبر.', fLinks: 'تصفح', copy: '© 2026 TKR الخبر. موقع تجريبي أُعد لمراجعة المطعم — وليس موقعًا رسميًا لـ TKR بعد.', close: 'إغلاق', prev: 'السابق', next: 'التالي', printedCap: n => `القائمة المطبوعة — صفحة ${n} من 13`,
  nf: 'الصفحة غير موجودة', nfP: 'الصفحة التي تبحث عنها غير موجودة.', nfB: 'العودة إلى الرئيسية' }
};
/* ---------- helpers ---------- */
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const store = { get: k => { try { return localStorage.getItem(k); } catch { return null; } }, set: (k, v) => { try { localStorage.setItem(k, v); } catch {} } };
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const norm = s => String(s || '').toLowerCase().normalize('NFKD').replace(/[\u064B-\u065F\u0670\u0640]/g, '').replace(/[أإآٱ]/g, 'ا').replace(/ى/g, 'ي').replace(/ة/g, 'ه').replace(/[^\p{L}\p{N} ]/gu, ' ').replace(/\s+/g, ' ').trim();
const D = { en: 'ltr', ar: 'rtl' };
let lang = 'en', MENU = null, lbList = [], lbI = 0;
const t = k => T[lang][k];

/* ---------- language ---------- */
function setLang(l, push) {
  lang = l === 'ar' ? 'ar' : 'en'; store.set('tkr-lang', lang);
  const h = document.documentElement; h.lang = lang; h.dir = lang === 'ar' ? 'rtl' : 'ltr';
  $$('[data-i18n]').forEach(e => { const v = T[lang][e.dataset.i18n]; if (typeof v === 'string') e.innerHTML = v; });
  $$('[data-i18n-ph]').forEach(e => e.placeholder = t(e.dataset.i18nPh));
  $$('[data-i18n-alt]').forEach(e => e.alt = t(e.dataset.i18nAlt));
  $$('[data-i18n-aria]').forEach(e => e.setAttribute('aria-label', t(e.dataset.i18nAria)));
  document.title = t('title'); $('meta[name=description]').content = t('desc');
  $('meta[property="og:title"]').content = t('title'); $('meta[property="og:description"]').content = t('desc');
  $('meta[property="og:locale"]').content = lang === 'ar' ? 'ar_SA' : 'en_US'; $('meta[property="og:locale:alternate"]').content = lang === 'ar' ? 'en_US' : 'ar_SA';
  $$('.lang').forEach(b => { b.textContent = lang === 'ar' ? 'English' : 'العربية'; b.lang = lang === 'ar' ? 'en' : 'ar'; });
  $('#lbX').setAttribute('aria-label', t('close')); $('#lbP').setAttribute('aria-label', t('prev')); $('#lbN').setAttribute('aria-label', t('next'));
  const u = new URL(location.href); u.searchParams.set('lang', lang); if (push !== false) history.replaceState(null, '', u);
  renderMenu(); renderGallery(); renderReviews(); renderChips(); if (!$('#lb').open) return; showLb();
}
/* ---------- menu ---------- */
function priceHtml(p) {
  if (!p || !p.length) return `<div class="pr tbc">${t('tbc')}</div>`;
  const c = `<span class="cur">${t('cur')}</span>`;
  if (p.length === 1) return `<div class="pr"><bdi>${p[0]}</bdi>${c}</div>`;
  return `<div class="pr"><i>${t('half')}</i><bdi>${p[0]}</bdi>${c}<i>${t('full')}</i><bdi>${p[1]}</bdi>${c}</div>`;
}
function renderChips() {
  if (!MENU) return;
  $('#chips').innerHTML = MENU.map(s => `<a href="#m-${s.id}" data-id="${s.id}">${esc(s[lang])}</a>`).join('');
}
function renderMenu() {
  const box = $('#menuList'); if (!MENU) return;
  const q = norm($('#q').value); let total = 0;
  const html = MENU.map(s => {
    const secHit = q && (norm(s.en).includes(q) || norm(s.ar).includes(q));
    const items = s.items.filter(i => !q || secHit || norm(i.en).includes(q) || norm(i.ar).includes(q));
    if (!items.length) return ''; total += items.length;
    const [p, o] = lang === 'ar' ? ['ar', 'en'] : ['en', 'ar'];
    return `<section class="msec" id="m-${s.id}" aria-labelledby="h-${s.id}"><h3 id="h-${s.id}">${esc(s[p])}<small lang="${o}" dir="${D[o]}">${esc(s[o])}</small></h3><div class="cards">` +
      items.map(i => `<article class="card"><div class="n"><b lang="${p}" dir="${D[p]}">${esc(i[p])}</b><span lang="${o}" dir="${D[o]}">${esc(i[o])}</span>${(lang === 'ar' ? i.noteAr : i.noteEn) ? `<em>${esc(lang === 'ar' ? i.noteAr : i.noteEn)}</em>` : ''}</div>${priceHtml(i.prices)}</article>`).join('') + `</div></section>`;
  }).join('');
  box.innerHTML = html || `<p class="empty">${t('noRes')}</p>`;
  $('#count').textContent = q ? t('items')(total) : '';
  $('#chips').style.display = q ? 'none' : '';
}
async function loadMenu() {
  try { const r = await fetch('data/menu.json'); if (!r.ok) throw 0; MENU = await r.json(); renderChips(); renderMenu(); }
  catch { $('#menuList').innerHTML = `<p class="empty" role="alert">${t('menuErr')}</p>`; }
}
/* ---------- gallery + lightbox ---------- */
function renderGallery() {
  $('#grid').innerHTML = GAL.map((g, i) => `<button type="button" data-i="${i}" aria-label="${esc(g[lang === 'ar' ? 2 : 1])}"><img src="img/gallery/${g[0]}.jpg" loading="lazy" decoding="async" alt="${esc(g[lang === 'ar' ? 2 : 1])}"></button>`).join('');
}
function openLb(list, i) { lbList = list; lbI = i; const d = $('#lb'); if (!d.open) d.showModal(); showLb(); }
function showLb() {
  const it = lbList[lbI]; if (!it) return; $('#lbImg').src = it.src; $('#lbImg').alt = it.alt(); $('#lbCap').textContent = it.alt();
  $('#lbP').style.display = $('#lbN').style.display = lbList.length > 1 ? '' : 'none';
}
const stepLb = d => { lbI = (lbI + d + lbList.length) % lbList.length; showLb(); };
/* ---------- reviews ---------- */
function renderReviews() {
  $('#bars').innerHTML = [5, 4, 3, 2, 1].map(n => `<li><span dir="ltr">${n}★</span><span class="t"><i style="width:${(RATING.dist[n] / RATING.total * 100).toFixed(1)}%"></i></span><b dir="ltr">${RATING.dist[n]}</b></li>`).join('');
  $('#revs').innerHTML = REVIEWS.map(r => `<article class="rev"><h4>${esc(r.n)}</h4><p class="m"><span class="stars" role="img" aria-label="${r.s} ${t('star')}">${'★'.repeat(r.s)}${'☆'.repeat(5 - r.s)}</span> · ${esc(r[lang])} · ${esc(r.tag)}</p>` +
    `<blockquote lang="en" dir="ltr">${esc(r.t)}</blockquote>${r.more ? `<a href="${B.reviewsUrl}" target="_blank" rel="noopener">${t('readMore')}</a>` : ''}` +
    `${r.own ? `<div class="own"><b>${t('ownerReply')}</b><span lang="en" dir="ltr">${esc(r.own)}</span></div>` : ''}</article>`).join('');
}
/* ---------- reservation form (WhatsApp hand-off; no fake confirmation) ---------- */
function setErr(id, msg) { const e = $('#e-' + id); e.textContent = msg || ''; e.parentElement.classList.toggle('bad', !!msg); $('#' + id).setAttribute('aria-invalid', !!msg); }
function submitForm(ev) {
  ev.preventDefault(); const v = { n: $('#fn').value.trim(), p: $('#fp').value.trim(), d: $('#fd').value, t: $('#ft').value, g: +$('#fg').value, x: $('#fx').value.trim() };
  const today = new Date(); today.setHours(0, 0, 0, 0); let bad = null;
  const chk = (id, ok, k) => { setErr(id, ok ? '' : t(k)); if (!ok && !bad) bad = id; };
  chk('fn', v.n.length > 1, 'eName'); chk('fp', v.p.replace(/\D/g, '').length >= 7, 'ePhone');
  chk('fd', v.d && new Date(v.d + 'T00:00') >= today, 'eDate'); chk('ft', !!v.t, 'eTime'); chk('fg', Number.isInteger(v.g) && v.g >= 1 && v.g <= 50, 'eGuests');
  if (bad) { $('#' + bad).focus(); $('#fnote').textContent = ''; return; }
  window.open(`https://wa.me/${B.wa}?text=${encodeURIComponent(T[lang].waMsg(v))}`, '_blank', 'noopener');
  $('#fnote').textContent = t('fOk');
}
/* ---------- init ---------- */
function init() {
  ['dir1', 'dir2', 'dir3'].forEach(i => $('#' + i).href = B.dir); $('#revAll').href = B.reviewsUrl; $('#revWrite').href = B.reviewsUrl;
  const d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset()); $('#fd').min = d.toISOString().slice(0, 10);
  const q = new URLSearchParams(location.search).get('lang'), saved = store.get('tkr-lang');
  const nav = (navigator.language || '').toLowerCase().startsWith('ar') ? 'ar' : 'en';
  setLang(q === 'ar' || q === 'en' ? q : (saved === 'ar' || saved === 'en' ? saved : nav), false);
  loadMenu();
  $$('.lang').forEach(b => b.addEventListener('click', () => setLang(lang === 'ar' ? 'en' : 'ar')));
  $('#q').addEventListener('input', renderMenu);
  $('#burger').addEventListener('click', e => { const o = $('#nav').classList.toggle('open'); e.currentTarget.setAttribute('aria-expanded', o); });
  $('#nav').addEventListener('click', e => { if (e.target.tagName === 'A') { $('#nav').classList.remove('open'); $('#burger').setAttribute('aria-expanded', 'false'); } });
  $('#grid').addEventListener('click', e => { const b = e.target.closest('button'); if (b) openLb(GAL.map(g => ({ src: `img/gallery/${g[0]}.jpg`, alt: () => g[lang === 'ar' ? 2 : 1] })), +b.dataset.i); });
  $('#printedBtn').addEventListener('click', () => openLb(Array.from({ length: 13 }, (_, i) => ({ src: `img/menu/menu-${String(i + 1).padStart(2, '0')}.jpg`, alt: () => t('printedCap')(i + 1) })), 12));
  $('#lbX').addEventListener('click', () => $('#lb').close()); $('#lbP').addEventListener('click', () => stepLb(-1)); $('#lbN').addEventListener('click', () => stepLb(1));
  $('#lb').addEventListener('click', e => { if (e.target.id === 'lb') $('#lb').close(); });
  $('#lb').addEventListener('keydown', e => { const rtl = lang === 'ar'; if (e.key === 'ArrowRight') stepLb(rtl ? -1 : 1); if (e.key === 'ArrowLeft') stepLb(rtl ? 1 : -1); });
  $('#form').addEventListener('submit', submitForm);
  const io = 'IntersectionObserver' in window && new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) $$('#chips a').forEach(a => a.classList.toggle('on', a.dataset.id === en.target.id.slice(2))); }), { rootMargin: '-30% 0px -65% 0px' });
  if (io) new MutationObserver(() => $$('.msec').forEach(s => io.observe(s))).observe($('#menuList'), { childList: true });
}
window.TKR = { setLang: l => setLang(l), T, get lang() { return lang; } };
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
