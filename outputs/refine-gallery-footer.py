from pathlib import Path
import re

for name in ['index.html', 'custom-plushies.html']:
    path = Path('dist') / name
    html = path.read_text(encoding='utf-8').replace('>Developed by <a', '>Powered by <a')
    path.write_text(html, encoding='utf-8')

# Give the shared footer one set of layout rules instead of competing breakpoint overrides.
for name in ['styles.css', 'experience.css']:
    path = Path('dist') / name
    css = path.read_text(encoding='utf-8')
    css = re.sub(r'[^{}]*\.(?:site-footer|footer-top|footer-bottom|developer-credit|privacy-button)[^{}]*\{[^{}]*\}', '', css)
    if name == 'experience.css':
        css = re.sub(r'[^{}]*\.motion-toggle[^{}]*\{[^{}]*\}', '', css)
        css = re.sub(r'[^{}]*:has\(#pause-animation:checked\)[^{}]*\{[^{}]*\}', '', css)
        # Finish decorative movement within five seconds; keep system reduced-motion support.
        css = css.replace('animation:banner-breathe 14s ease-in-out infinite alternate', 'animation:banner-breathe 4s ease-out both')
        css = css.replace('animation:cloud-drift 10s ease-in-out infinite alternate', 'animation:cloud-drift 4s ease-out both')
        css = css.replace('animation:shooting-star 14s ease-in-out 4s infinite', 'animation:shooting-star 4s ease-in-out both')
        css = css.replace('animation:star-glimmer 4s ease-in-out var(--delay) infinite alternate', 'animation:star-glimmer 2s ease-in-out calc(var(--delay)*.25) 2 alternate both')
    path.write_text(css, encoding='utf-8')

footer_css = '''
.site-footer{padding-top:44px}
.footer-top{display:flex;align-items:center;gap:40px;padding-bottom:32px}
.footer-top>p{font-size:14px;line-height:1.6;margin:0}
.footer-top nav{display:flex;align-items:center;justify-content:flex-end;flex-wrap:wrap;gap:12px 26px;margin-left:auto;font-size:14px;color:#d4c4de}
.footer-top nav a{padding-block:8px}
.footer-top nav a:hover{color:var(--accent)}
.footer-bottom{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:20px;border-top:1px solid var(--line);padding-block:22px;color:var(--muted)}
.footer-bottom>p{font-size:14px;line-height:1.6;margin:0}
.footer-bottom>p:nth-child(2){text-align:center}
.privacy-button{justify-self:end;border:0;background:none;padding:10px 0;min-height:44px;color:#d4c4de;font-size:14px}
.privacy-button:hover{text-decoration:underline}
.developer-credit{border-top:1px solid var(--line);padding:20px 0 26px;text-align:center;font-size:14px;line-height:1.7;color:var(--muted)}
.developer-credit a{color:#e0cee9;font-weight:500;text-decoration:underline;text-decoration-color:#d2afea66;text-underline-offset:4px}
.developer-credit a:hover{color:var(--accent)}
.work-feature .universe-art{aspect-ratio:1672/941}
.universe-art picture{display:block;width:100%;height:100%}
.universe-art picture img{width:100%;height:100%;object-fit:cover;object-position:center}
.brand-world-mark{position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);width:31%;text-align:center;pointer-events:none}
.brand-world-mark img{width:100%;height:auto;object-fit:contain;filter:drop-shadow(0 2px 16px #160d21)}
.brand-world-mark>span{display:block;font-size:clamp(10px,1.25vw,17px);line-height:1.5;color:#f8eafb;margin-top:8px;text-shadow:0 2px 8px #170e24}
.universe-art .image-tag{top:18px;bottom:auto}
@media(max-width:1000px){.footer-top{display:flex;flex-direction:column;gap:16px;text-align:center;padding-bottom:24px}.footer-top>p{margin:0}.footer-top nav{width:100%;margin:0;justify-content:center;gap:12px 24px}.footer-bottom{display:flex;flex-direction:column;gap:10px;text-align:center;padding-block:22px}.privacy-button{padding:6px 14px}.developer-credit{padding-block:18px 24px}}
@media(max-width:480px){.footer-top nav{gap:8px 18px;font-size:13px}.footer-bottom>p,.developer-credit{font-size:13px}.brand-world-mark>span{display:none}.universe-art .image-tag{top:10px;left:10px;font-size:10px;padding:5px 10px}}
'''
path = Path('dist/experience.css')
path.write_text(path.read_text(encoding='utf-8') + footer_css, encoding='utf-8')
