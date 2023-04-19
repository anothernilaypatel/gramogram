# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:47:47 2023

@author: Nilay Patel
"""

import pronouncing
import re

#GET PHONETICS FOR ALL LETTERS, SAVE TO ONE MASSIVE ARRAY
alphabet = "abcdefghijklmnopqrstuvxyz"
antiNumberPattern = r'[0-9]'

phoneticArray = []
phonemeFlag = False
phonemeFinal = ""

gramArray = []
gramWordArray = []

def swapPhonemes(array):
    global phonemeFlag
    global phonemeFinal
    
    for x in range(0, 3):
        currentSearch = array[0:x + 1]
        if currentSearch in phoneticArray:
            phonemeFinal += alphabet[phoneticArray.index(currentSearch)]
            if array[x + 1:] == []:
                phonemeFlag = True;
                return
            else:
                swapPhonemes(array[x + 1:])
        
        
#LOOP THROUGH THE ALPHABET, GET THE PHONEMES, SAVE IT TO A 2D ARRAY
for letter in alphabet:
    pronunciation = pronouncing.phones_for_word(letter)
    pronunciationArray = pronunciation[-1].split(" ")
    for x in range(0, len(pronunciationArray)):
        pronunciationArray[x] = re.sub(antiNumberPattern, "", pronunciationArray[x])
        
    #WE ONLY WANT THE SOUNDS OF THE LETTER TO BE SAVED
    #EX: A SHOULD BE "AYYY" NOT "UHHH"
    phoneticArray.append(pronunciationArray)
    
#GET INPUT FOR WORD
fileIn = open("finalDict.txt", "r")
readFile = fileIn.read()
wordArray = readFile.split("\n")

for word in wordArray:
    print(word)
    inputtedPronunciations = pronouncing.phones_for_word(word)
    
    #WORDS CAN HAVE MULTIPLE PRONUNCIATIONS, SO LOOP THROUGH THEM
    for x in range(0, len(inputtedPronunciations)):
        phonemeFlag = False
        phonemeFinal = ""    
        
        currentWord = inputtedPronunciations[x]
        currentWord = re.sub(antiNumberPattern, "", currentWord)
        currentPhonemes = currentWord.split(" ")
        
        swapPhonemes(currentPhonemes)
        if phonemeFlag:
            if not(phonemeFinal.lower() == word.lower()):
                gramArray.append(phonemeFinal)
                gramWordArray.append(word)
            
print("LONGEST WORD: " + max(gramWordArray, key = len) + " (" + gramArray[gramWordArray.index(max(gramWordArray, key = len))] + ")")
print("LONGEST GRAMOGRAM: " + max(gramArray, key = len) + " (" + gramWordArray[gramArray.index(max(gramArray, key = len))] + ")")

