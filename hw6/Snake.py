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
        """Instantiates a SnakeModel object, which creates a snake with a length of three, random position, and random direction 
        (up, down, right, or left), and creates a pellet with a random position."""
        
        # prevents snake from moving diagonally or not moving at all
        x_dir = random.randint(-1,1) 
        if x_dir == 1 or x_dir == -1:  
            y_dir = 0
        else:
            y_dir = random.randint(-1,1)
            while(y_dir == 0):
                y_dir = random.randint(-1,1)
        
        self.snake = Snake(3,random.randrange(0,700,15),random.randrange(0,700, 15),self,(x_dir,y_dir)) #initializes a snake of length 3, with a random direction and a random position  
        self.pellet = Pellet(random.randrange(0,700,15),random.randrange(0,700, 15)) # initializes a pellet with a random position
        
    def update(self):
        """Updates the snake."""
        self.snake.update()

class Snake: 

    def __init__(self,length,x,y, model,direction):
        """Instantiates a Snake object with a given length, an x and y position, and a direction."""
 
        self.head = body_part(x,y,None)
        self.tail = self.head
        self.direction = direction
        self.model = model
   
        for i in range(length): # adds 'length' number of body parts to the snake
            new_body_part = body_part(self.tail.x,self.tail.y, None)
            self.tail.setNext(new_body_part);
            self.tail = new_body_part
        
    def add_body_part(self):
        """Creates a snake body part and adds it to the snake."""
        
        new_body_part = body_part(self.tail.x,self.tail.y,None)
        self.tail.setNext(new_body_part);
        self.tail = new_body_part
         
    def get_length(self):
        """Returns the length of the snake."""
        return self.length
    
    def update(self):
        """ Check the Game Over conditions and checks if the snake has eaten a food pellet, given its current position and direction.
        Updates the snake's head's position."""        
        
        # the current position and direction of the snake head
        current_x = self.head.x
        current_y = self.head.y
        current_dir = self.direction
        
        # the position that the snake head should move to next
        next_x = current_x + current_dir[0]*15
        next_y = current_y + current_dir[1]*15
        
        # Game Over conditions - checks whether the snake has collided with the border of the playing field
        if next_x > 700 or next_x < 0: 
            return False 
        elif next_y > 700 or next_y < 0:  
            return False
        
        # checks if the snake has reached a pellet
        elif self.head.x == model.pellet.x_pellet and self.head.y == model.pellet.y_pellet:
            # if so, the snake eat the pellet and another pellet is regenerated
            model.pellet.set_new_pellet_location()
            self.add_body_part()
        else:
            self.head.update(next_x, next_y) # moves the head to its next positions
               
    def set_direction(self, direction): 
        """Sets the direction of the snake to the given direction."""
        self.direction = direction
        
    def get_direction(self): 
        """Returns the current direction of the snake."""
        return self.direction
        
class body_part: 
    """Body part of a snake instance."""
    
    def __init__(self,x, y, next_body_part):
        """Instantiates a snake body part with a given x position, y position, and another body part."""
        self.x = x
        self.y = y 
        self.next_body_part = next_body_part 
    
    def update(self,x,y):
        """Updates the position of each snake body part in a snake instance.""" 
        if self.next_body_part is not None:
            self.next_body_part.update(self.x,self.y)
        self.x = x
        self.y = y
        
    def setNext(self,next_body_part):
        """ Creates a pointer to the body part following the current body part. """
        self.next_body_part = next_body_part;

class Pellet:
    """Food pellet that the snake wants to eat."""
    def __init__(self, x_pellet, y_pellet):
        """Instantiates a food pellet object with an x position and a y position. """
        self.x_pellet = x_pellet
        self.y_pellet = y_pellet
        
    def set_new_pellet_location(self): 
         """Gives the pellet a new random position."""
         self.x_pellet = random.randrange(0,700,15)
         self.y_pellet = random.randrange(0,700, 15)

class PyGameWindowView:
    def __init__(self,model,screen,pellet,snake):
        """Instantiates a view window object with a game model, a screen, a pellet, and a snake."""
        self.model = model
        self.screen = screen
        self.pellet = pellet
        self.snake = snake
        
    def draw(self):
        """ Sets the screen color to white, draws a food pellet, draws a snake, and updates the display."""
        self.screen.fill(pygame.Color(255,255,255))
        
        rows = 200
        columns = 200
        width = 15
        height = 15

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
        """ Instantiates a keyboard controller object with a game model and a snake."""
        self.model = model
        self.snake = snake
        
    def handle_keyboard_event(self,event):
        """ Sets the keyboard controls - pressing one of the arrow keys changes the direction of the snake."""
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
    """ Main function that runs the game and handles replay and quit options."""
    prompt = raw_input("S N A K E \n Type 'PLAY' to start a new game: ");
    
    playing = True
    if prompt == "PLAY":
        size = (700,700)
        screen = pygame.display.set_mode(size)
        while(playing):
            model = SnakeModel()
            view = PyGameWindowView(model,screen,model.pellet,model.snake)
            controller= PyGameKeyboardController(model,model.snake)
            
            running = True
            while running:
                if model.snake.update() == False:
                    prompt = raw_input("Game Over! Type 'PLAY' to try again. Type 'QUIT' to quit the Snake: ")
                    if prompt == 'PLAY':
                        running = False
                    elif prompt == 'QUIT':
                        running = False
                        playing = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == KEYDOWN:
                        controller.handle_keyboard_event(event)
                model.update()
                view.draw()
                time.sleep(0.1)
        pygame.quit()