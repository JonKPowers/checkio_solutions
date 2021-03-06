# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:49:07 2018

@author: jonpo
"""

def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
        print(word, count)
    return count
        


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
