from pathlib import Path
from html.parser import HTMLParser
import json, re, shutil

root = Path.cwd().resolve()
app = root / 'app'
components = root / 'components'
lib = root / 'lib'
public = root / 'public'
for p in [app, app/'custom-plushies', components, lib, public]: p.mkdir(parents=True, exist_ok=True)
home = (root/'dist/index.html').read_text(encoding='utf-8')
plush = (root/'dist/custom-plushies.html').read_text(encoding='utf-8')
source_app = (root/'dist/app.js').read_text(encoding='utf-8')

class JSX(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.result=[]
    def handle_starttag(self, tag, attrs):
        names={'class':'className','for':'htmlFor','tabindex':'tabIndex','fetchpriority':'fetchPriority','srcset':'srcSet','maxlength':'maxLength','minlength':'minLength','autocomplete':'autoComplete','viewbox':'viewBox','stroke-width':'strokeWidth','stroke-linecap':'strokeLinecap','stroke-linejoin':'strokeLinejoin'}
        out='<'+tag
        for key,val in attrs:
            key=names.get(key,key)
            if val is None: out+=' '+key; continue
            if key=='style':
                styles=dict(x.strip().split(':',1) for x in val.split(';') if x.strip())
                out+=' style={'+json.dumps(styles)+'}'
            else: out+=' '+key+'='+json.dumps(val.replace('/custom-plushies.html','/custom-plushies'),ensure_ascii=False)
        if tag=='select': out+=' defaultValue=""'
        self.result.append(out+(' />' if tag in ['img','input','br','source','meta','link','hr'] else '>'))
    def handle_endtag(self,tag):
        if tag not in ['img','input','br','source','meta','link','hr']: self.result.append('</'+tag+'>')
    def handle_data(self,data): self.result.append('{'+json.dumps(data,ensure_ascii=False)+'}')

def jsx(html):
    p=JSX();p.feed(html);return ''.join(p.result)
def write(path,data): path.write_text(data,encoding='utf-8')
def section(html,tag): return re.search(fr'<{tag}\b.*?</{tag}>',html,re.S).group()

header=jsx(section(home,'header'))
header=header.replace('<header className=', '<header ref={headerRef} className=')
header=header.replace('aria-expanded="false"', 'aria-expanded={open} onClick={() => setOpen(!open)}')
header=header.replace('id="navigation"', 'id="navigation" className={open ? "is-open" : ""} onClick={() => setOpen(false)}')
header=header.replace('href="#"','href="/"').replace('href="#services"','href="/#services"').replace('href="#studio"','href="/#studio"').replace('href="#project"','href={showcase ? "/?service=Custom%20Plushies#project" : "/#project"}')
write(components/'Header.jsx', ''''use client';
import { useEffect, useRef, useState } from 'react';
export default function Header({ showcase = false }) {
  const [open, setOpen] = useState(false);
  const headerRef = useRef(null);
  useEffect(() => {
    const onKey = event => { if (event.key === 'Escape') { setOpen(false); if (headerRef.current.querySelector('button').getAttribute('aria-expanded') === 'true') headerRef.current.querySelector('button').focus(); } };
    const onOutside = event => { if (!headerRef.current.contains(event.target)) setOpen(false); };
    const media = window.matchMedia('(min-width: 768px)');
    const close = () => setOpen(false);
    document.addEventListener('keydown', onKey);
    document.addEventListener('click', onOutside);
    media.addEventListener('change', close);
    return () => { document.removeEventListener('keydown', onKey); document.removeEventListener('click', onOutside); media.removeEventListener('change', close); };
  }, []);
  return ('''+header+''');
}
''')

privacy=re.search(r'<dialog id="privacy-dialog".*?</dialog>',home,re.S).group()
privacy=jsx(privacy).replace('<dialog ', '<dialog ref={dialogRef} onClick={closeOnBackdrop} ')
privacy=privacy.replace('className="dialog-close"', 'className="dialog-close" onClick={() => dialogRef.current.close()}')
write(components/'Privacy.jsx',''''use client';
import { useRef } from 'react';
export default function Privacy() {
  const dialogRef = useRef(null);
  function closeOnBackdrop(event) {
    const dialog = dialogRef.current;
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  }
  return <><button className="privacy-button" type="button" onClick={() => dialogRef.current.showModal()}>Privacy</button>'''+privacy+'''</>;
}
''')
footer=re.sub(r'<button class="privacy-button".*?</button>', '<Privacy></Privacy>',section(home,'footer'),flags=re.S)
footer=jsx(footer).replace('<privacy></privacy>','<Privacy />')
write(components/'Footer.jsx',"import Privacy from './Privacy';\nexport default function Footer() { return ("+footer+"); }\n")

projects=source_app[source_app.index('const projects ='):source_app.index('const projectDialog')]
write(lib/'projects.js',projects.replace('const projects =','export const projects ='))
write(lib/'brief.js',(root/'dist/brief.js').read_text(encoding='utf-8'))

main=section(home,'main')
form=re.search(r'<form id="project-form".*?</form>',main,re.S).group()
form_children=re.sub(r'^<form[^>]*>|</form>$','',form)
form_children=re.sub(r'<p id="form-status".*?</p>','',form_children,flags=re.S)
main=main.replace(form,'<ProjectForm></ProjectForm>')
grid=re.search(r'<div class="work-grid">.*?</div><p class="work-note">',main,re.S).group()
main=main.replace(grid,'<Gallery>'+grid.replace('</div><p class="work-note">','</div>')+'</Gallery><p class="work-note">')
main=jsx(main).replace('<projectform></projectform>','<ProjectForm />').replace('<gallery>','<Gallery>').replace('</gallery>','</Gallery>')

write(components/'ProjectForm.jsx',''''use client';
import { useEffect, useRef, useState } from 'react';
import { createBrief } from '../lib/brief';
export default function ProjectForm() {
  const formRef = useRef(null);
  const [status, setStatus] = useState('');
  useEffect(() => {
    const select = formRef.current.elements.service;
    const service = new URLSearchParams(window.location.search).get('service');
    if ([...select.options].some(option => option.value === service)) select.value = service;
    const onService = event => { const link = event.target.closest('[data-service]'); if (link && [...select.options].some(option => option.value === link.dataset.service)) select.value = link.dataset.service; };
    document.addEventListener('click', onService);
    return () => document.removeEventListener('click', onService);
  }, []);
  function submit(event) {
    event.preventDefault();
    const form = formRef.current;
    if (!form.reportValidity()) return;
    const values = Object.fromEntries(new FormData(form));
    if (!values.name.trim() || values.message.trim().length < 20) {
      setStatus('Please add your name and at least 20 characters describing your idea.');
      (!values.name.trim() ? form.elements.name : form.elements.message).focus(); return;
    }
    let url;
    try {
      url = URL.createObjectURL(new Blob([createBrief(values)], {type: 'text/plain;charset=utf-8'}));
      const link = document.createElement('a'); link.href = url; link.download = 'velunova-project-brief.txt';
      document.body.append(link); link.click(); link.remove();
      setStatus('Your brief is ready. Share the downloaded file with Velunova through your preferred contact channel.');
    } catch { setStatus('Your browser could not download the brief. You can copy your answers into a document instead.'); }
    finally { if (url) window.setTimeout(() => URL.revokeObjectURL(url), 1000); }
  }
  return <form id="project-form" ref={formRef} onSubmit={submit}>'''+jsx(form_children)+'''<p id="form-status" role="status">{status}</p></form>;
}
''')
write(components/'Gallery.jsx',''''use client';
import { useEffect, useRef, useState } from 'react';
import { projects } from '../lib/projects';
export default function Gallery({ children }) {
  const [project, setProject] = useState(null);
  const dialogRef = useRef(null);
  useEffect(() => { if (project) dialogRef.current.showModal(); }, [project]);
  function close() { dialogRef.current.close(); setProject(null); }
  function backdrop(event) {
    const rect = dialogRef.current.getBoundingClientRect();
    if (event.target === dialogRef.current && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) close();
  }
  return <div onClick={event => { const button = event.target.closest('[data-project]'); if (button && projects[button.dataset.project]) setProject(projects[button.dataset.project]); }}>
    {children}
    <dialog id="project-dialog" ref={dialogRef} aria-labelledby="dialog-title" onCancel={() => setProject(null)} onClick={backdrop}>
      <button className="dialog-close" type="button" aria-label="Close project details" onClick={close}>×</button>
      <p className="eyebrow">{project?.category}</p><h2 id="dialog-title">{project?.title}</h2><p>{project?.description}</p>
      <ul>{project?.deliverables.map(text => <li key={text}>{text}</li>)}</ul>
      <a className="button" href="#project" data-service={project?.service} onClick={close}>Plan a project <span aria-hidden="true">✦</span></a>
    </dialog>
  </div>;
}
''')

def metadata(source):
    title=re.search(r'<title>(.*?)</title>',source).group(1).replace('&amp;','&')
    desc=re.search(r'<meta name="description" content="(.*?)"',source).group(1)
    url=re.search(r'<link rel="canonical" href="(.*?)"',source).group(1).replace('/custom-plushies.html','/custom-plushies')
    image=re.search(r'<meta property="og:image" content="(.*?)"',source).group(1)
    return 'export const metadata = '+json.dumps({'title':title,'description':desc,'alternates':{'canonical':url},'openGraph':{'title':title,'description':desc,'url':url,'images':[image]},'twitter':{'card':'summary_large_image','title':title,'description':desc,'images':[image]}},ensure_ascii=False)+';\n'
def schema(source):
    data=re.search(r'<script type="application/ld\+json">(.*?)</script>',source,re.S).group(1).strip().replace('/custom-plushies.html','/custom-plushies')
    return '<script type="application/ld+json" dangerouslySetInnerHTML={{__html: '+json.dumps(data)+'}} />'

write(app/'page.jsx', "import Header from '../components/Header';\nimport Footer from '../components/Footer';\nimport Gallery from '../components/Gallery';\nimport ProjectForm from '../components/ProjectForm';\n"+metadata(home)+'export default function Home() { return <div className="home-page"><a className="skip-link" href="#main">Skip to content</a><Header />'+schema(home)+main+'<Footer /></div>; }\n')
write(app/'custom-plushies/page.jsx', "import Header from '../../components/Header';\nimport Footer from '../../components/Footer';\n"+metadata(plush)+'export default function Plushies() { return <><a className="skip-link" href="#main">Skip to content</a><Header showcase />'+schema(plush)+jsx(section(plush,'main'))+'<Footer /></>; }\n')
write(app/'layout.jsx', '''import './globals.css';
import './experience.css';
export const viewport = { themeColor: '#171021' };
export const metadata = { metadataBase: new URL('https://velunova.vercel.app'), icons: { icon: '/assets/favicon.svg' } };
export default function RootLayout({ children }) {
  return <html lang="en"><body>{children}</body></html>;
}
''')
shutil.copyfile(root/'dist/styles.css',app/'globals.css')
shutil.copyfile(root/'dist/experience.css',app/'experience.css')
shutil.copytree(root/'dist/assets', public/'assets',dirs_exist_ok=True)
for file in ['robots.txt','sitemap.xml','_headers']:
    write(public/file,(root/'dist'/file).read_text(encoding='utf-8').replace('/custom-plushies.html','/custom-plushies'))
hosting=root/'.openai/hosting.json'
data=json.loads(hosting.read_text());data['static']['directory']='out';write(hosting,json.dumps(data,indent=2)+'\n')
