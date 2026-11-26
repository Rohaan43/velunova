'use client';
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
  return <form id="project-form" ref={formRef} onSubmit={submit}><div className="form-row"><div className="field"><label htmlFor="name">{"Your name "}<span aria-hidden="true">{"*"}</span></label><input id="name" name="name" autoComplete="name" placeholder="Alex Morgan" required maxLength="100" /></div><div className="field"><label htmlFor="email">{"Email address "}<span aria-hidden="true">{"*"}</span></label><input id="email" name="email" type="email" autoComplete="email" placeholder="you@yourcompany.com" required maxLength="254" /></div></div><div className="field"><label htmlFor="service">{"What can we help with? "}<span aria-hidden="true">{"*"}</span></label><select id="service" name="service" required defaultValue=""><option value="">{"Choose a service"}</option><option>{"Custom Plushies"}</option><option>{"Character Artwork"}</option><option>{"2D/3D Models"}</option><option>{"Illustrations"}</option><option>{"Collectibles"}</option><option>{"& More!"}</option></select></div><div className="field"><label htmlFor="message">{"Tell us about your idea "}<span aria-hidden="true">{"*"}</span></label><textarea id="message" name="message" rows="3" placeholder="Tell us about your character, your inspiration, and what you have in mind…" required minLength="20" maxLength="5000" aria-describedby="message-hint"></textarea><span className="field-hint" id="message-hint">{"At least 20 characters. Include your timeline if you have one."}</span></div><button className="button" type="submit">{"Download brief "}<span aria-hidden="true">{"↓"}</span></button><p className="form-privacy">{"Your details stay on your device. This downloads a brief; it does not send an inquiry."}</p><noscript><p>{"Enable JavaScript to download a brief, or copy your answers into a document to share with the studio."}</p></noscript><p id="form-status" role="status">{status}</p></form>;
}
