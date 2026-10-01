#!/usr/bin/env python3
"""Post-sync checks: frontmatter names, relative links, stray artifacts.

Exits 1 when any problem is found.
"""
import pathlib
import re
import subprocess

here = pathlib.Path(__file__).resolve().parent
root = pathlib.Path(subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'], cwd=here, text=True).strip())
skip = {'.git', 'node_modules', '.claude'}
ok = True

# Frontmatter names must match their directories.
for p in sorted((root / '.agents/skills').glob('*/SKILL.md')):
    fm = re.match(r'\A---\s*\n(.*?)\n---(?:\n|$)', p.read_text(), re.DOTALL)
    if not fm:
        print(f'NO FRONTMATTER: {p.relative_to(root)}'); ok = False; continue
    name = re.search(r'^name:\s*(\S+)', fm.group(1), re.M)
    if not name or name.group(1) != p.parent.name:
        print(f'NAME MISMATCH: {p.relative_to(root)}'); ok = False
print('frontmatter ok' if ok else 'frontmatter problems above')

# Relative links must resolve.
bad = []
for doc in root.rglob('*.md'):
    if skip & set(doc.relative_to(root).parts):
        continue
    for n, line in enumerate(doc.read_text().splitlines(), 1):
        for raw in re.findall(r'\]\(([^)]+)\)', line):
            if '://' in raw or raw.startswith(('#', 'mailto:')):
                continue
            rel = raw.split('#')[0].strip('<>')
            if rel and not (doc.parent / rel).resolve().exists():
                bad.append(f'{doc.relative_to(root)}:{n} -> {raw}')
print(f'dangling links: {len(bad)}')
for b in bad:
    print(' ', b)

# No stray artifacts.
stray = [p for p in (root / '.agents').rglob('*')
         if p.name in ('.DS_Store', '__pycache__')]
print(f'stray artifacts: {len(stray)}')
for s in stray:
    print(' ', s.relative_to(root))

raise SystemExit(0 if ok and not bad and not stray else 1)
