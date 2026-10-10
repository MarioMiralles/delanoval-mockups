# Regenerates the shared menu + footer on every built page, and rebuilds the practice-area,
# Contact, FAQs and Guides pages (content lives in SUBS here and in gen_more.py).
# Run from the repo root:  python tools/gen_site.py
# Homepage, About and the two attorney profiles are hand-edited: this script only rewrites
# their <nav class="main"> block and footer columns.
import re, os

ABOUT = open('about/index.html', encoding='utf-8').read()
HOME = open('homepage/index.html', encoding='utf-8').read()

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'
ARROW16 = ARROW.replace('width="18" height="18"', 'width="16" height="16"')
CARET = '<svg class="caret" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'

AREAS = [('property-damage', 'Property &amp; insurance'), ('personal-injury', 'Personal injury'), ('family-law', 'Family law')]
PEOPLE = [('lazaro-de-la-noval', 'Lazaro De La Noval'), ('elizabeth-diaz-fernandez', 'Elizabeth Diaz Fernandez')]


def rep(s, a, b, count=1):
    assert a in s, a[:80]
    return s.replace(a, b, count)


# ---------- shared menu and footer ----------
def nav(root, section=None, current=None, home=False):
    """root: path from this page to the repo root. section: 'about' | 'practice'. current: exact href of this page."""
    def link(href, text):
        cur = ' aria-current="page"' if href == current else ''
        return '<a href="%s"%s>%s</a>' % (href, cur, text)
    about = root + 'about/'
    prac = root + 'practice-areas/'
    about_sub = link(about, 'Our firm') + ''.join(link(about + s + '/', n) for s, n in PEOPLE)
    prac_sub = link(prac, 'All practice areas') + ''.join(link(prac + s + '/', n) for s, n in AREAS)
    a_cur = ' aria-current="page"' if section == 'about' else ''
    p_cur = ' aria-current="page"' if section == 'practice' else ''
    g_cur = ' aria-current="page"' if section == 'guides' else ''
    c_cur = ' aria-current="page"' if section == 'contact' else ''
    return f'''    <nav class="main" id="nav" aria-label="Main">
      <div class="has-sub"><a class="sweep" href="{about}"{a_cur}>About{CARET}</a>
        <div class="sub-menu">{about_sub}</div></div>
      <div class="has-sub"><a class="sweep" href="{prac}"{p_cur}>Practice areas{CARET}</a>
        <div class="sub-menu">{prac_sub}</div></div>
      <a class="sweep" href="{root}guides/"{g_cur}>Guides</a>
      <a class="sweep" href="{root}contact/"{c_cur}>Contact</a>
      <a class="btn btn-ghost" href="#review">Request a case review</a>
    </nav>'''


def footer_cols(root, home=False):
    prac = ''.join('<li><a class="sweep" href="%spractice-areas/%s/">%s</a></li>' % (root, s, n) for s, n in AREAS)
    ppl = ''.join('<li><a class="sweep" href="%sabout/%s/">%s</a></li>' % (root, s, n) for s, n in PEOPLE)
    return ('    <div><h3>Practice</h3><ul>%s</ul></div>\n'
            '    <div><h3>Attorneys</h3><ul>%s</ul></div>\n'
            '    <div><h3>Firm</h3><ul><li><a class="sweep" href="%sabout/">About</a></li><li><a class="sweep" href="%sguides/">Guides</a></li><li><a class="sweep" href="%sfaqs/">FAQs</a></li><li><a class="sweep" href="%scontact/">Contact</a></li></ul></div>\n'
            % (prac, ppl, root, root, root, root))


def apply_shared(s, root, section=None, current=None, home=False):
    s, n = re.subn(r'    <nav class="main" id="nav" aria-label="Main">.*?</nav>', lambda m: nav(root, section, current, home), s, count=1, flags=re.S)
    assert n == 1
    s, n = re.subn(r'    <div><h3>Practice</h3>.*?<div><h3>Firm</h3>.*?</div>\n', lambda m: footer_cols(root, home), s, count=1, flags=re.S)
    assert n == 1
    return s


# ---------- update the pages that already exist ----------
def update_existing():
    s = apply_shared(HOME, '../', home=True)
    for slug, _ in AREAS:
        key = {'property-damage': 'property', 'personal-injury': 'injury', 'family-law': 'family'}[slug]
        m = re.search(r'<div class="panel" role="tabpanel" id="panel-%s".*?<div class="panel-card">' % key, s, re.S)
        block = m.group(0)
        s = s.replace(block, block.replace('href="#"', 'href="../practice-areas/%s/"' % slug))
    s = s.replace('<a class="more sweep nudge" href="#" data-reveal style="--d:200ms">All guides', '<a class="more sweep nudge" href="../guides/" data-reveal style="--d:200ms">All guides')
    s = s.replace('<a class="guide" href="#" data-reveal>', '<a class="guide" href="../guides/after-the-storm/" data-reveal>', 1)
    s = s.replace('<a class="guide" href="#" data-reveal', '<a class="guide" href="../guides/" data-reveal')
    open('homepage/index.html', 'w', encoding='utf-8', newline='\n').write(s)

    s = apply_shared(ABOUT, '../', 'about', '../about/')
    open('about/index.html', 'w', encoding='utf-8', newline='\n').write(s)
    for slug, _ in PEOPLE:
        p = 'about/%s/index.html' % slug
        s = apply_shared(open(p, encoding='utf-8').read(), '../../', 'about', '../../about/%s/' % slug)
        open(p, 'w', encoding='utf-8', newline='\n').write(s)


# ---------- page shell built from the About page ----------
STYLE = ABOUT.split('<style>', 1)[1].split('</style>', 1)[0]
REVIEW = re.search(r'  <section class="review".*?</section>\n', ABOUT, re.S).group(0)
FOOT_TAIL = ABOUT.split('</main>', 1)[1]  # footer, mock links, scripts
CHECK_JS = re.search(r'    // Claim checks\n.*?(?=    // Case review form)', HOME, re.S).group(0)

PRACTICE_CSS = '''
  /* Practice pages */
  .intro2 .wrap{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(40px,6vw,112px);padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
  .intro2 .label{color:var(--royal);margin-bottom:28px}
  .intro2 p.big{margin:0;font:500 clamp(34px,3.8vw,58px)/1.16 var(--serif)}
  .intro2 p.big em{color:var(--royal)}
  .intro2 .body{padding-top:clamp(0px,4vw,52px)}
  .intro2 .body p{margin:0 0 24px;color:var(--slate)}
  .intro2 .body p:last-child{margin-bottom:0}
  .intro2 .src{font-size:13px;color:var(--muted)}
  @media (max-width:900px){.intro2 .wrap{grid-template-columns:1fr}}

  .types{background:var(--ice)}
  .types .wrap{padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
  .tgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 clamp(24px,3vw,48px)}
  .tgrid>div{padding:32px 0 40px;border-top:1px solid #c9d2e6}
  .tgrid h3{font-size:clamp(26px,2.2vw,32px);line-height:1.12;margin-bottom:12px}
  .tgrid p{margin:0;font-size:16px;color:var(--slate)}
  @media (max-width:900px){.tgrid{grid-template-columns:1fr 1fr}}
  @media (max-width:600px){.tgrid{grid-template-columns:1fr}}

  .checkband{background:var(--deep);color:#fff}
  .checkband .wrap{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(32px,5vw,88px);align-items:center;padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
  .checkband .label{color:var(--royal-tint);margin-bottom:24px}
  .checkband h2{font-size:clamp(40px,4.4vw,68px);margin-bottom:24px}
  .checkband .copy p{margin:0;color:#c9d2e6;max-width:440px}
  .panel-card{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:560px;padding:clamp(28px,4vw,56px);overflow:hidden;isolation:isolate}
  .panel-card .ph{position:absolute;inset:0;z-index:-2}
  .panel-card .ph img{width:100%;height:100%;object-fit:cover}
  .panel-card::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(3,16,31,.35) 0%,rgba(3,16,31,.78) 45%,rgba(3,16,31,.96) 100%)}
  .panel-card blockquote{margin:0 0 32px;font:500 clamp(30px,3vw,44px)/1.18 var(--serif);max-width:560px}
  .check .head{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:24px}
  .check .head .label{color:#c3cdff;margin:0}
  .check .count{font:400 12px/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:#a9b6cc}
  .progress{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:36px}
  .progress span{height:1px;background:rgba(245,247,255,.28);transform-origin:left center;transition:background .6s var(--ease-out)}
  .progress span.on{background:var(--royal-tint);height:2px;margin-top:-.5px}
  .check .step{transition:opacity .35s var(--ease-out),transform .35s var(--ease-out)}
  .check .step.swap{opacity:0;transform:translate3d(0,10px,0)}
  .check h4{margin:0 0 32px;font:500 clamp(28px,2.7vw,40px)/1.15 var(--serif);max-width:620px}
  .check .choices{display:flex;flex-wrap:wrap;gap:14px}
  .check .choices .btn{min-width:140px}
  .check .result p{margin:-14px 0 30px;color:#dfe5f2;max-width:520px}
  .check .result .actions{display:flex;flex-wrap:wrap;align-items:center;gap:14px 28px}
  .check .restart{background:none;border:0;padding:12px 0;color:#dfe5f2;font:400 12px/1 var(--sans);letter-spacing:.24em;text-transform:uppercase;cursor:pointer}
  .check .note{margin:32px 0 0;padding-top:20px;border-top:1px solid var(--line-dark);font-size:13px;color:#a9b6cc}
  @media (max-width:1000px){.checkband .wrap{grid-template-columns:1fr}.panel-card{min-height:520px}}
  @media (max-width:640px){.panel-card{min-height:0;padding-top:200px}}
  @media (max-width:520px){.check .choices .btn{flex:1;min-width:0}}

  .faq .wrap{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:clamp(40px,6vw,112px);padding-top:clamp(96px,11vw,152px);padding-bottom:clamp(96px,11vw,152px)}
  .faq .sec-head{margin:0}
  .faq .sec-head h2{font-size:clamp(40px,4.4vw,64px)}
  .faq details{border-bottom:1px solid var(--line)}
  .faq details:first-child{border-top:1px solid var(--line)}
  .faq summary{display:flex;justify-content:space-between;align-items:center;gap:24px;padding:26px 0;cursor:pointer;list-style:none;font:500 clamp(22px,1.9vw,28px)/1.25 var(--serif)}
  .faq summary::-webkit-details-marker{display:none}
  .faq summary::after{content:"";flex:none;width:14px;height:14px;background:linear-gradient(var(--royal),var(--royal)) center/14px 1.5px no-repeat,linear-gradient(var(--royal),var(--royal)) center/1.5px 14px no-repeat;transition:transform .4s var(--ease-out)}
  .faq details[open] summary::after{transform:rotate(45deg)}
  .faq details p{margin:0;padding:0 48px 28px 0;color:var(--slate)}
  @media (max-width:900px){.faq .wrap{grid-template-columns:1fr}}

  .others{border-top:1px solid var(--line)}
  .others .wrap{padding-top:clamp(72px,8vw,112px);padding-bottom:clamp(72px,8vw,112px)}
  .others .label{color:var(--royal);margin-bottom:28px}
  .others ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 clamp(24px,3vw,48px)}
  .others a{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:24px 0;border-top:1px solid var(--line);text-decoration:none;font:500 clamp(24px,2.2vw,32px)/1.2 var(--serif);transition:color .4s}
  .others a:hover{color:var(--royal)}
  .others a[aria-current]{color:var(--muted);pointer-events:none}
  .others svg{flex:none;color:var(--royal)}
  @media (max-width:800px){.others ul{grid-template-columns:1fr}}

  .area{display:grid;grid-template-columns:1fr 1fr;align-items:stretch}
  .area .ph{display:block;position:relative;min-height:560px;overflow:hidden;background:var(--deep)}
  .area .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--ease-out)}
  .area .ph:hover img{transform:scale(1.03)}
  .area .copy{padding:clamp(56px,7vw,120px);display:flex;flex-direction:column;justify-content:center}
  .area .no{color:var(--royal);margin-bottom:22px}
  .area h2{font-size:clamp(40px,4.4vw,68px);margin-bottom:22px}
  .area h2 a{text-decoration:none}
  .area p{margin:0 0 32px;color:var(--slate);max-width:480px}
  .area .cases{list-style:none;margin:0 0 36px;padding:0;border-top:1px solid var(--line);max-width:480px}
  .area .cases li{padding:14px 0;border-bottom:1px solid var(--line);font-size:17px}
  .area .more{color:var(--navy)}
  .area.alt{background:var(--ice)}
  .area.alt .ph{order:2}
  @media (max-width:900px){.area{grid-template-columns:1fr}.area .ph{min-height:320px}.area.alt .ph{order:0}.area .copy{padding:72px var(--gut)}}
'''


def page(root, title, desc, preload, main, section, current, check=False, extra_css='', extra_js='', review=True):
    style = STYLE.replace('url("data:', 'url("data:')  # unchanged; kept for clarity
    head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | De La Noval, P.A.</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Rubik:wght@300;400;500&display=swap">
<link rel="preload" as="image" href="{root}assets/img/stock/{preload}">
<link rel="stylesheet" href="{root}assets/motion.css">
<script src="{root}assets/motion.js"></script>
<style>{style}{PRACTICE_CSS}{extra_css}</style>
</head>
<body>

<header class="site" data-header>
  <div class="util">
    <div class="wrap">
      <span class="hide-sm">Se habla español</span>
      <a href="tel:+17862578847">(786) 257-8847</a>
      <span class="lang"><a href="#" aria-current="true">EN</a><a href="#" lang="es">ES</a></span>
    </div>
  </div>
  <div class="wrap bar">
    <a class="logo" href="{root}homepage/" aria-label="De La Noval, P.A. home">
      <img class="dark" src="{root}assets/img/logo-wordmark-white.png" alt="De La Noval, P.A., Attorneys at Law" width="1000" height="171">
      <img class="light" src="{root}assets/img/logo-wordmark-navy.png" alt="" width="1000" height="171">
    </a>
{nav(root, section, current)}
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  </div>
</header>

<main>
'''
    tail = FOOT_TAIL.replace('"../homepage/', '"%shomepage/' % root).replace('"../assets/', '"%sassets/' % root).replace('href="../index.html"', 'href="%sindex.html"' % root)
    tail, n = re.subn(r'    <div><h3>Practice</h3>.*?<div><h3>Firm</h3>.*?</div>\n', lambda m: footer_cols(root), tail, count=1, flags=re.S)
    assert n == 1
    if check:
        tail = rep(tail, '    // Case review form', CHECK_JS + '    // Case review form')
    if extra_js:
        tail = rep(tail, '    // Case review form', extra_js + '    // Case review form')
    review = REVIEW.replace('"../assets/', '"%sassets/' % root) if review is True else (review or '')
    return head + main + review + '</main>\n' + tail


def hero(root, crumbs, h1a, h1b, lede, photo, w, h, pos='60% 50%'):
    crumb = ''.join('<a class="sweep" href="%s">%s</a><i aria-hidden="true"></i>' % c for c in crumbs[:-1]) + '<span aria-current="page">%s</span>' % crumbs[-1]
    return f'''  <section class="phero" aria-labelledby="page-title">
    <div class="bg kenburns"><img src="{root}assets/img/stock/{photo}" alt="" width="{w}" height="{h}" fetchpriority="high" style="object-position:{pos}"></div>
    <div class="wrap">
      <nav class="crumbs label" aria-label="Breadcrumb" data-load style="--d:200ms">{crumb}</nav>
      <h1 id="page-title"><span class="line"><span style="--d:300ms">{h1a}</span></span><span class="line"><span style="--d:450ms">{h1b}</span></span></h1>
      <p class="lede" data-load style="--d:750ms">{lede}</p>
    </div>
  </section>

'''


def steps_section(title, steps, sub):
    items = ''.join('<div class="pr" data-reveal><span class="no label">%02d</span><h3>%s</h3><p>%s</p></div>' % (i + 1, h, t) for i, (h, t) in enumerate(steps))
    return f'''  <section class="principles" aria-labelledby="steps-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="label" data-reveal>What happens next</div>
        <div>
          <h2 id="steps-title" data-reveal style="--d:100ms">{title}</h2>
          <p data-reveal style="--d:200ms">{sub}</p>
        </div>
      </div>
      <div class="grid4" data-stagger="120">{items}</div>
    </div>
  </section>

'''


# ---------- content ----------
SUBS = {
 'property-damage': dict(
    title='Property &amp; Insurance Claims', key='property', case='Property damage or insurance claim',
    desc='Denied, delayed or underpaid property insurance claim in Florida? De La Noval, P.A. represents homeowners and businesses in hurricane, water, roof and fire claims. Se habla español.',
    h1a='Property &amp;', h1b='insurance <em>claims.</em>', photo=('hurricane-palms.webp', 1024, 683),
    lede='When a storm, leak or fire damages your home or business and your insurer denies, delays or underpays the claim, we pursue what your policy promised.',
    big='Your home is likely your most important investment. <em>Your policy should protect it the way it promised.</em>',
    body=['You buy insurance with the reasonable expectation that your insurer will pay a covered claim. Yet every year, residential and commercial claims that should be covered are denied, leaving owners wondering how they will pay for the repairs.',
          'If your insurer is not honoring your policy, or you believe your claim was wrongfully denied, we can help you fight back with a strategy built around your policy and your property.',
          'Our founder began his career defending insurance companies. We know how a claim is reviewed from the inside, and where an insurer\'s position is weakest.'],
    types=[('Hurricane &amp; wind damage', 'Roof, window and structural damage after a named storm or severe wind.'),
           ('Water damage &amp; leaks', 'Burst pipes, plumbing failures, appliance leaks and the damage they leave behind.'),
           ('Roof claims', 'Claims denied as "wear and tear" or underpaid for a partial repair instead of a replacement.'),
           ('Fire &amp; smoke damage', 'Structural, contents and smoke damage, including additional living expenses.'),
           ('Commercial property', 'Claims for business owners, landlords and property managers.'),
           ('Denied, delayed or underpaid', 'Insurers that refuse to pay, stall the claim or offer far less than the repairs cost.')],
    check_title='Is your claim worth a second look?', check_text='Answer three quick questions. Nothing is sent until you request a review.',
    steps=[('Case review', 'We review your policy, the damage and the insurer\'s decision, then explain your options in plain language.'),
           ('Documentation', 'We document the loss with photos, estimates and independent experts where the claim calls for it.'),
           ('Negotiation', 'We present the claim and press the insurer to pay what the policy owes.'),
           ('Litigation', 'If the insurer still will not pay, we are prepared to take the claim to court.')],
    faq=[('My claim was denied. Is it too late to do anything?', 'Not necessarily. A denial is often the start of the conversation, not the end. Florida law sets deadlines for reporting and disputing a claim, so have an attorney review your policy and the denial letter as soon as you can.'),
         ('How long do I have to report property damage in Florida?', 'For most property claims, Florida law now requires notice to your insurer within one year of the date of loss, and supplemental claims within 18 months. Deadlines can depend on the policy and on when the loss happened, so call us if you are unsure.'),
         ('What should I do right after the damage?', 'Photograph everything before cleanup, make temporary repairs to prevent further damage and keep the receipts, and report the claim to your insurer promptly.'),
         ('Should I accept the insurer\'s first offer?', 'Not before you understand it. Underpaid claims are common, and accepting a payment can make it harder to recover the rest. We can compare the offer with your policy and the real cost of repairs.'),
         ('Do you handle commercial claims?', 'Yes. We represent business owners, landlords and property managers as well as homeowners.')],
    feature=dict(photo='lazaro-seated.webp', label='Inside knowledge', h2='Led by a former insurance defense attorney.',
                 p='Lazaro De La Noval began his career defending insurance companies. Since 2016 he has represented hundreds of homeowners and businesses in insurance disputes.',
                 link=('about/lazaro-de-la-noval/', 'Meet Lazaro'))),
 'personal-injury': dict(
    title='Personal Injury', key='injury', case='Car accident',
    desc='Injured in a car accident, slip and fall or other accident in Florida? De La Noval, P.A. pursues fair compensation for injured people. Se habla español.',
    h1a='Personal', h1b='<em>injury.</em>', photo=('brickell-night.webp', 1024, 768),
    lede='Car accidents, slips and falls and other injuries caused by someone else\'s carelessness, pursued for the full compensation the law allows while you focus on recovering.',
    big='An accident can change your year in a moment. <em>We handle the claim so you can focus on getting well.</em>',
    body=['More than 800 crashes happen on Florida roads every day. Medical bills, lost income and calls from insurance adjusters often arrive all at once, while you are still recovering.',
          'Without an attorney, it can be hard to know what your claim is worth. We investigate what happened, document your injuries and losses, and pursue fair compensation from the people and insurers responsible.',
          'Our partners have litigated hundreds of injury cases, and one of them spent her early career as a prosecutor learning how a case is built.'],
    types=[('Car accidents', 'Collisions of every kind, from rear-end crashes to intersection accidents.'),
           ('Truck accidents', 'Crashes involving commercial trucks, delivery vans and fleet vehicles.'),
           ('Rideshare accidents', 'Injuries as a passenger, driver or other motorist in a rideshare crash.'),
           ('Pedestrian &amp; bicycle accidents', 'Injuries to people walking or riding when a driver was not paying attention.'),
           ('Slip and fall', 'Falls caused by wet floors, uneven surfaces or other hazards someone should have fixed.'),
           ('Premises injuries', 'Injuries on someone else\'s property due to unsafe conditions.')],
    check_title='Do you have an injury claim?', check_text='Answer three quick questions. Nothing is sent until you request a review.',
    steps=[('Case review', 'We listen to what happened, review your medical care and explain your options.'),
           ('Investigation', 'We gather police reports, photos, witness statements and medical records.'),
           ('Claim &amp; negotiation', 'We present your damages to the insurers and negotiate for a fair settlement.'),
           ('Litigation', 'If a fair offer does not come, we are prepared to file suit and take your case to court.')],
    faq=[('How long do I have to file an injury claim in Florida?', 'For most negligence claims arising after March 24, 2023, Florida law allows two years from the date of the injury to file a lawsuit. Some claims have shorter deadlines, so speak with an attorney early.'),
         ('What should I do after a car accident?', 'Get medical care, call the police, photograph the scene and the vehicles, and collect contact details from witnesses. In Florida, seeing a doctor within 14 days of the crash matters for your PIP benefits.'),
         ('What if I was partly at fault?', 'You may still recover, reduced by your share of fault. Under Florida law since 2023, a person found more than 50 percent at fault generally cannot recover damages in most negligence cases.'),
         ('Should I talk to the other driver\'s insurance company?', 'Be careful. Adjusters may ask for a recorded statement or offer a quick settlement before you know the full extent of your injuries. It is usually best to speak with an attorney first.'),
         ('Will my case go to court?', 'Most injury claims resolve through negotiation, but we prepare every case as if it might go to trial.')],
    feature=dict(photo='elizabeth-seated.webp', label='Inside knowledge', h2='We know how the other side builds its case.',
                 p='Elizabeth Diaz Fernandez prosecuted cases as a Miami-Dade Assistant State Attorney and has litigated hundreds of personal injury and property insurance cases.',
                 link=('about/elizabeth-diaz-fernandez/', 'Meet Elizabeth'))),
 'family-law': dict(
    title='Family Law', key=None, case='Family law',
    desc='Divorce, time-sharing, child support and alimony in Doral and Miami-Dade. De La Noval, P.A. handles family matters with discretion. Se habla español.',
    h1a='Family', h1b='<em>law.</em>', photo=('glass-tower.webp', 960, 720),
    lede='Divorce, time-sharing and support, handled with discretion and care, whether the right answer is an agreement or a day in court.',
    big='Every family is different. <em>The solution should fit yours.</em>',
    body=['We understand family matters are delicate. Our attorneys give you the tools and information to craft a solution that is right for you and your children.',
          'Whether the answer is an amicable agreement or advocating firmly for your rights in court, we are dedicated to fair and reasonable results.',
          'Every conversation is private, and available in English or Spanish.'],
    types=[('Divorce', 'Contested and uncontested divorce, including the division of property and debts.'),
           ('Parenting plans &amp; time-sharing', 'Custody arrangements built around your children\'s best interests.'),
           ('Child support', 'Establishing and enforcing support under Florida\'s guidelines.'),
           ('Alimony', 'Requests for, and defense against, spousal support.'),
           ('Modifications', 'Changing support or time-sharing when circumstances change.'),
           ('Domestic violence injunctions', 'Petitions for protection, and responses to them.')],
    steps=[('Private consultation', 'We listen, answer your questions and explain how the process works in Florida.'),
           ('A plan', 'We define your goals and gather the financial and family information the case needs.'),
           ('Negotiation &amp; mediation', 'Many family cases resolve through negotiation or mediation. We prepare you for both.'),
           ('Court, if needed', 'When agreement is not possible, we present your case before the judge.')],
    faq=[('Do I need a lawyer for an uncontested divorce?', 'Not always, but an attorney helps make sure the agreement is complete and enforceable, especially when children, property or support are involved.'),
         ('How is time-sharing decided in Florida?', 'Courts approve parenting plans based on the best interests of the child. Since 2023, Florida law presumes that equal time-sharing is in the child\'s best interests, though that presumption can be overcome.'),
         ('Is my consultation confidential?', 'Yes. What you share with us in a consultation is kept confidential.'),
         ('Can support or time-sharing be changed later?', 'Often, yes, when there has been a substantial change in circumstances. We can review whether a modification makes sense for you.')],
    feature=None),
}

ORDER = [s for s, _ in AREAS]


def build_sub(slug):
    d = SUBS[slug]; root = '../../'; here = root + 'practice-areas/%s/' % slug
    name = dict(AREAS)[slug]
    m = hero(root, [(root + 'homepage/', 'Home'), (root + 'practice-areas/', 'Practice areas'), name], d['h1a'], d['h1b'], d['lede'], *d['photo'])
    m += f'''  <section class="intro2" aria-labelledby="intro-label">
    <div class="wrap">
      <div>
        <div class="label" id="intro-label" data-reveal>{name}</div>
        <p class="big" data-reveal style="--d:100ms">{d['big']}</p>
      </div>
      <div class="body" data-reveal style="--d:200ms">{''.join('<p>%s</p>' % p for p in d['body'])}</div>
    </div>
  </section>

'''
    tiles = ''.join('<div data-reveal><h3>%s</h3><p>%s</p></div>' % t for t in d['types'])
    m += f'''  <section class="types" aria-labelledby="types-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="label" data-reveal>Cases we handle</div>
        <h2 id="types-title" data-reveal style="--d:100ms">How we can help</h2>
      </div>
      <div class="tgrid" data-stagger="80">{tiles}</div>
    </div>
  </section>

'''
    photo, w, h = d['photo']
    if d['key']:
        m += f'''  <section class="checkband" aria-labelledby="check-title">
    <div class="wrap">
      <div class="copy">
        <div class="label" data-reveal>30-second check</div>
        <h2 id="check-title" data-reveal style="--d:100ms">{d['check_title']}</h2>
        <p data-reveal style="--d:200ms">{d['check_text']}</p>
      </div>
      <div class="panel-card" data-reveal="fade" style="--d:250ms">
        <div class="ph"><img src="{root}assets/img/stock/{photo}" alt="" width="{w}" height="{h}" loading="lazy"></div>
        <div class="check" data-check="{d['key']}" aria-live="polite"></div>
      </div>
    </div>
  </section>

'''
    else:
        m += f'''  <section class="checkband" aria-labelledby="check-title">
    <div class="wrap">
      <div class="copy">
        <div class="label" data-reveal>Private consultations</div>
        <h2 id="check-title" data-reveal style="--d:100ms">Start with a private conversation.</h2>
        <p data-reveal style="--d:200ms">Tell us a little about your situation. An attorney will call you, in English or Spanish, at a time that is safe and convenient for you.</p>
      </div>
      <div class="panel-card" data-reveal="fade" style="--d:250ms">
        <div class="ph"><img src="{root}assets/img/stock/pen.webp" alt="" width="1024" height="769" loading="lazy"></div>
        <div>
          <div class="label" style="color:#c3cdff;margin-bottom:24px">Discreet &amp; confidential</div>
          <blockquote>Every family matter begins with a private conversation.</blockquote>
          <a class="btn btn-ghost" href="#review">Request a private consultation</a>
        </div>
      </div>
    </div>
  </section>

'''
    m += steps_section('How your case moves forward', d['steps'], 'You will always know where your case stands and what happens next.')
    if d['feature']:
        f = d['feature']
        m += f'''  <section class="feature" aria-labelledby="feature-title">
    <div class="ph"><img src="{root}assets/img/{f['photo']}" alt="" width="800" height="1000" loading="lazy" style="top:0;height:100%;object-position:50% 0"></div>
    <div class="copy">
      <div class="label" data-reveal>{f['label']}</div>
      <h2 id="feature-title" data-reveal style="--d:100ms">{f['h2']}</h2>
      <p data-reveal style="--d:200ms">{f['p']}</p>
      <a class="more sweep nudge" href="{root}{f['link'][0]}" data-reveal style="--d:300ms;align-self:flex-start">{f['link'][1]} {ARROW16}</a>
    </div>
  </section>

'''
    qa = ''.join('<details><summary>%s</summary><p>%s</p></details>' % q for q in d['faq'])
    m += f'''  <section class="faq" aria-labelledby="faq-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="label" data-reveal>Questions</div>
        <h2 id="faq-title" data-reveal style="--d:100ms">Common questions</h2>
        <p data-reveal style="--d:200ms">General information only, not legal advice. Every case is different.</p>
      </div>
      <div data-reveal style="--d:150ms">{qa}</div>
    </div>
  </section>

'''
    others = ''.join('<li><a href="%s"%s>%s %s</a></li>' % (root + 'practice-areas/%s/' % s, ' aria-current="page"' if s == slug else '', n, ARROW) for s, n in AREAS)
    m += f'''  <section class="others" aria-label="Other practice areas">
    <div class="wrap">
      <div class="label">Practice areas</div>
      <ul>{others}</ul>
    </div>
  </section>

'''
    out = page(root, d['title'], d['desc'], photo, m, 'practice', here, check=bool(d['key']))
    out = out.replace('<option>%s</option>' % d['case'], '<option selected>%s</option>' % d['case'], 1)
    os.makedirs('practice-areas/' + slug, exist_ok=True)
    open('practice-areas/%s/index.html' % slug, 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote', slug)


def build_overview():
    root = '../'; here = root + 'practice-areas/'
    m = hero(root, [(root + 'homepage/', 'Home'), 'Practice areas'], 'How we', '<em>can help.</em>',
             'Three practice areas, one standard: you will always know where your case stands and what happens next.', 'skyline-storm.webp', 1024, 511)
    rows = [
        ('property-damage', 'hurricane-palms.webp', 1024, 683, 'Storm, water, fire and roof claims that were denied, delayed or underpaid, for homes and businesses.', ['Hurricane &amp; wind damage', 'Water damage &amp; leaks', 'Roof, fire &amp; smoke claims', 'Commercial property']),
        ('personal-injury', 'brickell-night.webp', 1024, 768, 'Car accidents, slips and falls and other injuries, pursued for the full compensation the law allows.', ['Car, truck &amp; rideshare accidents', 'Pedestrian &amp; bicycle accidents', 'Slip and fall', 'Premises injuries']),
        ('family-law', 'pen.webp', 1024, 769, 'Divorce, time-sharing and support, handled with discretion, whether the answer is agreement or court.', ['Divorce', 'Parenting plans &amp; time-sharing', 'Child support &amp; alimony', 'Modifications']),
    ]
    for i, (slug, photo, w, h, p, cases) in enumerate(rows):
        name = dict(AREAS)[slug]; href = root + 'practice-areas/%s/' % slug
        lis = ''.join('<li>%s</li>' % c for c in cases)
        m += f'''  <section class="area{' alt' if i % 2 else ''}" aria-labelledby="a{i}">
    <a class="ph" href="{href}" tabindex="-1" aria-hidden="true"><img src="{root}assets/img/stock/{photo}" alt="" width="{w}" height="{h}" loading="lazy"></a>
    <div class="copy">
      <div class="no label" data-reveal>0{i + 1}</div>
      <h2 id="a{i}" data-reveal style="--d:100ms"><a href="{href}">{name}</a></h2>
      <p data-reveal style="--d:200ms">{p}</p>
      <ul class="cases" data-reveal style="--d:250ms">{lis}</ul>
      <a class="more sweep nudge" href="{href}" data-reveal style="--d:300ms;align-self:flex-start">Explore {name.lower().replace('&amp;', '&amp;')} {ARROW16}</a>
    </div>
  </section>

'''
    m += steps_section('How a case works', [
        ('Case review', 'Tell us what happened. An attorney reviews it and calls to explain your options.'),
        ('Investigation', 'We gather the documents, records and evidence your case needs.'),
        ('Negotiation', 'We present your case to the other side and press for a fair result.'),
        ('Court, if needed', 'If a fair result does not come, we are prepared to take your case to court.')],
        'The steps are similar in every practice area, and you will know where your case stands at each one.')
    out = page(root, 'Practice Areas', 'De La Noval, P.A. handles property insurance claims, personal injury and family law in Doral, Miami-Dade and across Florida. Se habla español.', 'skyline-storm.webp', m, 'practice', here)
    os.makedirs('practice-areas', exist_ok=True)
    open('practice-areas/index.html', 'w', encoding='utf-8', newline='\n').write(out)
    print('wrote overview')


exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_more.py'), encoding='utf-8').read())

update_existing()
build_overview()
for s in ORDER:
    build_sub(s)
build_contact()
build_faqs()
build_guides()
build_article()
