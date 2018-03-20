# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:03:24 2018

@author: jonpo
"""

VOWELS = "aeiouy"
import re

def translate(phrase):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    phrase = [letter for letter in phrase]
    translation = []
    while phrase:
        translation.append(phrase[0])
        if not phrase[0].isalpha():
            del phrase[0]
        elif phrase[0].isalpha() and phrase[1].isalpha() and phrase[0] not in vowels:
            del phrase[0:2]
        elif phrase[0].isalpha() and phrase[0] in vowels:
            del phrase[0:3]
        
    return ''.join(translation)
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
