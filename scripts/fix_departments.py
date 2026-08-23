#!/usr/bin/env python3
"""scripts/fix_departments.py

Preview and apply path-aware replacements for department labels across the
static site. Creates `.bak` backups by default. Supports dry-run and an
optional git branch commit.

Usage examples:
  python3 scripts/fix_departments.py --dry-run
  python3 scripts/fix_departments.py --apply --root /home/madani/Bureau/site-enseignement-belacel --git-branch fix/departments-20260823

The default mappings are conservative; pass `--mapping-file path.json`
to override or extend mappings.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from typing import Dict, List, Tuple


DEFAULT_MAPPINGS = [
    # pattern (relative path contains) -> replacement label
    {
        "pattern": os.path.join("cours", "Licence 1 Anglais"),
        "label": "Université de Mostaganem — Faculté des langues étrangères · Département de français",
    },
    {
        "pattern": os.path.join("cours", "Dialogues_Anglais"),
        "label": "Université de Mostaganem — Faculté des langues étrangères · Département de français",
    },
    {
        "pattern": os.path.join("cours", "Dialogues_TICE"),
        "label": "Université de Mostaganem — Faculté des langues étrangères · Département de français",
    },
    {
        "pattern": os.path.join("cours", "Module_Réseau_Mostaganem"),
        "label": "Université de Mostaganem — Faculté des Sciences Exactes et Informatique · Département de Mathématiques et Informatique",
    },
    {
        "pattern": os.path.join("cours", "Module Informatique ENS"),
        "label": "École Normale Supérieure de Mostaganem",
    },
]


EMAIL_RE = re.compile(r"([A-Za-z0-9._%+-]+\s*(?:@|\[at\]|\[AT\])\s*[A-Za-z0-9._%+-]+\.[A-Za-z]{2,})")

# A line is eligible ONLY if it is a simple institutional paragraph:
# optional indentation, <p>…</p> wrapping the whole line, containing the
# university name and no markup other than inline formatting tags.
SIMPLE_P_RE = re.compile(r"^(\s*)<p>(.*)</p>\s*$")
ALLOWED_TAGS_RE = re.compile(r"</?(?:br\s*/?|strong|em|b|i|small)>", re.IGNORECASE)
ANCHOR_RE = re.compile(r"<[a-zA-Z!/]")


def find_target_label(path: str, mappings: List[Dict[str, str]]) -> str | None:
    rel = os.path.normpath(path)
    for m in mappings:
        if m["pattern"] in rel:
            return m["label"]
    return None


def process_file(path: str, new_label: str, do_apply: bool, make_backup: bool) -> Tuple[bool, List[Tuple[str, str]]]:
    """Return (changed, list_of_diffs (old_line, new_line)).

    Only simple institutional paragraphs are touched:
    ``<p>Université de Mostaganem … [email]</p>`` on a single line.
    Any other line containing the university name (JSON-LD, <img>, <div>,
    <meta>, breadcrumbs…) is left strictly untouched.
    """
    changed = False
    diffs: List[Tuple[str, str]] = []

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out_lines = lines.copy()

    for i, line in enumerate(lines):
        if "Université de Mostaganem" not in line and new_label not in line and "École Normale Supérieure" not in line:
            continue
        m = SIMPLE_P_RE.match(line)
        if not m:
            continue  # not a standalone <p>…</p> line -> never touch
        indent, orig_inner = m.group(1), m.group(2)
        inner = orig_inner
        email_part = ""
        em = EMAIL_RE.search(inner)
        if em:
            email_part = em.group(1).strip()
            inner = EMAIL_RE.sub("", inner)
            inner = re.sub(r"(?:<br\s*/?>\s*)+$", "", inner.strip()).strip()
        residue = ALLOWED_TAGS_RE.sub("", inner)
        if ANCHOR_RE.search(residue):
            continue  # contains real markup (links, spans with attrs…) -> skip
        text = re.sub(r"\s+", " ", residue).strip()
        for inst in ("Université de Mostaganem", "École Normale Supérieure"):
            if text.startswith(inst):
                remainder = text[len(inst):]
                break
        else:
            continue  # does not start with an institution name -> never touch
        # The remainder must look like a faculty/department label only:
        # a single em-dash separated segment, no sentence punctuation.
        remainder = remainder.strip()
        if remainder and not re.fullmatch(r"—\s*[^:;,.(?!][^:;,.(?!]*", remainder):
            continue  # real sentence mentioning the university -> never touch
        expected = new_label + ("<br>" + email_part if email_part else "")
        if orig_inner == expected:
            continue  # already normalized
        old_line = line.rstrip("\n")
        new_content = f"{indent}<p>{expected}</p>"
        out_lines[i] = new_content + "\n"
        changed = True
        diffs.append((old_line, new_content))

    if changed and do_apply:
        if make_backup:
            bak_path = path + ".bak"
            shutil.copy2(path, bak_path)
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(out_lines)

    return changed, diffs


def walk_and_fix(root: str, mappings: List[Dict[str, str]], do_apply: bool, backup: bool) -> Dict[str, List[Tuple[str, str]]]:
    results: Dict[str, List[Tuple[str, str]]] = {}
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.lower().endswith(".html"):
                continue
            full = os.path.join(dirpath, fn)
            # determine mapping by relative path from root
            rel = os.path.relpath(full, root)
            target_label = None
            for m in mappings:
                if m["pattern"] in rel:
                    target_label = m["label"]
                    break
            if not target_label:
                continue
            changed, diffs = process_file(full, target_label, do_apply, backup)
            if changed:
                results[full] = diffs
    return results


def load_mappings(path: str | None) -> List[Dict[str, str]]:
    if not path:
        return DEFAULT_MAPPINGS
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def git_commit_branch(root: str, branch: str, message: str) -> None:
    cwd = root
    subprocess.check_call(["git", "checkout", "-b", branch], cwd=cwd)
    subprocess.check_call(["git", "add", "-A"], cwd=cwd)
    subprocess.check_call(["git", "commit", "-m", message], cwd=cwd)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fix department labels across site HTML files")
    parser.add_argument("--root", default=".", help="site root (default: current directory)")
    parser.add_argument("--mapping-file", help="optional JSON mapping file")
    parser.add_argument("--dry-run", action="store_true", help="only show what would change")
    parser.add_argument("--apply", action="store_true", help="apply changes")
    parser.add_argument("--no-backup", dest="backup", action="store_false", help="do not create .bak backups")
    parser.add_argument("--git-branch", help="if provided, create branch and commit changes (requires --apply)")
    parser.add_argument("--commit-message", default="fix: normalise department labels by folder", help="git commit message when creating branch")
    args = parser.parse_args()

    mappings = load_mappings(args.mapping_file)
    root = os.path.abspath(args.root)

    if not args.apply and not args.dry_run:
        print("Please specify either --dry-run or --apply")
        return

    print(f"Scanning site root: {root}")
    results = walk_and_fix(root, mappings, do_apply=args.apply, backup=args.backup)

    if not results:
        print("No changes detected.")
        return

    total_files = len(results)
    total_changes = sum(len(v) for v in results.values())
    print(f"Found {total_changes} change(s) in {total_files} file(s)")

    for path, diffs in results.items():
        print("---", path)
        for old, new in diffs:
            print("- ", old)
            print("+ ", new)

    if args.apply and args.git_branch:
        print(f"Creating git branch {args.git_branch} and committing changes...")
        git_commit_branch(root, args.git_branch, args.commit_message)
        print("Git commit complete.")


if __name__ == "__main__":
    main()
