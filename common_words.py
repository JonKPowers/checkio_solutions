# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:48:01 2018

@author: jonpo
"""

def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    intersection = set(first) & set(second)
    return ','.join(sorted(intersection))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
