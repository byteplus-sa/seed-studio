#!/usr/bin/env python3
"""Scan skill bundles for tool and skill references this prompt-only workspace
does not ship, and for code files a prompt-only skill should not contain.

Usage: leaks.py [--count] [PATH ...]

PATH is a skill directory, a skills directory (every skill inside it except
sync-skills), or a single file. With no PATH, scans this repo's
.agents/skills. The forbidden names live in forbidden-refs.txt beside this
script. Prints one `path:line: [pattern] text` line per hit and exits 1 when
anything is found. With --count, prints only the number of hits and exits 0, so
a plan can preview what an upstream copy would bring in.
"""
import pathlib
import re
import subprocess
import sys

here = pathlib.Path(__file__).resolve().parent
TEXT = {'.md', '.json', '.yaml', '.yml', '.txt'}
CODE = {'.py', '.sh', '.js', '.ts', '.mjs', '.cjs'}
SKIP_PARTS = {'.git', '__pycache__', 'node_modules'}


def load_patterns():
    pats = []
    for raw in (here / 'forbidden-refs.txt').read_text().splitlines():
        line = raw.strip()
        if line and not line.startswith('#'):
            pats.append((line, re.compile(line)))
    return pats


def repo_skills():
    root = pathlib.Path(subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel'], cwd=here, text=True).strip())
    return root / '.agents' / 'skills'


def bundles(path):
    """Yield the files to scan under PATH."""
    path = pathlib.Path(path)
    if path.is_file():
        yield path
        return
    if (path / 'SKILL.md').exists():
        roots = [path]
    else:  # a skills directory: every skill bundle except sync-skills
        roots = [p for p in sorted(path.iterdir())
                 if p.is_dir() and p.name != 'sync-skills']
    for r in roots:
        for f in sorted(r.rglob('*')):
            if f.is_file() and not (SKIP_PARTS & set(f.parts)) \
                    and f.name != '.DS_Store':
                yield f


def scan(paths):
    pats = load_patterns()
    hits = []
    for p in paths:
        for f in bundles(p):
            if f.suffix in CODE:
                hits.append(f'{f}: [code file] a prompt-only skill ships no code')
                continue
            if f.suffix not in TEXT:
                continue
            for n, line in enumerate(f.read_text(errors='replace').splitlines(), 1):
                for src, rx in pats:
                    if rx.search(line):
                        hits.append(f'{f}:{n}: [{src}] {line.strip()[:120]}')
    return hits


def main(argv):
    count_only = '--count' in argv
    paths = [a for a in argv if a != '--count'] or [repo_skills()]
    hits = scan(paths)
    if count_only:
        print(len(hits))
        return 0
    for h in hits:
        print(h)
    print(f'leaks: {len(hits)}')
    return 1 if hits else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
