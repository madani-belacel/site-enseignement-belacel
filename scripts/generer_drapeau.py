#!/usr/bin/env python3
"""Genere un drapeau algerien vectoriel correct (rapport officiel 2:3).

L'embleme (croissant + etoile) doit etre centre sur le drapeau, le croissant
s'ouvrant vers la droite et l'etoile logee dans son ouverture.

Geometrie : deux cercles (exterieur R, interieur r) centres de part et
d'autre de l'axe ; le croissant est le disque exterieur MOINS l'interieur.
On calcule les deux points d'intersection puis on trace l'arc exterieur
majeur (par la gauche) suivi de l'arc interieur mineur (qui creuse vers la
droite).
"""
import math

L, H = 90.0, 60.0          # 3:2 -> hauteur 2, longueur 3
VERT = "#006233"
BLANC = "#ffffff"
ROUGE = "#d21034"

cx0, cy0 = L / 2.0, H / 2.0

# --- symbole, construit autour de l'origine puis translate -----------------
R = 15.0                   # rayon exterieur du croissant
d = 12.0                   # distance entre les deux centres
cx_ext, cx_int = -6.0, 6.0
r = 12.3                   # rayon interieur

a = (d * d - r * r + R * R) / (2 * d)
h = math.sqrt(R * R - a * a)
ix = cx_ext + a            # abscisse des deux points d'intersection
iy = h

etoile_cx, etoile_cy = 5.0, 0.0
Re, ri = 6.5, 6.5 * 0.382

# --- etoile a 5 branches ----------------------------------------------------
pts = []
for k in range(5):
    ao = math.radians(-90 + 72 * k)
    pts.append((etoile_cx + Re * math.cos(ao), etoile_cy + Re * math.sin(ao)))
    ai = math.radians(-90 + 36 + 72 * k)
    pts.append((etoile_cx + ri * math.cos(ai), etoile_cy + ri * math.sin(ai)))
etoile = "M" + " L".join("%.3f %.3f" % p for p in pts) + " Z"

# --- centrage de l'ensemble sur le drapeau ---------------------------------
gauche = cx_ext - R
droite = etoile_cx + Re
dx = cx0 - (gauche + droite) / 2.0
dy = cy0 - (cy_ext if (cy_ext := 0.0) else 0.0)

# arc exterieur majeur passant par la gauche  -> sweep 0
# arc interieur mineur creusant vers la droite -> sweep 1
croissant = (
    "M%.3f %.3f A%.3f %.3f 0 1 0 %.3f %.3f A%.3f %.3f 0 0 1 %.3f %.3f Z"
    % (ix, -iy, R, R, ix, iy, r, r, ix, -iy)
)

svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" width="%g" height="%g" role="img" aria-labelledby="t">
  <title id="t">Drapeau de l'Algerie</title>
  <rect width="%g" height="%g" fill="%s"/>
  <rect x="%g" width="%g" height="%g" fill="%s"/>
  <g transform="translate(%.3f %.3f)">
    <path d="%s" fill="%s"/>
    <path d="%s" fill="%s"/>
  </g>
</svg>
""" % (L, H, L, H, L / 2, H, VERT, L / 2, L / 2, H, BLANC,
       dx, dy, croissant, ROUGE, etoile, ROUGE)

import sys
sortie = sys.argv[1] if len(sys.argv) > 1 else "images/flag-algerie.svg"
open(sortie, "w", encoding="utf-8").write(svg)
print("ecrit :", sortie)
print("croissant :", croissant)
print("etoile    :", etoile)
print("translation: %.3f %.3f" % (dx, dy))
