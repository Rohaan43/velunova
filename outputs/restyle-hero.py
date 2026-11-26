from pathlib import Path
import re

path = Path('dist/experience.css')
css = path.read_text(encoding='utf-8')
rest = css[css.index('.service-body .showcase-link'):]
# Replace the old hero's breakpoint rules along with its main styles.
rest = re.sub(r'[^{}]*\.(?:banner-|motion-toggle)[^{}]*\{[^{}]*\}', '', rest)
hero = '''.home-page .site-header{position:absolute;inset:18px 0 auto;border:0}
.home-page .header-inner{position:relative;display:flex;align-items:center;min-height:66px;width:min(1040px,calc(100% - 80px));padding:8px 28px;border:1px solid #ffffffa6;border-radius:100px;background:#fff9ffe8;box-shadow:0 5px 22px #553c6420;backdrop-filter:blur(18px)}
.home-page .site-header .brand{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:146px}
.home-page .site-header .brand img{height:54px;filter:brightness(0);opacity:.86}
.home-page .site-header nav{display:flex;width:100%;gap:26px;color:#38283f;font-size:14px}
.home-page .site-header nav>a:not(.button){color:#52425a}
.home-page .site-header nav>a:hover{color:#7f4393}
.home-page .site-header nav>a:first-child{margin-left:0}
.home-page .site-header nav>a:nth-child(3){margin-left:auto}
.home-page .site-header nav .button{margin:0;background:none;color:#38283f;border:0;padding:10px 0;box-shadow:none}
.home-page .site-header nav .button span{display:none}
.banner-hero{background:#eacbf1}
.banner-stage{position:relative;isolation:isolate;min-height:720px;height:min(100svh,1000px);overflow:hidden}
.banner-art{position:absolute;inset:0;display:block;z-index:-2;animation:banner-breathe 14s ease-in-out infinite alternate}
.banner-art img{width:100%;height:100%;object-fit:cover;object-position:center bottom}
.banner-stage::before{content:'';position:absolute;inset:0;z-index:-1;pointer-events:none;background:linear-gradient(180deg,#f5e8f614,transparent 65%)}
.banner-atmosphere{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:1}
.banner-atmosphere::before,.banner-atmosphere::after{content:'';position:absolute;pointer-events:none}
.banner-atmosphere::before{width:70%;height:25%;left:15%;bottom:5%;border-radius:50%;background:radial-gradient(ellipse,#ffe6f338,transparent 70%);animation:cloud-drift 10s ease-in-out infinite alternate}
.banner-atmosphere::after{width:100px;height:1px;top:20%;left:75%;background:linear-gradient(90deg,transparent,#fff6e9);box-shadow:0 0 8px #fff0dc;opacity:0;animation:shooting-star 14s ease-in-out 4s infinite}
.banner-stars{position:absolute;inset:0;pointer-events:none;z-index:1}
.banner-stars i{position:absolute;left:var(--x);top:var(--y);color:#fff9ef;font-size:var(--size);font-style:normal;line-height:1;text-shadow:0 0 10px #fce8e1;animation:star-glimmer 4s ease-in-out var(--delay) infinite alternate}
.banner-copy{position:relative;z-index:2;text-align:center;width:min(860px,calc(100% - 48px));margin-inline:auto;padding-top:clamp(140px,17vh,180px)}
.banner-copy h1{font-size:clamp(44px,4.4vw,68px);font-weight:600;line-height:1.08;letter-spacing:-.045em;color:#261a36;text-wrap:balance}
.banner-copy p{max-width:670px;margin:24px auto 0;font-size:17px;line-height:1.6;color:#42314f;text-wrap:pretty}
.banner-actions{display:flex;justify-content:center;margin-top:30px}
.banner-actions .button{min-width:224px;padding:16px 28px;font-size:16px;background:#281b3c;border:1px solid #fff8ffb3;color:#fff4fc;box-shadow:0 0 0 5px #fff6ff47,0 10px 24px #734a8120}
.banner-actions .button:hover{background:#432b5d;box-shadow:0 0 0 5px #fff6ff80,0 12px 28px #734a8130}
.motion-toggle{position:absolute;z-index:3;right:24px;bottom:20px;display:flex;align-items:center;gap:8px;padding:8px 12px;border:1px solid #ffffff80;border-radius:100px;background:#fff3ffe3;color:#40284e;font-size:12px;cursor:pointer;backdrop-filter:blur(8px)}
.motion-toggle input{accent-color:#67457b;width:15px;height:15px;margin:0;padding:0}
.banner-stage:has(#pause-animation:checked) *,.banner-stage:has(#pause-animation:checked) *::before,.banner-stage:has(#pause-animation:checked) *::after{animation-play-state:paused}
@keyframes banner-breathe{from{transform:scale(1.005) translateY(0)}to{transform:scale(1.018) translateY(-3px)}}
@keyframes cloud-drift{from{transform:translateX(-4%) scale(.95);opacity:.4}to{transform:translateX(4%) scale(1.1);opacity:1}}
@keyframes star-glimmer{from{opacity:.2;transform:scale(.65) rotate(-15deg)}to{opacity:.95;transform:scale(1.15) rotate(15deg)}}
@keyframes shooting-star{0%,80%,100%{opacity:0;transform:translate(0,0) rotate(-35deg)}85%{opacity:.8}95%{opacity:0;transform:translate(180px,100px) rotate(-35deg)}}
@media(max-width:1000px) and (min-width:768px){.home-page .header-inner{padding-inline:22px}.home-page .site-header nav{gap:18px;font-size:13px}.home-page .site-header .brand{width:130px}.home-page .site-header nav .button{font-size:13px}}
@media(max-width:767px){.home-page .site-header{top:14px}.home-page .header-inner{width:calc(100% - 32px);min-height:64px;padding:8px 16px;justify-content:flex-end}.home-page .site-header .brand{width:134px}.home-page .menu-toggle{border-color:#40284e33;color:#40284e}.home-page .menu-toggle>span:not(.sr-only){background:#40284e}.home-page .site-header nav{display:none;top:74px;left:0;right:0;width:100%;padding:22px;border:1px solid #ffffffa6;border-radius:22px;background:#fff4ff;box-shadow:0 12px 30px #553c6433}.home-page .site-header nav.is-open{display:flex;align-items:stretch;gap:12px}.home-page .site-header nav>a:nth-child(3){margin-left:0}.home-page .site-header nav .button{padding:12px 0}.banner-stage{min-height:690px;height:100svh;max-height:840px;background:radial-gradient(ellipse at 50% 30%,#fff1f9 0,#f5d9f4 38%,#dec0f2 100%)}.banner-art{inset:auto 0 0;height:auto;mask-image:linear-gradient(to bottom,transparent,#000 20%)}.banner-art img{height:auto;object-fit:contain}.banner-copy{width:calc(100% - 40px);padding-top:135px}.banner-copy h1{font-size:clamp(36px,9.2vw,52px);line-height:1.1}.banner-copy p{font-size:16px;max-width:440px;margin-top:22px}.banner-actions{margin-top:28px}.banner-actions .button{min-width:210px;font-size:15px;padding:15px 24px}.motion-toggle{right:12px;bottom:12px;font-size:11px;padding:6px 9px}.banner-stars i{font-size:calc(var(--size)*.75)}}
@media(max-width:380px){.banner-copy{padding-top:125px}.banner-copy h1{font-size:34px}.banner-copy p{font-size:15px}.banner-actions{margin-top:24px}}
@media(prefers-reduced-motion:reduce){.motion-toggle{display:none}.banner-art,.banner-stars i,.banner-atmosphere::before,.banner-atmosphere::after{animation:none}.banner-atmosphere::after{display:none}}
'''
path.write_text(hero+rest,encoding='utf-8')
