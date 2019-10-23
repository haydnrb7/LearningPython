#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:21:13 2019

@author: haydnbraun
"""

# Chapter 4 Challenge 2
# Create a program that gets a message from the user and then prints it 
# out backwards
#
# Prompt the user to input a string
# 


word = input("enter a word and I will print it backwards: ")

length = int(len(word)) -1
print("the word is " , length +1 , "long \n" )
 


for i in word:
    print(word[length])
    length -=1

#while length > -1:
#    print(word[length])
#    length -= 1

