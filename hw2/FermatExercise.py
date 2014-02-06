# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 03:16:54 2014

@author: casey
"""

def check_fermat(a, b, c, n): 
    if n >2: 
        if a**n + b**n == c**n:
            print "Holy Smokes, Fermat was wrong" 
        else:
            print "No that doesn't work"
    else:
        print "N is not greater than 2" 

