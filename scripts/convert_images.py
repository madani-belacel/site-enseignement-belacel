#!/usr/bin/env python3
"""M11: Generate WebP/AVIF versions of images and update HTML <img> → <picture>."""

import os
import re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(ROOT, "images")

IMAGES_TO_CONVERT = [
    "photo-profil.png",
    "Université_de_Mostaganem.png",
    "module-tic-banner.png",
    "LOGO-FLE-UNIV-Mosta.jpeg",
]

# Small responsive variants used by the compact site header.
HEADER_VARIANTS = {
    "photo-profil.png": ("photo-profil-96", 96),
    "Université_de_Mostaganem.png": ("universite-mostaganem-96", 96),
}


def generate_modern_formats():
    """Generate WebP and AVIF versions for each image."""
    created = {}
    for fname in IMAGES_TO_CONVERT:
        src = os.path.join(IMAGES_DIR, fname)
        base, _ = os.path.splitext(fname)
        webp_path = os.path.join(IMAGES_DIR, f"{base}.webp")
        avif_path = os.path.join(IMAGES_DIR, f"{base}.avif")

        img = Image.open(src)
        orig_size = os.path.getsize(src)

        # WebP
        if img.mode == "RGBA":
            img.save(webp_path, "WEBP", quality=80)
        else:
            img.convert("RGB").save(webp_path, "WEBP", quality=80)
        webp_size = os.path.getsize(webp_path)

        # AVIF
        if img.mode == "RGBA":
            img.save(avif_path, "AVIF", quality=65)
        else:
            img.convert("RGB").save(avif_path, "AVIF", quality=65)
        avif_size = os.path.getsize(avif_path)

        print(f"  {fname}: {orig_size:,}B → WebP {webp_size:,}B ({webp_size*100//orig_size}%) / AVIF {avif_size:,}B ({avif_size*100//orig_size}%)")
        created[fname] = (webp_path, avif_path)

    for source_name, (variant_name, max_size) in HEADER_VARIANTS.items():
        source_path = os.path.join(IMAGES_DIR, source_name)
        image = Image.open(source_path).convert("RGBA")
        image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        image.save(os.path.join(IMAGES_DIR, f"{variant_name}.webp"), "WEBP", quality=82, method=6)
        image.save(os.path.join(IMAGES_DIR, f"{variant_name}.avif"), "AVIF", quality=62)
        print(
            f"  {variant_name}: {image.width}×{image.height} "
            f"WebP {os.path.getsize(os.path.join(IMAGES_DIR, f'{variant_name}.webp')):,}B / "
            f"AVIF {os.path.getsize(os.path.join(IMAGES_DIR, f'{variant_name}.avif')):,}B"
        )

    return created


def wrap_img_with_picture(html_content, img_filename):
    """Replace <img src='...img_filename'> with <picture> wrapper."""
    # Match <img tags that reference this image file (any relative path depth)
    pattern = re.compile(
        r'(<img\s[^>]*src="([^"]*' + re.escape(img_filename) + r')"[^>]*>)',
        re.DOTALL,
    )

    def replacer(m):
        full_tag = m.group(1)
        src_path = m.group(2)  # e.g. "../../images/photo-profil.png"
        base, _ = os.path.splitext(src_path)
        webp_src = f"{base}.webp"
        avif_src = f"{base}.avif"
        return (
            f'<picture>'
            f'<source srcset="{avif_src}" type="image/avif">'
            f'<source srcset="{webp_src}" type="image/webp">'
            f'{full_tag}'
            f'</picture>'
        )

    new_content, count = pattern.subn(replacer, html_content)
    return new_content, count


def update_html_files(created):
    """Walk all HTML files and wrap matching <img> tags."""
    total_replaced = 0
    files_changed = 0

    for dirpath, _, filenames in os.walk(ROOT):
        # Skip non-site directories
        if any(skip in dirpath for skip in ("/.git", "/.venv", "/node_modules", "/__pycache__")):
            continue
        for fname in filenames:
            if not fname.endswith(".html"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            original = content
            file_count = 0
            for img_fname in created:
                content, count = wrap_img_with_picture(content, img_fname)
                file_count += count

            if content != original:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                total_replaced += file_count
                files_changed += 1

    return files_changed, total_replaced


def main():
    print("=== M11: Génération WebP/AVIF ===")
    print("\n1. Conversion des images...")
    created = generate_modern_formats()

    print(f"\n2. Mise à jour des fichiers HTML...")
    files_changed, total_replaced = update_html_files(created)
    print(f"   {files_changed} fichiers modifiés, {total_replaced} balises <img> wrappées en <picture>")

    print("\nTerminé.")


if __name__ == "__main__":
    main()
