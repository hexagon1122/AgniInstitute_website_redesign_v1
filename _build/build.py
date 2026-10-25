import os,re,json,html,shutil,sys
sys.path.insert(0,os.path.dirname(__file__))
from landing import L
from pages import P
SRC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(SRC,'_publish')
SITE='https://agniinstitute.org'
AW='AW-11064265096'
E=html.escape

GTAG=f"""<!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={AW}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{AW}');</script>"""

NAV=[('index','Home'),('about','About'),('programs','Programs'),('study-groups','Study Groups'),('contact','Contact')]
PROGRAM_PAGES={'program-meditation','program-subtle-realm','program-studies','program-institute-research','program-collaborative-research'}

def url(slug): return SITE+'/' if slug=='index' else f'{SITE}/{slug}'

def header(slug):
    links=''.join(f'\n        <a href="{s}.html"{" aria-current=\"page\"" if s==slug else ""}>{n}</a>' for s,n in NAV)
    cur=' aria-current="page"' if slug=='donate' else ''
    return f"""  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="nav-wrap">
      <a class="brand" href="index.html" aria-label="Agni Institute">
        <img src="assets/logo.png" alt="" width="100" height="46" />
      </a>
      <nav class="nav" aria-label="Primary">{links}
      </nav>
      <a class="nav-donate" href="donate.html"{cur}>Donate</a>
    </div>
  </header>"""

FOOTER=open(os.path.join(os.path.dirname(__file__),'footer.html')).read()

def ld(obj): return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False)+'</script>'

def head(slug,title,desc,noindex=False,jsonld=(),extra=''):
    robots='\n  <meta name="robots" content="noindex, follow" />' if noindex else ''
    canon='' if slug=='404' else f'\n  <link rel="canonical" href="{url(slug)}" />'
    pre=''
    if slug=='index':
        pre='''
  <link rel="preload" as="image" type="image/webp" href="assets/hero-pillars-800.webp" media="(max-width: 700px)" fetchpriority="high" />
  <link rel="preload" as="image" type="image/webp" href="assets/hero-pillars-1920.webp" media="(min-width: 701px)" fetchpriority="high" />'''
    j=''.join('\n  '+ld(x) for x in jsonld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  {GTAG}
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}" />{robots}{canon}
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Agni Institute" />
  <meta property="og:title" content="{E(title)}" />
  <meta property="og:description" content="{E(desc)}" />
  <meta property="og:url" content="{url(slug)}" />
  <meta property="og:image" content="{SITE}/assets/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" href="favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png" />
  <link rel="apple-touch-icon" href="apple-touch-icon.png" />{pre}
  <link rel="stylesheet" href="styles.css" />{j}{extra}
</head>
<body>
"""

def crumbs_ld(slug,name,crumbs):
    items=[('Home','index')]+[(n,h.replace('.html','')) for n,h in crumbs]+[(name,slug)]
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":url(s)} for i,(n,s) in enumerate(items)]}

def faq_ld(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}

def faq_html(faq):
    return '<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>'+''.join(
        f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q,a in faq)+'</section>'

CTA='<div class="actions hero-cta"><a class="btn btn-accent" href="contact.html">Join a free intro session</a>%s</div>'

def page_hero(h1,lede,second='',nocta=False):
    return f"""  <div class="page-hero">
    <h1>{h1}</h1>
    <p>{lede}</p>
    {'' if nocta else CTA%second}
  </div>"""

def write(slug,doc):
    open(os.path.join(OUT,slug+'.html'),'w').write(doc)

def extract(slug):
    s=open(os.path.join(SRC,slug+'.html')).read()
    return s.split('</header>',1)[1].split('<footer',1)[0]

def title_of(slug):
    s=open(os.path.join(SRC,slug+'.html')).read()
    return re.search(r'<h1>(.*?)</h1>',s).group(1)

META={
'program-meditation':("Meditation Program: Practice, Sittings & Retreats | Agni Institute","Learn meditation as a discipline of consciousness: periodic sittings, mentoring and retreats at the Agni Institute. There is no charge for any program."),
'program-subtle-realm':("Subtle Realm Program: Dreams, Sleep & Consciousness | Agni Institute","The Subtle Realm program explores consciousness beyond the physical body: dreaming, lucid dreaming and states of sleep, through study and shared experiments."),
'program-studies':("Studies in Agni Yoga: Dialogues & Mentoring | Agni Institute","Study the Agni Yoga teachings through dialogues, mentoring and selected content from more than 35 years of studies at the Agni Institute."),
'program-institute-research':("Institute Research: Consciousness & Natural Law | Agni Institute","Specialized laboratory research based on investigations suggested in the texts of Agni Yoga, from protocols and benchwork to collaboration with universities."),
'program-collaborative-research':("Collaborative Research: Citizen Science Projects | Agni Institute","Join open, global research projects at three levels: enthusiast, citizen scientist, or professional investigator. Share methods, data and findings."),
'programs':("Programs: Meditation, Agni Yoga Study & Research | Agni Institute","Explore the Agni Institute's programs: meditation, Studies in Agni Yoga, Institute and Collaborative Research, and the Subtle Realm dream program."),
'study-groups':("Agni Yoga Study Groups & Meditation Sittings | Agni Institute","Join an Agni Yoga study group: dialogues on inner yoga, the heart and consciousness, meditation sittings and mentoring. No charge to participate."),
'index':("Agni Institute – Meditation, Agni Yoga & Consciousness Research","Agni Institute is a volunteer 501(c)(3) nonprofit for Agni Yoga study, meditation training and open research into nature and consciousness. Programs are free."),
}

GUIDES=[('meditation-for-beginners','Meditation for Beginners','A step-by-step guide to posture, breath and building a daily practice.'),
('benefits-of-meditation','Benefits of Meditation','What research shows about meditation, stress, attention and wellbeing.'),
('lucid-dreaming','Lucid Dreaming','How conscious dreaming works, what science knows, and how to begin.'),
('science-of-consciousness','Science of Consciousness','The hard problem, leading theories and contemplative research.'),
('helena-roerich','Helena Roerich','The life of the author of the Agni Yoga teachings.')]
def guides_section(h='h2'):
    cards=''.join(f'<article class="card"><{h}><a href="{s}.html">{t}</a></{h}><p>{d}</p><a class="more" href="{s}.html">Read the guide →</a></article>' for s,t,d in GUIDES)
    return f'<section class="section guides" aria-labelledby="guides-h"><p class="kicker">Guides</p><h2 id="guides-h">Start exploring</h2><div class="cards cards-5">{cards}</div></section>'

def books_body():
    titles=[("Leaves of Morya's Garden I","lomg1","Leaves-of-Moryas-Garden-I"),("Leaves of Morya's Garden II","lomg2","Leaves-of-Moryas-Garden-II"),("New Era Community","community","New-Era-Community"),("Agni Yoga","ay","Agni-Yoga"),("Infinity I","infinity1","Infinity-I"),("Infinity II","infinity2","Infinity-II"),("Hierarchy","hierarchy","Hierarchy"),("Heart","heart","Heart"),("Fiery World I","fw1","Fiery-World-I"),("Fiery World II","fw2","Fiery-World-II"),("Fiery World III","fw3","Fiery-World-III"),("Aum","aum","Aum"),("Brotherhood","broth","Brotherhood"),("Supermundane","supm","Supermundane"),("Letters of Helena Roerich I","lohr1","Letters-of-Helena-Roerich-I"),("Letters of Helena Roerich II","lohr2","Letters-of-Helena-Roerich-II"),("On Eastern Crossroads","crossroads","On-Eastern-Crossroads"),("Foundations of Buddhism","FoB","Foundations-of-Buddhism")]
    rows=''.join(f'<li><span class="book-title">{E(t)}</span><span class="book-links"><a href="AYBooks/ay_{c}.pdf">PDF</a> <a href="AYBooks/ay_{c}.epub">ePub</a> <a href="https://agniyoga.org/ay_en/{o}.php" rel="noopener noreferrer">View online</a></span></li>' for t,c,o in titles)
    return f"""<p>All the texts available for download here are under copyright protection, with the copyrights held by the Agni Yoga Society, Inc. Out of their generosity we are able to offer the texts for free download, just as the Agni Yoga Society does, under the principle that the Teaching should be available to everyone. The texts may be downloaded for your own use or copied for the use of others. They may not be modified in any way, nor used for any commercial purpose. "View online" links go to the Agni Yoga Society website.</p>
<h2>The Agni Yoga series and related works</h2>
<ul class="books-list">{rows}</ul>
<p>New to the Teaching? Start with <a href="about-agni-yoga.html">What Is Agni Yoga?</a> and the life of <a href="helena-roerich.html">Helena Roerich</a>, or join a <a href="study-groups.html">study group</a>.</p>"""

MED_EXTRA="""
    <h2>Begin or deepen your practice</h2>
    <p>Still the mind, find inner peace, increase focus, clarity and creativity, subdue the noise of the world and begin to realize your higher nature. At Agni Institute, meditation is taught and practiced as the principal skill for investigating the nature of consciousness, existence and reality.</p>
    <p>If you wish to learn about and begin to meditate, or have already begun and wish to learn more, there are practical offerings to help you establish meditation as part of your lifestyle. If you have meditated for many years and wish to deepen your practice, you are invited to take part in thought-provoking and heart-centered discussions and sessions to directly experience and understand consciousness in its most fundamental states.</p>
    <h2>What practice includes</h2>
    <ul>
      <li>Discussions on methods of meditation and personal striving</li>
      <li>Periodic group sittings</li>
      <li>Mentoring and mutual care</li>
      <li>Multi-day retreats from time to time for more committed practitioners</li>
    </ul>
    <h2>Helpful reading</h2>
    <ul>
      <li><a href="meditation-for-beginners.html">Meditation for Beginners: a step-by-step guide</a></li>
      <li><a href="benefits-of-meditation.html">The benefits of meditation: what the research shows</a></li>
      <li><a href="science-of-consciousness.html">The science of consciousness</a></li>
    </ul>
    <p>Contact us for details about current sessions.</p>
"""

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    sitemap=[]
    def finish(slug,title,desc,body,jsonld=(),noindex=False,extra=''):
        doc=head(slug,title,desc,noindex,jsonld,extra)+header(slug)+'\n  <main id="main">\n'+body+'\n  </main>\n\n  '+FOOTER+'\n</body>\n</html>\n'
        write(slug,doc)
        if not noindex: sitemap.append(slug)
    # existing content pages kept from source
    for slug in ['index','programs','study-groups']+sorted(PROGRAM_PAGES):
        b=extract(slug)
        h1=title_of(slug)
        if slug=='index':
            b=b.replace('<a class="btn btn-primary" href="programs.html">Explore programs</a>\n        <a class="btn btn-ghost" href="study-groups.html">Join a study group</a>',
                        '<a class="btn btn-primary" href="contact.html">Join a free intro session</a>\n        <a class="btn btn-ghost" href="programs.html">Explore programs</a>')
            assert 'Join a free intro session' in b
            b=b.replace('  <div class="band-dark">',guides_section('h3')+'\n\n  <div class="band-dark">',1)
            b=b.replace('<p class="kicker" style="color:#f58e32">','<p class="kicker kicker-warm">')
            b=b.replace('style="margin-left:0.5rem"','')
            ngo={"@context":"https://schema.org","@type":"NGO","name":"Agni Institute","url":SITE+"/","logo":SITE+"/assets/logo.png",
                 "description":META['index'][1],"email":"info@agniinstitute.org","telephone":"+1-206-735-8697","foundingDate":"2009",
                 "taxID":"26-4479032","nonprofitStatus":"Nonprofit501c3",
                 "address":{"@type":"PostalAddress","postOfficeBoxNumber":"3589","addressLocality":"Amherst","addressRegion":"MA","postalCode":"01004-3589","addressCountry":"US"}}
            web={"@context":"https://schema.org","@type":"WebSite","name":"Agni Institute","url":SITE+"/"}
            finish(slug,*META[slug],b,[ngo,web]); continue
        b=re.sub(r'(<div class="page-hero">.*?)(\n  </div>)',lambda m:m.group(1)+'\n    '+CTA%''+m.group(2),b,count=1,flags=re.S)
        if slug=='programs':
            b=re.sub(r'<h3>(.*?)</h3>',r'<h2 class="card-title">\1</h2>',b)
            b=b.replace('</section>','</section>\n'+guides_section('h3'),1)
        if slug=='program-meditation':
            b=b.replace('    <p><a href="programs.html">← All programs</a>',MED_EXTRA+'    <p><a href="programs.html">← All programs</a>',1)
        crumbs=[('Programs','programs.html')] if slug in PROGRAM_PAGES else []
        finish(slug,*META[slug],b,[crumbs_ld(slug,h1,crumbs)])
    # landing pages
    for slug,d in L.items():
        second='<a class="btn btn-outline" href="#faq-h">Read the FAQ</a>'
        body=page_hero(d['h1'],d['lede'],second)+'\n  <article class="content prose">'+d['body']+faq_html(d['faq'])+'</article>\n'+\
            '  <div class="band-dark"><div class="section tight"><h2 class="cta-h">Explore with us</h2><p class="lead">Meditation, study and research, offered free by volunteers.</p><div class="actions"><a class="btn btn-primary" href="contact.html">Join a free intro session</a><a class="btn btn-ghost" href="donate.html">Support our work</a></div></div></div>'
        finish(slug,d['title'],d['desc'],body,[crumbs_ld(slug,d['h1'],[]),faq_ld(d['faq'])])
    # rewritten pages
    for slug,d in P.items():
        body=d['body'] if d['body'] is not None else books_body()
        second='' if slug!='donate' else ''
        b=page_hero(d['h1'],d['lede'],second,d.get('nocta',False))
        if slug=='donate':
            b=b.replace(CTA%'','<div class="actions hero-cta"><a class="btn btn-warm" href="#paypal-donate">Donate now</a><a class="btn btn-outline" href="contact.html">Join a free intro session</a></div>')
        body=b+'\n  <div class="content prose">'+body+'</div>\n'
        jl=[] if d.get('noindex') else [crumbs_ld(slug,d['h1'],d.get('crumbs',[]))]
        finish(slug,d['title'],d['desc'],body,jl,d.get('noindex',False),('\n  '+d['extra_head']) if d.get('extra_head') else '')
    # assets
    shutil.copy(os.path.join(SRC,'_build','styles.css'),OUT)
    shutil.copytree(os.path.join(SRC,'_build','assets'),os.path.join(OUT,'assets'))
    for f in ['favicon.ico','favicon-32.png','apple-touch-icon.png','_redirects','robots.txt']:
        shutil.copy(os.path.join(SRC,'_build',f),OUT)
    shutil.copytree('/workspace/agni/AYBooks',os.path.join(OUT,'AYBooks'))
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(
        f'  <url><loc>{url(s)}</loc><lastmod>2026-10-24</lastmod></url>\n' for s in sitemap)+'</urlset>\n'
    open(os.path.join(OUT,'sitemap.xml'),'w').write(sm)
    print('pages',len(os.listdir(OUT)),'sitemap',len(sitemap))
build()
