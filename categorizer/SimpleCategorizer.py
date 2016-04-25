# coding=utf-8
from __future__ import unicode_literals
from categorizer.Categorizer import Categorizer
from categorizer.Category import Category


class SimpleCategorizer(Categorizer):
    def __init__(self, syllabifier):
        self.syllabifier = syllabifier

    def classify(self, word):
        syllables = self.syllabifier.syllabify(word)
        accentuated = ['à', 'è', 'é', 'í', 'ò', 'ó', 'ú']
        interesting_ends = ['a', 'e', 'i', 'o', 'u', 'as', 'es', 'is', 'os', 'us', 'en', 'in', 'èn', 'én', 'ín']
        if any(e in syllables[-1] for e in accentuated):
            return Category.AGUDA
        elif any(e in syllables[-2] for e in accentuated):
            return Category.PLANA
        elif any(e in "".join(syllables[:-2]) for e in accentuated):
            return Category.ESDRUIXOLA
        elif any(syllables[-1].endswith(ending) for ending in interesting_ends):
            return Category.PLANA
        else:
            return Category.AGUDA