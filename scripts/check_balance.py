#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifie l'equilibre des balises d'une ou plusieurs pages HTML.

Un <div> oublie laisse la page balanced pour un lecteur naif mais fausse le
rendu : c'est le genre d'erreur que seule une vraie pile de balises revele.

Usage : python3 check_balance.py page1.html [page2.html ...]
Sortie : « OK » par page, code de retour 1 si au moins une page est calee.
"""
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.err = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass  # deja equilibre par construction

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        elif any(t == tag for t, _ in self.stack):
            while self.stack and self.stack[-1][0] != tag:
                t, l = self.stack.pop()
                self.err.append("auto-ferme <%s> ouvert ligne %d" % (t, l))
            if self.stack:
                self.stack.pop()
        else:
            self.err.append("fermeture orpheline </%s> ligne %d"
                            % (tag, self.getpos()[0]))


def main():
    rc = 0
    for chemin in sys.argv[1:]:
        b = Balance()
        b.feed(open(chemin, encoding="utf-8", errors="ignore").read())
        if b.stack or b.err:
            print("KO  %-56s ouverts=%s erreurs=%s"
                  % (chemin[-56:], [t for t, _ in b.stack][:4], b.err[:4]))
            rc = 1
        else:
            print("OK  %s" % chemin)
    return rc


if __name__ == "__main__":
    sys.exit(main())
