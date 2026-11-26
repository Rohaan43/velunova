import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile, access} from 'node:fs/promises';
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
  const html = await readFile('dist/index.html', 'utf8');
  for (const [,path] of html.matchAll(/(?:src|href)="(\/[^"#]+)"/g)) await access(resolve('dist', '.' + path));
  for (const [,id] of html.matchAll(/href="#([^"]+)"/g)) assert.ok(html.includes(`id="${id}"`), `Missing section: ${id}`);
  assert.equal([...html.matchAll(/<h1[\s>]/g)].length, 1);
  const metadata = JSON.parse(html.match(/<script type="application\/ld\+json">\s*([\s\S]+?)\s*<\/script>/)[1]);
  assert.equal(metadata.name, 'Velunova Creative Studio');
  assert.equal(metadata['@type'], 'ProfessionalService');
});
