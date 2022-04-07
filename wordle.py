# (C) 2022 Benjamin Steenkamer

import sys
import nltk
nltk.download("words")
from nltk.corpus import words

# Get user word (* = any letter)
word = sys.argv[1]
assert len(word) == 5

# Remove letters that are known not to be in word
bad_letters = list(sys.argv[2])
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for bl in bad_letters:
    alphabet.remove(bl)

def insert_letters(word):
    possible_words = []
    for alp in alphabet:
        possible_words.append(word.replace("*", alp, 1))
    return possible_words

guess_words = [word]
cont = True
while cont:
    cont = False
    for i in range(len(guess_words)):
        if "*" in guess_words[i]:
            guess_words += insert_letters(guess_words.pop(i))
            cont = True

assert "*" not in guess_words
print(len(guess_words)) #FIXME MANY possible words... too large to compute
for w in guess_words:
    if w in words.words():
        print(w)
