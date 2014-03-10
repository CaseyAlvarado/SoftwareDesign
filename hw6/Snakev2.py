# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 10:10:28 2014

@author: casey
"""

import pygame
from pygame.locals import *
import random
import time

class SnakeModel:
    def __init__(self):
        self.playing_field = PlayingField()
        self.snake = Snake(3) #Needs to be updates with direction 
        self.pellet = Pellet(random.randint(0,200),random.randint(0,200)) # should this be completely random? no. We can restrict it to only the top of the grid 
        
    def update(self): # update playing field + snake + food pellets
        self.playing_field.update()
        self.snake.update()
        self.pellet.update()

class PlayingField:
    def __init__(self):
        playing_field = []
        for i in range(200): # for each row of the playing field grid
            for j in range(200): # for each column of the playing field grid
                playing_field.append(0) # grid initially set to a matrix of all 0's
    def update(self):
        pass # update grid!

class Snake: 
    def __init__(self,length,x,y, model, direction):
        self.head = body_part(x,y,None)
        self.tail = self.head
        self.model = model 
        self.direction = direction
        
        for i in range(length):
            add_body_part()
        
    def add_body_part(self):
        new_body_part = body_part(self.tail.x,self.tail.y,None)
        self.tail.next = new_body_part
        self.tail = new_body_part
    
    def update(self):
        current_x = self.head.x
        current_y = self.head.y
        current_dir = self.direction
        
        next_x = current_x + current_dir[0]
        next_y = current_y + current_dir[1]
        
        if next_x > 200 or next_x <0: 
            print "You lose! Game Over!" 
            return False 
        if next_y >200 or next_y <0: 
            print "You lose!" 
            return False 
        #here add things that make snake longer 
        else:         
            self.head.update(next_x, next_y)
        
               
    def set_direction(self, direction): 
        self.direction = direction
    
        
class body_part: 
    def __init__(self,x, y, next_body_part): 
        #this is just updating the x and y position. 
        self.x = x
        self.y = y 
        self.next_body_part = next_body_part 
    
    def update(self,x,y):
        if next_body_part is not None:
            next_body_part.update(self.x,self.y)
        self.x = x
        self.y = y

class Pellet:
    def __init__(self,x,y):
        self.x = x # position of pellet on playing field
        self.y = y
        
    def update(self):
        pass # update pellet! (location when eaten?) Yes, we want to delete it from the boardafter eaten 

class PyGameWindowView:
    def __init__(self,model,screen,pellet):
        self.model = model
        self.screen = screen
        self.pellet = pellet
    def draw(self):
        self.screen.fill(pygame.Color(200,0,0))
        
        rows = 200
        columns = 200
        width = 15
        height = 15
        
        for i in range(rows):
            for j in range(columns):
                cell = pygame.Rect((i*width),(j*height),width, height)
                pygame.draw.rect(self.screen,(255,255,255), cell)
        
        food_pellet = pygame.Rect(self.pellet.x,self.pellet.y,width,height)
        pygame.draw.rect(self.screen,(random.randint(0,200),random.randint(0,200), random.randint(0,200)), food_pellet)
                
        # fill with food and snake
        pygame.display.update()

class PyGameKeyboardController:
    def __init__(self,model,snake):
        self.model = model
        self.snake = snake
        
    def handle_keyboard_event(self,event):
        if event.key == pygame.K_LEFT:
            self.snake.set_direction((-1,0))
        elif event.key == pygame.K_RIGHT:
            self.snake.set_direction((-1,0))
        elif event.key == pygame.K_UP:
            self.snake.set_direction((0,1))
        elif event.key == pygame.K_DOWN:
            self.snake.set_direction((0,-1))

if __name__ == '__main__':
    pygame.init()
    prompt = raw_input("S N A K E \n Type 'play' to start a new game: ");
    if prompt.lower() == "play":
        size = (700,700)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("S N A K E")
        
        model = SnakeModel()
        view = PyGameWindowView(model,screen,model.pellet) ##pellet? snake?
        controller = PyGameKeyboardController(model)
        
    
        
        #playing = True
        running = True
        #while model.snake.update():
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type ==KEYDOWN:
                    controller.handle_keyboard_event(event)
            model.update()
            view.draw()
            time.sleep(0.01)
        pygame.quit()
        
