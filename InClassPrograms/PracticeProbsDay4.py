# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:11:34 2014

@author: casey
"""

def get_complimentary_base(letter):
    """Takes a base and returns its complementary base 
    x: is a base respresented as a length 1 string 
    returns: the corresponding complentary base""" 
    
    if letter == 'A': 
        return 'T' 
    elif letter =='T': 
        return 'A' 
    elif letter == 'C': 
        return 'G'
    elif letter == 'G':
        return 'C'
    else: 
        print "Not a nucleotide" 

def is_between(x,y,z): 
    if x<=y<=z:
        return True
    else: 
        print "Y is not between X and Z" 

#def random_float(start, stop): 
def factorial(n): 
    s = 1
    for i in range (1,n +1):
        s = s + 1    
    return s 
    