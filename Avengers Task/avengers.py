Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from spellchecker import SpellChecker
import re


spellings_to_check = ["hello", "how", "what", "however", "something", "anything",
                    "give", "day", "about", "time", "make", "just", "people", "good", 
                    "could", "would", "think", "after", "work", "because"]

# Checks the word if it is in the checkSpellings list. If so, it corrects it.
def check(word):
    global spellings_to_check
    
    spell = SpellChecker()
    word = word.lower()
    
    for possible in spell.candidates(word):
        if possible in spellings_to_check:
            return possible
    
    return word        


# shows list of words that shall be checked
print()
print("The spellings will be checked for the following words:")
for a in spellings_to_check:
    if a != spellings_to_check[-1]:
        print(a, end=", ")
    else:
        print("\n")


# Asks for input
input_para = input("Enter the paragraph you want to check>> ")
print()
paragraph =  re.split('[\s]', input_para)


# Prints out the corrected paragraph
for word in paragraph:
    a = check(word)
    print(a + " ", end="")

print()
