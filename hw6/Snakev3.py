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
    """This class initializes a snake object with the snake's starting direction and position. 
    As well as a pellet object with its starting position."""
    
    def __init__(self):
        
        x_dir = random.randint(-1,1) # prevents snake from moving diagonally or not moving at all
        if x_dir == 1 or x_dir == -1:  
            y_dir = 0
        else:
            y_dir = random.randint(-1,1)
            while(y_dir == 0):
                y_dir = random.randint(-1,1)
        
        self.snake = Snake(3,random.randrange(0,700,15),random.randrange(0,700, 15), self,(x_dir,y_dir)) #Initializes a snake of length 3, with a random direction and random position.  
        self.pellet = Pellet(random.randrange(0,700,15),random.randrange(0,700, 15)) # initializes a pellet with a random position. 
        
    def update(self): # update the snake 
                
        self.snake.update()

class Snake: 
    """This class takes in a length of the snake, position of the snake, direction of the snake, 
    and the game model. It creates three body parts, allows for the addition of more body parts when the snake eats food pellets, and 
    checks for Game Over conditions.""" 
    
    def __init__(self,length,x,y, model, direction):
        """This method takes in a length, an x and y position, a direction, and a game model to initialize a snake instance. 
        This method creates a snake with three body parts."""  
        self.head = body_part(x,y,None)
        self.tail = self.head
        self.direction = direction
        self.model = model
   
        for i in range(length):
            new_body_part = body_part(self.tail.x,self.tail.y, None)
            self.tail.setNext(new_body_part);
            self.tail = new_body_part
        
    def add_body_part(self):
        """Creates a new body part and adds it to the snake instance."""
        
        new_body_part = body_part(self.tail.x,self.tail.y,None)
        self.tail.setNext(new_body_part);
        self.tail = new_body_part
         
    def get_length(self):
        """Returns the length of the snake"""
        return self.length
    
    def update(self):
        """First, takes in the position and direction of the snake. 
        Second, checks Game Over conditions and growth of the snake. 
        Third, updates the snake's position.""" 
        
        current_x = self.head.x
        current_y = self.head.y
        current_dir = self.direction
        
        next_x = current_x + current_dir[0]*15
        next_y = current_y + current_dir[1]*15
        
        if next_x > 700 or next_x < 0: 
            print "Game Over!" 
            return False 
        elif next_y >700 or next_y <0: 
            print "Game Over!" 
            return False 
        elif self.head.x == model.pellet.x_pellet and self.head.y == model.pellet.y_pellet: 
            model.pellet.set_new_pellet_location() #changing the location of the pellet
            self.add_body_part()
        else:         
            self.head.update(next_x, next_y)
               
    def set_direction(self, direction): 
        """sets the direction of the snake instance."""
        self.direction = direction
        
    def get_direction(self): 
        """Returns the current direction of the snake.""" 
        return self.direction
        
class body_part: 
    """Body part of the snake"""
    
    def __init__(self,x, y, next_body_part):
        """Takes in the position of the snake and the next body part"""
        #this is just updating the x and y position. 
        self.x = x
        self.y = y 
        self.next_body_part = next_body_part 
    
    def update(self,x,y):
        """Updates the position of each snake body part.""" 
        if self.next_body_part is not None:
            self.next_body_part.update(self.x,self.y)
        self.x = x
        self.y = y
        
    def setNext(self,next_body_part):
        """ Takes in a body part and sets the body part to be the one after a given body part """
        self.next_body_part = next_body_part;

class Pellet:
    """Food Pellet that the snake eats """
    def __init__(self, x_pellet, y_pellet):
        """Takes in the position of the pellet."""
        self.x_pellet = x_pellet # position of pellet on playing field
        self.y_pellet = y_pellet
        
    def set_new_pellet_location(self): 
         """Gives the pellet a new random position"""
         self.x_pellet = random.randrange(0,700,15)
         self.y_pellet = random.randrange(0,700, 15)

class PyGameWindowView:
    def __init__(self,model,screen,pellet,snake):
        """Takes in a game model, screen, pellet instance, and snake instance."""
        self.model = model
        self.screen = screen
        self.pellet = pellet
        self.snake = snake
    def draw(self):

        self.screen.fill(pygame.Color(255,255,255))
        
        rows = 200
        columns = 200
        width = 15
        height = 15
        
        for i in range(rows):
            for j in range(columns):
                cell = pygame.Rect((i*width),(j*height),width, height)
                pygame.draw.rect(self.screen,(255,255,255), cell)
        
        
        food_pellet = pygame.Rect(self.pellet.x_pellet,self.pellet.y_pellet,width,height)
        pygame.draw.rect(self.screen,(random.randint(0,255),random.randint(0,255), random.randint(0,255)), food_pellet)
        
        body_part = self.snake.head
        while body_part is not None:
            body_part_cell = pygame.Rect(body_part.x,body_part.y,width,height)
            pygame.draw.rect(self.screen,(47,192,47),body_part_cell)
            body_part = body_part.next_body_part
        
        pygame.display.update()

class PyGameKeyboardController:
    def __init__(self,model,snake):
        self.model = model
        self.snake = snake
        
    def handle_keyboard_event(self,event):
        dire = self.snake.get_direction()  
        if dire[0] == 0: 
            if event.key == pygame.K_LEFT:
                self.snake.set_direction((-1,0))
            elif event.key == pygame.K_RIGHT:
                self.snake.set_direction((1,0))
        elif dire[1] ==0: 
            if event.key == pygame.K_UP:
                self.snake.set_direction((0,-1))
            elif event.key == pygame.K_DOWN:
                self.snake.set_direction((0,1))       

if __name__ == '__main__':
    prompt = raw_input("S N A K E \n Type 'PLAY' to start a new game: ");
    if prompt == "PLAY":
        size = (700,700)
        screen = pygame.display.set_mode(size)
        
        model = SnakeModel()
        view = PyGameWindowView(model,screen,model.pellet,model.snake)
        controller= PyGameKeyboardController(model,model.snake)
        
        running = True
        while running:
            if model.snake.update() == False:
                prompt = raw_input("Type 'PLAY' to try again. Type 'QUIT' to quit the game: ")
                if prompt == 'PLAY':
                    pass
                elif prompt == 'QUIT':
                    running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    controller.handle_keyboard_event(event)
            model.update()
            view.draw()
            time.sleep(0.01)
        pygame.quit()