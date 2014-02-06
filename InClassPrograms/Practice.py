# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:02:04 2014

@author: casey
"""
x = 300

if 0 <= x <= 100: 
    print "goodbye" 
elif 100 <= x <= 500: 
    print "goodbye" 
elif 600 <= x <=1000: 
    print "ciao" 

weekday = False 
vacation = False 


if weekday ==True or vacation ==False: 
    print "False"
else: 
    print "True" 

     
     
def hello_world(x): 
    print "hello, World!" 
    print "My name is" + x 
    
#from Practice import hello_world

def hypotenuse(a,b): 
    answer =(a**2 + b**2)**0.5
    return answer 