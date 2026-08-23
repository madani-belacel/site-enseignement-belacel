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
        "label": "Université de Mostaganem — Faculté des langues étrangères · Département d'anglais",
    },
    {
        "pattern": os.path.join("cours", "Dialogues_Anglais"),
        "label": "Université de Mostaganem — Faculté des langues étrangères · Département d'anglais",
    },
    {
        "pattern": os.path.join("cours", "Dialogues_TICE"),
        "label": "Université de Mostaganem — Faculté des langues étrangères · Département d'anglais",
    },
    {
        "pattern": os.path.join("cours", "Module_Réseau_Mostaganem"),
        "label": "Université de Mostaganem — Faculté des Sciences · Département Mathématiques et Informatique",
    },
    {
        "pattern": os.path.join("cours", "Module Informatique ENS"),
        "label": "Université de Mostaganem — Faculté des Sciences · Département Mathématiques et Informatique",
    },
]


EMAIL_RE = re.compile(r"([A-Za-z0-9._%+-]+\s*(?:@|\[at\]|\[AT\])\s*[A-Za-z0-9._%+-]+\.[A-Za-z]{2,})")


def find_target_label(path: str, mappings: List[Dict[str, str]]) -> str | None:
    rel = os.path.normpath(path)
    for m in mappings:
        if m["pattern"] in rel:
            return m["label"]
    return None


def process_file(path: str, new_label: str, do_apply: bool, make_backup: bool) -> Tuple[bool, List[Tuple[str, str]]]:
    """Return (changed, list_of_diffs (old_line, new_line))."""
    changed = False
    diffs: List[Tuple[str, str]] = []

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out_lines = lines.copy()

    for i, line in enumerate(lines):
        if "Université de Mostaganem" in line:
            old_line = line.rstrip("\n")
            # extract possible email to preserve
            m = EMAIL_RE.search(line)
            email_part = ""
            if m:
                email_part = m.group(1).strip()
            # preserve existing closing tags if present
            closing = ""
            if old_line.strip().endswith("</p>"):
                closing = "</p>"
            elif old_line.strip().endswith("<br>"):
                closing = ""

            # build replacement
            new_content = f"<p>{new_label}"
            if email_part:
                new_content += "<br>" + email_part
            new_content += closing

            if new_content != old_line:
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
