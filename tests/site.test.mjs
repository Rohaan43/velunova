import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile, access, readdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createBrief} from '../dist/brief.js';

test('project brief preserves customer content and explains delivery', () => {
  const brief = createBrief({name:'  Alex  ',email:'alex@example.com',service:'Brand identity & design',message:'  Launch our new café with a memorable identity.  '});
  assert.ok(brief.includes('Name: Alex\n'));
  assert.ok(brief.includes('Email: alex@example.com'));
  assert.ok(brief.includes('Launch our new café with a memorable identity.'));
  assert.ok(brief.includes('has not been sent to the studio'));
});
test('all local page assets and fragment links resolve', async () => {
  const pages = (await readdir('dist')).filter(file => file.endsWith('.html'));
  for (const page of pages) {
    const html = await readFile(`dist/${page}`, 'utf8');
    for (const [,path] of html.matchAll(/(?:src|href)="([^"]+)"/g)) {
      const url = new URL(path, `https://velunova.vercel.app/${page}`);
      if (url.origin !== 'https://velunova.vercel.app') continue;
      const file = resolve('dist', '.' + (url.pathname === '/' ? '/index.html' : url.pathname));
      await access(file);
      if (url.hash) assert.ok((await readFile(file, 'utf8')).includes(`id="${url.hash.slice(1)}"`), `Missing section: ${url.href}`);
    }
    assert.equal([...html.matchAll(/<h1[\s>]/g)].length, 1, `${page} needs one main heading`);
    const metadata = JSON.parse(html.match(/<script type="application\/ld\+json">\s*([\s\S]+?)\s*<\/script>/)[1]);
    assert.ok(metadata.name);
    assert.equal(metadata['@type'], page === 'index.html' ? 'ProfessionalService' : 'CollectionPage');
    const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
    assert.equal(new Set(ids).size, ids.length, `Duplicate IDs in ${page}`);
  }
});
