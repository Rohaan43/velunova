from pathlib import Path
import re

root = Path('dist')
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
hero = '''    <section class="banner-hero container" aria-labelledby="hero-heading">
      <div class="banner-stage">
        <picture class="banner-art"><source srcset="/assets/velunova-banner-768.webp 768w, /assets/velunova-banner.webp 1536w" sizes="(max-width: 767px) 100vw, 90vw" type="image/webp"><img src="/assets/velunova-banner.webp" alt="Velunova Creative Studio: a moonlit castle, original characters, plush companions, and the words Where Imagination Takes Shape" width="1536" height="1024" fetchpriority="high"></picture>
        <div class="banner-atmosphere" aria-hidden="true"></div>
        <div class="banner-stars" aria-hidden="true">'''
for x,y,size,delay in [(6,12,16,0),(36,8,10,1),(47,18,14,2),(68,8,12,3),(93,18,18,1),(33,44,10,2),(54,28,12,4),(72,49,16,3),(20,60,10,1),(80,71,12,4),(46,74,9,2),(65,64,16,0)]:
    hero += f'<i style="--x:{x}%;--y:{y}%;--size:{size}px;--delay:{delay}s">✦</i>'
hero += '''</div>
        <div class="banner-copy"><h1 id="hero-heading">Imagination you can hold.</h1><p>Original characters. Extraordinary creations.</p><div class="banner-actions"><a class="button" href="/custom-plushies.html">Explore custom plushies</a><a class="banner-link" href="#services">Discover our services</a></div></div>
        <label class="motion-toggle"><input type="checkbox" id="pause-animation"><span>Pause animation</span></label>
      </div>
    </section>'''
html = re.sub(r'    <section class="hero container".*?</section>', hero, html, count=1, flags=re.S)
html = html.replace('data-service="Custom Plushies">Plan a project</a>', 'data-service="Custom Plushies">Plan a project</a> <a class="showcase-link" href="/custom-plushies.html">View the plushies showcase</a>')
html = html.replace('/assets/brand-universe.jpeg', '/assets/velunova-banner.webp')
html = html.replace('<title>Velunova Creative Studio | Digital Marketing, Branding &amp; Design</title>', '<title>Velunova Creative Studio | Custom Plushies, Characters &amp; Illustration</title>')
html = html.replace('<title>Velunova Creative Studio | Digital Marketing, Branding & Design</title>', '<title>Velunova Creative Studio | Custom Plushies, Characters &amp; Illustration</title>')
html = html.replace('Make your brand impossible to overlook. Velunova brings digital marketing, social media, SEO, branding, web design and imaginative creative production together.', 'Where imagination takes shape. Explore custom plushies, character artwork, 2D/3D models, illustrations, collectibles and personalized creations from Velunova.')
html = html.replace('Creative thinking. Digital impact. Discover social media, SEO, digital campaigns, branding and web design with Velunova.', 'Bring your ideas to life through custom plushies, character artwork, 2D/3D models, illustrations and collectibles.')
html = html.replace('Digital marketing, branding, web design and imaginative creative production.', 'Custom plushies, character artwork, 2D/3D models, illustrations and collectibles.')
html = html.replace('https://velunova-creative-studio.chalkymyrtle8.chatgpt.site', 'https://velunova.vercel.app')
html = html.replace('/assets/celestial-hero.webp', '/assets/velunova-banner.webp').replace('Velunova\'s sculptural lavender planet and celestial brand world', 'Velunova Creative Studio illustrated character and plushie world').replace('content="1280"', 'content="1536"').replace('content="853"', 'content="1024"')
html = html.replace('A creative studio bringing together digital marketing, social media, SEO, branding, web design, illustration and custom creative production.', 'A creative studio making custom plushies, character artwork, 2D/3D models, illustrations, collectibles and personalized creations.')
html = html.replace('"knowsAbout":["Digital marketing","Social media marketing","Search engine optimization","Brand identity","Web design","Character artwork","Illustration","2D and 3D modeling","Custom plushies","Collectibles"]', '"knowsAbout":["Custom plushies","Character artwork","2D/3D models","Illustrations","Collectibles","Personalized creative commissions"]')
html = html.replace('Strategy with purpose', 'Characters with personality').replace('Design with personality', 'Made around you').replace('Marketing that connects', 'Ideas brought to life')
html = html.replace('Velunova is where imaginative ideas meet thoughtful execution. We bring the personality of a creative studio to the purpose of digital marketing.', 'Velunova is where imaginative ideas meet thoughtful craft. From a character on paper to a plush companion, we create work with personality and purpose.')
html = html.replace("Whether you're finding your brand's voice, building a digital presence, or bringing a character to life, we shape the work around what makes you, you.", "Whether you're imagining a new character, commissioning an illustration, or creating a collectible, we shape the work around what makes your idea special.")
html = html.replace('We start with your business, your audience, and the goals that matter.', 'We start with your character, your inspiration, and the details that matter.')
html = html.replace('Strategy gives the creative direction. Together, we refine the concepts, the message, and the plan.', 'Your brief gives the creative direction. Together, we refine the look, the details, and the plan.')
html = html.replace('A bright idea? A big ambition? Put it into words and take the first step toward bringing it to life.', 'A favorite character? A one-of-a-kind gift? Put your idea into words and take the first step toward bringing it to life.')
html = html.replace('A little about your brand, your goals, and what you have in mind…', 'Tell us about your character, your inspiration, and what you have in mind…')
html = re.sub(r'<details><summary>Can you guarantee a particular search ranking\?.*?</details>', '<details><summary>Can I turn my own character into a plushie?<span class="expand" aria-hidden="true"></span></summary><p>Yes. Bring your original artwork or a character you have permission to use. Visit our <a href="/custom-plushies.html">custom plushies showcase</a> to explore the possibilities and creation process.</p></details>', html)
footer_start = html.index('  <footer')
footer_end = html.index('</footer>', footer_start) + len('</footer>')
footer = '''  <footer class="site-footer container"><div class="footer-top"><a class="brand" href="/" aria-label="Velunova Creative Studio home"><img src="/assets/velunova-logo.webp" alt="Velunova Creative Studio" width="210" height="82" loading="lazy"></a><p>Where imagination<br>takes shape.</p><nav aria-label="Footer navigation"><a href="/#services">What we do</a><a href="/custom-plushies.html">Plushies showcase</a><a href="/#project">Plan a project</a></nav></div><div class="footer-bottom"><p>© <span id="year">2026</span> Velunova Creative Studio.</p><p>Dream it. Create it. Cherish it.</p><button class="privacy-button" type="button" data-privacy>Privacy</button></div><p class="developer-credit">Developed by <a href="https://www.invortechdigitalsolutions.com/" target="_blank" rel="noopener noreferrer">Invortech Digital Solutions</a></p></footer>'''
html = html[:footer_start] + footer + html[footer_end:]
html = html.replace('<link rel="stylesheet" href="/styles.css">', '<link rel="stylesheet" href="/styles.css">\n  <link rel="stylesheet" href="/experience.css">')
page.write_text(html, encoding='utf-8')

# Share navigation and privacy behavior across both pages.
app_path = root / 'app.js'
app = app_path.read_text(encoding='utf-8')
start = app.index('const menuButton')
end = app.index('const projects')
shared = app[start:end]
dialog_start = app.index("document.querySelectorAll('dialog')")
dialog_end = app.index("document.querySelectorAll('[data-service]", dialog_start)
shared += app[dialog_start:dialog_end]
privacy = "document.querySelector('[data-privacy]').addEventListener('click', () => document.querySelector('#privacy-dialog').showModal());"
shared += privacy + '\n'
(root / 'site.js').write_text(shared, encoding='utf-8')
app = app[:start] + app[end:dialog_start] + app[dialog_end:]
app = "import './site.js';\n" + app.replace(privacy, '')
app += '''
const requestedService = new URLSearchParams(window.location.search).get('service');
if ([...serviceField.options].some(option => option.value === requestedService)) {
  serviceField.value = requestedService;
}
'''
app_path.write_text(app, encoding='utf-8')

header = html[html.index('  <header'):html.index('</header>')+len('</header>')]
header = header.replace('href="#"', 'href="/"').replace('href="#services"', 'href="/#services"').replace('href="#work"', 'href="#showcase"').replace('Creative world</a>', 'Showcase</a>').replace('href="#studio"', 'href="/#studio"').replace('href="#project"', 'href="/?service=Custom%20Plushies#project"')
privacy_dialog = html[html.index('  <dialog id="privacy-dialog"'):html.index('</dialog>', html.index('  <dialog id="privacy-dialog"'))+len('</dialog>')]
showcase = '''<!doctype html>
<html lang="en"><head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#171021">
  <title>Custom Character Plushies Showcase | Velunova Creative Studio</title>
  <meta name="description" content="Explore Velunova's custom character plushies: original characters, childhood drawings, gaming avatars and meaningful gifts. See the ideas and the creation process.">
  <link rel="canonical" href="https://velunova.vercel.app/custom-plushies.html">
  <meta property="og:type" content="website"><meta property="og:title" content="Custom Character Plushies | Velunova"><meta property="og:description" content="Your drawing. Your character. Your very own plush companion."><meta property="og:url" content="https://velunova.vercel.app/custom-plushies.html"><meta property="og:image" content="https://velunova.vercel.app/assets/plushies/workshop.webp"><meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/outfit-latin.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/experience.css">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Custom Character Plushies Showcase","url":"https://velunova.vercel.app/custom-plushies.html","description":"Custom plushie concepts and the Velunova creation process.","isPartOf":{"@type":"WebSite","name":"Velunova Creative Studio","url":"https://velunova.vercel.app/"}}</script>
  <script type="module" src="/site.js"></script>
</head><body><a class="skip-link" href="#main">Skip to content</a>
HEADER
<main id="main">
  <section class="plush-intro container" aria-labelledby="plush-heading">
    <a class="breadcrumb" href="/#services">Velunova / Our services / Custom Plushies</a>
    <div class="plush-intro-copy"><p class="eyebrow">Little characters. Big personality.</p><h1 id="plush-heading">From a spark of imagination<br>to <span>someone to hold.</span></h1><p>Your drawing. Your character. Your very own plush companion. Explore a softer side of the Velunova world.</p><a class="button" href="/?service=Custom%20Plushies#project">Plan your custom plushie</a></div>
    <figure class="workshop-image"><img src="/assets/plushies/workshop.webp" alt="Mint, lavender and blue plush characters beside their original sketches in a sunlit workshop" width="1440" height="779" fetchpriority="high"><figcaption>Custom plushie concepts from the Velunova collection.</figcaption></figure>
  </section>
  <section class="showcase-section section" id="showcase" aria-labelledby="showcase-heading"><div class="container"><div class="showcase-heading"><p class="eyebrow">A character for every kind of story</p><h2 id="showcase-heading">Uniquely yours.<br><span>Unmistakably lovable.</span></h2><p>Childhood drawings, original characters, gaming avatars, and thoughtful gifts. Every idea has a different personality.</p></div><div class="plush-gallery">
'''.replace('HEADER', header)
cards = [('childhood','A little drawing. A lasting friend.','For kids & parents','A colorful character plush with a scarf, inspired by childhood artwork','Turn a treasured drawing into a keepsake full of personality.'),('gamer','Your avatar, off screen.','For gamer communities','A teal-haired plush character with headphones and a game controller','Bring an original avatar, guild mascot, or tabletop character into your world.'),('original-character','An original, in every sense.','For character creators','A purple cat-like plush with dark ears and a lavender outfit','Give your own character a soft new dimension.'),('creator','Made for your creative world.','For artists & creators','An artist plush holding a paint palette and brush','Explore character collections and plush concepts for your community.'),('gift','A gift that says “I know you.”','For someone special','A smiling silver-haired plush wearing a dark outfit','A personal idea for birthdays, milestones, and meaningful surprises.')]
for name,title,label,alt,desc in cards:
    showcase += f'<article class="plush-card"><div class="plush-card-image"><img src="/assets/plushies/{name}.webp" alt="{alt}" width="285" height="285" loading="lazy"></div><p class="eyebrow">{label}</p><h3>{title}</h3><p>{desc}</p></article>\n'
showcase += '''</div><p class="showcase-note">Illustrative plush concepts supplied in the studio presentation. Your design, materials, dimensions, timeline, and delivery details are agreed for your individual project.</p></div></section>
  <section class="section container" aria-labelledby="plush-process-heading"><div class="showcase-heading"><p class="eyebrow">From idea to companion</p><h2 id="plush-process-heading">A little care.<br><span>At every stitch.</span></h2><p>A collaborative journey from your first reference to your finished creation.</p></div><div class="plush-process">
'''
steps = [('artwork','Share your artwork','Start with your original drawing, digital artwork, or a character reference you have permission to use.'),('preview','Shape the design','Explore a plush design preview, including proportions, colors, textures, and character details.'),('approval','Make it yours','Review the design together, discuss adjustments, and approve the direction before production.'),('shipping','Bring it home','Confirm the materials and delivery arrangements for your project, then let your companion begin its journey.')]
for name,title,desc in steps:
    showcase += f'<article><img src="/assets/plushies/{name}.webp" alt="{title} — custom plushie creation concept" width="466" height="262" loading="lazy"><h3>{title}</h3><p>{desc}</p></article>\n'
showcase += '''</div></section>
  <section class="plush-outro container"><div><p class="eyebrow">Your next little companion</p><h2>A character in mind?<br><span>Let's meet them.</span></h2><p>Tell us about your character, the details you love, and the occasion you have in mind.</p><a class="button" href="/?service=Custom%20Plushies#project">Start a plushie project</a><p class="rights-note">Bring your own original design, or artwork you have permission to use. For licensed characters, include the relevant permissions with your brief.</p></div><img src="/assets/plushies/collection.webp" alt="A collection of character plushies with colorful outfits in a bright seaside studio" width="1442" height="776" loading="lazy"></section>
</main>
'''
showcase += footer + '\n' + privacy_dialog + '\n</body></html>\n'
(root / 'custom-plushies.html').write_text(showcase, encoding='utf-8')

css = (root / 'styles.css').read_text(encoding='utf-8')
# Remove the replaced orbital hero's unused styles, keeping the specialties strip.
css = re.sub(r'[^{}]*\.(?:hero|tiny-star|circle-play|art-caption|orbital-stamp)[^{}]*\{[^{}]*\}', '', css)
(root / 'styles.css').write_text(css, encoding='utf-8')
sitemap = (root/'sitemap.xml').read_text(encoding='utf-8').replace('https://velunova-creative-studio.chalkymyrtle8.chatgpt.site','https://velunova.vercel.app')
sitemap = sitemap.replace('</urlset>', '<url><loc>https://velunova.vercel.app/custom-plushies.html</loc></url></urlset>')
(root/'sitemap.xml').write_text(sitemap, encoding='utf-8')
robots = (root/'robots.txt').read_text().replace('https://velunova-creative-studio.chalkymyrtle8.chatgpt.site','https://velunova.vercel.app')
(root/'robots.txt').write_text(robots)
