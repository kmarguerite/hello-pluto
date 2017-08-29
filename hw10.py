#!usr/bin/env Python 3

"""

Hangman Game!

This script will play a game of hangman against the computer!

To run this script from the commandline type
python hw10.py

Assumptions:

Requirements:
Anaconda Python3
random

"""



#imports
import random


#welcoming the user
name = input("What is your name? ")



def main():
    print(" I'm going to pick a word. Guess one letter at a time! You have 10 guesses!")

    # setting up the game loop
    game = True
    while game:
        # set up the game loop

        words = ["wizard", "potions", "herbology", "wand",
                 "quidditch", "quaffle", "owlry", "accio", "cauldron",
                 "mandrake", "basilisk", "dragon", "charms"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

# hangman constants (template obtained from Python Programming Third Edition)
        print_hangman = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(print_hangman[0])
        attempts = len(print_hangman) - 1

        #track the number of failed attempts,
        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue
            #error messages if uder inputs non-letters, too many letters.
            else:
                if not player_guess.isalpha():
                    print("Did you take a forgetfullness potion! That is not a letter! Try again.")
                    continue
                elif len(player_guess) > 1:
                    print("Try again.")
                    continue

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(print_hangman[(len(print_hangman) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            game = False

if __name__ == "__main__":
    main()
