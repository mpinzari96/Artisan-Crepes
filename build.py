#!/usr/bin/env python3
"""Generates the HTML pages. Shared header/footer + inlined critical CSS live here.
Edit content below, then run: python3 build.py  (no dependencies)."""
D="https://artisancrepes.example.com"   # PLACEHOLDER domain
PHONE="(916)&nbsp;555&#8209;0123"; TEL="+19165550123"; EMAIL="orders@example.com"  # PLACEHOLDER contact
CTA="Request a Catering Order"
CSS="".join(open(f"css/{f}").read() for f in ["tokens.css","base.css","site.css"])
import re; CSS=re.sub(r"/\*.*?\*/","",CSS,flags=re.S); CSS=re.sub(r"\s*\n\s*","",CSS)

def head(title,desc,path,cur,extra="",preload=False):
    pre='<link rel="preload" as="image" href="/img/logo-mark-320.webp" fetchpriority="high">\n' if preload else ""
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}</a></li>' for h,t in
        [("/","Home"),("/menu.html","Menu"),("/about.html","Our Story"),("/order.html","Catering Order")])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<!-- PLACEHOLDER: replace artisancrepes.example.com with the real domain (also sitemap.xml, robots.txt) -->
<link rel="canonical" href="{D}/{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{D}/{path}">
<meta property="og:image" content="{D}/img/logo-full-563.webp">
<meta name="theme-color" content="#78322E">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon-32.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{pre}<!-- Critical CSS inlined from css/tokens.css + css/base.css (design v1.1) + css/site.css; regenerate with build.py -->
<style>{CSS}</style>
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="container">
<a class="brand" href="/"><img src="/img/logo-header-120.webp" width="64" height="53" alt=""><span>Artisan Crepes</span></a>
<button type="button" class="nav-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
<nav aria-label="Primary"><ul class="nav" id="primary-nav">{nav}</ul></nav>
<a class="btn header-cta" href="/order.html">{CTA}</a>
</div></header>
<main id="main">
'''
FOOT=f'''</main>
<footer class="site-footer"><div class="container"><div class="footer-grid">
<div><img class="footer-logo" src="/img/logo-mark-320.webp" width="120" height="99" alt="Artisan Crepes" loading="lazy" decoding="async"><p style="margin-top:var(--sp-3)">French crêpe catering for Sacramento weddings, parties &amp; events.</p><p style="margin-top:var(--sp-3)"><a class="btn btn--butter" href="/order.html">{CTA}</a></p></div>
<div><h2>Contact</h2>
<!-- PLACEHOLDER: phone and email (also in schema on index.html) -->
<p>Catering · Pickup only<br>Serving Sacramento, CA &amp; nearby<br><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h2>Order hours</h2>
<!-- PLACEHOLDER: hours and lead times (also in schema on index.html) -->
<div class="hours"><span>Inquiries</span><span>Mon–Fri 9a–5p</span><span>Pickups</span><span>Tue–Sun, by appt.</span><span>Lead time</span><span>72 hrs · weddings 2 wks</span></div></div>
<div><h2>Follow</h2>
<!-- PLACEHOLDER: social profile URLs (also sameAs in schema) -->
<ul class="socials"><li><a href="https://instagram.com/" aria-label="Instagram" rel="noopener">IG</a></li><li><a href="https://facebook.com/" aria-label="Facebook" rel="noopener">FB</a></li><li><a href="https://tiktok.com/" aria-label="TikTok" rel="noopener">TT</a></li></ul></div>
</div><p class="legal">© 2026 Artisan Crepes · Sacramento, CA · Pickup address shared after order confirmation.</p></div></footer>
<div class="sticky-cta"><a class="btn btn--lg" href="/order.html">{CTA}</a></div>
<script src="/js/nav.js" defer></script>
</body>
</html>
'''
SCHEMA=f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":["Restaurant","LocalBusiness"],"@id":"{D}/#business",
"name":"Artisan Crepes","description":"Handmade hot, cold and savory crêpes made by the dozen for weddings, parties and corporate events. Pickup-only catering in Sacramento, CA.",
"url":"{D}/","image":"{D}/img/logo-full-563.webp","logo":"{D}/img/logo-mark-320.webp",
"telephone":"{TEL}","email":"{EMAIL}","servesCuisine":["French","Crêpes"],"priceRange":"$$","acceptsReservations":false,"hasMenu":"{D}/menu.html",
"address":{{"@type":"PostalAddress","addressLocality":"Sacramento","addressRegion":"CA","addressCountry":"US"}},
"areaServed":[{{"@type":"City","name":"Sacramento","containedInPlace":{{"@type":"State","name":"California"}}}},{{"@type":"City","name":"Elk Grove"}},{{"@type":"City","name":"Roseville"}},{{"@type":"City","name":"Folsom"}},{{"@type":"City","name":"Davis"}},{{"@type":"City","name":"West Sacramento"}}],
"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"17:00"}}],
"sameAs":["https://instagram.com/","https://facebook.com/","https://tiktok.com/"]}}
</script>
<!-- PLACEHOLDER: schema uses placeholder domain, phone, email, hours (inquiry hours) and social URLs -->
'''
# PLACEHOLDER menu: names, descriptions and per-dozen prices
MENU={"hot":("Hot Crêpes","Served warm, best within an hour of pickup.",[("Nutella Banane","Hazelnut, banana, toasted almond.","$42/dz"),("Salted Caramel Apple","Warm apples, house caramel, fleur de sel.","$46/dz"),("Lemon Sugar","Butter, fresh lemon, cane sugar.","$38/dz"),("Crème Brûlée","Vanilla custard, torched sugar.","$48/dz")]),
"cold":("Cold Crêpes","Chilled and fresh for showers, brunches and summer events.",[("Berry Chantilly","Delta strawberries, blueberries, chantilly.","$46/dz"),("Lemon Ricotta","Meyer lemon curd, whipped ricotta, mint.","$42/dz"),("Strawberry Nutella","Strawberries, hazelnut spread.","$44/dz"),("Peach Mascarpone","Valley peaches, sweet mascarpone.","$46/dz")]),
"savory":("Savory Galettes","Buckwheat galettes for lunches, receptions and corporate events.",[("Jambon Gruyère","Buckwheat, ham, Gruyère, egg.","$54/dz"),("Garden Chèvre","Goat cheese, spinach, roasted tomato, pesto.","$50/dz"),("Chicken Pesto","Roasted chicken, basil pesto, mozzarella.","$54/dz"),("Smoked Salmon Dill","Smoked salmon, crème fraîche, dill.","$58/dz")])}
def card(k,i,lbl):
    n,d,p=MENU[k][2][i]
    return f'<article class="card" style="--accent:var(--c-{k})"><div class="media media--{k}" role="img" aria-label="{n} (placeholder image)"></div><div class="card__body"><span class="tag">{lbl} · by the dozen</span><div class="card__top"><h3>{n}</h3><span class="price">{p}</span></div><p class="muted">{d}</p><a class="btn btn--outline" href="/order.html">Add to request</a></div></article>'
STEPS='''<ol class="steps"><li><h3>Request</h3><p class="muted">Tell us your event, date, guest count and favorite crêpes.</p></li><li><h3>Confirm</h3><p class="muted">We send a quote and the pickup address within one business day.</p></li><li><h3>Pick up &amp; serve</h3><p class="muted">Collect them boxed and labeled, ready for your guests.</p></li></ol>'''

idx=head("Crepes Sacramento | Crêpe Catering for Events | Artisan Crepes",
 "Best crepes in Sacramento for weddings, parties &amp; corporate events. Hot, cold &amp; savory crêpes by the dozen. Pickup only. Request a catering order.","","/",SCHEMA,True)
idx+=f'''<section class="hero"><div class="container"><div><p class="eyebrow">Crêpe catering · Sacramento, CA</p>
<h1>Crêpes by the dozen for weddings, parties &amp; events.</h1>
<p class="lead">Handmade French crêpes in big batches, filled with fresh Sacramento Valley produce. Order ahead, pick them up, and serve.</p>
<div class="actions"><a class="btn btn--lg" href="/order.html">{CTA}</a><a class="btn btn--outline btn--lg" href="/menu.html">See the menu</a></div>
<ul class="events" role="list" aria-label="We cater"><li>Weddings</li><li>Parties</li><li>Corporate</li><li>Showers</li></ul>
<p class="muted" style="margin-top:var(--sp-3);font-size:var(--fs-sm)">Pickup only · Order 72 hours ahead · Pickup address sent once your order is confirmed</p></div>
<img class="hero__mark" src="/img/logo-mark-320.webp" width="320" height="264" alt="Artisan Crepes monogram with whisk" fetchpriority="high"></div></section>
<div class="container">
<section class="section"><div class="section-head"><p class="eyebrow">Featured</p><h2>Favorite crêpes for Sacramento events</h2></div>
<div class="grid">{card("hot",0,"Hot")}{card("cold",0,"Cold")}{card("savory",0,"Savory")}</div></section>
<section class="section"><div class="section-head"><p class="eyebrow">How it works</p><h2>Ordering is easy</h2></div>{STEPS}</section>
<section class="section center"><p class="eyebrow">Sacramento &amp; nearby</p><h2>Planning an event in Sacramento?</h2>
<p class="lead" style="margin-top:var(--sp-3)">Weddings, birthdays, showers, office breakfasts and more. We serve Sacramento, Elk Grove, Roseville, Folsom, Davis and West Sacramento.</p>
<p style="margin-top:var(--sp-5)"><a class="btn btn--lg" href="/order.html">{CTA}</a></p></section>
</div>
'''+FOOT

def msec(k):
    t,l,items=MENU[k]
    li="".join(f'<li class="menu-item"><div class="menu-item__row"><h3>{n}</h3><span class="price">{p}</span></div><p>{d}</p></li>' for n,d,p in items)
    return f'<section id="{k}" class="menu-section menu-section--{k}"><h2>{t}</h2><p class="lead">{l}</p><ul class="menu-list">{li}</ul></section>'
menu=head("Crepe Menu Sacramento | Hot, Cold &amp; Savory Crêpes",
 "Crêpe catering menu in Sacramento: hot crêpes, cold crêpes and savory galettes, priced by the dozen for parties, weddings and events.","menu.html","/menu.html")
menu+=f'''<section class="page-hero"><div class="container"><p class="eyebrow">Menu · Priced by the dozen</p><h1>Our Crêpe Menu</h1>
<p class="lead">Every crêpe is made to order in large batches. Mix and match hot, cold and savory.</p>
<nav aria-label="Menu sections"><ul class="jump"><li><a href="#hot" style="--accent:var(--c-hot)">Hot</a></li><li><a href="#cold" style="--accent:var(--c-cold)">Cold</a></li><li><a href="#savory" style="--accent:var(--c-savory)">Savory</a></li></ul></nav></div></section>
<div class="container section">
<!-- PLACEHOLDER: all menu items and prices are placeholders; edit MENU in build.py -->
{msec("hot")}{msec("cold")}{msec("savory")}
<div class="center" style="margin-top:var(--sp-8)"><h2>Ready to plan your event?</h2><p style="margin-top:var(--sp-5)"><a class="btn btn--lg" href="/order.html">{CTA}</a></p></div>
</div>
'''+FOOT

about=head("Our Story | Artisan Crepes Sacramento Crêpe Catering","Artisan Crepes is a Sacramento crêpe kitchen making handmade hot, cold and savory crêpes by the dozen for weddings, parties and events.","about.html","/about.html")
about+=f'''<section class="page-hero"><div class="container"><p class="eyebrow">Our story</p><h1>French tradition, California freshness.</h1></div></section>
<div class="container section about">
<!-- PLACEHOLDER: story copy; swap the logo for a real kitchen photo (WebP, width/height, lazy) -->
<img src="/img/logo-full-563.webp" width="563" height="698" alt="Artisan Crepes logo" loading="lazy" decoding="async">
<div class="stack">
<p class="lead">Artisan Crepes started with a simple idea: the thin, golden crêpes of a Paris street corner belong at Sacramento’s biggest moments.</p>
<p>Today we make them by hand in large batches for weddings, birthdays, showers, office events and community gatherings.</p>
<p>We use California produce whenever we can: Delta strawberries in spring, valley stone fruit in summer and apples in fall, alongside classic French fillings.</p>
<p>You choose the mix of hot, cold and savory crêpes and tell us when you need them. We have everything boxed, labeled and ready for pickup.</p>
<a class="btn btn--lg" href="/order.html">{CTA}</a></div></div>
'''+FOOT

def chips(k): return "".join(f'<label class="chip-opt"><input type="checkbox" name="{k}[]" value="{n}"><span>{n}</span></label>' for n,_,_ in MENU[k][2])
order=head("Request a Catering Order | Crepes Sacramento | Artisan Crepes","Request crêpe catering for your Sacramento wedding, party or event. Choose hot, cold and savory crêpes, batch size and pickup time. Nothing charged online.","order.html","/order.html")
order+=f'''<section class="page-hero"><div class="container"><p class="eyebrow">Catering order</p><h1>{CTA}</h1>
<p class="lead">Tell us about your event. We reply with a quote and the pickup address.</p></div></section>
<div class="container section order-wrap">
<!-- PLACEHOLDER: lead times -->
<p class="notice">Pickup only in Sacramento, CA. Please order at least 72 hours ahead (two weeks for weddings). We send the pickup address with your confirmation.</p>
<form class="form order-form" name="catering-order" method="POST" action="/thank-you.html" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="catering-order"><p class="hidden"><label>Leave blank <input type="text" name="bot-field"></label></p>
<fieldset class="fieldset"><legend>Your event</legend>
<div class="row-3"><div class="field"><label for="et">Event type <span class="req">*</span></label><select class="select" id="et" name="event-type" required><option value="">Choose…</option><option>Wedding</option><option>Birthday / party</option><option>Corporate / office</option><option>Shower / brunch</option><option>Holiday party</option><option>Other</option></select></div>
<div class="field"><label for="pd">Pickup date <span class="req">*</span></label><input class="input" id="pd" name="pickup-date" type="date" required></div>
<div class="field"><label for="pt">Pickup time <span class="req">*</span></label><select class="select" id="pt" name="pickup-time" required><option value="">Choose…</option><option>9:00 AM</option><option>11:00 AM</option><option>1:00 PM</option><option>3:00 PM</option><option>5:00 PM</option></select></div></div>
<div class="row"><div class="field"><label for="bs">Batch size <span class="req">*</span></label><select class="select" id="bs" name="batch-size" required><option value="">Choose…</option><option>2 dozen (24) · ~12–20 guests</option><option>4 dozen (48) · ~25–40 guests</option><option>6 dozen (72) · ~40–60 guests</option><option>10 dozen (120) · ~60–100 guests</option><option>15+ dozen · 100+ guests (custom quote)</option></select></div>
<div class="field"><label for="gc">Guest count</label><input class="input" id="gc" name="guest-count" type="number" min="10" step="1" inputmode="numeric" placeholder="e.g. 80"><span class="hint">Plan on about 1.5 crêpes per guest.</span></div></div></fieldset>
<fieldset class="fieldset"><legend>Crêpe picks <span class="muted" style="font:400 var(--fs-sm) var(--font-body)">(choose any)</span></legend>
<fieldset class="picks picks--hot"><legend>Hot</legend><div class="chips">{chips("hot")}</div></fieldset>
<fieldset class="picks picks--cold"><legend>Cold</legend><div class="chips">{chips("cold")}</div></fieldset>
<fieldset class="picks picks--savory"><legend>Savory</legend><div class="chips">{chips("savory")}</div></fieldset>
<div class="field"><label for="od">Order details</label><textarea class="textarea" id="od" name="order-details" placeholder="Quantities per crêpe, mix of hot/cold/savory, packaging…"></textarea></div></fieldset>
<fieldset class="fieldset"><legend>Contact</legend>
<div class="field"><label for="n">Name <span class="req">*</span></label><input class="input" id="n" name="name" type="text" autocomplete="name" required></div>
<div class="row"><div class="field"><label for="e">Email <span class="req">*</span></label><input class="input" id="e" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="p">Phone <span class="req">*</span></label><input class="input" id="p" name="phone" type="tel" autocomplete="tel" required></div></div>
<div class="field"><label for="m">Notes</label><textarea class="textarea" id="m" name="notes" placeholder="Allergies, dietary needs, labels, theme colors…"></textarea></div></fieldset>
<div class="form-foot"><button class="btn btn--lg" type="submit">{CTA}</button><span class="hint muted" style="font-size:var(--fs-xs)">We reply within one business day with a quote and the pickup details. Nothing is charged until you confirm.</span></div>
</form></div>
'''+FOOT
ty=head("Thank You | Artisan Crepes","Thanks for your catering order request.","thank-you.html","",'<meta name="robots" content="noindex">\n')
ty+='<section class="section"><div class="container center"><p class="eyebrow">Merci!</p><h1>Your request is in.</h1><p class="lead" style="margin-top:var(--sp-4)">We reply within one business day with a quote and the pickup address. Nothing is charged until you confirm.</p><p style="margin-top:var(--sp-5)"><a class="btn btn--outline" href="/">Back to home</a></p></div></section>\n'+FOOT
nf=head("Page Not Found | Artisan Crepes","Page not found.","404.html","",'<meta name="robots" content="noindex">\n')+'<section class="section"><div class="container center"><h1>This page flipped away.</h1><p style="margin-top:var(--sp-5)"><a class="btn btn--outline" href="/">Back to home</a></p></div></section>\n'+FOOT
for n,c in [("index.html",idx),("menu.html",menu),("about.html",about),("order.html",order),("thank-you.html",ty),("404.html",nf)]:
    open(n,"w").write(c)
print("built")
