# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:15:11 2015

@author: Nelson
"""

def insertionSort(ar):    
    return ""


s = int(raw_input())
ar = raw_input().split()
V = int(ar[s-1])
for i in range(s):
    if i == (s-1):
        ar[0] = str(V)
        print ' '.join(ar)
        break
    foo = ar[s - 2 - i]
    ar[s - 1 - i] = foo
    if int(foo) < V:
        ar[s - 1 - i] = str(V)
        print ' '.join(ar)
        break
    print ' '.join(ar)