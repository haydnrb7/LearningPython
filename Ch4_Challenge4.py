#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:41:07 2019

@author: haydnbraun
"""

# Chapter 4 Challenge 4

# Create a game where the computer picks a random word and the player has to 
# guess the word. The computer tells the player how many letters are in
# the word. Then the player gets five chances to ask if a letter is in the
# word. The computer can only respond with "yes" or "no". Then, the player
# must guess the word.



# import stuff
import random

# give the computer available words
WORDS = ("blue", "yellow", "green", "orange", "purple", "pink")
         
        
# pick one word randomly from the sequence
wordint = random.randint(0,5)
word = WORDS[wordint]

guesses_left = 5
guesses = ()

#print(word)

# prompt user
print("the computer has chosen a word")
print("you get five chances to guess if letters are in the word")
print("After the five chances you must guess the word")



#initate while loop for guessing
while guesses_left > 0:
    letter_guess = input("what letter would you like to guess? \n")
    
    if letter_guess in word:
        print("That letter is in the word \n")
        
    else:
        print("That letter is not in the word \n")
        
    guesses_left-=1
    print("You have ",guesses_left ,"guesses left \n" )
    
    
word_guess = input("what is your guess for the entire word? \n")

if word_guess == word:
    print("good job!")
    
else:
    print("nope!")
    print("the correct answer was ", word )




