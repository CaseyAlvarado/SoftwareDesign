# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/casey/.spyder2/.temp.py
"""

print "Hello World" 


from unum.units import *
from unum import Unum

ft = 0.3048*m 
lb =  0.453592*kg

wrench = 181*foot*pound
acceleration = 9.81 *m/s**2
NewtonMeters = wrench*acceleration
print NewtonMeters

ft = Unum.unit('ft', 1/5280.0*mile,'foot')
lb = Unum.unit('lb', 0.22481*N, 'pound(force)')

print (181*ft*lb).asUnit(N*m)