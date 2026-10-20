#!/usr/bin/env python3
"""Print a build recipe as shell KEY=VALUE lines for GitHub Actions."""
import csv, shlex, sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit('usage: load_build_recipe.py <recipe_id>')
want = sys.argv[1]
path = Path(__file__).resolve().parent.parent / 'data/build_recipes.csv'
rows = list(csv.DictReader(open(path, encoding='utf-8')))
row = next((r for r in rows if r.get('recipe_id') == want), None)
if not row:
    raise SystemExit(f'recipe not found: {want}. Add it to data/build_recipes.csv first.')
for key in ('recipe_id', 'device', 'codename', 'repository_url', 'ref', 'defconfig', 'arch', 'block_device', 'toolchain', 'build_script', 'build_patch'):
    print(f"{key.upper()}={shlex.quote(row.get(key, ''))}")
