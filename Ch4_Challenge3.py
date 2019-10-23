#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:07:27 2019

@author: haydnbraun
"""
# Chapter 4 Challenge 3
# Improve "Word Jumble" so that each word is paired with a hint. The player
# should be abel to see the hint if he or she is stuck. Add a scoring system 
# that rewards players who solve a jumble without asking for the hint.







# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
WORDS_HINT = ("pyt", "jum", "ea", "diffi", "ans", "xylo")

# pick one word randomly from the sequence
wordint = random.randint(0,5)
word = WORDS[wordint]
hint = WORDS_HINT[wordint]

print(word)
print(hint)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    want_hint = input("if you would like a hint type y/n? \n")
    if want_hint == ("y"):
        print(hint)

    if want_hint ==("n"):
        print("aight")
    
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")
    


print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
