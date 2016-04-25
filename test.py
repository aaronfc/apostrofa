# coding=utf-8
from __future__ import unicode_literals
from categorizer.Category import Category
from categorizer.SimpleCategorizer import SimpleCategorizer
from syllabifier.SimpleSyllabifier import SimpleSyllabifier

words = [
    ['tauró', 2, Category.AGUDA],
    ['febril', 2, Category.AGUDA],
    ['treball', 2, Category.AGUDA],
    ['palangana', 4, Category.PLANA],
    ['òptic', 2, Category.PLANA],
    ['òptica', 3, Category.ESDRUIXOLA],
]

# Test separating into syllables
print "Syllabifying...",
syllabifier = SimpleSyllabifier()
for word, num_syllables, category in words:
    syllables = syllabifier.syllabify(word)
    assert len(syllables) == num_syllables
    #print "{} -> {}".format(word, "-".join(syllables))
print "DONE!"

# Test categorization
print "Categorizying...",
categorizer = SimpleCategorizer(syllabifier)
for word, num_syllables, category in words:
    guess = categorizer.classify(word)
    assert guess == category
    #print "[{}] {} -> {}".format("V" if guess == category else "X", word, guess)
print "DONE"
