#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cours 01 — Introduction à l'IA : 30 diapositives.

Complète la version de 11 diapositives déjà en ligne, qui ne présentait l'IA
que comme un assistant de conversation. Les sixAjouts qui répondent aux
questions réellement posées en classe :

  - diapos 5 à 8   : l'IA dans la vie réelle, réparation et flashage compris ;
  - diapos 18       : la boucle des agents, Cursor et OpenCode ;
  - diapos 23 à 27  : réparer, créer un site, réviser, traduire, enseigner ;
  - diapos 28       : les astuces de terrain, celles qu'on utilise vraiment.

Usage : python3 scripts/generer_ppt_cours01.py [sortie.pptx]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx_commun import (AMBER, BLUE, BLUE_L, DARK, GREEN, GREEN_L, GREY,
                         GREY_L, LINE_C, NAVY, WHITE, add_footer,
                         add_paragraph, add_shape, add_textbox, couverture,
                         draw_flow, ecrire_notes, nouveau_conteneur)

from communs_ppt_cours01 import (DEFAUT, IMG_FLE, IMG_UNIV, L_D, L_G, PIED,
                                 chapo, entete, grille, deux_colonnes,
                                 notes, section, tableau)

prs, LAYOUT = nouveau_conteneur()
N = [0]


def nouvelle(idee, titre, sous_partie=None, pied=True):
    s = prs.slides.add_slide(LAYOUT)
    entete(s, idee, titre, sous_partie)
    N[0] += 1
    if pied:
        add_footer(s, N[0], PIED)
    return s


# ===========================================================================
# 1 — Couverture
# ===========================================================================
s = prs.slides.add_slide(LAYOUT)
N[0] = 1
cache = {}
couverture(s, IMG_UNIV, IMG_FLE,
           "Introduction à l'Intelligence Artificielle",
           "Comprendre l'IA, ses usages et ses limites",
           "Questions & Réponses — Cours 01",
           "Dr. Madani BELACEL — MCB",
           "Module Intelligence Artificielle  ·  30 diapositives  ·  questions et réponses dans les notes",
           adresse="Cours en ligne : madani-belacel.github.io/site-enseignement-belacel",
           cache=cache)
ecrire_notes(s, notes(
    "COUVERTURE", "Introduction à l'IA",
    "Faire comprendre que l'IA n'est ni une baleine bleue ni une science de "
    "fiction : c'est un outil qu'ils ont déjà dans la poche.",
    "Accueil. Avant de poser la moindre théorie, je demande à la classe : "
    "« combien de fois aujourd'hui une machine a décidé quelque chose pour "
    "vous ? ». Je laisse le silence s'installer trois secondes. On obtient "
    "tj��toujours le même chiffre — entre dix et cinquante fois. Le cours "
    "part de là : ils utilisent déjà de l'IA sans le savoir. Le badge "
    "annonce la durée pour qu'ils sachent qu'on va travailler.",
    [("Est-ce qu'on aura une évaluation ?",
      "Pas aujourd'hui. Le défi de la deuxième diapositive sert de "
      "départ, on en reparlera à la fin."),
     ("Pourquoi 30 diapositives en 90 minutes ?",
      "Trois minutes par diapositive en moyenne. On ne les lit pas toutes, "
      "certaines ne sont que des repères visuels.")],
    "Ne pas commencer par la définition. Si vous dites « l'IA est une "
    "discipline qui… », vous perdez la salle en dix secondes."))

# ===========================================================================
# 2 — Le défi : accroche
# ===========================================================================
s = nouvelle("IDÉE 1", "Ce soir, six problèmes. Tu en résous cinq ?")
chapo(s, "Voici six situations réelles. Aucune n'a besoin de savoir "
         "informatiquement. À la fin de ce cours, cinq seront résolues.")
grille(s, [("Téléphone", "ne charge plus", "warn"),
           ("Ordinateur", "planté, fichier non sauvegardé", "warn"),
           ("Devoir", "à rendre demain", "primary"),
           ("Site web", "pour le club de la faculté", "primary"),
           ("Photo", "floue, à restaurer", "primary"),
           ("Devis", "trois réparateurs à comparer", "alt")],
       y=3.55, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 1", "Ce soir, six problèmes",
    "Créer le manque. Ils doivent vouloir les six réponses.",
    "Je lis les six problèmes à voix haute, un par dix secondes, sans "
    "commentaire. Ensuite je pose la question : « lequel de ces six vous a "
    "déjà posé problème cette année ? ». La réponse arrive toujours, "
    "généralement le téléphone ou le fichier perdu. Je dis alors : « ce soir "
    "on va en traiter cinq ». Je ne promets rien, je donne un objectif.",
    [("On va vraiment apprendre tout ça en une séance ?",
      "Non. On va apprendre à poser les bonnes questions, et à savoir quand "
      "l'IA peut aider. Le reste se lit sur le site."),
     ("C'est la même chose que les cours précédents ?",
      "Non. Les cours 02 à 05 sont des domaines précis. Aujourd'hui on "
      "construit la carte générale.")],
    "Ne pas résoudre les problèmes maintenant, même si la classe "
    "s'y erhebe. Il faut garder le fil pour la fin : c'est le fil rouge."))

# ===========================================================================
# 3 — Objectif
# ===========================================================================
s = nouvelle("IDÉE 2", "À la fin de ce cours, tu sauras trois choses")
grille(s, [("1 · Où", "Où l'IA est déjà utilisée dans ta journée, sans que "
                      "tu t'en aperçoives.", "primary"),
           ("2 · Comment", "Comment elle fonctionne : des données, un motif, "
                           "une prédiction.", "alt"),
           ("3 · Quoi", "Ce que tu peux en faire dès demain, concrètement, "
                        "et dans quels domaines.", "primary")],
       y=3.55, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 2", "À la fin, tu sauras trois choses",
    "Donner un contrat clair : à la fin, trois questions auxquelles ils "
    "sauront répondre.",
    "Je lis les trois points et j'insiste sur le premier. Beaucoup "
    "d'étudiants pensent que l'IA est une technique de laboratoire. Le "
    "premier point les surprend toujours : elle est déjà dans leur téléphone, "
    "dans leur boîte mail et dans leur carte bancaire. Les points 2 et 3 "
    "servent à installed : on ne cherche pas à faire d'eux des "
    "informaticiens, mais des utilisateurs capables de juger.",
    [("Est-ce qu'on va apprendre à coder ?",
      "Pas dans ce cours. Le code est le moyen, pas le but. On verra les "
      "agents, mais pour comprendre ce qu'ils font, pas pour devenir "
      "développeur."),
     ("Pourquoi commencer par « où » ?",
      "Parce qu'on ne peut pas juger un outil qu'on n'a pas utilisé.")],
    "Ne pas promising de devenir expert. Promettre un usage juste."))

# ===========================================================================
# 4 — Séparation partie 1
# ===========================================================================
s = prs.slides.add_slide(LAYOUT)
N[0] += 1
section(s, 1, "Où l'IA est déjà là",
        "Elle ne vit pas dans les laboratoires. Elle est dans votre poche, "
        "votre boîte mail, votre voiture et votre atelier.",
        ["Dans le téléphone", "Sur le web et les réseaux sociaux",
         "À l'université", "Chez le technicien : réparer et flasher"],
        notes("PARTIE 1", "Où l'IA est déjà là",
              "Faire sortir la classe de l'idée que l'IA est une technique "
              "de laboratoire.",
              "Transition. Je demande : où avez-vous utilisé de l'IA "
              "aujourd'hui, sans y penser ? La plupart citent le correcteur "
              "du téléphone ou les recommandations. Je dis alors : vous en "
              "avez déjà utilisé cinq fois. On va voir où, en commençant par "
              "ce que vous avez dans la main.",
              [("On va parler de nous ?",
                "Oui, et c'est la partie la plus importante : comprendre où "
                "l'IA agit déjà, avant de choisir un outil."),
               ("Pourquoi commencer par ça ?",
                "Parce qu'on ne choisit bien un outil que si on sait quel "
                "problème il résout.")],
              "Ne pas faire durer cette diapositive : c'est un repère, pas "
              "un contenu."))
add_footer(s, N[0], PIED)

# ===========================================================================
# 5 — Dans le téléphone
# ===========================================================================
s = nouvelle("IDÉE 3", "Dans ton téléphone, l'IA est partout")
chapo(s, "Sept zones, sept mécanismes différents. Aucune n'est de la "
         "magie : toutes apprennent à partir d'exemples.")
grille(s, [("Déblocage facial", "compare ton visage à une image apprise", "primary"),
           ("Correction photo", "corrige la lumière, la netteté, les couleurs", "primary"),
           ("Clavier prédictif", "prédit le mot suivant d'après le tien", "primary"),
           ("Navigation GPS", "prédit l'itinéraire le plus rapide", "primary"),
           ("Correction d'écriture", "propose le mot suivant à l'oral", "alt"),
           ("Photo de groupe", "découpe et recompose les visages", "alt"),
           ("Traduction de conversation", "traduit pendant que l'un parle", "alt"),
           ("Fil d'actualité", "te propose ce que tu regarderas", "warn")],
       y=3.45, colonnes=4)
ecrire_notes(s, notes(
    "IDÉE 3", "Dans ton téléphone",
    "Faire réaliser que la moitié du smartphone est une IA, et que "
    "chacune correspond à un mécanisme identifiable.",
    "Je fais deviner la classe avant de dévoiler. Pour « correction "
    "photo », je demande : « est-ce que c'est cosmétique ou de l'IA ? » et la "
    "réponse est presque toujours non. Je précise que chaque mécanisme "
    "apprend d'exemples : le déblocage a appris ton visage, le GPS a "
    "appris les routes. La dernière case, le fil d'actualité, est celle qui "
    "intéresse le plus : je demande à deux ou trois étudiants ce que "
    "l'algorithme sait d'eux, sans qu'ils l'aient demandé.",
    [("Est-ce que mon téléphone m'écoute ?",
      "Pour déverrouiller, oui. Le traitement se fait sur l'appareil dans "
      "la plupart des modèles récents. Ce n'est pas le micro qui enregistre "
      "en continu : c'est un modèle qui compare."),
     ("Comment le fil d'actualité sait ce que je veux ?",
      "Il observe ce que je regarde, ce que je like et ce que je saute. "
      "Plus tu interagis, plus il prédit juste."),
     ("Je peux vérifier ce qu'il sait de moi ?",
      "Oui, dans les réglages, section « publicité » ou « données », la "
      "plupart des téléphones permettent de voir et de supprimer cet "
      "historique.")],
    "Ne pas dire que le téléphone « lit dans tes pensées ». Dire qu'il "
    "reconnaît des formes qu'il a déjà vues."))

# ===========================================================================
# 6 — Web et réseaux sociaux
# ===========================================================================
s = nouvelle("IDÉE 4", "Sur le web et les réseaux sociaux")
chapo(s, "L'IA ne se contente pas de te montrer des pubs : elle décide ce "
         "que tu vois, dans quel ordre, et quand tu t'arrêtes.")
grille(s, [("Fil mathematicien", "propose le calcul que tu vas faire", "primary"),
           ("Facebook · TikTok", "choisit la vidéo suivante, vise l'attention", "primary"),
           ("Anti-spam", "classe le courriel comme indésirable", "alt"),
           ("Traduction automatique", "traduit en direct dans le navigateur", "alt"),
           ("Recommandation", "musique, films, produits, restaurants", "alt"),
           ("Modération", "détecte les images et les messages signalés", "warn")],
       y=3.55, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 4", "Sur le web et les réseaux sociaux",
    "Montrer que l'IA décide de l'ordre dans lequel on voit l'information.",
    "Je pose une question directe : « qui décide de la première vidéo que "
    "vous voyez ? ». Personne n'a la réponse dans la classe. Je révèle que "
    "c'est un modèle qui prédit votre attention, et que le critère n'est "
    "pas l'intérêt mais le temps passé. Sur l'anti-spam, je précise que "
    "c'est une IA discrète : elle apprend de ce que vous avez classé comme "
    "indésirable, elle apprend des autres utilisateurs.",
    [("Un ami m'a dit que les réseaux manipulaient.",
      "Ce n'est pas une théorie : c'est le mécanisme lui-même. La "
      "manipulation vient du choix de l'objectif — garder l'écran allumé."),
     ("L'anti-spam se trompe ?",
      "Oui. Un message légitime peut finir en indésirable, surtout s'il "
      "contient des mots inhabituels. Il faut vérifier la liste « courrier "
      "indésirable » de temps en temps."),
     ("Puis-jeafari me désabonner de ça ?",
      "Partiellement. On peut limiter la collecte, mais pas la supprimer "
      "entièrement : c'est le prix d'accès aux services gratuits.")],
    "Ne pas faire de la théorie conspirationniste. Reste sur le "
    "mécanisme observable."))

# ===========================================================================
# 7 — À l'université
# ===========================================================================
s = nouvelle("IDÉE 5", "À l'université et dans l'administration")
chapo(s, "Les services que vous utilisez tous les jours sont, pour la "
         "plupart, des IA déguisés en formulaires.")
grille(s, [("Dossier d'inscription", "trie et vérifie les pièces automatiquement", "primary"),
           ("Notes etPvjet", "calcule, classe, prédit les mentions", "primary"),
           ("Détection de plagiat", "compare vos phrases à des corpus entiers", "primary"),
           ("Archives", "reconnaît et classe des documents numérisés", "alt"),
           ("Transport", "prédit l'affluence, propose des trajets", "alt"),
           ("Santé", "aide au diagnostic à partir d'images médicales", "warn")],
       y=3.55, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 5", "À l'université",
    "Faire apparaître l'IA administrative avant que l'étudiant ne la "
    "découvre chez un compteur.",
    "Je commence par la prise en charge sanitaire : cette année, tout le "
    "monde a vu unExpiry assistant poser des questions avant deFam donner un "
    "numéro. C'est la première fois qu'ils touchent une IA sans que personne "
    "ne l'annonce. La détection de plagiat est le second point : je précise "
    "qu'elle ne juge pas la qualité d'un texte mais sa ressemblance avec un "
    "corpus. C'est important pour la suite du cours.",
    [("La détection de plagiat tombe-t-elle juste ?",
      "Elle tombe surtout juste quand le texte est entièrement recopié. "
      "Elle peut manquer un texte réécrit, et signaler une citation "
      "correctement attribuée. Aucune de ces deux erreurs ne rend la "
      "détection inutile."),
     ("Un agent de santé peut se tromper ?",
      "Oui, et c'est pour cela qu'il ne décide pas seul : il prépare le "
      "dossier, le médecin tranche."),
     ("Est-ce que l'université utilise mes notes pour quoi que ce soit ?",
      "Prévoir les échecs, organiser les groupes. C'est ce que la loi sur "
      "les données personnelles encadre.")],
    "Ne pas laisser croire que l'administration est défaillante. Citer un "
    "cas d'usage vérifiable."))
# ===========================================================================
# 8 — Chez le technicien
# ===========================================================================
s = nouvelle("IDÉE 6", "Chez le technicien : l'IA aide à réparer")
chapo(s, "Un technicien ne demande pas à l'IA de réparer. Il lui demande de "
         "lui éviter deux heures de recherche, puis il vérifie et il "
         "intervient de ses mains.")
grille(s, [("Lire un schéma", "photographier le circuit et l'expliquer", "primary"),
           ("Identifier un composant", "datasheet : valeur, tension, tolérance", "primary"),
           ("Interpréter une erreur", "traduire le code d'erreur en cause probable", "primary"),
           ("Choisir une pièce", "comparer les équivalents disponibles", "alt"),
           ("Écrire un script de flash", "adapter un script existant à son appareil", "alt"),
           ("Rédiger la fiche d'intervention", "mise en forme automatique", "alt")],
       y=3.55, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 6", "Chez le technicien : l'IA aide à réparer",
    "Faire le pont entre l'IA et le métier de l'étudiant ou de son "
    "proche — et poser la limite : l'IA conseille, elle ne répare pas.",
    "C'est la diapositive qui touche le plus la classe, je la prends "
    "longtemps. Je raconte un cas réel : une student de terminale avait un "
    "téléphone qui ne chargeait plus, elle a voulu le flasher. Un script "
    "mal adapté a mal verrouillé l'appareil. L'IA avait bien répondu, mais "
    "elle ne pouvait pas savoir que sa copie était périmée. Je conclude : "
    "l'IA gagne du temps, elle ne prend pas la responsabilité. Le technicien "
    "garde le diagnostic.",
    [("Est-ce que l'IA peut vraiment réparer ?",
      "Non. Elle accélère la recherche : elle donne les causes "
      "probables et les datasheets. La mesure, le démontage et la décision "
      "restent à l'humain."),
     ("Flasher un téléphone, c'est dangereux ?",
      "Oui. Un script de flash mal adapté peut verrouiller "
      "définitivement l'appareil. Il faut toujours vérifier la compatibilité "
      "exacte du modèle avant de lancer quoi que ce soit."),
     ("Et si l'appareil est encore sous garantie ?",
      "Le flash annule la garantie, et peut même rendre l'appareil "
      "inutilisable. C'est la première vérification à faire.")],
    "Ne pas donner l'impression que tout est réparable par IA. "
    "L'exemple du téléphone verrouillé sert précisément à éviter "
    "cette confiance."))

# ===========================================================================
# 9 — Synthèse partie 1
# ===========================================================================
s = nouvelle("IDÉE 7", "Douze domaines, un seul mécanisme")
chapo(s, "L'IA change de nom et de métier selon le domaine. Le mécanisme, "
         "lui, ne change jamais : des exemples, un motif, une décision.")
grille(s, [("Téléphone", "photos, voix, clavier", "plain"),
           ("Santé", "images, triage", "plain"),
           ("Banque", "fraude, crédit", "plain"),
           ("Transport", "trafic, itinéraires", "plain"),
           ("Agriculture", "rendement, maladies", "plain"),
           ("Éducation", "notes, contenu", "plain"),
           ("Industrie", "contrôle qualité", "plain"),
           ("Énergie", "réseau, prévision", "plain"),
           ("Vidéo", "recommandation", "plain"),
           ("Recherche", "tri, résumé", "plain"),
           ("Réparation", "schémas, composants", "plain"),
           ("Site web", "code, mise en page", "plain")],
       y=3.50, colonnes=4)
ecrire_notes(s, notes(
    "IDÉE 7", "Douze domaines, un seul mécanisme",
    "Faire comprendre que la diversité des noms cache une seule technique.",
    "Je balaie la grille vite, en dix secondes, pour que l'image entre. "
    "Puis je marque un temps : « douze métiers différents, un seul "
    "mécanisme ». C'est la transition vers la partie 2. Si j'ai le temps, "
    "je demande à un étudiant de citer un domaine absent de la grille — il "
    "y en a toujours un, et je le note au tableau pour y revenir à la fin.",
    [("Pourquoi douze et pas plus ?",
      "Parce que la liste n'est pas exhaustive, elle est illustrative. "
      "Le même mécanisme sert partout ailleurs."),
     ("La recherche est-elle une IA ?",
      "Les moteurs ont des parties non-IA, mais le classement, la "
      "compréhension de la question et les réponses générées en sont.")],
    "Ne pas s'attarder : cette diapositive sert de respiration."))

# ===========================================================================
# 10 — Séparation partie 2
# ===========================================================================
s = prs.slides.add_slide(LAYOUT)
N[0] += 1
section(s, 2, "Comment ça marche vraiment",
        "Pas de mathématiques. Une phrase suffit à comprendre toute l'IA "
        "qui tourne autour de vous.",
        ["L'idée centrale en une phrase", "Un exemple chiffré",
         "Pourquoi elle se trompe", "Le rôle des données"],
        notes("PARTIE 2", "Comment ça marche vraiment",
              "Passer de l'usage au mécanisme, en une phrase et sans "
              "mathématiques.",
              "Transition. Je pose la question : comment une machine peut-elle "
              "dire qu'une photo contient un chat ? La réponse spontanée est "
              "« elle regarde ». C'est faux, et c'est justement ce qu'il faut "
              "corriger. Je préviens la classe : aucune formule dans cette "
              "partie. Une phrase et des exemples suffisent.",
              [("C'est des mathématiques ?",
                "Non. Une image en quatre mots : des exemples, un motif, une "
                "prédiction. Si vous savez compter jusqu'à dix, vous "
                "suffisez."),
               ("Est-ce que je dois tout retenir ?",
                "Non, une seule phrase. Le reste sert à vous faire réagir "
                "aux erreurs.")],
              "Ne pas laisser croire que le mécanisme est secret : tout est "
              "public et vérifiable."))
add_footer(s, N[0], PIED)

# ===========================================================================
# 11 — L'idée centrale
# ===========================================================================
s = nouvelle("IDÉE 8", "Une phrase : une machine qui devine le suivant")
chapo(s, "Pour prévoir quelque chose de nouveau, elle cherche ce qui "
         "ressemble le plus à ce qu'elle a déjà vu.")
draw_flow(s, [("box", "DONNÉES", "10 000 photos étiquetées", "plain"),
              ("arrow", "→"),
              ("box", "MOTIF", "des chats ont des oreilles pointues", "primary"),
              ("arrow", "→"),
              ("box", "PRÉDICTION", "cette image est un chat : 92 %", "primary"),
              ("arrow", "→"),
              ("box", "DÉCISION", "je le classe « chat »", "alt")],
         0.95, 3.65, 11.4, 1.35)
tf = add_textbox(s, 0.95, 5.30, 11.4, 0.95)
add_paragraph(tf, [("Le mot à retenir : ", {"bold": True, "color": NAVY}),
                   ("ce qui compte n'est pas la machine, c'est la qualité "
                    "des exemples. Deux mille bons exemples valent mieux que "
                    "cent mille mauvais.", {})],
              size=15, color=DARK, space_after=0, line_spacing=1.2)
ecrire_notes(s, notes(
    "IDÉE 8", "Une machine qui devine le suivant",
    "Donner à la classe une seule phrase à retenir pour toute la séance.",
    "Je laisse la diapositive affichée une bonne minute avant de parler. "
    "Puis je demande à la classe de reformuler l'idée avec leurs mots. "
    "J'attends des réponses du type : « elle regarde ce qui ressemble ». "
    "Quand quelqu'un trouve une bonne formulation, je l'écris au tableau "
    "et je m'y réfère le reste du cours. C'est la phrase qui permet de "
    "comprendre toutes les autres diapositives sans mathématiques.",
    [("Est-ce qu'elle choisit au hasard ?",
      "Non. Elle calcule une probabilité. « 92 % » veut dire qu'elle a "
      "trouvé beaucoup d'exemples très proches, pas qu'elle a compris "
      "l'animal."),
     ("Pourquoi les probabilities ?",
      "Parce qu'elle ne peut pas être sûre : elle ne fait que comparer "
      "des formes. La plupart des erreurs viennent d'exemples trop rares."),
     ("Comment devine-t-elle sans comprendre ? sans comprendre ?",
      "Elle ne devine pas au sens humain : elle mesure des ressemblances "
      "et attribue une valeur. La différence est importante.")],
    "Ne pas employer le mot « magicien » ni «ekt ». Parler de mesure de "
    "ressemblance."))

# ===========================================================================
# 12 — Exemple chiffré
# ===========================================================================
s = nouvelle("IDÉE 9", "Le même mécanisme, cinq fois par jour")
chapo(s, "Rien de nouveau dans chaque ligne : uniquement le même enchaînement, "
         "avec des données différentes.")
tableau(s, ["Ce que tu fais", "Ce que la machine a vu", "Ce qu'elle prédit"],
        [["Reconnaître un visage au portail", "des milliers de visages étiquetés", "« c'est lui »"],
         ["Compléter ton message", "des milliards de phrases", "le mot « instituteur »"],
         ["Choisir un itinéraire", "des millions de trajets et leurs temps", "20 min via la RN1"],
         ["Photographier une pièce à payer", "des millions de factures", "le montant de la ligne 4"],
         ["Filtrer un pourriel", "des milliards de messages classés", "probabilité de spam : 99 %"]],
        y=3.55, h=2.30, largeurs=[4.35, 3.85, 3.63])
ecrire_notes(s, notes(
    "IDÉE 9", "Le même mécanisme, cinq fois par jour",
    "Montrer que la phrase de la diapositive précédente s'applique "
    "concrètement à cinq gestes de leur journée.",
    "Je lis la première ligne entièrement, en détail, puis je "
    "demande à la classe de trouver les trois étapes dans les autres "
    "lignes. Ils les trouvent vite, et c'est exactement l'effet voulu. "
    "Je termine sur la ligne du pourriel : c'est celle où la confiance "
    "est le plus justifiée, parce qu'un faux positif coûte peu.",
    [("Pourquoi la ligne des photos du portal est-elle fiable ?",
      "Parce que l'écart entre un visage connu et un inconnu est net. Un "
      "modèle bien entraîné sur des milliers de personnes ne confond pas "
      "deux personnes."),
     ("Et si les données sont biaisées ?",
      "Alors les prédictions le sont aussi. C'est le sujet de la "
      "diapositive sur les données.")],
    "Ne pas commenter chaque ligne en détail : la classe doit faire le "
    "travail."))

# ===========================================================================
# 13 — Pourquoi elle se trompe
# ===========================================================================
s = nouvelle("IDÉE 10", "Pourquoi l'IA se trompe")
chapo(s, "Trois causes suffisent à expliquer presque toutes les erreurs. "
         "Aucune n'est un bug : ce sont les conséquences directes du "
         "mécanisme.")
grille(s, [("Données insuffisantes", "vu 100 chats roux, il ne reconnaît "
                                     "pas un chat noir", "warn"),
           ("Cas rares", "vu 10 000 photos mais aucun cas de panne rare", "warn"),
           ("Bonne réponse à la mauvaise question", "une réponse "
            "convaincante sur une question mal posée", "warn")],
       y=3.60, colonnes=3)
tf = add_textbox(s, 0.85, 5.70, 11.63, 0.55)
add_paragraph(tf, [("Conséquence : ", {"bold": True, "color": AMBER if False else NAVY}),
                   ("une erreur n'est pas un échec de l'IA. C'est la "
                    "conséquence logique de données insuffisantes. "
                    "D'où la règle : toujours vérifier.", {})],
              size=15, color=DARK, space_after=0)
ecrire_notes(s, notes(
    "IDÉE 10", "Pourquoi l'IA se trompe",
    "Enlever la peur de l'erreur et installer l'habitude de vérifier.",
    "Je prends l'exemple du chat noir et je le fais raconter : il y a trois "
    "ans, les téléphones reconnaissaient mal les visages foncés parce que "
    "les données d'entraînement étaient majoritairement européennes. Sur "
    "les cas rares, je prends l'exemple du médicament qui manque dans la "
    "base : la machine ne dit pas « je ne sais pas », elle dit la chose la "
    "plus proche. C'est ce point qui justifie toute la formation à la "
    "vérification.",
    [("Pourquoi l'IA ne dit-elle pas « je ne sais pas » ?",
      "Parce qu'elle a quand même une réponse plausible : elle ne distingue "
      "pas « je ne sais pas » de « ce qui est le plus probable ». C'est "
      "précisément ce qui rend ses erreurs si convaincantes."),
     ("Plus il y a de données, moins il y a d'erreurs ?",
      "Oui, jusqu'à un certain point. Le gain devient ensuite marginal, et "
      "le risque de biais augmente si les données sont déséquilibrées."),
     ("Comment je vérifie vite ?",
      "Je demande deux fois, de deux façons différentes. Si la réponse "
      "change, c'est qu'il n'y avait pas de sources.")],
    "Ne pas montrer l'exemple chat noir sans le rattacher aux données : "
    "la conclusion doit être le rôle des exemples."))

# ===========================================================================
# 14 — Ce que l'IA ne fait pas
# ===========================================================================
s = nouvelle("IDÉE 11", "Ce que l'IA ne fait pas")
chapo(s, "Quatre limites qui restent valables, quels que soient les "
         "progrès : elles découlent du mécanisme, pas de la puissance de "
         "la machine.")
grille(s, [("Elle ne comprend pas", "elle mesure des ressemblances, elle "
            "ne saisit pas l'intention", "plain"),
           ("Elle n'a pas de mémoire fiable", "tout ce qui n'est pas dans "
            "la fenêtre de conversation est oublié", "plain"),
           ("Elle n'a pas conscience", "aucune expérience vécue, aucune "
            "intention propre", "plain"),
           ("Elle n'est pas sourde aux biais", "elle reproduit les biais "
            "présents dans ses données", "plain")],
       y=3.70, colonnes=4)
ecrire_notes(s, notes(
    "IDÉE 11", "Ce que l'IA ne fait pas",
    "Poser les limites du mécanisme, pour que l'étudiant sache quand il "
    "peut et quand il ne peut pasdeleguer.",
    "Je passe vite sur les deux premières cases, qui sont évidentes, et je "
    "m'arrête sur la troisième. La question « est-ce qu'elle est vivante » "
    "revient à chaque cours. Ma réponse tient en une phrase : une IA n'a "
    "rien vécu, elle ne peut donc pas être maltraitée, mais elle ne peut "
    "pas non plus être responsable. C'est pour ça que la responsabilité "
    "d'un travail reste à l'étudiant.",
    [("Est-ce que cela va changer dans dix ans ?",
      "Les limites de mémoire et de biais sur les données vont s'atténuer. "
      "Le fait qu'elle ne vive rien, non : c'est structurel."),
     ("Comment puis-je savoir si elle comprend ?",
      "On ne peut pas. Ce qui est observable, c'est la régularité et la "
      "cohérence de ses réponses, pas sa compréhension."),
     ("Alors pourquoi on lui parle comme à une personne ?",
      "Parce que ça aide à formuler une bonne demande. Mais la relation "
      "est de l'ordre de l'outil, pas du partenaire.")],
    "Ne pas ouvrir le débat sur la conscience des machines : ce n'est pas "
    "l'objet du cours et cela displace les étudiants."))

# ===========================================================================
# 15 — Séparation partie 3
# ===========================================================================
s = prs.slides.add_slide(LAYOUT)
N[0] += 1
section(s, 3, "Les familles d'outils",
        "Six familles, cinq façons de raisonner, et une frontière récente : "
        "les agents, qui n'écrivent plus des phrases mais des fichiers.",
        ["La grille des 6 familles", "La boucle des agents",
         "Cursor et OpenCode", "Cinq modèles de raisonnement"],
        notes("PARTIE 3", "Les familles d'outils",
              "Passer du mécanisme aux outils, et faire apparaître la "
              "frontière entre assistant et agent.",
              "Transition. Je demande : si je vous demande de découper une "
              "tâche en étapes, quel outil citez-vous ? La plupart citent "
              "ChatGPT. Je révèle alors qu'il existe une famille qui ne "
              "répond pas mais qui agit, et qu'elle est déjà utilisée par "
              "des étudiants de la promotion. C'est la partie la plus "
              "nouvelle du cours.",
              [("Pourquoi commencer par les familles ?",
                "Parce que les produits changent tous les trois mois, les "
                "familles non. C'est la grille qui vous servira."),
               ("Je n'ai pas d'ordinateur portable, puis-je utiliser les "
                "agents ?",
                "Sur téléphone, très peu. Un agent modifie un dossier de "
                "fichiers : c'est le métier de l'ordinateur d'abord.")],
              "Ne pas transformer cette partie en catalogue de marques."))
add_footer(s, N[0], PIED)

# ===========================================================================
# 16 — Les 6 familles
# ===========================================================================
s = nouvelle("IDÉE 12", "Six familles d'outils, six usages")
chapo(s, "Le nom du produit change tous les trois mois. La famille, elle, "
         "ne change pas — et c'est elle qui détermine ce que l'outil peut "
         "faire pour vous.")
grille(s, [("Conversation", "ChatGPT, Claude,\nGemini, DeepSeek, Grok",
            "répond en texte", "primary"),
           ("Recherche", "Perplexity, Google IA", "cite ses sources", "primary"),
           ("Image et vidéo", "Midjourney, Runway, Firefly", "crée et édite", "alt"),
           ("Voix et audio", "Whisper, ElevenLabs", "transcrit, imite", "alt"),
           ("Agents", "Cursor, OpenCode,\nCopilot, Claude Code", "agit sur vos fichiers", "warn"),
           ("Locale", "Ollama, modèles téléchargés", "tourne chez vous", "warn")],
       y=3.60, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 12", "Six familles d'outils",
    "Donner une grille de repérage qui tient encore dans deux ans, malgré "
    "les changements de produits.",
    "Je demande d'abord à la classe de classer les outils qu'ils ont déjà "
    "utilisés dans ces six cases. Ils Placement gets it quickly. J'insiste "
    "sur les deux dernières cases, moins connues : les agents, qui agissent, "
    "et les modèles locaux, qui tournent sur la machine. Pour la locale, "
    "je précise l'intérêt concret : aucune donnée ne sort de chez soi. "
    "C'est la réponse à la question sur la vie privée.",
    [("Qu'est-ce qu'un agent, concrètement ?",
      "Un outil qui ne se contente pas de répondre : il utilise des outils "
      "sur votre machine — lire un fichier, en écrire un, lancer une "
      "commande. La prochaine diapositive y est consacrée."),
     ("Un modèle local, c'est moins bien ?",
      "Plus petit, donc moins capable sur les tâches complexes. Mais il "
      "fonctionne sans internet et n'envoie rien à personne."),
     ("Lequel dois-je choisir ?",
      "Celui qui résout votre problème aujourd'hui. Les produits se "
      "ressemblent plus qu'ils ne diffèrent sur les tâches de base.")],
    "Ne pas faire le tour d'écran des marques : la grille, pas le catalogue."))

# ===========================================================================
# 17 — La boucle des agents
# ===========================================================================
s = nouvelle("IDÉE 13", "L'agent ne répond pas, il agit")
chapo(s, "C'est la différence qui sépare un assistant de conversation d'un "
         "agent. Il ne rédige pas une phrase : il exécute une suite "
         "d'opérations sur vos fichiers.")
draw_flow(s, [("box", "1 · DEMANDE", "« corrige ce script »", "plain"),
              ("arrow", "→"),
              ("box", "2 · PLAN", "« je lis, je corrige, "
                                  "je teste »", "primary"),
              ("arrow", "→"),
              ("box", "3 · OUTILS", "lit, écrit, lance", "primary"),
              ("arrow", "→"),
              ("box", "4 · VÉRIFICATION", "le script marche-t-il ?", "alt")],
         0.75, 3.70, 11.83, 1.40)
tf = add_textbox(s, 0.85, 5.35, 11.63, 1.05)
add_paragraph(tf, [("Pourquoi le plan d'abord : ", {"bold": True, "color": NAVY}),
                   ("parce qu'il vous permet de l'arrêter avant qu'il "
                    "n'écrive. Un agent qui écrit sans demander votre avis "
                    "peut modifier dix fichiers pour rien. Demandez le "
                    "plan, lisez-le, puis validez.", {})],
              size=15, color=DARK, space_after=6, line_spacing=1.2)
ecrire_notes(s, notes(
    "IDÉE 13", "L'agent ne répond pas, il agit",
    "Faire comprendre la différence technique ET la règle de sécurité qui "
    "en découle.",
    "C'est la diapositive la plus nouvelle du cours et celle qui intéresse "
    "le plus la classe. Je fais la démonstration à mains levées : quand je "
    "dis « corrige ce script », un assistant de conversation me proposerait "
    "un code à recopier ; l'agent ouvre le fichier, le modifie, puis le "
    "teste. La différence pratique est immédiate. J'insiste ensuite sur le "
    "plan : c'est la seule règle de sécurité vraiment utile, et je demande "
    "à la classe de la reformuler. Elle l'écrit au tableau.",
    [("Est-ce que l'agent peut casser mon projet ?",
      "Oui, s'il n'a pas de filet de sécurité. D'où deux règles : toujours "
      "demander le plan d'abord, et garder une copie avant. Git fait "
      "exactement ça."),
     ("Comment savoir s'il a vraiment testé ?",
      "On lui demande de montrer la commande qu'il a exécutée et son "
      "résultat. S'il ne peut pas, il n'a pas testé."),
     ("Est-ce que ça coûte plus cher ?",
      "Oui, nettement : un agent qui travaille dix étapes consomme beaucoup "
      "plus qu'une réponse. À utiliser quand la tâche justifie le coût.")],
    "Ne pas laisser croire que l'agent est fiable par construction. "
    "L'exemple de l'agent qui teste sans le dire suffit."))

# ===========================================================================
# 18 — Deux familles
# ===========================================================================
s = nouvelle("IDÉE 14", "Deux familles : lui parler, ou coder avec elle")
chapo(s, "Vous connaissez déjà ces deux familles sans être informaticien. "
         "L'une aide à penser et à rédiger, l'autre construit des logiciels "
         "avec vous, sur votre propre disque dur.")
deux_colonnes(s,
              ("Assistants de conversation",
               "ChatGPT · Grok · Gemini · DeepSeek\n\n"
               "Vous écrivez une question en langue normale, vous obtenez "
               "une réponse rédigée. Rien n'est touché sur votre ordinateur.",
               "primary"),
              ("Assistants de code et agents",
               "OpenCode · Cursor · GitHub Copilot\n\n"
               "L'IA lit vos fichiers, en crée, les modifie, analyse un "
               "dossier entier. Elle construit le logiciel avec vous.",
               "alt"),
              y=3.70, h=2.30)
ecrire_notes(s, notes(
    "IDÉE 14", "Deux familles",
    "Conserver une diapositive qui fonctionne et fixer la frontière entre "
    "parler et agir.",
    "Cette diapositive existait déjà en version courte et elle marchait "
    "bien : je l'ai gardée telle quelle, en développant seulement la "
    "deuxième colonne. Je pose la question à la classe : « les deux vous "
    "parlent. Quelle est la vraie différence ? ». La réponse attendue est "
    "qu'un seul touche à vos fichiers. C'est exactement la frontière entre "
    "un assistant et un agent.",
    [("Quelle est la différence entre ChatGPT et Cursor ?",
      "ChatGPT parle : il répond avec des phrases dans la fenêtre de "
      "discussion. Cursor agit : il écrit et modifie directement les lignes "
      "de votre programme dans votre éditeur."),
     ("Est-ce que le second est réservé aux programmateurs ?",
      "Non. Il faut savoir décrire ce qu'on veut faire. L'IA écrit le "
      "code, mais c'est l'utilisateur qui décide de ce qui est juste et ce "
      "qui ne l'est pas."),
     ("Puis-je utiliser les deux ?",
      "Oui, et c'est même conseillé : on discute avec le premier, on "
      "exécute avec le second.")],
    "Ne pas laisser croire qu'un agent comprend mieux. Il agit "
    "seulement."))

# ===========================================================================
# 19 — Les 5 modèles de raisonnement
# ===========================================================================
s = nouvelle("IDÉE 15", "Cinq façons de demander, cinq résultats différents")
chapo(s, "La même question posée de cinq façons donne cinq réponses "
         "différentes. Choisir la bonne façon fait gagner plus de temps "
         "qu'un outil supplémentaire.")
tableau(s, ["Manière de demander", "Ce que vous obtenez", "Pour quoi"],
        [["Enchaîner les étapes", "un raisonnement détaillé, vérifiable",
          "comprendre, réviser"],
         ["Décomposer en parties", "un plan, puis une partie à la fois",
          "un exposé, un mémoire"],
         ["Croiser plusieurs IA", "un consensus, et les désaccords",
          "une information importante"],
         ["Faire critiquer", "une relecture hostile, utile",
          "avant de rendre un devoir"],
         ["Demander le plan d'abord", "un programme d'action avant l'exécution",
          "toute tâche sur des fichiers"]],
        y=3.55, h=2.30, largeurs=[3.45, 4.45, 3.93])
ecrire_notes(s, notes(
    "IDÉE 15", "Cinq façons de demander",
    "Montrer que la qualité vient surtout de la façon de formuler la "
    "demande, pas du choix de l'outil.",
    "Je prends la dernière ligne comme conclusion : demander le plan d'abord "
    "est la seule technique qui change tout quand on travaille sur des "
    "fichiers. Les quatre autres sont des variantes de la première. Je "
    "demande à la classe de citer une question récente et on cherche ensemble "
    "laquelle des cinq méthodes aurait donné une meilleure réponse.",
    [("Comment je sais laquelle choisir ?",
      "Si la question est simple, n'importe laquelle suffit. Si la réponse "
      "compte et qu'elle doit être vérifiable, croisez : demandez la même "
      "chose à deux IA."),
     ("Faire critiquer, ça ne sert à rien ?",
      "Au contraire. Une relecture demandée à froid trouve les trous que "
      "vous ne voyez plus parce que vous écrivez depuis deux heures."),
     ("Le plan d'abord, ça prend du temps ?",
      "Trente secondes. Il évite dix minutes de corrections quand l'IA a "
      "compris de travers.")],
    "Ne pas transformer ça en liste de commandes à réciter. Donner le "
    "principe : penser le résultat avant de demander."))

# ===========================================================================
# 20 — Synthèse partie 3
# ===========================================================================
s = nouvelle("IDÉE 16", "Choisir son outil en trois questions")
grille(s, [("Quel résultat ?", "une réponse en texte, un fichier, une "
            "modification, une image ?", "primary"),
           ("Quel risque ?", "données confidentielles, fichiers importants, "
            "usage au quotidien ?", "alt"),
           ("Quel coût ?", "gratuit avec limites, ou abonnement ? Le temps "
            "compté aussi.", "plain")],
       y=3.70, colonnes=3)
ecrire_notes(s, notes(
    "IDÉE 16", "Choisir en trois questions",
    "Fermer la partie outils sur une méthode, pas sur une liste.",
    "Je récapitule : la famille se choisit selon le résultat recherché, le "
    "risque décide entre un outil distant et un modèle local, le coût "
    "arbitre en dernier. C'est cette grille qu'ils utiliseront le lendemain. "
    "Je la fais noter, elle est plus utile que la liste des outils, qui "
    "sera périmée dans six mois.",
    [("Et si je ne sais pas ?",
      "Commence par la conversation : c'est le risque le plus faible. Tu "
      "passeras à l'agent quand tu voudras un fichier modifié."),
     ("Le modèle local est-il vraiment confidentiel ?",
      "Si le modèle est téléchargé chez toi, oui : rien ne sort. Si tu "
      "utilises un service en ligne, non, même avec un compte.")],
    "Ne pas recommander un outil précis comme favorite : ils changent, "
    "la méthode non."))

# ===========================================================================
# 21 — Séparation partie 4
# ===========================================================================
s = prs.slides.add_slide(LAYOUT)
N[0] += 1
section(s, 4, "Cinq cas concrets",
        "Les six problèmes de la deuxième diapositive : voici comment on les "
        "résout, et ce que l'IA ne fera pas à votre place.",
        ["Réparer et flasher un appareil", "Créer un site web",
         "Réviser un examen", "Rédiger et traduire",
         "Utiliser l'IA pour enseigner le FLE"],
        notes("PARTIE 4", "Cinq cas concrets",
              "Résoudre les problèmes posés au début du cours.",
              "Transition, et promesse tenue : je reviens à nos six problèmes "
              "du début. Je les reprends un par un, et pour chacun je nomme "
              "l'astuce correspondante du site. Le lien avec le module en "
              "ligne est ainsi visible : les 152 astuces ne sont pas une "
              "liste à part, c'est le prolongement de ce cours.",
              [("Les six problèmes étaient donc tous traitables ?",
                "Cinq sur six. Le téléphone qui ne charge plus relève du "
                "matériel : l'IA aide à chercher la cause, elle ne répare "
                "pas. Je le dis clairement."),
               ("Où est-ce que je trouve ces astuces ?",
                "Sur le site du module, rubrique Astuces : 152 fiches, "
                "classées par domaine.")],
              "Ne pas survoler les cinq cas : c'est la partie que la classe "
              "photographie."))
add_footer(s, N[0], PIED)

# ===========================================================================
# 22 — Cas 1 : réparer
# ===========================================================================
s = nouvelle("IDÉE 17", "Cas 1 — Réparer, flasher, diagnostiquer")
chapo(s, "L'IA ne répare rien. Elle évite la recherche : en trente secondes "
         "de questions bien posées, onEconomise une heure.")
tableau(s, ["Le problème réel", "La question à poser", "Le gain"],
        [["Comprendre un schéma", "« ce circuit alimente quel composant ? »",
          "évite 30 min de fouille"],
         ["Identifier une pièce", "« valeur et tension de ce composant ? »",
          "on commande la bonne"],
         ["Lire un code d'erreur", "« que signifie ce code sur ce modèle ? »",
          "plus de tâtonnement"],
         ["Choisir un script de flash", "« compatible avec ce modèle exact ? »",
          "on ne bloque pas l'appareil"],
         ["Rédiger la fiche d'intervention", "« mets en forme ces mesures »",
          "10 min gagnées à la fin"]],
        y=3.50, h=2.45, largeurs=[3.25, 5.45, 3.13])
ecrire_notes(s, notes(
    "IDÉE 17", "Cas 1 : réparer et flasher",
    "Montrer que l'IA sert dans un métier manuel, et marquer la limite "
    "avec l'exemple du téléphone bloqué.",
    "Je raconte le cas réel d'une étudiante de terminale : téléphone qui "
    "ne charge plus, elle a voulu le flasher, un script mal adapté a mal "
    "verrouillé l'appareil. L'IA avait bien répondu, mais elle ne pouvait "
    "pas savoir que sa copie était périmée. Le script existe, la procédure "
    "était documentée — et le résultat a été un appareil mort. Conclusion : "
    "l'IA gagne du temps, elle ne prend pas la responsabilité.",
    [("Est-ce que l'IA peut vraiment réparer ?",
      "Non. Elle accélère la recherche : causes probables, datasheets, "
      "codes d'erreur. La mesure, le démontage et la décision restent à "
      "l'humain."),
     ("Flasher un téléphone, c'est dangereux ?",
      "Oui. Un script mal adapté peut verrouiller définitivement l'appareil. "
      "Il faut vérifier la compatibilité exacte du modèle avant de lancer "
      "quoi que ce soit."),
     ("Et si l'appareil est encore sous garantie ?",
      "Le flash annule la garantie et peut rendre l'appareil inutilisable. "
      "C'est la première vérification à faire.")],
    "Ne pas donner l'impression que tout est réparable par IA. "
    "L'exemple du téléphone bloqué sert précisément à éviter cette "
    "confiance."))

# ===========================================================================
# 23 — Cas 2 : créer un site web
# ===========================================================================
s = nouvelle("IDÉE 18", "Cas 2 — Un site web pour le club, en un cours")
chapo(s, "Le schéma d'un site est simple : trois fichiers. L'agent écrit le "
         "code, vous choisissez ce qui est juste et ce qui ne l'est pas.")
draw_flow(s, [("box", "PAGE", "HTML\nle texte et la structure", "plain"),
              ("arrow", "→"),
              ("box", "STYLE", "CSS\nles couleurs et la mise en page", "primary"),
              ("arrow", "→"),
              ("box", "SCRIPT", "JavaScript\nles interactions", "primary"),
              ("arrow", "→"),
              ("box", "MISE EN LIGNE", "hébergé, visible par tous", "alt")],
         0.75, 3.65, 11.83, 1.35)
tf = add_textbox(s, 0.85, 5.25, 11.63, 1.15)
add_paragraph(tf, [("Les 4 questions à poser dans l'ordre : ", {"bold": True, "color": NAVY}),
                   ("① quel est le contenu exact (liste des membres, "
                    "dates, photos) · ② quelles couleurs et quel style · "
                    "③ quelles pages (accueil, à propos, contact) · "
                    "④ où l'héberger, gratuitement.", {})],
              size=14.5, color=DARK, space_after=0, line_spacing=1.2)
ecrire_notes(s, notes(
    "IDÉE 18", "Cas 2 : créer un site web",
    "Montrer qu'un site web est un projet faisable en classe, et faire "
    "comprendre que l'IA ne fait pas le choix du contenu.",
    "Je pose la question : « qu'est-ce qu'un site web, techniquement ? ». "
    "Personne ne sait. Je révèle qu'il n'y a que trois fichiers : le texte "
    "en HTML, le style en CSS, le comportement en JavaScript. C'est ce "
    "déplacement qui démystifie le sujet. Les quatre questions de la "
    "diapositive sont à écrire au tableau : elles constituent le cahier "
    "des charges réel, et c'est la partie qui appartient à l'étudiant.",
    [("Combien de temps pour un vrai site ?",
      "Une à deux heures pour une page correcte, si le contenu est prêt. "
      "Le contenu est toujours le plus long à écrire : l'IA ne décide pas "
      "de vos dates ni de vos photos."),
     ("Faut-il savoir coder ?",
      "Non pour le résultat. Oui pour vérifier : il faut pouvoir relire ce "
      "qui a été produit, sinon on ne sait pas ce qu'on publie."),
     ("Hébergement ?",
      "GitHub Pages, Netlify ou Cloudflare Pages offrent un hébergement "
      "gratuit. Le site est alors accessible par une adresse publique.")],
    "Ne pas promettre « un site en dix minutes ». Le délai honnête est une "
    "à deux heures, contenu compris."))

# ===========================================================================
# 24 — Cas 3 : réviser
# ===========================================================================
s = nouvelle("IDÉE 19", "Cas 3 — Réviser un examen avec l'IA")
grille(s, [("Explication en deux niveaux",
            "une version simple, une version technique. Vous comprenez, et "
            "vous savez réciter pour l'examen.", "primary"),
           ("Cartes mémoire",
            "une notion par carte, réponse de cinq mots maximum. "
            "Import direct dans Anki ou Quizlet.", "alt"),
           ("QCM d'entraînement",
            "dix questions, corrigées, avec l'explication de chaque "
            "réponse. Vous voyez vos lacunes.", "primary"),
           ("Explication à rebours",
            "« explique-moi la méthode Feynman » : vous expliquez, "
            "l'IA repère ce qui manque.", "warn")],
       y=3.65, colonnes=4)
ecrire_notes(s, notes(
    "IDÉE 19", "Cas 3 : réviser un examen",
    "Donner quatre méthodes de révision vérifiables, toutes basées sur le "
    "rappel actif plutôt que la relecture.",
    "Je commence par un constat que tout le monde connaît : relire trois "
    "fois son cours ne fait pas retenir. Le rappel actif, c'est extraire de "
    "la mémoire, et les quatre méthodes ici le font. Je m'attarde sur les "
    "cartes mémoire, parce que la règle des cinq mots change tout : une "
    "réponse trop longue transforme la révision en relecture. "
    "L'explication à rebours est la plus formatrice et la moins connue.",
    [("Pourquoi cinq mots maximum ?",
      "Parce qu'au-delà, tu lis la réponse au lieu de la produire. La carte "
      "ne doit servir qu'à vérifier ce que tu sais déjà dedans."),
     ("Combien de cartes par chapitre ?",
      "Une vingtaine pour un chapitre de taille moyenne. Au-delà, on "
      "commence à répéter au lieu d'apprendre."),
     ("Puis-je utiliser l'IA pour noter mon cours ?",
      "Oui, à condition de vérifier les résumés : l'IA condense bien mais "
      "supprime parfois ce qui était exactement ce que l'examinateur "
      "voulait.")],
    "Ne pas vendre Anki comme une obligation. La méthode s'applique avec "
    "des fiches papier."))

# ===========================================================================
# 25 — Cas 4 : rédiger, corriger, traduire
# ===========================================================================
s = nouvelle("IDÉE 20", "Cas 4 — Rédiger, corriger, traduire en 3 langues")
grille(s, [("Français", "le plus fiable. Dépouillez vos textes, "
            "l'IA respecte bien les nuances.", "primary"),
           ("Anglais", "très bon niveau. Attention aux faux amis et au "
            "registre : précisez « académique » ou « familier ».", "primary"),
           ("Arabe", "correct, mais fragile sur les formes verbales et le "
            "genre. Faites toujours relire par un natif.", "warn"),
           ("Traduction littéraire", "traduit le sens, pas le tour. "
            "Jamais pour un texte que vous devez signer.", "warn")],
       y=3.65, colonnes=4)
ecrire_notes(s, notes(
    "IDÉE 20", "Cas 4 : Rédiger, corriger, traduire",
    "Donner le niveau de confiance réel par langue — c'est la moitié de la "
    "réponse.",
    "Je donne le niveau de confiance par langue, ce qui est plus utile "
    "qu'un optimisme général. Le point sur l'arabe est important pour cette "
    "promotion : la traduction automatique s'améliore, mais les formes "
    "verbales et le genre restent fautifs. Le conseil est simple : "
    "traduisez, puis faites relire. Je rappuie sur le registre, parce que "
    "c'est là que se joue la différence entre un texte d'examen et un texte "
    "de conversation.",
    [("Est-ce que je peux rendre un texte traduit ?",
      "Seulement si l'original est dans une autre langue et si vous "
      "déclarez la traduction. Un texte integralement écrit par l'IA et "
      "signé sans mention n'est pas admissible."),
     ("Pourquoi préciser le registre ?",
      "Sans consigne, l'IA choisit un registre moyen. « Explique comme à "
      "un élève de 6e » ou « pour un jury universitaire » change "
      "complètement le résultat."),
     ("Elle peut corriger mon orthographe ?",
      "Oui, et c'est même l'usage le plus rentable : demander « corrige "
      "ce texte sans changer le sens ».")],
    "Ne pas laisser croire que tout se traduit également. Les trois "
    "niveaux de confiance sont le message."))

# ===========================================================================
# 26 — Cas 5 : enseigner le FLE
# ===========================================================================
s = nouvelle("IDÉE 21", "Cas 5 — Préparer un cours de FLE avec l'IA")
chapo(s, "Plusieurs d'entre vous enseigneront l'anglais. C'est le domaine "
         "où l'IA vous fait gagner le plus de temps, parce que le matériel "
         "est standardisé.")
grille(s, [("Fiche de vocabulaire", "20 mots avec le niveau CECRL, des "
            "exemples et un exercice", "primary"),
           ("Activités de classe", "jeux de rôle, jeux de rôle grammaticaux, "
            "textes à trous", "alt"),
           ("Évaluation corrigée", "QCM, exercices, barème, et l'explication "
            "de chaque erreur attendue", "primary"),
           ("Adaptation", "un même texte rendu plus facile pour un niveau "
            "déterminé, sans le réécrire", "alt")],
       y=3.65, colonnes=4)
ecrire_notes(s, notes(
    "IDÉE 21", "Cas 5 : enseigner le FLE",
    "Montrer un usage directement professionnel pour cette promotion, et "
    "déplacer l'IA du côté de l'enseignant.",
    "Cette diapositive est celle qui les concerne le plus : plusieurs "
    "seront en stage ou en poste dans des écoles. Je précise d'emblée que "
    "l'IA ne prépare pas à la place de l'enseignant : elle prépare les "
    "documents que l'enseignant valide. L'adaptation de niveau est "
    "l'exemple le plus convaincant : on donne un texte, on demande la même "
    "chose en A2 et en B2, et on compare. Ça prend deux minutes.",
    [("Les documents produits sont-ils utilisables tels quels ?",
      "Comme brouillon, oui directement. Avant diffusion, il faut les "
      "relire : le niveau annoncé peut être faux, et une erreur dans un "
      "support pédagogique se voit immédiatement."),
     ("Comment vérifier le niveau annoncé ?",
      "En le faisant tester par un élève du niveau visé. C'est le seul "
      "contrôle qui fonctionne."),
     ("Et si les élèves utilisent l'IA aussi ?",
      "C'est déjà le cas. Le cours 12 du module leur donne une charte "
      "d'usage propre, plutôt que de leur dire de ne pas s'en servir.")],
    "Ne pas placer cette diapositive avant les cas généraux : elle n'a de "
    "sens qu'après la colonne « agents »."))

# ===========================================================================
# 27 — Séparation partie 5
# ===========================================================================
s = prs.slides.add_slide(LAYOUT)
N[0] += 1
section(s, 5, "Les vraies astuces du terrain",
        "Ce que font les étudiants qui en tirent le plus : des gestes "
        "simples, ningún outil interdit, aucune règle de produit violée.",
        ["Contourner les limites sans tricher",
         "Les quatre pièges à éviter", "La charte en sept lignes",
         "Cinq gestes à retenir"],
        notes("PARTIE 5", "Les vraies astuces du terrain",
              "Donner les solutions qui fonctionnent, et la ligne de "
              "conduite à tenir.",
              "Dernière partie, et la plus attendue. Je dis d'emblée que rien "
              "ici ne viole les conditions d'utilisation d'un outil. Changer "
              "d'outil quand on est bloqué est normal et légal. Créer des "
              "comptes fantômes ne l'est pas : on risque de perdre le "
              "compte principal. Le reste porte sur les pièges et la charte.",
              [("Pourquoi ne pas simplement payer ?",
                "Pour beaucoup, l'abonnement n'est pas une option. Les "
                "solutions gratuites présentées ici suffisent pour la "
                "quasi-totalité des travaux."),
               ("Si je suis bloqué pendant un examen ?",
                "Personne ne vous sanctionne pour cela, mais ce n'est pas là "
                "qu'il faut apprendre : servez-vous-en la semaine "
                "d'avant.")],
              "Ne pas vendre cette partie comme un catalogue de "
              "contournement. Le message : contourner une attente, jamais "
              "une règle."))
add_footer(s, N[0], PIED)

# ===========================================================================
# 28 — Les astuces de terrain
# ===========================================================================
s = nouvelle("IDÉE 22", "Sept solutions qui marchent vraiment")
chapo(s, "Vous allez être bloqués. Voilà ce que font les étudiants qui "
         "n'arrêtent jamais de travailler — sans créer de compte fantôme et "
         "sans script de contournement.")
tableau(s, ["Le problème", "Ce qui marche"],
        [["Le quota est atteint", " regrouper 5 questions en un seul message"],
         ["Toujours bloqué", " changer d'outil : ChatGPT, Gemini, Claude, DeepSeek"],
         ["Le site ne s'ouvre plus", " l'application mobile fonctionne souvent"],
         ["Trop lent aux heures de pointe", " travailler aux heures creuses"],
         ["C'est cher", " chercher l'offre étudiante officielle de l'université"],
         ["La session va expire", " copier la réponse avant de la perdre"],
         ["La réponse est trop générique", " rôle + contexte + tâche + format + contraintes"]],
        y=3.45, h=2.50, largeurs=[4.55, 7.28])
ecrire_notes(s, notes(
    "IDÉE 22", "Sept solutions qui marchent vraiment",
    "Donner les contournements légaux, et le dire explicitement : c'est ce "
    "qui rend cette diapositive défendable.",
    "Je commence par la ligne du bas, la formule magique : rôle, contexte, "
    "tâche, format, contraintes. Cinq mots, et c'est ce qui explique la "
    "plupart des « l'IA ne comprend pas ». Ensuite j'insiste sur un point "
    "qui m'est déjà arrivé : il ne faut jamais créer de comptes fantômes "
    "pour contourner un quota. Cela viole les conditions d'utilisation, on "
    "se fait bannir, et on donne une mauvaise image du métier. Changer "
    "d'outil est légal et tout aussi efficace. Si un étudiantзpolitics "
    "contourne le quota, il met son compte en danger et le perte de temps "
    "est plus importante que le gain.",
    [("Et si je crée plusieurs comptes ?",
      "C'est la seule solution interdite. Cela viole les conditions "
      "d'utilisation, le compte principal est banni, et on perd "
      "l'historique de travail. Changer d'outil fait le même effet sans "
      "aucun risque."),
     ("Pourquoi l'application mobile fonctionne-t-elle ?",
      "Parce que les quotas sont souvent gérés séparément sur le mobile. "
      "C'est une marge, pas une règle : ça peut être corrigé."),
     ("La formule magique, c'est vraiment cinq mots ?",
      "Cinq éléments : le rôle que vous donnez à l'IA, votre contexte, la "
      "tâche précise, le format attendu, et les contraintes. Sans l'un "
      "des cinq, elle invente le reste."),
     ("Il y a des études étudiantes ?",
      "Oui : beaucoup d'universités et d'entreprises offrent un accès "
      "gratuit ou à tarif réduit. Cela se demande au secrétariat "
      "pédagogique.")],
    "Ne jamais faire la promotion d'un contournement qui casse les "
    "conditions d'utilisation. Cette diapositive doit pouvoir être "
    "montrée à la direction du département sans problème."))

# ===========================================================================
# 29 — Les quatre pièges
# ===========================================================================
s = nouvelle("IDÉE 23", "Les quatre pièges, et la charte")
grille(s, [("1 · Elle invente", "une référence, un chiffre, un auteur. "
            "Toujours vérifier avant de citer.", "warn"),
           ("2 · Elle se trompe sur vous", "elle ne sait pas votre niveau, "
            "votre module, votre programme : dites-le.", "warn"),
           ("3 · Elle oublie", "au-delà de quelques pages, la conversation "
            "n'est plus reliable : reprenez le contexte.", "warn"),
           ("4 · Elle expose", "coller un nom, une adresse, une photo de "
            "carte d'étudiant : ne le faites jamais.", "warn")],
       y=3.60, colonnes=4)
tf = add_textbox(s, 0.85, 5.70, 11.63, 0.60)
add_paragraph(tf, [("La charte en une ligne : ", {"bold": True, "color": NAVY}),
                   ("l'IA propose, l'humain décide, l'étudiant assume.", {})],
              size=16, color=DARK, space_after=0)
ecrire_notes(s, notes(
    "IDÉE 23", "Les quatre pièges et la charte",
    "Terminer la formation sur les limites, puis donner une phrase à "
    "retenir : l'IA propose, l'humain décide, l'étudiant assume.",
    "Je prends le piège 1 avec un exemple vérifié : les références "
    "inventées existent bel et bien, avec un auteur réel, une année "
    "plausible et un titre qui existe presque. On les vérifie en trente "
    "secondes dans un moteur de recherche. Le piège 3 est le plus "
    "surprenant pour les étudiants : au bout de quelques pages, la "
    "conversation n'a plus aucun sens et l'IA continue avec assurance. "
    "Il faut entonces relancer avec un résumé.",
    [("Comment vérifier une référence rapidement ?",
      "Copier le titre exact dans un moteur de recherche, et ouvrir le lien "
      "de l'article. Trente secondes suffisent à éliminer une référence "
      "inventée."),
     ("Pourquoi ne pas coller de données personnelles ?",
      "Tout ce que vous envoyez peut être conservé et réutilisé pour "
      "l'entraînement. Nom, adresse, carte d'étudiant : rien de tout cela ne "
      "doit partir."),
     ("Et les données de l'université ?",
      "Pire : les notes de vos étudiants, leurs copies, leurs noms. Ce sont "
      "des données sensibles, avec des obligations légales.")],
    "Ne pas terminer sur les pièges : finir sur la charte, pour que la "
    "classe sorte avec une règle et non avec des craintes."))

# ===========================================================================
# 30 — Les cinq gestes
# ===========================================================================
s = nouvelle("IDÉE 24", "Cinq gestes, et ton défi de la semaine")
grille(s, [("1 · Commence par l'exemple", "ne demande jamais « explique "
            "l'IA » : donne un cas précis.", "primary"),
           ("2 · Rôle + contexte + tâche", "les trois premiers mots qui "
            "changent la qualité d'une réponse.", "primary"),
           ("3 · Fais critiquer avant de rendre", "une relecture à froid "
            "trouve ce que tu ne vois plus.", "alt"),
           ("4 · Demande le plan", "sur toute tâche qui touche un fichier, "
            "avant toute écriture.", "alt"),
           ("5 · Vérifie toujours", "une référence, un chiffre, un nom : "
            "trente secondes de vérification.", "warn")],
       y=3.45, colonnes=5)
tf = add_textbox(s, 0.85, 5.40, 11.63, 0.95)
add_paragraph(tf, [("Ton défi pour la semaine : ", {"bold": True, "color": NAVY}),
                   ("① résous un des six problèmes de la deuxième "
                    "diapositive ② fabrique dix cartes mémoire sur un "
                    "chapitre ③ demande le plan avant d'écrire dans un "
                    "fichier. Puis raconte le résultat au prochain cours.", {})],
              size=15, color=DARK, space_after=0, line_spacing=1.2)
ecrire_notes(s, notes(
    "IDÉE 24", "Cinq gestes et le défi de la semaine",
    "Fermer sur cinq actions, pas sur un résumé. Donner une tâche "
    "concrète pour la semaine.",
    "Je fais photographier cette diapositive par la classe : ce sont les "
    "cinq gestes qu'ils doivent retrouver sans moi. Le défi de la semaine "
    "reprend volontairement les six problèmes de l'ouverture : le premier "
    "point ferme la boucle du cours. Je précise que je veux du "
    "retournement d'expérience, pas des captures d'écran. Terminer en "
    "laissant deux minutes pour les questions réelles.",
    [("Pourquoi ces cinq gestes et pas d'autres ?",
      "Parce qu'ils sont les seuls qui changent le résultat sans changer "
      "d'outil. Les quatre premiers costsent rien, le cinquième coûte "
      "trente secondes."),
     ("Le défi est-il noté ?",
      "Non, mais il sera évalué à l'oral : c'est plus utile qu'une note et "
      "cela oblige à expérimenter vraiment."),
     ("Puis-je avoir le cours en français et en anglais ?",
      "Le module est en français, filière français. Les versions autres "
      "sont sur le site, en anglais et en arabe.")],
    "Ne pas conclure par « des questions ? » tout seul : lancer le défi "
    "avant, pour que la classe parte avec une tâche."))

# ===========================================================================
# Écriture
# ===========================================================================
sortie = sys.argv[1] if len(sys.argv) > 1 else DEFAUT
prs.save(sortie)
print("  diapositives : %d" % len(prs.slides))
print("  fichier      : %s" % sortie)
