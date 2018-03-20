# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:34:45 2018

@author: jonpo
"""

def checkio(matrix):
    #replace this for solution
    height = len(matrix)
    width = len(matrix[0])

    
    for x in range(width):
        for y in range(height):
            # Do a rightwards traverse if there's room for four in a row
            if x + 3 <= width - 1:
                if matrix[x][y] == matrix[x+1][y] == matrix[x+2][y] == matrix[x+3][y]:
                    return True
            # Do a downwards traverse if there's room for four in a row
            if y + 3 <= height - 1:
                if matrix[x][y] == matrix[x][y+1] == matrix[x][y+2] == matrix[x][y+3]:
                    return True
            # Do a down and right traverse if there's room
            if x + 3 <= width - 1 and y + 3 <= height - 1:
                if matrix[x][y] == matrix[x+1][y+1] == matrix[x+2][y+2] == matrix[x+3][y+3]:
                    return True
            # Do a up and right traverse if there's room
            if x - 3 >= 0 and y + 3 <= height - 1:
                if matrix[x][y] == matrix[x-1][y+1] == matrix[x-2][y+2] == matrix[x-3][y+3]:
                    return True
    
    return False
                
                

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
