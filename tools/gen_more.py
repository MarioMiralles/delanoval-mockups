# Contact, FAQs, Blog index and a sample blog article. Exec'd by gen_site.py (shares its globals).

CARDS_CSS = '''
  .cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:72px clamp(24px,3vw,48px)}
  .guide{display:flex;flex-direction:column;text-decoration:none}
  .guide .ph{overflow:hidden;background:#c9ced6;margin-bottom:28px}
  .guide .ph img{width:100%;aspect-ratio:3/2;object-fit:cover;transition:transform 1.6s var(--ease-out)}
  .guide:hover .ph img{transform:scale(1.05)}
  .guide .meta{display:flex;justify-content:space-between;gap:12px;padding-top:18px;border-top:1px solid var(--line);margin-bottom:16px;font:400 12px/1.4 var(--sans);letter-spacing:.28em;text-transform:uppercase;color:var(--royal)}
  .guide .meta span:last-child{color:var(--muted);letter-spacing:.16em}
  .guide h3{font-size:clamp(26px,2.2vw,34px);line-height:1.12;margin-bottom:22px}
  .guide .more{margin-top:auto;color:var(--navy)}
  .guide.soon .more{color:var(--muted)}
  .guide.soon:hover .ph img{transform:none}
  @media (max-width:900px){.cards{grid-template-columns:1fr 1fr}}
  @media (max-width:640px){.cards{grid-template-columns:1fr;row-gap:64px}.guide .ph img{aspect-ratio:16/9}}
'''

GUIDES = [
    ('after-the-storm', 'property', 'Property claims', '5 min read', 'everglades-storm.webp', 1920, 1316, 'After the storm: what to document before you call your insurer', None),
    ('#', 'injury', 'Personal injury', '4 min read', 'brickell-night.webp', 1024, 768, 'Hurt in a crash? Five things to do in the first week', None),
    ('#', 'es', 'En español', '5 min', 'pen.webp', 1024, 769, '¿Le negaron su reclamo de seguro? Sus próximos pasos', 'es'),
    ('#', 'property', 'Property claims', '6 min read', 'skyline-storm.webp', 1024, 511, 'Underpaid roof claim? How to read your insurer\'s estimate', None),
    ('#', 'injury', 'Personal injury', '3 min read', 'brickell-river.webp', 1024, 683, 'Florida\'s two-year deadline for injury claims, explained', None),
    ('#', 'family', 'Family law', '5 min read', 'glass-tower.webp', 960, 720, 'Time-sharing in Florida: what parents should know', None),
    ('#', 'property', 'Property claims', '4 min read', 'library.webp', 1024, 683, 'What a "reservation of rights" letter from your insurer means', None),
]


def guide_card(root, g, extra=''):
    slug, cat, catname, mins, photo, w, h, title, lang = g
    href = root + 'blog/%s/' % slug if slug != '#' else '#'
    la = ' lang="es"' if lang else ''
    read = 'Leer el artículo' if lang else 'Read the article'
    inner = (f'<div class="ph"><img src="{root}assets/img/stock/{photo}" alt="" width="{w}" height="{h}" loading="lazy"></div>'
             f'<div class="meta"><span>{catname}</span><span>{mins}</span></div><h3>{title}</h3>')
    if slug == '#':
        soon = 'Próximamente' if lang else 'Coming soon'
        return f'<div class="guide soon" data-cat="{cat}" data-reveal{la}{extra}>{inner}<span class="more">{soon}</span></div>'
    return f'<a class="guide" href="{href}" data-cat="{cat}" data-reveal{la}{extra}>{inner}<span class="more nudge">{read} {ARROW16}</span></a>'


# ---------------- Contact ----------------
CONTACT_CSS = '''
  .ways .wrap{padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
  .wgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:48px clamp(20px,2.6vw,44px)}
  .way{display:flex;flex-direction:column;padding-top:28px;border-top:1px solid var(--line);position:relative}
  .way::before{content:"";position:absolute;left:0;top:-1px;width:48px;height:2px;background:var(--royal)}
  .way .label{color:var(--royal);margin-bottom:24px}
  .way h3{font-size:clamp(22px,1.75vw,28px);line-height:1.25;margin-bottom:14px;font-variant-numeric:lining-nums}
  .way h3.nowrap{white-space:nowrap}
  .way h3 a{text-decoration:none}
  .way p{margin:0 0 24px;font-size:16px;color:var(--slate)}
  .way .more{margin-top:auto;color:var(--navy);align-self:flex-start;background-color:transparent;border:0;padding:0;cursor:pointer}
  @media (max-width:1000px){.wgrid{grid-template-columns:1fr 1fr}}
  @media (max-width:600px){.wgrid{grid-template-columns:1fr}}
  .mapband{position:relative;background:var(--ice)}
  .mapband iframe{display:block;width:100%;height:clamp(380px,42vw,540px);border:0;filter:grayscale(.35) contrast(1.05)}
  .mapcard{position:absolute;left:max(var(--gut),calc((100% - var(--wrap)) / 2 + var(--gut)));bottom:48px;width:min(400px,calc(100% - 2 * var(--gut)));padding:36px;background:#fff;box-shadow:0 24px 48px rgba(3,16,31,.18)}
  .mapcard .label{color:var(--royal);margin-bottom:14px}
  .mapcard p{margin:0 0 6px;font:500 24px/1.3 var(--serif)}
  .mapcard small{display:block;margin-bottom:22px;font-size:15px;color:var(--slate)}
  .mapcard .more{color:var(--navy)}
  @media (max-width:700px){.mapcard{position:static;width:auto;box-shadow:none;border-top:1px solid var(--line)}}
'''


def build_contact():
    root = '../'
    m = hero(root, [(root + 'homepage/', 'Home'), 'Contact'], 'Talk to an', '<em>attorney.</em>',
             'Call, email, chat or visit. However you reach us, an attorney will review your situation and explain your options in English or Spanish.',
             'brickell-golden.webp', 1920, 1280)
    m += f'''  <section class="ways" aria-labelledby="ways-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="label" data-reveal>Ways to reach us</div>
        <h2 id="ways-title" data-reveal style="--d:100ms">However is easiest for you</h2>
      </div>
      <div class="wgrid" data-stagger="100">
        <div class="way" data-reveal><span class="label">Call</span><h3><a class="sweep" href="tel:+17862578847">(786) 257-8847</a></h3><p>Monday to Friday, 8:30 AM to 5:00 PM. Closed weekends.</p><a class="more sweep nudge" href="tel:+17862578847">Call the firm {ARROW16}</a></div>
        <div class="way" data-reveal><span class="label">Email</span><h3 class="nowrap"><a class="sweep" href="mailto:LD@delanovalpa.com">LD@delanovalpa.com</a></h3><p>Send questions or documents at any time, and we will follow up during office hours.</p><a class="more sweep nudge" href="mailto:LD@delanovalpa.com">Send an email {ARROW16}</a></div>
        <div class="way" data-reveal><span class="label">Visit</span><h3>8780 NW 18th Terrace, Doral, Florida 33172</h3><p>Please call ahead to schedule a meeting at the office.</p><a class="more sweep nudge" href="https://www.google.com/maps/dir/?api=1&amp;destination=8780+NW+18th+Terrace,+Doral,+FL+33172" target="_blank" rel="noopener">Get directions {ARROW16}</a></div>
        <div class="way" data-reveal><span class="label">Chat</span><h3>Day or night</h3><p>Our AI assistant answers common questions and takes your details for an attorney, in English or Spanish.</p><button class="more sweep nudge" type="button" data-open-chat>Start a chat {ARROW16}</button></div>
      </div>
    </div>
  </section>

'''
    m += REVIEW
    m += '''  <section class="mapband" aria-label="Office location">
    <iframe title="Map of De La Noval, P.A. at 8780 NW 18th Terrace, Doral" src="https://www.google.com/maps?q=8780+NW+18th+Terrace,+Doral,+FL+33172&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    <div class="mapcard">
      <div class="label">Our office</div>
      <p>De La Noval, P.A.</p>
      <small>8780 NW 18th Terrace, Doral, Florida 33172<br>Monday to Friday, 8:30 AM to 5:00 PM</small>
      <a class="more sweep nudge" href="https://www.google.com/maps/dir/?api=1&amp;destination=8780+NW+18th+Terrace,+Doral,+FL+33172" target="_blank" rel="noopener">Get directions ''' + ARROW16 + '''</a>
    </div>
  </section>
'''
    js = '''    // "Start a chat" opens the chat mockup
    document.querySelectorAll('[data-open-chat]').forEach(function (b) {
      b.addEventListener('click', function () { var l = document.querySelector('.ssw-launch'); if (l) l.click(); });
    });

'''
    out = page(root, 'Contact', 'Contact De La Noval, P.A. in Doral, Florida: call (786) 257-8847, email, chat or visit 8780 NW 18th Terrace. Se habla español.',
               'brickell-golden.webp', m, 'contact', root + 'contact/', extra_css=CONTACT_CSS, extra_js=js, review=False)
    os.makedirs('contact', exist_ok=True)
    open('contact/index.html', 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote contact')


# ---------------- FAQs ----------------
FAQ_CSS = '''
  .faqall .wrap{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,8fr);gap:clamp(40px,6vw,112px);padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
  .faqall aside{align-self:start;position:sticky;top:120px}
  .faqall aside .label{color:var(--royal);margin-bottom:20px}
  .faqall aside ul{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
  .faqall aside a{display:block;padding:14px 0;border-bottom:1px solid var(--line);font-size:16px;text-decoration:none;transition:color .3s,padding .4s var(--ease-out)}
  .faqall aside a:hover{color:var(--royal);padding-left:8px}
  .fgroup{scroll-margin-top:110px}
  .fgroup+.fgroup{margin-top:clamp(72px,8vw,112px)}
  .fgroup .head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:12px 24px;margin-bottom:28px}
  .fgroup h2{font-size:clamp(36px,3.6vw,54px)}
  .fgroup .more{color:var(--navy);white-space:nowrap}
  .fgroup details{border-bottom:1px solid var(--line)}
  .fgroup details:first-of-type{border-top:1px solid var(--line)}
  .fgroup summary{display:flex;justify-content:space-between;align-items:center;gap:24px;padding:26px 0;cursor:pointer;list-style:none;font:500 clamp(22px,1.9vw,28px)/1.25 var(--serif)}
  .fgroup summary::-webkit-details-marker{display:none}
  .fgroup summary::after{content:"";flex:none;width:14px;height:14px;background:linear-gradient(var(--royal),var(--royal)) center/14px 1.5px no-repeat,linear-gradient(var(--royal),var(--royal)) center/1.5px 14px no-repeat;transition:transform .4s var(--ease-out)}
  .fgroup details[open] summary::after{transform:rotate(45deg)}
  .fgroup details p{margin:0;padding:0 48px 28px 0;color:var(--slate)}
  .faqall .fine{margin-top:56px;font-size:14px;color:var(--muted)}
  @media (max-width:900px){.faqall .wrap{grid-template-columns:1fr}.faqall aside{position:static}.faqall aside ul{display:flex;flex-wrap:wrap;gap:10px;border:0}.faqall aside a{padding:10px 16px;border:1px solid var(--line)}.faqall aside a:hover{padding-left:16px}}
'''

GENERAL_FAQ = [
    ('How much does a consultation cost?', '[Fee policy to confirm with the firm.] Call us or request a case review, and we will explain how fees work for your type of case before you decide anything.'),
    ('Do you speak Spanish?', 'Sí. Every consultation is available in English or Spanish, and we can work with you in either language for the life of your case.'),
    ('Do you only handle cases in Miami-Dade?', 'No. Our office is in Doral, and we represent clients throughout Florida in state court and federal court.'),
    ('What should I bring to my first consultation?', 'Anything related to your case: insurance policies and letters, photos, medical records, police reports, court papers and a list of your questions. If you do not have everything, call anyway.'),
    ('How will I know what is happening with my case?', 'You will speak with the attorney handling your case, and we keep you updated at every step, so you always know where things stand and what happens next.'),
    ('Does contacting the firm make me a client?', 'No. Calling, emailing or sending a form does not create an attorney-client relationship. Representation begins only once we agree to it in writing.'),
]


def build_faqs():
    root = '../'
    groups = [('general', 'Working with us', GENERAL_FAQ, None)] + [
        (s, dict(AREAS)[s], SUBS[s]['faq'], root + 'practice-areas/%s/' % s) for s in ORDER]
    m = hero(root, [(root + 'homepage/', 'Home'), 'FAQs'], 'Frequently asked', '<em>questions.</em>',
             'Straight answers to the questions clients ask us most. For advice about your own situation, request a case review.',
             'library.webp', 1024, 683)
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (k, n) for k, n, _, _ in groups)
    body = ''
    for k, n, qs, link in groups:
        more = '<a class="more sweep nudge" href="%s" aria-label="Learn more about %s">Learn more %s</a>' % (link, n.lower(), ARROW16) if link else ''
        qa = ''.join('<details><summary>%s</summary><p>%s</p></details>' % q for q in qs)
        body += f'<div class="fgroup" id="{k}" data-reveal><div class="head"><h2>{n}</h2>{more}</div>{qa}</div>'
    m += f'''  <section class="faqall" aria-label="Frequently asked questions">
    <div class="wrap">
      <aside data-reveal>
        <div class="label">Topics</div>
        <ul>{toc}</ul>
      </aside>
      <div>{body}
        <p class="fine">General information only, not legal advice. Every case is different, and laws change. Contacting the firm does not create an attorney-client relationship.</p>
      </div>
    </div>
  </section>

'''
    out = page(root, 'FAQs', 'Answers to common questions about property insurance claims, personal injury, family law and working with De La Noval, P.A. Se habla español.',
               'library.webp', m, None, root + 'faqs/', extra_css=FAQ_CSS)
    os.makedirs('faqs', exist_ok=True)
    open('faqs/index.html', 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote faqs')


# ---------------- Guides index ----------------
GUIDES_CSS = CARDS_CSS + '''
  .glist .wrap{padding-top:clamp(72px,8vw,112px);padding-bottom:clamp(96px,11vw,152px)}
  .chips{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:clamp(48px,6vw,72px)}
  .chips button{min-height:44px;padding:0 20px;border:1px solid var(--line);background:#fff;color:var(--navy);font:400 12px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;cursor:pointer;transition:background .3s,color .3s,border-color .3s}
  .chips button:hover{border-color:var(--navy)}
  .chips button[aria-pressed="true"]{background:var(--navy);border-color:var(--navy);color:#fff}
  .feat{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(32px,5vw,80px);align-items:center;margin-bottom:clamp(72px,8vw,112px);text-decoration:none}
  .feat .ph{overflow:hidden;background:#c9ced6}
  .feat .ph img{width:100%;aspect-ratio:3/2;object-fit:cover;transition:transform 1.6s var(--ease-out)}
  .feat:hover .ph img{transform:scale(1.04)}
  .feat .label{color:var(--royal);margin-bottom:20px}
  .feat h2{font-size:clamp(36px,3.8vw,58px);line-height:1.08;margin-bottom:22px}
  .feat p{margin:0 0 28px;color:var(--slate)}
  .feat .more{color:var(--navy)}
  .guide[hidden],.feat[hidden]{display:none}
  .gempty{display:none;color:var(--slate)}
  @media (max-width:900px){.feat{grid-template-columns:1fr}}
'''


def build_blog():
    root = '../'
    m = hero(root, [(root + 'homepage/', 'Home'), 'Blog'], 'Know your', '<em>rights.</em>',
             'Plain-language articles from our attorneys on insurance claims, injuries and family matters, in English and Spanish.',
             'pen.webp', 1024, 769)
    f = GUIDES[0]
    chips = ''.join('<button type="button" data-filter="%s" aria-pressed="%s">%s</button>' % (k, 'true' if k == 'all' else 'false', n)
                    for k, n in (('all', 'All articles'), ('property', 'Property claims'), ('injury', 'Personal injury'), ('family', 'Family law'), ('es', 'En español')))
    cards = ''.join(guide_card(root, g) for g in GUIDES[1:])
    m += f'''  <section class="glist" aria-label="Blog articles">
    <div class="wrap">
      <div class="chips" role="group" aria-label="Filter articles">{chips}</div>
      <a class="feat" href="{root}blog/{f[0]}/" data-cat="{f[1]}" data-reveal>
        <div class="ph"><img src="{root}assets/img/stock/{f[4]}" alt="" width="{f[5]}" height="{f[6]}" loading="lazy"></div>
        <div>
          <div class="label">Featured · {f[2]} · {f[3]}</div>
          <h2>{f[7]}</h2>
          <p>The steps you take in the first days after a storm can shape how your claim is handled. Here is what to photograph, save and write down.</p>
          <span class="more sweep nudge">Read the article {ARROW16}</span>
        </div>
      </a>
      <div class="cards" data-stagger="100">{cards}</div>
    </div>
  </section>

'''
    js = '''    // Blog filters
    var chips = document.querySelectorAll('[data-filter]'), items = document.querySelectorAll('.glist [data-cat]');
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        var f = c.getAttribute('data-filter');
        chips.forEach(function (o) { o.setAttribute('aria-pressed', String(o === c)); });
        items.forEach(function (it) { it.hidden = f !== 'all' && it.getAttribute('data-cat') !== f; });
      });
    });

'''
    out = page(root, 'Blog', 'Plain-language legal articles from De La Noval, P.A. on Florida property insurance claims, personal injury and family law, in English and Spanish.',
               'pen.webp', m, 'blog', root + 'blog/', extra_css=GUIDES_CSS, extra_js=js)
    os.makedirs('blog', exist_ok=True)
    open('blog/index.html', 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote blog')


# ---------------- Sample article ----------------
ARTICLE_CSS = CARDS_CSS + '''
  .ahero{position:relative;background:var(--deep);color:#fff;overflow:hidden}
  .ahero .bg{position:absolute;inset:0;opacity:.35}
  .ahero .bg img{width:100%;height:100%;object-fit:cover}
  .ahero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(3,16,31,.96) 0%,rgba(3,16,31,.85) 55%,rgba(5,27,52,.55) 100%)}
  .ahero .wrap{position:relative;z-index:1;padding-top:168px;padding-bottom:clamp(56px,6vw,88px)}
  .ahero .cat{color:var(--royal-tint);margin-bottom:22px}
  .ahero h1{font-size:clamp(42px,5vw,78px);line-height:1.04;max-width:18ch;margin-bottom:34px}
  .byline{display:flex;flex-wrap:wrap;align-items:center;gap:14px 28px;font-size:15px;color:#c9d2e6}
  .byline .who{display:flex;align-items:center;gap:14px;color:#fff;text-decoration:none}
  .byline img{width:48px;height:48px;border-radius:50%;object-fit:cover;object-position:50% 0;background:#c9ced6}
  .byline .sep{width:1px;height:20px;background:var(--line-dark)}
  @media (max-width:760px){.ahero .wrap{padding-top:172px}.ahero h1{font-size:38px}.byline .sep{display:none}}

  .article .wrap{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,4fr);gap:clamp(40px,7vw,128px);padding-top:clamp(72px,8vw,112px);padding-bottom:clamp(96px,11vw,152px)}
  .prose{max-width:720px}
  .prose>p:first-child{font-size:clamp(20px,1.6vw,23px);line-height:1.6;color:var(--navy)}
  .prose p,.prose li{color:var(--slate)}
  .prose p{margin:0 0 24px}
  .prose h2{font-size:clamp(32px,3vw,44px);line-height:1.1;margin:56px 0 18px;scroll-margin-top:110px}
  .prose h2 span{display:block;margin-bottom:10px;font:400 12px/1 var(--sans);letter-spacing:.32em;text-transform:uppercase;color:var(--royal)}
  .prose ul{margin:0 0 24px;padding:0;list-style:none}
  .prose ul li{position:relative;padding:0 0 12px 28px}
  .prose ul li::before{content:"";position:absolute;left:0;top:.8em;width:14px;height:1px;background:var(--royal)}
  .callout{margin:40px 0;padding:28px 32px;background:var(--ice);border-left:2px solid var(--royal)}
  .callout .label{color:var(--royal);margin-bottom:10px}
  .callout p{margin:0!important;color:var(--navy)!important;font:500 22px/1.4 var(--serif)}
  .author{display:grid;grid-template-columns:96px 1fr;gap:24px;align-items:center;margin-top:64px;padding-top:36px;border-top:1px solid var(--line)}
  .author img{width:96px;height:96px;border-radius:50%;object-fit:cover;object-position:50% 0;background:#c9ced6}
  .author .label{color:var(--royal);margin-bottom:6px}
  .author h3{font-size:30px;margin-bottom:6px}
  .author h3 a{text-decoration:none}
  .author p{margin:0;font-size:15px;color:var(--slate)}
  .prose .disclaimer{margin:36px 0 0;font-size:14px;color:var(--muted)}
  .side{align-self:start;position:sticky;top:120px;display:grid;gap:40px}
  .toc .label{color:var(--royal);margin-bottom:16px}
  .toc ol{list-style:none;margin:0;padding:0;border-top:1px solid var(--line);counter-reset:t}
  .toc li{counter-increment:t}
  .toc a{display:flex;gap:14px;padding:12px 0;border-bottom:1px solid var(--line);font-size:15px;text-decoration:none;transition:color .3s}
  .toc a::before{content:counter(t,decimal-leading-zero);font-size:12px;letter-spacing:.2em;color:var(--royal);padding-top:3px}
  .toc a:hover{color:var(--royal)}
  .sidecta{padding:36px;background:var(--deep);color:#fff}
  .sidecta .label{color:var(--royal-tint);margin-bottom:16px}
  .sidecta h3{font-size:32px;line-height:1.12;margin-bottom:14px}
  .sidecta p{margin:0 0 26px;font-size:15px;color:#c9d2e6}
  .sidecta .btn{width:100%;min-height:52px;padding:0 20px;font-size:12px}
  @media (max-width:1000px){.article .wrap{grid-template-columns:1fr}.side{position:static}.toc{display:none}}

  .related{background:var(--ice)}
  .related .wrap{padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
'''

ARTICLE = [
    ('safe', 'Make sure everyone is safe first', ['No photo is worth an injury. Stay clear of downed power lines, standing water and damaged structures, and wait until local authorities say it is safe to return.']),
    ('photos', 'Photograph and film everything before cleanup', ['Before you move, repair or throw anything away, capture the damage in detail:',
        ['Wide shots of every side of the home, then close-ups of each damaged area.',
         'The roof, gutters, windows and fences, photographed from the ground. Do not climb onto a damaged roof.',
         'Inside: ceilings, walls and floors, and anything stained, warped or wet.',
         'Damaged belongings, before you move them.',
         'A slow video walk-through of the property, narrating what you see.'],
        'Your phone records the date and time of each photo automatically. Keep the original files and back them up.']),
    ('mitigate', 'Prevent further damage, and keep every receipt', ['Most policies expect you to take reasonable steps to protect the property from further damage, such as covering a damaged roof with a tarp or removing standing water. Photograph the damage first, then make temporary repairs and keep receipts for every material and service.',
        'Hold off on permanent repairs until the damage has been documented and inspected.']),
    ('list', 'List what was damaged', ['Write down each damaged item, roughly when you bought it and what it cost. Receipts, bank statements and old photos all help. If something must be thrown away for health reasons, photograph it first and note it on your list.']),
    ('policy', 'Find your policy and declarations page', ['Your full policy and declarations page show what is covered, your deductibles (including any separate hurricane deductible) and the conditions you must follow after a loss. If you cannot find them, ask your insurer or agent for a certified copy.',
        ('callout', 'Florida deadline', 'For most property claims, Florida law now requires notice to your insurer within one year of the date of loss. Do not wait to report.')]),
    ('log', 'Report the claim and keep a claim log', ['Report the claim promptly and write down your claim number. From then on, keep a simple log of every call, email and inspection: the date, the person you spoke with and what was said. Save every letter and email from the insurer.']),
    ('sign', 'Be careful before you sign or accept', ['An adjuster may ask for a recorded statement or offer a quick payment. Before you agree to anything, make sure you understand what you are signing and what you may be giving up.',
        'If your claim is denied or delayed, or the offer seems low, an attorney can review your policy and the insurer\'s decision with you.']),
]


def build_article():
    root = '../../'
    g = GUIDES[0]
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (k, t) for k, t, _ in ARTICLE)
    body = '<p>The hours and days after a storm are stressful, and the steps you take before you call your insurance company can shape how your claim is handled. Here is what to document, and why it matters.</p>'
    for i, (k, t, parts) in enumerate(ARTICLE):
        body += '<h2 id="%s"><span>Step %02d</span>%s</h2>' % (k, i + 1, t)
        for p in parts:
            if isinstance(p, list):
                body += '<ul>%s</ul>' % ''.join('<li>%s</li>' % x for x in p)
            elif isinstance(p, tuple):
                body += '<div class="callout"><div class="label">%s</div><p>%s</p></div>' % (p[1], p[2])
            else:
                body += '<p>%s</p>' % p
    body += '<p>If you have questions about your claim, we are here to help, in English or Spanish.</p>'
    related = ''.join(guide_card(root, x) for x in (GUIDES[3], GUIDES[2], GUIDES[1]))
    m = f'''  <section class="ahero" aria-labelledby="page-title">
    <div class="bg"><img src="{root}assets/img/stock/{g[4]}" alt="" width="{g[5]}" height="{g[6]}" fetchpriority="high"></div>
    <div class="wrap">
      <nav class="crumbs label" aria-label="Breadcrumb" data-load style="--d:200ms"><a class="sweep" href="{root}homepage/">Home</a><i aria-hidden="true"></i><a class="sweep" href="{root}blog/">Blog</a><i aria-hidden="true"></i><span aria-current="page">{g[2]}</span></nav>
      <div class="cat label" data-load style="--d:300ms">{g[2]} · Article</div>
      <h1 id="page-title" data-load style="--d:400ms">{g[7]}</h1>
      <div class="byline" data-load style="--d:600ms">
        <a class="who" href="{root}about/lazaro-de-la-noval/"><img src="{root}assets/img/lazaro-cutout.webp" alt="" width="1000" height="936">By Lazaro De La Noval</a>
        <span class="sep" aria-hidden="true"></span><span>{g[3]}</span>
        <span class="sep" aria-hidden="true"></span><span>Updated October 2026</span>
      </div>
    </div>
  </section>

  <section class="article" aria-label="Article">
    <div class="wrap">
      <article class="prose">{body}
        <div class="author">
          <img src="{root}assets/img/lazaro-cutout.webp" alt="" width="1000" height="936" loading="lazy">
          <div>
            <div class="label">Written by</div>
            <h3><a href="{root}about/lazaro-de-la-noval/">Lazaro De La Noval</a></h3>
            <p>Founder and managing partner. A former insurance defense attorney who now represents homeowners and businesses in insurance disputes.</p>
          </div>
        </div>
        <p class="disclaimer">This article is general information, not legal advice, and reading it does not create an attorney-client relationship. Every claim is different and laws change; speak with an attorney about your situation.</p>
      </article>
      <aside class="side">
        <nav class="toc" aria-label="On this page"><div class="label">On this page</div><ol>{toc}</ol></nav>
        <div class="sidecta">
          <div class="label">Claim denied or underpaid?</div>
          <h3>Have an attorney look at it.</h3>
          <p>Tell us what happened. We will review your policy and call to explain your options.</p>
          <a class="btn btn-royal nudge" href="#review">Request a case review {ARROW16}</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="related" aria-labelledby="related-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="label" data-reveal>Keep reading</div>
        <h2 id="related-title" data-reveal style="--d:100ms">Related articles</h2>
      </div>
      <div class="cards" data-stagger="100">{related}</div>
    </div>
  </section>

'''
    out = page(root, 'After the Storm: What to Document Before You Call Your Insurer',
               'A Florida property insurance attorney explains what to photograph, save and write down after storm damage, before you call your insurance company.',
               g[4], m, 'blog', root + 'blog/', extra_css=ARTICLE_CSS)
    out = out.replace('<option>Property damage or insurance claim</option>', '<option selected>Property damage or insurance claim</option>', 1)
    os.makedirs('blog/after-the-storm', exist_ok=True)
    open('blog/after-the-storm/index.html', 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote article')
