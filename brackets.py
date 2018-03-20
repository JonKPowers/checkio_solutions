# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:57:09 2018

@author: jonpo
"""

def checkio(expression):
    types = {
        '{': 'bracket',
        '}': 'bracket',
        '[': 'square',
        ']': 'square',
        '(': 'round',
        ')': 'round',
    }
    
    open_list = ['{', '[', '(']
    close_list = ['}', ']', ')']
    
    queue = []
    
    for character in expression:
        if character in types.keys():
            if character in open_list:
                queue.append(types[character])
            else:
                try:
                    if types[character] == queue[-1]:
                        del queue[-1]
                    else:
                        return False
                except IndexError:
                    return False
    
    if len(queue) == 0:
        return True
    else:
        return False

# Alternate solution:
def checkio(data):
    brack_dict = {")": "(", "]": "[", "}": "{"}
    stack = []
    for d in data:
        # found opening bracket
        if d in brack_dict.values():
            stack.append(d)
        # found closing bracket
        elif d in brack_dict:
            if stack and stack[-1] == brack_dict[d]:
                stack.pop()
            else:
                return False
    return stack == []
            

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
