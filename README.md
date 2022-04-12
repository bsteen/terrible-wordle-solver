# terrible-wordle-solver
My terrible attempt at a Wordle solver

# Usage Example
`python3 wordle.py "s???d" "iertn" "a"`
- 1st Argument: green letters (known letter positions) and unknown letters (?)
- 2nd Argument: incorrect letters guessed, in any order (enter `""` if there are none)
- 3rd Argument (optinal): yellow letters, in any order (letters you know are in the word, but don't know the position; enter `""` if there are none)
- Wordle dictionary must be provide in text file named `wordle-dict.txt`
