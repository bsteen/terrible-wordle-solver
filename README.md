# terrible-wordle-solver
My terrible attempt at a Wordle solver:
- 1st Argument: green letters (correctly guessed letters) and unknown letters (enter as `?`)
- 2nd Argument: incorrectly guessed letters, in any order (enter `""` if there are none)
- 3rd Argument: yellow letters, in any order (letters you know are in the word, but don't know the position; enter `""` if there are none)

Dictionary list contains all accepted Wordle words as of April 2022.  
Copyright 2022 - 2023 Benjamin Steenkamer

# Usage Example
`python3 wordle.py "s???d" "iertn" "a"`  
Output:
```
9261 letter combinations, 7 valid words, 1.008 seconds
['salad', 'scald', 'scaud', 'skald', 'spald', 'spayd', 'squad']
```
# TODO
1. Add ability to enter where yellow letters are
2. Generate "best guess" word: out of all possible words, highlight the word(s) that would eliminate the most possibilities next round if entered
