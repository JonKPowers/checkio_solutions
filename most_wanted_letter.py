# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:37:15 2018

@author: jonpo
"""

def checkio(text):

    #replace this for solution
    letters = [letter.lower() for letter in text if letter.isalpha()]
    freq_dict = {letter: letters.count(letter) for letter in letters}
    high_count = 0
    top_letter = []
    for letter in freq_dict.keys():
        if freq_dict[letter] > high_count:
            high_count = freq_dict[letter]
            top_letter = list(letter)
        if freq_dict[letter] == high_count:
            top_letter.append(letter)
    return min(top_letter)

# I like this one:
from string import ascii_lowercase

def checkio(text):
    return max(ascii_lowercase, key=text.lower().count)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
