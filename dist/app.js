import { createBrief } from './brief.js';

const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('is-open');
}
menuButton.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(expanded));
  navigation.classList.toggle('is-open', expanded);
});
navigation.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});
document.addEventListener('click', event => {
  if (!event.target.closest('.site-header')) closeMenu();
});
window.matchMedia('(min-width: 768px)').addEventListener('change', closeMenu);
document.querySelector('#year').textContent = new Date().getFullYear();

const projects = {
  universe: {
    category: 'The Velunova brand universe',
    title: 'A little magic. Entirely Velunova.',
    description: 'The supplied Velunova artwork is the heart of this creative world: a violet night sky, a celestial wordmark, expressive characters, and collectible creations. This is our own brand artwork, presented as a window into the studio’s visual identity.',
    deliverables: ['Celestial visual language and violet brand palette', 'Character artwork and imaginative illustration', 'Custom plushies, collectibles, and 2D/3D possibilities'],
    service: 'Character Artwork'
  },
  campaign: {
    category: 'Illustrative studio concept · Not client work',
    title: 'Made for the next big thing.',
    description: 'An illustrative campaign direction exploring confident typography, a memorable visual motif, and a simple message. A starting point for discussing how campaign creative can reflect your brand and audience.',
    deliverables: ['Campaign message and visual direction', 'Adaptable social media layouts', 'Consistent creative across touchpoints'],
    service: 'Illustrations'
  },
  digital: {
    category: 'Illustrative studio concept · Not client work',
    title: 'A fresh digital perspective.',
    description: 'An imaginary brand concept exploring how a fresh identity can become a focused web experience. This design study pairs expressive forms with clear typography and an approachable interface.',
    deliverables: ['Visual identity direction', 'Website art direction and page composition', 'Responsive experience planning'],
    service: '& More!'
  }
};
const projectDialog = document.querySelector('#project-dialog');
const serviceField = document.querySelector('#service');
document.querySelectorAll('[data-project]').forEach(button => {
  button.addEventListener('click', () => {
    const project = projects[button.dataset.project];
    document.querySelector('#dialog-category').textContent = project.category;
    document.querySelector('#dialog-title').textContent = project.title;
    document.querySelector('#dialog-description').textContent = project.description;
    document.querySelector('#dialog-deliverables').replaceChildren(...project.deliverables.map(text => {
      const item = document.createElement('li');
      item.textContent = text;
      return item;
    }));
    document.querySelector('#dialog-cta').dataset.service = project.service;
    projectDialog.showModal();
  });
});
document.querySelectorAll('dialog').forEach(dialog => {
  dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
});
document.querySelectorAll('[data-service], #dialog-cta').forEach(link => {
  link.addEventListener('click', () => {
    serviceField.value = link.dataset.service;
    if (projectDialog.open) projectDialog.close();
  });
});
document.querySelector('[data-privacy]').addEventListener('click', () => document.querySelector('#privacy-dialog').showModal());

const form = document.querySelector('#project-form');
const status = document.querySelector('#form-status');
form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  // shortcut: briefs download locally; connect a verified business inbox when the studio provides one.
  const values = Object.fromEntries(new FormData(form));
  if (!values.name.trim() || values.message.trim().length < 20) {
    status.textContent = 'Please add your name and at least 20 characters describing your idea.';
    (!values.name.trim() ? form.elements.name : form.elements.message).focus();
    return;
  }
  let url;
  try {
    url = URL.createObjectURL(new Blob([createBrief(values)], {type: 'text/plain;charset=utf-8'}));
    const download = document.createElement('a');
    download.href = url;
    download.download = 'velunova-project-brief.txt';
    document.body.append(download);
    download.click();
    download.remove();
    status.textContent = 'Your brief is ready. Share the downloaded file with Velunova through your preferred contact channel.';
  } catch {
    status.textContent = 'Your browser could not download the brief. You can copy your answers into a document instead.';
  } finally {
    if (url) window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
});
