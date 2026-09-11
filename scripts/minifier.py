#!/usr/bin/env python3
"""Minify CSS and JS files in-place. Run before deployment."""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def minify_css(path):
    from cssmin import cssmin
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    out = cssmin(src)
    saved = len(src) - len(out)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"  CSS  {path.replace(ROOT+'/', '')}  {len(src):,} → {len(out):,} (-{saved:,} bytes, -{saved*100//max(len(src),1)}%)")


def minify_js(path):
    from jsmin import jsmin
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    out = jsmin(src)
    saved = len(src) - len(out)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"  JS   {path.replace(ROOT+'/', '')}  {len(src):,} → {len(out):,} (-{saved:,} bytes, -{saved*100//max(len(src),1)}%)")


def main():
    print("Minification des assets...")
    for f in ["css/style.css"]:
        minify_css(os.path.join(ROOT, f))
    for f in ["js/main.v2.js", "js/data-loader.js", "js/data.js"]:
        minify_js(os.path.join(ROOT, f))
    print("Terminé.")


if __name__ == "__main__":
    main()
