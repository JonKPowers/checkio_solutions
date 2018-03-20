# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:52:07 2018

@author: jonpo
"""

def checkio(n, m):
    binary_n = '{0:b}'.format(n)
    binary_m = '{0:b}'.format(m)
    
    len_n = len(binary_n)
    len_m = len(binary_m)
    
    difference = abs(len_n - len_m)
    
    if len_n > len_m:
        binary_m = ('0' * difference) + binary_m
    else:
        binary_n = ('0' * difference) + binary_n
    
    hamming = 0
    for i in range(len(binary_n)):
        hamming += 1 if binary_n[i] != binary_m[i] else 0
    
    return hamming
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
