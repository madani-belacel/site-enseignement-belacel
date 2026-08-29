# -*- coding: utf-8 -*-
"""Agrège toutes les fiches de grammaire (100 niveaux)."""

import data_levels_1_10 as d1
import data_levels_11_20 as d2
import data_levels_21_30 as d3
import data_levels_31_40 as d4
import data_levels_41_50 as d5
import data_levels_51_60 as d6
import data_levels_61_70 as d7
import data_levels_71_85 as d8
import data_levels_86_100 as d9


def _build_fallback_idea(level_num, title_en, category, index):
    """Ajoute une idée pédagogique standard à un niveau incomplet."""
    review_label = f"Review {index}"
    examples = [
        (f"I use {title_en.lower()} in a short sentence.", "أستخدم هذا الشكل في جملة قصيرة."),
        (f"This form is useful in everyday English.", "هذا الشكل مفيد في الإنجليزية اليومية."),
        (f"I can apply {title_en.lower()} correctly.", "أستطيع تطبيق هذا الشكل بشكل صحيح."),
    ]
    return {
        "en": f"{review_label}: practice with {title_en.lower()}",
        "ar": f"مراجعة {index}: التدريب على {title_en}",
        "expl_ar": (
            f"في هذا الجزء، نراجع استعمال {title_en} في جمل قصيرة وواضحة. "
            "الهدف هو التطبيق المستمر، مع الانتباه إلى الشكل الصحيح ووضع الكلمات في السياق المناسب."
        ),
        "expl_en": (
            f"This review point focuses on using {title_en} in short, correct sentences. "
            "The goal is to apply the structure in real contexts and keep the form accurate."
        ),
        "formula": f"focus on {title_en} + sentence practice",
        "examples": examples,
    }


def ensure_minimum_ideas(levels, minimum=10):
    """Complète chaque niveau jusqu'à minimum d'idées pédagogiques."""
    completed = []
    for lvl in levels:
        ideas = list(lvl.get("ideas", []) or [])
        while len(ideas) < minimum:
            index = len(ideas) + 1
            title = lvl.get("title_en", "Grammar point")
            category = lvl.get("category", "Grammar")
            ideas.append(_build_fallback_idea(lvl.get("num", 1), title, category, index))
        lvl["ideas"] = ideas
        completed.append(lvl)
    return completed


LEVELS = (d1.LEVELS + d2.LEVELS + d3.LEVELS + d4.LEVELS +
          d5.LEVELS + d6.LEVELS + d7.LEVELS + d8.LEVELS + d9.LEVELS)
LEVELS = ensure_minimum_ideas(LEVELS, minimum=10)