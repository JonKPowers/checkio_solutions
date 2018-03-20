# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 19:35:36 2018

@author: jonpo
"""

def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    iterate_me = [item for item in args[0]] if len(args) == 1 else args
    print(iterate_me)
    lowest = iterate_me[0]
    for item in iterate_me:
        if key(item) < key(lowest):
            lowest = item
    return lowest


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    iterate_me = [item for item in args[0]] if len(args) == 1 else args
    print(iterate_me)
    highest = iterate_me[0]
    for item in iterate_me:
        if key(item) > key(highest):
            highest = item
    return highest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
