# (C) 2022 Benjamin Steenkamer

import sys
import time

start = time.time()
# Get user word (green letters and ? = unknown letters)
user_word = sys.argv[1]
assert len(user_word) == 5

# Remove letters that are known not to be in word (incorrect guesses)
bad_letters = list(sys.argv[2])
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for bl in bad_letters:
    alphabet.remove(bl)

# Get yellow letters
must_contain = list(sys.argv[3]) 

# Load dictionary
with open("wordle-dict.txt", "r") as f:
    wordle_dict = f.read().splitlines()

def insert_letters(combo):
    possible_words = []
    for alp in alphabet:
        possible_words.append(combo.replace("?", alp, 1))
    return possible_words

# Replace "?" with every possible letter combination
letter_combos = [user_word]
cont = True
while cont:
    cont = False
    for i in range(len(letter_combos)):
        if "?" in letter_combos[i]:
            letter_combos += insert_letters(letter_combos.pop(i))
            cont = True

# print(len(letter_combos)) #FIXME MANY possible words... too large to compute quickly
# Go through letter combinations, remove invalid words
possible_words = []
for word in letter_combos:
    if word in wordle_dict:
        if all([mc in word for mc in must_contain]):
            possible_words.append(word)
possible_words.sort()

end = time.time()
print(f"{len(letter_combos)} letter combinations, {len(possible_words)} valid words, {end-start:0.3f} seconds\n{possible_words}")
