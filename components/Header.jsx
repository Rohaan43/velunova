'use client';
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
  return (<header ref={headerRef} className="site-header">{"\n    "}<div className="container header-inner">{"\n      "}<a className="brand" href="/" aria-label="Velunova Creative Studio home"><img src="/assets/velunova-logo.webp" alt="Velunova Creative Studio" width="210" height="82" fetchPriority="high" /></a>{"\n      "}<button className="menu-toggle" type="button" aria-expanded={open} onClick={() => setOpen(!open)} aria-controls="navigation"><span></span><span></span><span className="sr-only">{"Toggle navigation"}</span></button>{"\n      "}<nav id="navigation" className={open ? "is-open" : ""} onClick={() => setOpen(false)} aria-label="Main navigation">{"\n        "}<a href="/#services">{"What we do"}</a><a href="/custom-plushies">{"Showcase"}</a><a href="/#studio">{"The studio"}</a>{"\n        "}<a className="button button-small" href={showcase ? "/?service=Custom%20Plushies#project" : "/#project"}>{"Plan a project "}<span aria-hidden="true">{"✦"}</span></a>{"\n      "}</nav>{"\n    "}</div>{"\n  "}</header>);
}
