#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controle de securite des applications installees sur un telephone Android.

Usage : python3 audit_apps_telephone.py [numero_adb]

Ne lit AUCUNE donnee personnelle : uniquement la liste des applications, leurs
permissions et leurs dates d'installation. L'ADB doit etre autorise
(etat « device »).

Cherche ce qui caracterise un logiciel malveillant :
  - acces aux SMS (interception de codes 2FA) ;
  - administrateur d'appareil (verrouillage / effacement) ;
  - service d'accessibilite (controle de l'ecran, capture, clics) ;
  - droit d'installer d'autres applications ;
  - installation tres recente (les malwares arrivent souvent par un lien) ;
  - apps systeme marques comme teles qu'elles ne devraient pas l'etre.
"""
import re
import subprocess
import sys

ADB = ["adb"]
if len(sys.argv) > 1:
    ADB += ["-s", sys.argv[1]]

# permission -> risque
PERMISSIONS = {
    "android.permission.READ_SMS": ("SMS", "lit vos SMS — peut intercepter un code 2FA"),
    "android.permission.RECEIVE_SMS": ("SMS", "reçoit vos SMS — interception de code 2FA"),
    "android.permission.SEND_SMS": ("SMS", "envoie des SMS a votre frais"),
    "android.permission.RECEIVE_MMS": ("SMS", "reçoit vos MMS"),
    "android.permission.BIND_ACCESSIBILITY_SERVICE": ("accessibilité", "peut voir et cliquer sur votre écran"),
    "android.permission.BIND_DEVICE_ADMIN": ("administrateur", "peut verrouiller ou effacer le téléphone"),
    "android.permission.REQUEST_INSTALL_PACKAGES": ("installation", "peut installer d'autres applications"),
    "android.permission.READ_CALL_LOG": ("journal d'appels", "lit votre journal d'appels"),
    "android.permission.READ_CONTACTS": ("contacts", "lit vos contacts"),
    "android.permission.CAMERA": ("caméra", "accède à la caméra"),
    "android.permission.RECORD_AUDIO": ("micro", "accède au micro"),
    "android.permission.PACKAGE_USAGE_STATS": ("historique", "voit quelles applications vous utilisez"),
    "android.permission.SYSTEM_ALERT_WINDOW": ("overlay", "peut afficher par-dessus les autres applications"),
}


def sh(*args, **kw):
    return subprocess.run(list(ADB) + list(args), capture_output=True,
                          text=True, timeout=kw.get("timeout", 180))


def version(pkg, champ):
    txt = sh("shell", "dumpsys", "package", pkg).stdout
    m = re.search(r"%s=(\S+)" % champ, txt)
    return m.group(1) if m else "?"


def main():
    etat = sh("devices").stdout
    if "device" not in etat:
        print("Telephone non connecte ou non autorise.")
        print(etat.strip())
        return 1

    model = sh("shell", "getprop", "ro.product.model").stdout.strip()
    android = sh("shell", "getprop", "ro.build.version.release").stdout.strip()
    brut = sh("shell", "pm", "list", "packages", "-3").stdout   # applications tierces
    systeme = sh("shell", "pm", "list", "packages", "-s").stdout
    tiers = [l.replace("package:", "").strip() for l in brut.splitlines() if l.strip()]
    sysl = [l.replace("package:", "").strip() for l in systeme.splitlines() if l.strip()]

    print("=" * 74)
    print("TELEPHONE : %s  —  Android %s" % (model, android))
    print("%d applications installees : %d tierces, %d systeme"
          % (len(tiers) + len(sysl), len(tiers), len(sysl)))
    print("=" * 74)

    # ---- 1. applications sans icone (invisibles) --------------------------
    caches = []
    for pkg in tiers:
        d = sh("shell", "dumpsys", "package", pkg).stdout
        # une application « launcher » declare une activity CATEGORY_LAUNCHER
        if "android.intent.category.LAUNCHER" not in d:
            caches.append(pkg)

    # ---- 2. permissions sensibles -----------------------------------------
    alertes = []
    for pkg in tiers:
        d = sh("shell", "dumpsys", "package", pkg).stdout
        trouve = []
        for perm, (famille, why) in PERMISSIONS.items():
            if perm in d:
                trouve.append((famille, why))
        if trouve:
            alertes.append((pkg, trouve))

    # ---- 3. applications tres recemment installees ------------------------
    recents = []
    for pkg in tiers:
        t = version(pkg, "firstInstallTime")
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", t)
        if m:
            recents.append((m.group(0), pkg))
    recents.sort(reverse=True)

    # ---- rapport -----------------------------------------------------------
    print()
    print("-- 1. Authentification / mots de passe -------------------------")
    auth = [p for p in tiers + sysl if re.search(
        r"authenticator|authy|aegis|freeotp|andotp|yubikey|onepassword|bitwarden", p, re.I)]
    for p in auth:
        print("   %s" % p)
    if not auth:
        print("   aucune")

    print()
    print("-- 2. Applications SANS icone (invisibles dans le menu) ----------")
    for p in caches:
        print("   %s" % p)
    if not caches:
        print("   aucune : toutes les applications tierces sont visibles")

    print()
    print("-- 3. Permissions a surveiller ------------------------------------")
    graves = 0
    for pkg, trouve in sorted(alertes):
        famille = {f for f, _ in trouve}
        if famille & {"SMS", "accessibilité", "administrateur", "installation"}:
            graves += 1
            print("   [!] %s" % pkg)
            for f, why in trouve:
                print("       - %-14s %s" % (f, why))
    print("   (%d application(s) avec une permission vraiment sensible)" % graves)

    print()
    print("-- 4. 12 applications installees le plus recemment --------------")
    for d, p in recents[:12]:
        print("   %s  %s" % (d, p))
    return 0


if __name__ == "__main__":
    sys.exit(main())
