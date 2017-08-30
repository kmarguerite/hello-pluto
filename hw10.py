#!usr/bin/env Python 3

"""

Hangman Game!

This script will play a game of hangman against the computer!

To run this script from the commandline type
python hw10.py

Assumptions:
Everyone loves Harry Potter

Requirements:
Anaconda Python3
random

"""
from random import randint

# create a hangman class, use set_up and init in order to start the gameplay
class Hangman_Game():
    #initialize the game, set up a word bank, set up 'game art'
    #the initialize function outputs
    def __init__(self):
        self.words = ["wizard", "potions", "herbology", "wand", "quidditch", "quaffle", "owlry", "accio", "cauldron",  "mandrake", "basilisk", "dragon", "charms"]
        self.art = ["  ————\n     |\n     |\n     |\n——————", "  ————\n  O  |\n     |\n     |\n——————",
                    "  ————\n  O  |\n /   |\n     |\n——————", "  ————\n  O  |\n / \ |\n     |\n——————",
                    "  ————\n  O  |\n /|\ |\n     |\n——————", "  ————\n  O  |\n /|\ |\n /   |\n——————",
                    "  ————\n  0  |\n /|\ |\n / \ |\n——————"]
        # self.printFile()
        self.set_up()

    #create a function to set up including welcome message and counters and variables, printing functions.
    def set_up(self):
        print("Hi! Welcome to Harry Potter Hangman!")
        #randomly select a word from list in init
        self.selected_word = self.words[randint(0, 13)]
        self.blank_word = []
        for x in self.selected_word:
            self.blank_word.append("*")
        #initialize counters and set at 0
        self.current_art = 0
        self.correct_letters = 0
        print(self.art[0])
        print(''.join(self.blank_word))
        self.get_letter()
        return(self.selected_word)


    #create a function for guesses from user input, which are characters. Outputs continue guessing loop, winning, and losing
    def guess(self, letter):
        letter_occurrences = self.selected_word.count(letter)
        if letter_occurrences > 0:
            previous_occurrence = 0
            for occurrence in range(0, letter_occurrences):
                letter_location = self.selected_word.find(letter, previous_occurrence)
                self.blank_word[letter_location] = letter
                previous_occurrence = letter_location + 1
            print(self.art[self.current_art])
            print(''.join(self.blank_word))

            #print message for the winner!
            self.correct_letters += letter_occurrences
            if self.correct_letters == len(self.selected_word):
                print("\nCongratulations, You Win!")

            else:
                self.get_letter()

        #print message if game is lost
        else:
            self.current_art += 1
            if self.current_art < 7:
                print(self.art[self.current_art])
                if self.current_art == 6:
                    print("Game Over! The correct word was '{}'".format(self.selected_word))
                else:
                    print(''.join(self.blank_word))
                    self.get_letter()

    # create a function to get letter guesses through user input
    def get_letter(self):
        user_input = ""
        while (len(user_input) != 1):
            user_input = input("Guess a letter.\n").lower()
        print(user_input)
        self.guess(user_input)


Hangman_Game()

# write hangman word to a file
#returns error message that selected_word is not defined
f = open("hangman.txt", "w+")
f.write("Yout HP Hangman word was {}".format(selected_word))
f.close()
