# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 13:33:33 2025

@author: bless
"""
#Valid Anagram (check that two words match exactly with the same length when probably reversed)

#Easy (Sorting)
def is_anagram (s, t):
    return sorted(s) == sorted(t)
s = 'listen'
t = 'silent'
print(is_anagram (s, t))
#Time: O(n log n)
#Space: 0(n)

#Best (Hash Map/Counting)
from collections import Counter
def its_anagram (s, t):
    return Counter(s) == Counter(t)
s = 'listen'
t = 'silent'
#Time: O(n)
#Space: 0(n)