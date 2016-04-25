# coding=utf-8
from __future__ import unicode_literals
from syllabifier.Syllabifier import Syllabifier


class SimpleSyllabifier(Syllabifier):
    def __init__(self):
        pass

    def syllabify(self, word):
        syllables = []
        reversed = word[::-1]
        vowels = ['a', 'e', 'i', 'o', '', 'à', 'è', 'é', 'í', 'ò', 'ó', 'ú']
        syllable = ""
        last = None
        seen_vowels = 0
        for c in reversed:
            if c in vowels:
                if last is not None and last not in vowels and seen_vowels > 0:
                    syllables.append(syllable)
                    syllable = ""
                seen_vowels += 1
            syllable = c + syllable
            last = c
        if syllable != "":
            syllables.append(syllable)
        return syllables[::-1]