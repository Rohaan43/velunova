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
  function openGmail(event) {
    const form = formRef.current;
    const values = Object.fromEntries(new FormData(form));
    if (values.name?.trim() || values.message?.trim() || values.service) {
      event.preventDefault();
      const subject = encodeURIComponent(`Velunova Project Brief — ${values.service || 'General Inquiry'}`);
      const body = encodeURIComponent(createBrief(values));
      window.open(`https://mail.google.com/mail/?view=cm&fs=1&to=info@velunova.digital&su=${subject}&body=${body}`, '_blank', 'noopener,noreferrer');
    }
    setStatus('Opening Gmail to send your message to info@velunova.digital.');
  }
  return <form id="project-form" ref={formRef} onSubmit={event => event.preventDefault()}><div className="form-row"><div className="field"><label htmlFor="name">{"Your name "}<span aria-hidden="true">{"*"}</span></label><input id="name" name="name" autoComplete="name" placeholder="Alex Morgan" required maxLength="100" /></div><div className="field"><label htmlFor="email">{"Email address "}<span aria-hidden="true">{"*"}</span></label><input id="email" name="email" type="email" autoComplete="email" placeholder="you@yourcompany.com" required maxLength="254" /></div></div><div className="field"><label htmlFor="service">{"What can we help with? "}<span aria-hidden="true">{"*"}</span></label><select id="service" name="service" required defaultValue=""><option value="">{"Choose a service"}</option><option>{"Custom Plushies"}</option><option>{"Character Artwork & Illustration"}</option><option>{"Miniature Collectibles & 2D/3D Models"}</option><option>{"Character & D&D Custom Designs"}</option><option>{"Furry Character Arts"}</option><option>{"Conceptual Artworks"}</option><option>{"Furry Suits & Costumes"}</option><option>{"& More!"}</option></select></div><div className="field"><label htmlFor="message">{"Tell us about your idea "}<span aria-hidden="true">{"*"}</span></label><textarea id="message" name="message" rows="3" placeholder="Tell us about your character, your inspiration, and what you have in mind…" required minLength="20" maxLength="5000" aria-describedby="message-hint"></textarea><span className="field-hint" id="message-hint">{"At least 20 characters. Include your timeline if you have one."}</span></div><a className="button" href="https://mail.google.com/mail/?view=cm&fs=1&to=info@velunova.digital" target="_blank" rel="noopener noreferrer" onClick={openGmail}>{"Contact us"}</a><p className="form-privacy">{"Your details stay on your device until you send your email to info@velunova.digital."}</p><noscript><p>{"Enable JavaScript to prepare your brief, or email us directly at info@velunova.digital."}</p></noscript><p id="form-status" role="status">{status}</p></form>;
}
