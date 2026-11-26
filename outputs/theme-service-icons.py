from pathlib import Path

path = Path('dist/index.html')
html = path.read_text(encoding='utf-8')
icons = {
    '🧸': '<path d="M10.5 12.5C4 13 2 5 8 3c4-1 7 2 6 5a15 15 0 0 1 12 0c-1-4 3-7 7-4 5 4 2 10-3.5 8.5C37 19 35 29 28 33c-5 3-11 3-16 0-7-4-9-14-1.5-20.5Z"/><circle cx="14" cy="20" r="1" fill="currentColor"/><circle cx="26" cy="20" r="1" fill="currentColor"/><ellipse cx="20" cy="27" rx="6" ry="4.5"/><path d="m18 25 2 2 2-2M20 27v3"/>',
    '🎨': '<path d="M20 4C11 4 4 11 4 20s6 15 13 15c4 0 6-3 4-6-1-2 0-4 3-4h3c6 0 9-4 9-9C36 9 29 4 20 4Z"/><circle cx="12" cy="16" r="2"/><circle cx="18" cy="11" r="2"/><circle cx="27" cy="12" r="2"/><path d="m15 31 13-13 3 3-13 13M15 31c-4-1-6 1-6 5 4 0 7-1 9-2"/>',
    '🖼️': '<rect x="4" y="4" width="32" height="32" rx="2"/><rect x="8" y="8" width="24" height="24" rx="1"/><circle cx="15" cy="15" r="3"/><path d="m8 28 8-8 7 7 4-4 5 5"/>',
    '♛': '<path d="m5 12 8 7 7-12 7 12 8-7-4 19H9L5 12ZM9 36h22"/><circle cx="5" cy="10" r="2"/><circle cx="20" cy="5" r="2"/><circle cx="35" cy="10" r="2"/>',
    '🎁': '<rect x="5" y="12" width="30" height="7" rx="1"/><path d="M8 19v17h24V19M20 12v24M20 12C8 13 7 3 13 3c4 0 7 9 7 9ZM20 12C32 13 33 3 27 3c-4 0-7 9-7 9Z"/>',
}
for symbol, shapes in icons.items():
    old = f'<span class="service-icon" aria-hidden="true">{symbol}</span>'
    assert html.count(old) == 1, f'Missing service icon: {symbol}'
    html = html.replace(old, f'<span class="service-icon" aria-hidden="true"><svg viewBox="0 0 40 40" focusable="false">{shapes}</svg></span>')
html = html.replace('<svg viewBox="0 0 40 40"><path', '<svg viewBox="0 0 40 40" focusable="false"><path')
path.write_text(html, encoding='utf-8')

path = Path('dist/styles.css')
css = path.read_text(encoding='utf-8')
css = css.replace(".service-icon{font-size:36px;line-height:1;color:var(--accent);text-align:center;font-family:'Segoe UI Symbol',sans-serif}", '.service-icon{display:grid;place-items:center;color:var(--accent)}')
css = css.replace('.service-icon svg{width:36px;height:36px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linejoin:round}', '.service-icon svg{display:block;width:36px;height:36px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}')
path.write_text(css, encoding='utf-8')
