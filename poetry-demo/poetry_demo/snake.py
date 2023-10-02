from constants import *
from helper import *
import copy


class Snake:
    def __init__(self, locations: list, debug):
        self.__size: int = SNAKE_SIZE if not debug else 0
        self.__location: list = locations if not debug else [] # Head is always the last coordinate (index -1)
        self.__need_to_grow = 0
        
    def move_snake(self, direction: str = "Up"):
        ''' This function makes the snake move in the desired direction, and handles its grow if needed '''        
        is_dead = False
        old_loc = []
        current_head = self.__location[-1]
        # Handle snake growth if needed
        if self.__need_to_grow == 0:
            old_loc = self.__location[0]
            del self.__location[0]
        else:
            self.__size += 1
            self.__need_to_grow -= 1
        # Snake moves
        new_head = make_something_move(current_head, MOVES[direction])
        self.__location.append(new_head)
        
        if new_head in self.__location[0:-1]: # If the snake hurts himself, you lose
            is_dead = True
        return {"is_dead": is_dead, "old_loc": old_loc, "new_loc": new_head}
        
        
    def update_size(self, coordinate):
        """ This function updates size and location of snake if he got cut in half """
        for index, loc in enumerate(self.__location):
            if loc == coordinate:
                to_be_deleted = self.__location[0: index + 1]
                self.__location = self.__location[index + 1:]
                self.__size = len(self.__location)
                return to_be_deleted
        
        
    def return_head_and_neck(self):
        ''' This function returns the coordinates of the head and "neck" of the snake - that is, all of the coordinates
        who will kill the snake if a wall touches them '''
        return self.__location[-1:-3:-1]
    
    
    def get_location(self):
        """get location of snake"""
        return self.__location

    def get_head(self):
        """get location of the head of the snake"""
        return self.__location[-1]

    def get_size(self):
        """get the size of the snake"""
        return self.__size
    
    def growing(self):
        """tell the snake that he need to grow"""
        self.__need_to_grow += 3