import json,html,os
B=json.load(open(os.path.join(os.path.dirname(__file__),'bios.json')))
def bios(key):
    out=[]
    for name,paras in B[key]:
        nm,_,role=name.partition(', ')
        out.append('<article class="bio"><h2>%s</h2>%s%s</article>'%(html.escape(nm),
          '<p class="bio-role">%s</p>'%html.escape(role) if role else '',
          ''.join('<p>%s</p>'%html.escape(p) for p in paras)))
    return '<div class="bios">'+''.join(out)+'</div>'

P={}
P['about']=dict(title="About the Agni Institute: Mission, Methods & People",
desc="The Agni Institute is a volunteer-run 501(c)(3) nonprofit serving the common good by expanding human consciousness through study, meditation and research.",
h1="About Agni Institute", lede="A volunteer-run nonprofit dedicated to education, meditation and research inspired by Agni Yoga.",
body="""
<h2>Mission and purpose</h2>
<p>At the Agni Institute, our mission is to serve the common good by awakening and expanding human consciousness.</p>
<p>In our time of rapidly accelerating discoveries, the purification of consciousness is vitally important. We are therefore committed to the living practice of Agni Yoga, demonstrating through disciplined research and sincere personal application that moral and ethical foundations must become an inseparable part of knowledge, lest the gulf between intellect and conscience continue to widen.</p>
<p>By cultivating curiosity, inner discipline and mutual goodwill, we aim to empower individuals and communities to co-create the wise, ethical and holistic solutions our world needs.</p>
<h2>Our activities and methods</h2>
<p>The Institute organizes and participates in research programs to deepen understanding and practical application of the laws of nature. Our method is to drive self-cultivation and broadening of consciousness through education, exploration, exercise and refinement of the faculties of consciousness.</p>
<p>We encourage individual and collective pursuit of technical skills in disciplines such as physics, biology, chemistry, engineering, materials research and astronomy. We believe the combination of Eastern and Western methods, meaning disciplines of consciousness, critical thought and scientific methodology, when motivated by goodwill, is capable of enhancing both.</p>
<p>Outreach grows naturally from program work. Each participant has his or her own interests and research within the Institute, and collective efforts engage people project by project. In collaborative research programs, participants working independently follow a defined method and share methods, data and findings. Participation is not limited to any one region and is intended to be open-source.</p>
<p>From its activities the Institute produces content such as papers, commentary, articles, audio and video, collaborative websites, technical research plans and build instructions. We also organize meditation retreats and practicums to support meditation as a means of understanding consciousness.</p>
<h2>Our relationship to Agni Yoga</h2>
<p>Although we take inspiration from the writings and teachings of Agni Yoga, the Institute is not officially affiliated with any organization. Read more on <a href="agni-institute-and-agni-yoga.html">Agni Institute and Agni Yoga</a>.</p>
<h2>Who we are</h2>
<p>We are all volunteers, working collectively while each undergoes a personal journey of self-transformation, self-discovery and growth of consciousness. The Institute was founded in 2009 and is governed by a volunteer <a href="board-of-directors.html">Board of Directors</a>, supported by a <a href="board-of-advisors.html">Board of Advisors</a>. Agni Institute is a 501(c)(3) nonprofit organization.</p>
""")

P['board-of-directors']=dict(title="Board of Directors | Agni Institute",
desc="Meet the volunteer Board of Directors of the Agni Institute, the nonprofit for Agni Yoga study, meditation and consciousness research.",
h1="Board of Directors", lede="The volunteers who govern the Agni Institute.", body=bios('node_14')+'<p><a href="board-of-advisors.html">Board of Advisors</a> · <a href="about.html">About the Institute</a></p>',
crumbs=[('About','about.html')])

P['board-of-advisors']=dict(title="Board of Advisors | Agni Institute",
desc="Meet the Agni Institute's Board of Advisors, who offer guidance on research, governance and the Institute's mission.",
h1="Board of Advisors", lede="Advisory guidance for the Institute's mission.", body=bios('node_13')+'<p><a href="board-of-directors.html">Board of Directors</a> · <a href="about.html">About the Institute</a></p>',
crumbs=[('About','about.html')])

P['get-involved']=dict(title="Get Involved: Volunteer, Meditate, Research | Agni Institute",
desc="Volunteer or participate at the Agni Institute: meditate, investigate, learn research skills, explore dreaming, or donate. There is no charge for any program.",
h1="Get Involved", lede="Everyone at Agni Institute is a volunteer. Many are participants. Many are both.",
body="""
<h2>Volunteer and participate</h2>
<p>As a participant you can engage in studies, workshops, exercises, discussion groups, classes, research and explorations of consciousness. Expand your perception, abilities and understanding of who and what each of us is. We welcome all who are sincerely interested in understanding the nature of consciousness and reality, including in research projects, some of which involve laboratory settings, methods and instrumentation.</p>
<p>As a volunteer you can work with like-minded people to build projects and programs that advance human understanding and capability.</p>
<h2>Meditate</h2>
<p>Still the mind, find inner peace, increase focus, clarity and creativity, and begin to realize your higher nature. At Agni Institute, meditation is taught and practiced as the principal skill for investigating the nature of consciousness, existence and reality. Whether you are just starting or have meditated for many years, we offer practical support, discussions and sessions. See <a href="program-meditation.html">Meditation</a> and our <a href="meditation-for-beginners.html">beginner's guide</a>.</p>
<h2>Investigate</h2>
<p>We not only read about the natural world but want to experience it first hand. Drawing on the books of Agni Yoga and others, the Institute designs investigations and experiments into correlations between consciousness and the natural world, and invites participation at every level, from the enthusiast looking for hands-on activities to the trained professional investigator. See <a href="program-collaborative-research.html">Collaborative Research</a>.</p>
<h2>Learn</h2>
<p>As a participant or volunteer, you could learn or add skills in:</p>
<ul>
<li>Meditation</li><li>Dreaming methods</li><li>Designing research projects and experiments</li><li>Design, including CAD software</li><li>Collecting, analyzing and presenting data</li><li>Writing papers reporting findings</li><li>Building test fixtures and experimental apparatus</li><li>Solid-printing research parts</li><li>Instrumentation used in experiments</li>
</ul>
<h2>Dream</h2>
<p>The Subtle Realm group explores the nearly one-third of our lives spent asleep: how consciousness and physiology shape dreaming, and how to develop conscious activity in the dream state. See <a href="program-subtle-realm.html">Subtle Realm</a> and <a href="lucid-dreaming.html">Lucid Dreaming</a>.</p>
<h2>Donate</h2>
<p>Financial contributions help fund public outreach, community events and classes, research equipment and software, and basic administrative costs. <a href="donate.html">Make a donation</a>.</p>
<p>In keeping with long-standing tradition, there is no charge for any of our activities or programs. <a href="contact.html">Contact us</a> to get started.</p>
""")

P['agni-institute-and-agni-yoga']=dict(title="Agni Institute and Agni Yoga: Our Relationship",
desc="How the Agni Institute relates to the Agni Yoga teachings: study dialogues, meditation, mentoring and research, without official affiliation to any organization.",
h1="Agni Institute and Agni Yoga", lede="How the Institute relates to the Agni Yoga teachings.",
body="""
<p>Offerings to the public of Agni Yoga publications, as well as preservation and dissemination of writings, are under way. This includes dialogues focused on deepening an understanding of Agni Yoga and realizing its pursuit as a natural part of daily life.</p>
<p>Activities include ongoing discussions on practicing inner yogas, broadening of consciousness, and the blossoming of heart and awareness. Understanding, developing and sustaining methods of meditation and personal striving are provided through discussions, periodic sittings and meditation retreats. Ongoing mentoring and support are a foundational part of this work.</p>
<p>Inspiration for research is drawn from concepts and suggestions in the texts of Agni Yoga, and investigations may also include explorations motivated by ethics and values in accord with those expressed in Agni Yoga.</p>
<h2>Independence</h2>
<p>Although we at Agni Institute take inspiration from the writings and teachings of Agni Yoga, the Institute is not officially affiliated with any organization. The Agni Yoga texts are provided free of charge by their copyright holders on the sole condition that no modifications are introduced by any third party.</p>
<p>Learn more <a href="about-agni-yoga.html">about Agni Yoga</a>, about <a href="helena-roerich.html">Helena Roerich</a>, or <a href="books-of-agni-yoga.html">download the books</a>.</p>
""", crumbs=[('About','about.html')])

P['about-agni-yoga']=dict(title="What Is Agni Yoga? The Teaching of Living Ethics | Agni Institute",
desc="Agni Yoga, the Teaching of Living Ethics, is a book series recorded by Helena Roerich (1924–1938) on consciousness, ethics and spiritual practice.",
h1="What Is Agni Yoga?", lede="An introduction to the Teaching of Living Ethics that inspires the Institute's work.",
body="""
<h2>The meaning of Agni</h2>
<p>Agni is the god of fire found in the classical Hindu text the Rig Veda, dating to roughly 1500–1200 BCE. He also appears in the epics of the Mahabharata and Ramayana. As the god of fire, he represents physical, vital and spiritual fire within living beings. Agni is considered a protector, purifier and transformer of beings, and a mediator between humanity and a divine hierarchy.</p>
<h2>The Agni Yoga books</h2>
<p>Agni Yoga is the name given to a collection of writings recorded by <a href="helena-roerich.html">Helena Roerich</a>. These were essentially dictated to her between 1924 and 1938 by Eastern teachers. The series covers philosophy, ethics, spirituality and the evolution of human consciousness, and is sometimes referred to as the Teaching of Living Ethics. Together the books are regarded as a teaching given for modern times.</p>
<p>They comprise a synthesis of tenets, understanding and disciplines from Buddhist and Hindu traditions, with an emphasis on the transformation of consciousness, and were given with the intention of informing and mentoring humanity in a new era. The relationship between consciousness itself and the "fires" of life, in all their variations, is explored, bringing about an awakening of consciousness. Agni Yoga in this sense is intended to bring about an awakening and mastery of the fires of illumination of consciousness.</p>
<h2>Themes of the Teaching</h2>
<ul>
<li><strong>Living ethics:</strong> spiritual growth is shown in daily conduct, labor and cooperation, not set apart from ordinary life.</li>
<li><strong>Heart and consciousness:</strong> the heart is treated as a center of understanding, and the expansion of consciousness as the aim of evolution.</li>
<li><strong>Psychic energy and thought:</strong> the books repeatedly invite investigation of the energy of thought and its effects.</li>
<li><strong>Science and spirit:</strong> the Teaching encourages experiment and the joining of knowledge with conscience.</li>
<li><strong>Community and service:</strong> striving is directed toward the common good.</li>
</ul>
<h2>Agni Yoga at the Institute</h2>
<p>The Agni Institute takes its inspiration from these writings while remaining independent of any organization. We support study through dialogues and mentoring (see <a href="program-studies.html">Studies in Agni Yoga</a> and <a href="study-groups.html">Study Groups</a>), practice <a href="program-meditation.html">meditation</a> as a way to verify insights for oneself, and pursue <a href="program-institute-research.html">research</a> suggested in the texts.</p>
<h2>Read the books</h2>
<p>All the books in the series can be downloaded free in PDF and ePub on our <a href="books-of-agni-yoga.html">Books of Agni Yoga</a> page.</p>
""")

P['contact']=dict(title="Contact the Agni Institute",
desc="Contact the Agni Institute with sincere inquiries about meditation, Agni Yoga study, research or volunteering. Email, phone, mail or the contact form.",
h1="Contact Us", lede="We welcome all serious inquiries. Thank you for your interest in Agni Institute.", nocta=True,
body="""
<div class="contact-grid">
<form class="form" name="contact" method="POST" data-netlify="true" data-netlify-recaptcha="true" netlify-honeypot="bot-field" action="/thank-you">
  <input type="hidden" name="form-name" value="contact" />
  <p class="hp" aria-hidden="true"><label>Leave this field blank <input name="bot-field" tabindex="-1" autocomplete="off" /></label></p>
  <label>Name <input type="text" name="name" autocomplete="name" required /></label>
  <label>Email <input type="email" name="email" autocomplete="email" required /></label>
  <label>Subject <input type="text" name="subject" /></label>
  <label>Message <textarea name="message" required></textarea></label>
  <div class="recaptcha-wrap" data-netlify-recaptcha="true"></div>
  <div class="form-submit">
    <button class="btn btn-accent" type="submit">Send message</button>
    <p class="form-privacy">We use your details only to reply. See our <a href="privacy.html">privacy policy</a>. Protected by reCAPTCHA; Google <a href="https://policies.google.com/privacy" rel="noopener noreferrer">Privacy</a> and <a href="https://policies.google.com/terms" rel="noopener noreferrer">Terms</a> apply.</p>
  </div>
</form>
<aside class="contact-meta" aria-label="Other ways to reach us">
  <h2>Other ways to reach us</h2>
  <p><strong>Email</strong><br /><a href="mailto:info@agniinstitute.org">info@agniinstitute.org</a></p>
  <p><strong>Phone</strong><br /><a href="tel:+12067358697">(206) 735-8697</a></p>
  <p><strong>Mail</strong><br />Agni Institute<br />PO Box 3589<br />Amherst, MA 01004-3589</p>
  <p>Interested in meditation, study groups or research? Tell us a little about yourself and what you are looking for, and a volunteer will reply.</p>
</aside>
</div>
""")

P['donate']=dict(title="Donate to the Agni Institute | Tax-Deductible 501(c)(3)",
desc="Support free meditation, Agni Yoga study and research. Agni Institute is a 501(c)(3) nonprofit (EIN 26-4479032); gifts are tax-deductible as allowed by law.",
h1="Support the Agni Institute", lede="Your gift sustains free programs in meditation, study and research.",
body="""
<h2>Your impact</h2>
<p>Everyone at the Agni Institute is a volunteer, and in keeping with long-standing tradition there is no charge for any of our activities or programs. Donations are what make that possible. Your generous contribution helps us:</p>
<ul>
<li>fund public outreach, including the website and newsletters</li>
<li>fund community events, workshops, courses, tutorials and classes</li>
<li>purchase instruments, equipment and supplies for research</li>
<li>pay for essential productivity, design, engineering and scientific software</li>
<li>cover basic administrative costs</li>
</ul>
<div class="donate-box">
  <p><a class="btn btn-warm" id="paypal-donate" href="https://www.paypal.com/donate/?hosted_button_id=VJSKXRDE4SD24" onclick="gtag('event','conversion',{'send_to':'AW-11064265096/LpQJCNVJ5PgcEIiT7Zsp','transport_type':'beacon'});">Donate via PayPal</a></p>
  <p class="small">Secure donations are processed by PayPal.</p>
</div>
<h2>Tax deductibility</h2>
<p>Agni Institute is a tax-exempt 501(c)(3) nonprofit organization, EIN 26-4479032. Donations are tax-deductible to the extent allowed by law. Please consult your tax advisor about your situation.</p>
<h2>Other ways to give</h2>
<p>To give by check, or to ask about other ways to support the work, <a href="contact.html">contact us</a>. Mail: Agni Institute, PO Box 3589, Amherst, MA 01004-3589. You can also <a href="get-involved.html">volunteer your time and skills</a>.</p>
""")

P['books-of-agni-yoga']=dict(title="The Books of Agni Yoga: Free PDF & ePub Downloads | Agni Institute",
desc="Download the Agni Yoga book series free in PDF and ePub: Leaves of Morya's Garden, Agni Yoga, Infinity, Hierarchy, Heart, Fiery World, Aum and more.",
h1="The Books of Agni Yoga", lede="The Agni Yoga series and related works, free to download for study and reflection.", body=None)

P['privacy']=dict(title="Privacy Policy | Agni Institute",
desc="How the Agni Institute website handles your information: the contact form, Google Ads measurement, donations through PayPal, and your choices.",
h1="Privacy Policy", lede="Last updated October 24, 2026.",
body="""
<p>This policy explains what information the Agni Institute website collects and how it is used. We collect as little as we need.</p>
<h2>Contact form</h2>
<p>When you submit our contact form, the name, email address, subject and message you enter are sent to us through Netlify Forms, a service of our website host, Netlify. We use this information only to respond to your inquiry and keep a record of our correspondence. We do not sell or rent it, and we do not add you to a mailing list without your permission.</p>
<h2>Spam protection (Google reCAPTCHA)</h2>
<p>Our forms are protected by Google reCAPTCHA, provided through Netlify, to block automated spam. reCAPTCHA collects hardware and software information, such as device and browser data, and sends it to Google for analysis. Your use of reCAPTCHA is subject to the Google <a href="https://policies.google.com/privacy" rel="noopener noreferrer">Privacy Policy</a> and <a href="https://policies.google.com/terms" rel="noopener noreferrer">Terms of Service</a>.</p>
<h2>Google Ads tags and cookies</h2>
<p>This website uses the Google tag (gtag.js) for Google Ads. It helps us understand whether our ads lead people to our site and measure "conversions", such as a contact form being submitted or the donate button being clicked. Google may set cookies or use similar technologies and receive information such as your IP address, browser and device details, the pages you visit and how you arrived. Google's use of this information is governed by the <a href="https://policies.google.com/privacy" rel="noopener noreferrer">Google Privacy Policy</a>. You can manage ad personalization at <a href="https://adssettings.google.com" rel="noopener noreferrer">Google Ad Settings</a> or block cookies in your browser.</p>
<h2>Donations</h2>
<p>Donations are processed by PayPal on PayPal's own site. We do not see or store your card details. PayPal shares with us the information needed to record and acknowledge your gift. See the <a href="https://www.paypal.com/us/legalhub/privacy-full" rel="noopener noreferrer">PayPal Privacy Statement</a>.</p>
<h2>Hosting and logs</h2>
<p>Our website is hosted by Netlify, which may process technical data such as IP addresses in server logs to deliver and secure the site.</p>
<h2>Your choices</h2>
<p>You may ask us to access, correct or delete the personal information you have sent us by contacting <a href="mailto:info@agniinstitute.org">info@agniinstitute.org</a>.</p>
<h2>Contact</h2>
<p>Agni Institute, PO Box 3589, Amherst, MA 01004-3589 · <a href="mailto:info@agniinstitute.org">info@agniinstitute.org</a> · <a href="tel:+12067358697">(206) 735-8697</a></p>
""")

P['thank-you']=dict(title="Thank You for Contacting Us | Agni Institute", desc="Thank you for contacting the Agni Institute. A volunteer will reply to your message.",
h1="Thank you", lede="Your message has been sent. A volunteer will be in touch.", noindex=True, nocta=True,
extra_head="<script>gtag('event','conversion',{'send_to':'AW-11064265096/PUshCJPFqOocEIiT7Zsp'});</script>",
body="""<p>While you wait, you might like to read our <a href="meditation-for-beginners.html">meditation guide for beginners</a>, learn <a href="about-agni-yoga.html">about Agni Yoga</a>, or <a href="programs.html">explore our programs</a>.</p><p><a class="btn btn-accent" href="index.html">Back to home</a></p>""")

P['donate-thank-you']=dict(title="Thank You for Your Donation | Agni Institute", desc="Thank you for supporting the Agni Institute.",
h1="Thank you for your gift", lede="Your generosity keeps our programs free and open to all.", noindex=True, nocta=True,
body="""<p>Agni Institute is a 501(c)(3) nonprofit organization (EIN 26-4479032). PayPal will email you a receipt for your records; donations are tax-deductible to the extent allowed by law.</p><p>Questions about your gift? <a href="contact.html">Contact us</a>.</p><p><a class="btn btn-accent" href="index.html">Back to home</a></p>""")

P['404']=dict(title="Page Not Found | Agni Institute", desc="The page you were looking for could not be found.",
h1="Page not found", lede="Sorry, we couldn't find that page. It may have moved when our site was redesigned.", noindex=True, nocta=True,
body="""<div class="actions"><a class="btn btn-accent" href="/">Go to the homepage</a><a class="btn btn-outline" href="/programs">Explore programs</a><a class="btn btn-outline" href="/contact">Contact us</a></div>
<h2>Popular pages</h2><ul><li><a href="/meditation-for-beginners">Meditation for Beginners</a></li><li><a href="/about-agni-yoga">What Is Agni Yoga?</a></li><li><a href="/books-of-agni-yoga">The Books of Agni Yoga</a></li><li><a href="/lucid-dreaming">Lucid Dreaming</a></li><li><a href="/donate">Donate</a></li></ul>""")
