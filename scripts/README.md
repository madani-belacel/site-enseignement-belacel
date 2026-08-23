# scripts/README.md

Fix_departments utility

Usage

- Dry run (show changes, no files modified):

```bash
python3 scripts/fix_departments.py --root /home/madani/Bureau/site-enseignement-belacel --dry-run
```

- Apply changes (creates `*.bak` backups):

```bash
python3 scripts/fix_departments.py --root /home/madani/Bureau/site-enseignement-belacel --apply
```

- Apply changes and commit to a new git branch:

```bash
python3 scripts/fix_departments.py --root /home/madani/Bureau/site-enseignement-belacel --apply --git-branch fix/departments-20260823
```

Notes
- The default mappings hard-code common folders to target labels. Use `--mapping-file` with a JSON file to provide custom mappings.
- The script only edits `.html` files and looks for lines containing "Université de Mostaganem" to replace the department portion.
- Review `.bak` files before pushing any changes.
