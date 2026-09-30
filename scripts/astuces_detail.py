#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, une par entrée.

Chaque entrée porte le numéro de l'astuce (celui affiché dans le petit
carré bleu) et le HTML de l'explication longue. Le script
`ajouter_boutons_astuces.py` s'en sert pour insérer le bouton dépliant
juste après chaque astuce.

On écrit ici les explications dans l'ordre où l'on veut les produire :
ajouter une entrée suffit, relancer le script d'insertion met la page à
jour sans toucher aux autres.

Gabarit d'une explication :
    <h4>1. Titre de la partie</h4>
    <p>…</p>
    <ul><li>…</li></ul>
    <pre>code</pre>
    <div class="tip">…</div>   et   <div class="warn">…</div>
"""

# ---------------------------------------------------------------------------
ASTUCES = {}

# Version longue, écrite à la main : c'est le gabarit de référence.
# ASTUCES[1] : « Regrouper → décaler → alterner »
# ASTUCES[2] : « Alterner ChatGPT · Gemini · Claude · DeepSeek · Grok »

ASTUCES[2] = """
<h4>1. Le texte de l'astuce</h4>
<div class="prompt-box"><strong>Alterner ChatGPT · Gemini · Claude · DeepSeek · Grok</strong><br>
Leurs quotas sont indépendants. Ouvre les 4–5 en onglets permanents. Même question →
4 réponses en 30 secondes → tu vois immédiatement qui est le plus précis aujourd'hui.</div>

<h4>2. Que veut dire « alterner » ici ?</h4>
<p>Alterner, c'est <strong>ne pas dépendre d'un seul outil</strong>. Au lieu de rester
bloqué sur ChatGPT quand il affiche « limite atteinte », tu passes à un autre assistant.</p>
<p>L'idée est simple :</p>
<ul>
  <li>Chaque IA a <strong>son propre quota</strong>.</li>
  <li>Chaque IA a <strong>ses forces et ses faiblesses</strong>.</li>
  <li>Chaque IA est plus ou moins précise selon le jour, le sujet et la langue.</li>
</ul>
<p>Donc, en les utilisant <strong>en parallèle</strong>, tu ne restes jamais bloqué et tu
obtiens souvent une meilleure réponse.</p>

<h4>3. Pourquoi les quotas sont indépendants ?</h4>
<table>
  <tr><th>Outil</th><th>Qui le gère ?</th><th>Quota</th></tr>
  <tr><td>ChatGPT</td><td>OpenAI</td><td>Séparé</td></tr>
  <tr><td>Gemini</td><td>Google</td><td>Séparé</td></tr>
  <tr><td>Claude</td><td>Anthropic</td><td>Séparé</td></tr>
  <tr><td>DeepSeek</td><td>DeepSeek</td><td>Séparé</td></tr>
  <tr><td>Grok</td><td>xAI / X</td><td>Séparé</td></tr>
</table>
<p>Cela veut dire : si ChatGPT est bloqué, Gemini peut encore fonctionner. Si Gemini est
bloqué, Claude peut encore fonctionner. En ouvrant 4 ou 5 onglets, tu as <strong>4 ou 5
réservoirs de quota différents</strong>. Quand l'un est vide, tu passes au suivant.</p>

<h4>4. Comment faire concrètement ?</h4>
<ol>
  <li><strong>Ouvre les onglets.</strong> ChatGPT, Gemini, Claude, DeepSeek, Grok.
      Épingle-les pour les retrouver vite.</li>
  <li><strong>Prépare une seule question.</strong> La même pour tous, sinon tu ne peux
      rien comparer.</li>
  <li><strong>Colle partout.</strong> Un copier-coller, cinq envois.</li>
  <li><strong>Compare.</strong> Repère la plus claire, la plus précise, celle qui donne
      des exemples réels, celle qui <em>avoue ses limites</em> au lieu d'inventer.</li>
  <li><strong>Approfondis avec la meilleure.</strong> Et si tu veux aller plus loin,
      demande à un second outil de vérifier la réponse du premier.</li>
</ol>

<h4>5. Les forces de chaque outil</h4>
<table>
  <tr><th>Outil</th><th>Points forts</th><th>Quand l'utiliser</th></tr>
  <tr><td><strong>ChatGPT</strong></td><td>Rédaction, explication, correction, code</td><td>Travail rédactionnel et réflexion</td></tr>
  <tr><td><strong>Gemini</strong></td><td>PDF, images, intégration Google</td><td>Documents longs, multimédia</td></tr>
  <tr><td><strong>Claude</strong></td><td>Textes longs, style fluide, nuances</td><td>Rapports, articles, synthèses</td></tr>
  <tr><td><strong>DeepSeek</strong></td><td>Maths, code, gratuit</td><td>Calculs, scripts, logique</td></tr>
  <tr><td><strong>Grok</strong></td><td>Actualité, X/Twitter, ton direct</td><td>Infos récentes, veille</td></tr>
</table>
<p>Ce tableau n'est pas absolu : les modèles évoluent. Mais il donne une bonne base.</p>

<h4>6. Pourquoi c'est une excellente stratégie ?</h4>
<ul>
  <li><strong>Tu ne restes jamais bloqué.</strong> Un outil bloque ? Le suivant prend le relais.</li>
  <li><strong>Tu compares les réponses.</strong> Une IA peut se tromper, une autre peut voir l'erreur.</li>
  <li><strong>Tu gagnes du temps.</strong> Au lieu d'attendre 3 heures, tu as une réponse en 30 secondes.</li>
  <li><strong>Tu découvres le meilleur outil par tâche.</strong> Tu apprends à les utiliser au bon moment.</li>
  <li><strong>Tu améliores la qualité.</strong> Si 3 IA disent la même chose, c'est probablement fiable ; si elles divergent, tu sais qu'il faut vérifier.</li>
</ul>

<h4>7. Exemple complet</h4>
<p><strong>Sujet :</strong> « l'impact des réseaux sociaux sur les adolescents ».</p>
<div class="prompt-box">Explique l'impact des réseaux sociaux sur les adolescents en
5 points concrets, avec 1 exemple réel pour chaque point.
Si tu n'es pas sûr d'un fait, dis-le clairement.</div>
<p>Résultats possibles :</p>
<ul>
  <li><strong>ChatGPT</strong> — bonne structure, exemples scolaires.</li>
  <li><strong>Gemini</strong> — cite des études, mais parfois trop général.</li>
  <li><strong>Claude</strong> — réponse nuancée, style fluide.</li>
  <li><strong>DeepSeek</strong> — plus factuel, moins d'exemples.</li>
  <li><strong>Grok</strong> — cite des actualités récentes.</li>
</ul>
<p>Tu gardes la meilleure, tu vérifies les faits, tu rédiges.</p>

<h4>8. Les erreurs à éviter</h4>
<table>
  <tr><th>Erreur</th><th>Pourquoi c'est mauvais</th></tr>
  <tr><td>Poser une question différente sur chaque outil</td><td>Tu ne peux plus comparer</td></tr>
  <tr><td>Coller des données personnelles partout</td><td>Plus tu colles, plus tu t'exposes</td></tr>
  <tr><td>Croire une seule IA sans vérifier</td><td>Une IA peut inventer</td></tr>
  <tr><td>Créer 10 comptes pour contourner les limites</td><td>Risque de violation des conditions d'utilisation</td></tr>
  <tr><td>Ne pas relire</td><td>L'IA ne remplace pas ton jugement</td></tr>
</table>

<h4>9. Le lien avec l'astuce n° 1</h4>
<p>L'astuce n° 1 disait <strong>« Regrouper → Décaler → Alterner »</strong>. Le mot
« Alterner » renvoie directement à cette astuce n° 2. Les deux fonctionnent ensemble :</p>
<ul>
  <li><strong>Regrouper</strong> = 1 seul prompt au lieu de 5.</li>
  <li><strong>Décaler</strong> = attendre la recharge du quota.</li>
  <li><strong>Alterner</strong> = passer à un autre outil.</li>
</ul>

<h4>10. Le réflexe à retenir</h4>
<div class="reflexe">
  <strong>« Avant de paniquer parce qu'un outil est bloqué, quel autre outil puis-je ouvrir maintenant ? »</strong><br><br>
  Et avant de coller une question : <strong>« Puis-je poser la même question à 3 IA pour comparer ? »</strong>
</div>

<h4>11. Résumé de l'astuce n° 2</h4>
<table>
  <tr><th>Point</th><th>Explication</th></tr>
  <tr><td><strong>Principe</strong></td><td>Utiliser plusieurs IA en parallèle</td></tr>
  <tr><td><strong>Pourquoi</strong></td><td>Quotas indépendants + comparaison des réponses</td></tr>
  <tr><td><strong>Comment</strong></td><td>Ouvrir 4–5 onglets, coller la même question, comparer</td></tr>
  <tr><td><strong>Avantage</strong></td><td>Ne jamais rester bloqué, améliorer la qualité</td></tr>
  <tr><td><strong>Attention</strong></td><td>Ne pas coller de données sensibles partout</td></tr>
  <tr><td><strong>Réflexe</strong></td><td>« Quel autre outil puis-je ouvrir ? »</td></tr>
</table>

<h4>12. Le prompt prêt à copier-coller</h4>
<div class="prompt-box">Explique [sujet] en 5 points concrets, avec 1 exemple réel pour
chaque point. Si tu n'es pas sûr d'un fait, dis-le clairement.</div>
<p>Tu remplaces <code>[sujet]</code> par ton thème, et tu colles ce prompt dans ChatGPT,
Gemini, Claude, DeepSeek et Grok.</p>
"""

ASTUCES[3] = """
<h4>1. Le texte de l'astuce</h4>
<div class="prompt-box"><strong>Version mobile quand le web bloque</strong><br>
Souvent l'app mobile a un quota séparé ou moins saturé.
ChatGPT web saturé → app téléphone. Gemini idem.</div>

<h4>2. Que veut dire « version mobile » ?</h4>
<p>C'est l'<strong>application officielle</strong> de l'IA sur ton téléphone (Android ou
iPhone), par opposition à la version web que tu utilises dans ton navigateur.
ChatGPT, Gemini et Claude ont tous une application mobile officielle ; DeepSeek et Grok
proposent une application ou une version mobile du site.</p>
<p>Quand on dit « version mobile quand le web bloque », on veut dire :</p>
<div class="reflexe">Si la version web affiche « limite atteinte », essaie la même IA sur
l'application mobile de ton téléphone.</div>

<h4>3. Pourquoi ça peut débloquer ?</h4>
<p><strong>a) Quota séparé.</strong> Chez certains fournisseurs, le quota de l'application
mobile est compté séparément de celui du site web. Si tu as épuisé ton quota sur le web, il
peut t'en rester sur mobile. Ce n'est pas garanti partout, mais c'est fréquent.</p>
<p><strong>b) Moins de saturation.</strong> Même quand le quota est partagé, l'application
mobile est souvent moins saturée aux heures de pointe : il y a moins d'utilisateurs
simultanés à certains moments. C'est vrai le matin tôt, tard le soir, les week-ends et
pendant les vacances scolaires.</p>

<h4>4. Comment faire concrètement ?</h4>
<ol>
  <li><strong>Installe l'application officielle</strong> depuis le Play Store (Android)
      ou l'App Store (iPhone).</li>
  <li><strong>Connecte-toi avec le même compte</strong> que sur le web, pour retrouver
      ton historique et tes préférences.</li>
  <li><strong>Teste la même question.</strong> Si ça fonctionne, tu as une solution immédiate.</li>
  <li><strong>Continue sur mobile</strong>, et copie la réponse vers ton ordinateur si besoin.</li>
</ol>

<h4>5. Exemple concret</h4>
<p><strong>Situation :</strong> tu prépares un exposé sur l'ordinateur, ChatGPT web affiche
« Vous avez atteint votre limite ».</p>
<ol>
  <li>Tu prends ton téléphone.</li>
  <li>Tu ouvres l'application ChatGPT.</li>
  <li>Tu colles le même prompt.</li>
  <li>Si ça répond → tu continues sur mobile.</li>
  <li>Si ça bloque aussi → tu passes à un autre outil (astuce n° 2 : alterner).</li>
</ol>

<h4>6. Pourquoi ça marche parfois et pas toujours ?</h4>
<table>
  <tr><th>Cas</th><th>Explication</th></tr>
  <tr><td><strong>Quota séparé</strong></td><td>Le fournisseur compte web et mobile séparément.</td></tr>
  <tr><td><strong>Moins de saturation</strong></td><td>Moins d'utilisateurs sur mobile à certains moments.</td></tr>
  <tr><td><strong>Modèle différent</strong></td><td>L'application mobile peut recevoir une version plus légère du modèle.</td></tr>
  <tr><td><strong>Quota partagé</strong></td><td>Dans certains cas, c'est le même quota sur web et mobile.</td></tr>
</table>
<p>Donc : <strong>ça vaut toujours la peine d'essayer</strong>, même sans garantie.</p>

<h4>7. Les avantages</h4>
<ul>
  <li><strong>Immédiat</strong> — pas besoin d'attendre 3 heures.</li>
  <li><strong>Simple</strong> — tu as déjà ton téléphone à côté de toi.</li>
  <li><strong>Gratuit</strong> — aucun abonnement nécessaire.</li>
  <li><strong>Complémentaire</strong> — s'ajoute aux astuces n° 1 et n° 2.</li>
  <li><strong>Pratique</strong> — tu continues à travailler en déplacement.</li>
</ul>

<h4>8. Les limites et précautions</h4>
<table>
  <tr><th>Point</th><th>Attention</th></tr>
  <tr><td><strong>Même compte</strong></td><td>Un autre compte = autre quota, mais tu perds ton historique.</td></tr>
  <tr><td><strong>Confidentialité</strong></td><td>Évite de coller des données sensibles sur mobile aussi.</td></tr>
  <tr><td><strong>Petit écran</strong></td><td>Les réponses longues sont pénibles à lire sur téléphone.</td></tr>
  <tr><td><strong>Batterie</strong></td><td>L'application consomme de la batterie si tu l'utilises longtemps.</td></tr>
  <tr><td><strong>Mises à jour</strong></td><td>Garde l'application à jour.</td></tr>
</table>

<h4>9. Le lien avec les astuces précédentes</h4>
<table>
  <tr><th>Astuce</th><th>Action</th></tr>
  <tr><td><strong>n° 1</strong></td><td>Regrouper → Décaler → Alterner</td></tr>
  <tr><td><strong>n° 2</strong></td><td>Alterner entre ChatGPT, Gemini, Claude, DeepSeek, Grok</td></tr>
  <tr><td><strong>n° 3</strong></td><td>Version mobile quand le web bloque</td></tr>
</table>
<p>La logique complète est une <strong>stratégie en cascade</strong> :</p>
<ol>
  <li><strong>Regrouper</strong> tes questions en un seul prompt.</li>
  <li>Si ça bloque → <strong>Décaler</strong> (attendre).</li>
  <li>Si tu ne peux pas attendre → <strong>Alterner</strong> (autre outil).</li>
  <li>Si un outil est bloqué sur le web → <strong>l'application mobile</strong> de ce même outil.</li>
</ol>
<p>Tu essaies toujours l'option la plus simple et la plus rapide d'abord.</p>

<h4>10. Le réflexe à retenir</h4>
<div class="reflexe">
  <strong>« Avant de paniquer parce que le web est bloqué, ai-je l'application mobile de
  cette IA sur mon téléphone ? »</strong>
</div>
<p>Si oui → essaie. Si non → installe-la, c'est gratuit. Si ça bloque aussi → passe à un
autre outil (astuce n° 2).</p>

<h4>11. Résumé de l'astuce n° 3</h4>
<table>
  <tr><th>Point</th><th>Explication</th></tr>
  <tr><td><strong>Principe</strong></td><td>Utiliser l'application mobile quand le web est bloqué</td></tr>
  <tr><td><strong>Pourquoi</strong></td><td>Quota parfois séparé + moins de saturation</td></tr>
  <tr><td><strong>Comment</strong></td><td>Installer l'app, même compte, tester</td></tr>
  <tr><td><strong>Avantage</strong></td><td>Déblocage immédiat, sans attendre</td></tr>
  <tr><td><strong>Limite</strong></td><td>Pas garanti à 100 %, quota parfois partagé</td></tr>
  <tr><td><strong>Réflexe</strong></td><td>« Ai-je l'application mobile ? »</td></tr>
</table>

<h4>12. Le prompt à réutiliser</h4>
<div class="prompt-box">Explique [sujet] en 5 points concrets, avec 1 exemple réel pour
chaque point. Si tu n'es pas sûr d'un fait, dis-le clairement.</div>
<p>Tu le colles dans l'application mobile quand le web est bloqué.</p>
"""

ASTUCES[4] = """
<h4>1. Le texte de l'astuce</h4>
<div class="prompt-box"><strong>Heures creuses (nuit / matin tôt)</strong><br>
Les limites se relâchent entre 23h et 7h. Pour un gros travail : commence à 6h
ou après 23h.</div>

<h4>2. Que veut dire « heures creuses » ?</h4>
<p>Ce sont les moments où <strong>moins de personnes utilisent les IA en même temps</strong> :
la nuit entre 23h et 7h, très tôt le matin entre 6h et 8h, les week-ends, les jours fériés
et les vacances scolaires.</p>
<p>Quand il y a moins de monde, les serveurs sont moins sollicités. Donc les réponses
arrivent plus vite, les erreurs techniques sont plus rares, les limites temporaires sont
moins fréquentes, et parfois les quotas sont déjà rechargés.</p>

<h4>3. Pourquoi ça peut aider ?</h4>
<p><strong>a) Moins de saturation.</strong> Aux heures de pointe (9h–18h), des millions de
personnes utilisent ChatGPT, Gemini ou Claude. Résultat : ralentissements, messages
« limite atteinte », réponses parfois incomplètes. La nuit, il y a beaucoup moins de trafic.</p>
<p><strong>b) Quotas rechargés.</strong> Les quotas se rechargent souvent après quelques
heures. Si tu as épuisé le tien à 20h, il est probablement disponible à 6h du matin. Au
lieu d'attendre en journée, tu planifies ton gros travail sur un créneau où le quota est
frais.</p>
<p><strong>c) Meilleure qualité de réponse.</strong> Quand les serveurs sont moins chargés,
les requêtes sont traitées plus sereinement : les réponses sont parfois plus complètes et
plus cohérentes.</p>
<div class="tip">
  <strong>Nuance importante :</strong> les quotas sont <strong>personnels</strong> — l'heure
  ne change pas ton quota individuel. Mais elle change la <strong>charge globale</strong> des
  serveurs. L'astuce fonctionne donc pour deux raisons : ton quota s'est rechargé pendant
  la nuit, et la plateforme est moins saturée. Ce n'est pas magique, mais ça marche souvent.
</div>

<h4>4. Comment faire concrètement ?</h4>
<ol>
  <li><strong>Repère les gros travaux.</strong> Tu sais d'avance quand tu auras besoin de
      beaucoup de messages : rédaction longue, analyse de documents, code, révisions,
      préparation d'exposé.</li>
  <li><strong>Planifie-les sur les heures creuses.</strong> Le matin vers 6h ou 7h, le soir
      après 23h, ou les matinées du week-end.</li>
  <li><strong>Prépare tes prompts la veille.</strong> Note tes questions, regroupe-les
      (astuce n° 1), prépare le contexte. Le matin, tu colles tout en un seul prompt.</li>
  <li><strong>Garde les questions simples pour la journée</strong> et réserve les gros
      prompts pour la nuit ou tôt le matin.</li>
</ol>

<h4>5. Exemple concret</h4>
<p><strong>Situation :</strong> tu dois rendre un rapport demain, et il te faut 10 réponses
longues.</p>
<p><strong>Mauvaise méthode :</strong> tu commences à 14h. À 15h, « limite atteinte ». Tu
paniques, tu attends, tu perds du temps.</p>
<p><strong>Bonne méthode :</strong> la veille, tu prépares ton prompt regroupé. Le lendemain
à 6h, tu envoies ton prompt unique : le quota est rechargé, les serveurs sont calmes, et tu
obtiens ta réponse en quelques minutes.</p>

<h4>6. Les avantages</h4>
<table>
  <tr><th>Avantage</th><th>Explication</th></tr>
  <tr><td><strong>Quota rechargé</strong></td><td>Après quelques heures, le compteur repart.</td></tr>
  <tr><td><strong>Moins d'attente</strong></td><td>Serveurs moins saturés.</td></tr>
  <tr><td><strong>Réponses plus rapides</strong></td><td>Moins de files d'attente.</td></tr>
  <tr><td><strong>Meilleure concentration</strong></td><td>Le matin tôt ou la nuit, tu es moins dérangé.</td></tr>
  <tr><td><strong>Compatible avec les autres astuces</strong></td><td>Tu peux regroupé, alterner et utiliser le mobile en même temps.</td></tr>
</table>

<h4>7. Les limites et précautions</h4>
<table>
  <tr><th>Point</th><th>Attention</th></tr>
  <tr><td><strong>Pas garanti</strong></td><td>Ça dépend de l'outil, du pays, du fuseau horaire.</td></tr>
  <tr><td><strong>Fatigue</strong></td><td>Ne sacrifie pas ton sommeil pour un quota.</td></tr>
  <tr><td><strong>Santé</strong></td><td>Travailler à 3h du matin n'est pas une solution durable.</td></tr>
  <tr><td><strong>Fuseaux horaires</strong></td><td>23h–7h chez toi n'est pas forcément l'heure creuse mondiale.</td></tr>
  <tr><td><strong>Sécurité</strong></td><td>La nuit, reste dans un endroit sûr et éclairé.</td></tr>
</table>

<h4>8. Le lien avec les astuces précédentes</h4>
<table>
  <tr><th>Astuce</th><th>Action</th></tr>
  <tr><td><strong>n° 1</strong></td><td>Regrouper → Décaler → Alterner</td></tr>
  <tr><td><strong>n° 2</strong></td><td>Alterner entre plusieurs IA</td></tr>
  <tr><td><strong>n° 3</strong></td><td>Version mobile quand le web bloque</td></tr>
  <tr><td><strong>n° 4</strong></td><td>Heures creuses (nuit / matin tôt)</td></tr>
</table>
<p>La logique complète :</p>
<ol>
  <li><strong>Regrouper</strong> tes questions.</li>
  <li>Si ça bloque → <strong>Décaler</strong>.</li>
  <li>Si tu ne peux pas attendre → <strong>Alterner</strong>.</li>
  <li>Si le web bloque → <strong>Version mobile</strong>.</li>
  <li>Si tu veux éviter le blocage → <strong>travailler aux heures creuses</strong>.</li>
</ol>

<h4>9. Le réflexe à retenir</h4>
<div class="reflexe">
  <strong>« Avant de lancer un gros travail, puis-je le faire à 6h ou après 23h ? »</strong>
</div>
<p>Si oui → planifie-le sur ce créneau. Si non → utilise les autres astuces (regrouper,
alterner, version mobile).</p>

<h4>10. Résumé de l'astuce n° 4</h4>
<table>
  <tr><th>Point</th><th>Explication</th></tr>
  <tr><td><strong>Principe</strong></td><td>Travailler quand les serveurs sont moins sollicités</td></tr>
  <tr><td><strong>Quand</strong></td><td>23h–7h, tôt le matin, week-ends, vacances</td></tr>
  <tr><td><strong>Pourquoi</strong></td><td>Quotas rechargés + moins de saturation</td></tr>
  <tr><td><strong>Comment</strong></td><td>Planifier les gros travaux sur ces créneaux</td></tr>
  <tr><td><strong>Avantage</strong></td><td>Réponses plus rapides, moins de limites</td></tr>
  <tr><td><strong>Limite</strong></td><td>Pas garanti, attention à la fatigue</td></tr>
  <tr><td><strong>Réflexe</strong></td><td>« Puis-je le faire à 6h ou après 23h ? »</td></tr>
</table>

<h4>11. Le prompt de planification</h4>
<div class="prompt-box">Je dois faire [tâche] avant [date].
Aide-moi à planifier ce travail sur 3 jours en utilisant les heures creuses
(tôt le matin ou tard le soir).
Donne-moi un tableau :
| Jour | Heure | Tâche | Durée | Objectif |</div>
"""

ASTUCES[1] = """
<h4>1. Le problème de départ : « limite atteinte »</h4>
<p>Quand tu utilises ChatGPT (ou Gemini, Claude…), tu vois parfois apparaître un message
du type :</p>
<div class="prompt-box">« Vous avez atteint votre limite. Revenez plus tard. »</div>
<p>Ce message <strong>ne veut pas dire</strong> :</p>
<ul>
  <li>que ChatGPT est cassé,</li>
  <li>que tu as fait une erreur,</li>
  <li>que tu es puni,</li>
  <li>qu'il faut payer immédiatement.</li>
</ul>
<p>Ce message <strong>veut dire</strong> :</p>
<ul>
  <li>tu as envoyé beaucoup de messages sur une période donnée,</li>
  <li>le modèle a un plafond (un <em>quota</em>),</li>
  <li>ce plafond se recharge automatiquement après quelques heures,</li>
  <li>en attendant, tu ne peux plus rien envoyer sur ce modèle.</li>
</ul>
<p><strong>Pourquoi ça arrive ?</strong></p>
<ul>
  <li>Les versions gratuites ont des quotas <strong>plus bas</strong> que les versions payantes.</li>
  <li>Les modèles puissants (GPT-4o, Claude Sonnet, Gemini Pro…) consomment <strong>plus de ressources</strong> que les petits modèles.</li>
  <li>Chaque message envoyé consomme une unité de quota — parfois plus s'il est long.</li>
  <li>Si tu envoies 5 petits messages, tu consommes 5 unités. Si tu en envoies <strong>1 seul qui regroupe tout</strong>, tu consommes souvent 1 seule unité.</li>
</ul>
<p>Donc l'idée centrale de cette astuce est : <strong>arrêter de gaspiller ton quota
avec des messages courts et dispersés.</strong></p>

<h4>2. Première étape : REGROUPER</h4>
<p><strong>Principe.</strong> Au lieu d'envoyer plusieurs petits messages séparés, tu envoies
<strong>un seul message</strong> qui contient tout le contexte, toutes tes questions et le
format souhaité.</p>
<p><strong>Exemple concret (mauvais usage).</strong> Tu envoies 5 messages :</p>
<pre>1. « Explique-moi la photosynthèse. »
2. « Donne-moi un exemple. »
3. « Écris un petit schéma. »
4. « Quelles sont les erreurs fréquentes ? »
5. « Résume en 5 points. »</pre>
<p>Résultat : <strong>5 unités de quota</strong>, et à chaque fois l'IA doit deviner ce que
tu veux vraiment.</p>
<p><strong>Exemple concret (bon usage).</strong> Tu envoies <strong>un seul message</strong> :</p>
<pre>Contexte : je suis étudiant en 2e année PEP, je prépare un exposé
de 10 minutes sur la photosynthèse.
Objectif : comprendre et pouvoir expliquer clairement.

Tâches :
1) Explique la photosynthèse simplement (niveau lycée).
2) Donne 2 exemples concrets de son importance.
3) Propose un petit schéma textuel des étapes.
4) Liste 3 erreurs fréquentes que font les étudiants sur ce sujet.
5) Résume en 5 points clés à retenir.

Format : réponse structurée avec titres, en français clair.</pre>
<p>Résultat : <strong>1 seule unité</strong> consommée, et une réponse plus cohérente et
plus complète.</p>
<p><strong>Pourquoi ça marche mieux ?</strong></p>
<ul>
  <li><strong>Économie de quota</strong> : 1 message au lieu de 5.</li>
  <li><strong>Meilleure qualité</strong> : l'IA a tout le contexte dès le début, elle ne devine pas.</li>
  <li><strong>Moins d'allers-retours</strong> : tu ne répètes pas 4 fois ce que tu voulais.</li>
  <li><strong>Réponse cohérente</strong> : les 5 parties se répondent entre elles.</li>
</ul>
<div class="warn">
  <strong>Attention à ne pas faire :</strong> ne regroupe pas 30 questions sans lien. Regroupe
  par <strong>thème</strong>, 3 à 5 questions liées maximum. Si tu as 15 questions sur 3 sujets,
  fais <strong>3 prompts regroupés</strong> (un par sujet), pas 15 petits messages.
</div>
<p><strong>Le réflexe à adopter.</strong> Avant chaque envoi, demande-toi :</p>
<div class="reflexe">« Est-ce que je peux regrouper 3 questions en 1 seul message ? »</div>
<p>Si oui → fais-le. Si non → demande-toi : « quelle est la question la plus importante
maintenant ? »</p>

<h4>3. Deuxième étape : DÉCALER</h4>
<p><strong>Principe.</strong> Si même en regroupant tu es bloqué, tu <strong>décalés</strong> :
tu attends.</p>
<p><strong>Pourquoi attendre ?</strong> Les quotas se rechargent automatiquement, souvent après
quelques heures : chez ChatGPT en général toutes les 3 heures pour le modèle principal, chez
Gemini par plage horaire ou par jour, chez Claude après un délai lui aussi.</p>
<p><strong>Que faire pendant ce temps ?</strong></p>
<ul>
  <li><strong>Ne pas spammer</strong> de messages pour tester : ça ne débloque rien.</li>
  <li><strong>Préparer tes prochains prompts</strong> : note tes questions, regroupe-les, écris le contexte à l'avance.</li>
  <li><strong>Travailler sur autre chose</strong> : un autre cours, une autre tâche.</li>
  <li><strong>Revenir plus tard</strong> quand le quota est rechargé.</li>
</ul>
<p><strong>Ce que « décaler » veut dire concrètement :</strong> je ne force pas. J'accepte que
la limite soit temporaire. J'utilise ce temps pour préparer un meilleur prompt que celui que
j'aurais envoyé dans la panique. Je reviens quand c'est rechargé.</p>
<div class="tip">
  <strong>Astuce bonus :</strong> les limites se relâchent souvent <strong>le matin tôt (6h–8h)</strong>
  ou <strong>tard le soir (après 23h)</strong>. Si tu as un gros travail à faire, planifie-le sur ces plages.
</div>

<h4>4. Troisième étape : ALTERNER</h4>
<p><strong>Principe.</strong> Si tu ne peux pas attendre, ou si le quota reste bloqué, tu
<strong>alternes</strong> : tu changes d'outil, de modèle ou de méthode.</p>
<p><strong>Comment alterner concrètement ?</strong></p>
<ul>
  <li><strong>Changer de modèle</strong> dans le même outil : ChatGPT → GPT-4o mini, souvent moins saturé.</li>
  <li><strong>Changer d'outil</strong> : ChatGPT bloqué → Gemini, Claude, DeepSeek, Grok, Perplexity…</li>
  <li><strong>Changer de plateforme</strong> : version web bloquée → application mobile (parfois quota séparé).</li>
  <li><strong>Changer de méthode</strong> : recherche web, manuel, forum, document officiel.</li>
  <li><strong>Changer de tâche</strong> : avancer sur une autre partie du travail en attendant.</li>
</ul>
<p>Chaque outil a <strong>son propre quota indépendant</strong>. Si ChatGPT est bloqué, Gemini
fonctionne peut-être encore. En gardant 3 ou 4 outils ouverts en onglets permanents, tu ne
restes jamais bloqué.</p>
<div class="tip">
  <strong>L'astuce 2 en lien :</strong> « Alterner ChatGPT · Gemini · Claude · DeepSeek · Grok ».
  C'est exactement cela : plusieurs onglets ouverts, la même question partout, comparaison
  des réponses, et on continue à travailler même quand un outil est saturé.
</div>
<div class="warn">
  <strong>Attention :</strong> créer plusieurs comptes pour contourner les limites peut
  <strong>violer les conditions d'utilisation</strong> de l'outil. À éviter. Alterner ne veut pas
  dire « tricher », cela veut dire « utiliser intelligemment les outils disponibles ».
</div>

<h4>5. Le réflexe à retenir</h4>
<div class="reflexe">
  <strong>Avant d'envoyer, demande-toi : « Est-ce que je peux regrouper 3 questions en 1 message ? »</strong>
</div>
<p>Appliqué systématiquement, ce réflexe t'économise du quota, du temps, de l'énergie — et il
améliore la qualité des réponses.</p>

<h4>6. Résumé visuel de l'astuce n° 1</h4>
<table>
  <tr><th>Étape</th><th>Action</th><th>Pourquoi</th></tr>
  <tr><td><strong>Regrouper</strong></td><td>Fusionner plusieurs questions en 1 seul prompt</td><td>Économiser le quota + meilleure réponse</td></tr>
  <tr><td><strong>Décaler</strong></td><td>Attendre la recharge du quota</td><td>La limite est temporaire</td></tr>
  <tr><td><strong>Alterner</strong></td><td>Changer de modèle, d'outil ou de tâche</td><td>Continuer à travailler malgré la limite</td></tr>
  <tr><td><strong>Réflexe</strong></td><td>« Puis-je regrouper 3 questions en 1 ? »</td><td>Réduire le nombre de messages</td></tr>
</table>

<h4>7. Exemple complet d'application</h4>
<p><strong>Situation :</strong> tu dois préparer un exposé sur « l'impact des réseaux sociaux
sur les adolescents ».</p>
<p><strong>Mauvaise méthode</strong> — 5 messages :</p>
<pre>1. « C'est quoi l'impact des réseaux sociaux ? »
2. « Donne-moi des statistiques. »
3. « Quels sont les avantages ? »
4. « Quels sont les inconvénients ? »
5. « Fais-moi un plan. »</pre>
<p>5 unités de quota, réponse dispersée.</p>
<p><strong>Bonne méthode</strong> — 1 message :</p>
<pre>Contexte : exposé de 10 minutes, niveau licence, public non expert.
Sujet : impact des réseaux sociaux sur les adolescents.

Tâches :
1) Définis le sujet en 3 phrases.
2) Donne 5 statistiques récentes avec sources
   (ou signale si tu n'es pas sûr).
3) Liste 4 avantages et 4 inconvénients.
4) Propose un plan d'exposé en 3 parties avec transitions.
5) Termine par 3 questions pour ouvrir le débat.

Format : titres clairs, français simple, pas de jargon.</pre>
<p>1 unité de quota, réponse complète et directement utilisable.</p>
"""

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Chargement de tous les lots
#
# Les explications sont réparties dans des fichiers « lot » pour rester
# maniables : ce fichier garde l'astuce 1 (version longue, gabarit de
# référence) et fusionne ensuite tous les `astuces_detail_lot_*.py` voisins.
# Pour ajouter des explications : créer un nouveau lot, écrire
# LOT_x[72] = """…""", relancer ajouter_boutons_astuces.py.
# ---------------------------------------------------------------------------

import glob as _glob
import importlib.util as _spec
import os as _os

_dossier = _os.path.dirname(_os.path.abspath(__file__))
for _chemin in sorted(_glob.glob(_os.path.join(_dossier, "astuces_detail_lot_*.py"))):
    _nom = _os.path.splitext(_os.path.basename(_chemin))[0]
    _mod = _spec.spec_from_file_location(_nom, _chemin)
    if _mod is None:
        continue
    _charge = _mod.loader.load_module()
    for _cle, _val in vars(_charge).items():
        if _cle.startswith("LOT_") and isinstance(_val, dict):
            # setdefault : une version longue écrite ici (astuce 1, astuce 2)
            # ne doit jamais être écrasée par la version courte d'un lot.
            for _n, _t in _val.items():
                ASTUCES.setdefault(_n, _t)
