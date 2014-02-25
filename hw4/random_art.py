# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
from math import *
import Image

## SS: It took me a bit of reading to figure out what "Xv" and "Yv" do, it might be nice to include
##     them in your doc string or where you declare the 'functions' list. 
def build_random_function(min_depth, max_depth):
    """This function takes in a minimumum level depth of recursion and a maximum level. The it randomly computes a long function. Recursion allows the function to have many depths. """ 
        
    functions = ["prod", "cos_pi", "sin_pi", "Xv", "Yv", "x^2", "y^2"] #all the possible functions
    variables = ["x", "y"]#all the possible variables
    
    if max_depth ==0: #the basecase
        return [variables[randint(0,1)]]
    
    randomIndex = randint(0,6) #choosing a random number to go use to find a function
    if functions[randomIndex] =="prod" or "Xv" or "Yv": 
        return [functions[randomIndex], build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)] #if the random number generated is 0, then it is prod and this is the format
    if functions[randomIndex] == "cos_pi" or "sin_pi": 
        return [functions[randomIndex], build_random_function(min_depth-1, max_depth-1)] #if the random number generated is 1 or 2 then it is a sin or cos and this is the format
    if functions[randomIndex] == "x^2" or "y^2": 
        return [functions[randomIndex], (build_random_function(mindepth-1, max_depth-1))**2] #use this function to evaluate a part of a list and square the result 

## SS: Passed my tests :)
## SS: for this function, you might make use of 'elif' statements, even though the functionailty
##     is the same, stylistically, it's preferable
def evaluate_random_function(f, x, y):
    """This function takes in a function, f, with many levels within each argument. It also takes in x, an x corrdinate on the pixel plane. 
    Along with that, it takes in y, a y coordinate on the pixel plane. This function goes through each element of the list
    and with a governing set of rules, calls itself to evaluate a list down to the maximum depth. At the maximum depth, the function replaces "x" or "y" with whatever value the user gave for x or y. """
    if f[0] == "x": 
        return float(x)  ##if what evaluate_random_function is evaluating is simply "x", then replace it with an actual number the user gave 
    if f[0] =="y": 
        return float(y) ###if what evaluate_random_function is evaluating is simply ""y", then replace it with an actual number the user gave 
    if f[0] == "prod": 
        return evaluate_random_function(f[1], x, y)*evaluate_random_function(f[2],x,y) #f(0) wants to multiply f(1)*f(2) but f(1) and f(2) are lists that have many lists inside of them so we use evaluate_random_function to evaluate them for us
    if f[0] == "cos_pi": 
        return cos(pi*(evaluate_random_function(f[1],x,y))) #if the function is evaluating a list that starts with cos_pi, then take the next argument and use evaluate_random_function to evaluate it down to the maximum depth. 
    if f[0] == "sin_pi": 
        return sin(pi*(evaluate_random_function((f[1]),x,y))) #if the function is evaluating a list that starts with sin_pi, then take the next argument and use evaluate_random_function to evaluate it down to the maximum depth.
    if f[0] == "Xv":
        return evaluate_random_function(f[1],x,y) # if the first argument in a function is Xv, then it only returns the next argument 
    if f[0] == "Yv":
        return evaluate_random_function(f[2],x,y) #if the first argument in a function is Yv, then it only returns the second argument 
    if f[0] == "x^2":
        return (evaluate_random_function(f[1],x,y))**2 #this calls this function until the maximum depth is reached and then square the final result
    if f[0] == "y^2": 
        return (evaluate_random_function(f[1],x,y))**2 #this calls itself --recursion--until only a value is left and then squares the final result

## SS: Doc string please?? 
def i_dislike_pictures(filename):  
    
    funcGreen= build_random_function(1,1) #this function acquires an equation for the green portion of the picture
    funcBlue = build_random_function(1,2) #function gte random equation for blue in image
    funcRed = build_random_function(2,2) #this function gets random equation for red in the image 
    
    im = Image.new("RGB", (300,300))#this creates an output image of 300 pixels by 300 pixels
    pixels = im.load()    #this establishes that pixels is will be the variable printing my image
    
    for i in range(0,299): #for loop to transverse my x values 
        for k in range(0,299): #for loop to tranverse y values
            rawX = remap_interval(i,0, 299,-1,1) #changes from 300 X 300 pixels to -1 to 1 
            rawY = remap_interval(k,0,299,-1,1) #changes y values
            Green = remap_interval(evaluate_random_function(funcGreen, rawX,rawY),-1,1, 0, 255) #changes the green equation back to 255 X 255 poster size to fit within pixels
            Blue = remap_interval(evaluate_random_function(funcBlue, rawX,rawY), -1,1, 0,255) #changes blue
            Red = remap_interval(evaluate_random_function(funcRed, rawX, rawY), -1,1,0,255) #changes red            
            pixels[i,k]= (int(Red),int(Green),int(Blue)) #makes image 
    im.save(filename) #saves image 
    
## SS: Passed my tests :)
## SS: And nice job on naming your intermediate variables, it makes a lot of sense to read, and 
##     because you have a descriptive doc string and good variable names, I don't see the need for
##     the comments beside each line, only include them if they're helpful to you. 
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        This function divides the difference between the value and the starting value of the input range by the difference of the entire range.
        This is a percentage/ratio. Then we multiply this percentage by the output range. This is the fraction of the output range and we add 
        it to the output starting value. 
    """
    start = val-input_interval_start #take the subtracts the starting point of the range from the value to find the difference
    percentage = float(start)/(float(input_interval_end) - float(input_interval_start)) #divides the difference btwn the starting value and starting range by the total difference of the input range
    outRange = percentage *(output_interval_end - output_interval_start) #takes the necessary percentage and multiplies it by the output range to get the fraction of that range
    finalPercent = outRange + output_interval_start #adds the percentage of the range to the original to get the output value 
    return finalPercent
    
if __name__ == "__main__":
    print randint(0,2)
    print randint(0,2)