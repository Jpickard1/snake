#########################################################################################
#
#                                   Human Snake Class
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: A snake class that allows people to play the game
#
#   Class attributes:
#       1. size...............stores the length of the snake
#       2. x_delta............stores the number of pixels the snake moves in the x 
#                             direction each turn
#       3. y_delta............stores the number of pixels the snake moves in the y
#                             direction each turn
#       4. snake_block_size...stores the size of each chunk of snake
#       5. position...........a list storing the location of each snake block
#
#   Methods:
#       - __init__.......initializes the snake to have 1 block located at the center
#       - move...........takes user input to move the snake according to the game rules
#       - get_position...returns self.position
#       - grow...........increments self.size by 1
#       - get_size.......returns self.size
#       - valid_board....checks if the board size and block size work
#
#########################################################################################
import pygame
class Csnake_human:

    #####################################################################################
    #
    #   Csnake_human:__init__
    #       Parameters: 1. p_board_size.........number of pixels on the board
    #                   2. p_snake_block_size...size of each snake block
    #
    #       Description: Initializes the snake to the head of the snake is located at the
    #                    center of the screen
    #
    #####################################################################################
    def __init__(self,p_board_size, p_snake_block_size):
        if self.valid_board(p_board_size, p_snake_block_size):
            board_size = p_board_size
            self.snake_block_size = p_snake_block_size
        else:
            board_size = 800
            self.snake_block_size = 25
        self.position = list()
        head = (board_size/2, board_size/2)
        self.position.insert(0,head)
        self.size = 1
        self.x_delta = 0
        self.y_delta = 0

    #####################################################################################
    #
    #   Csnake_human:move
    #       Parameters: 1. snack_location...location of the snack on the board
    #
    #       Description: Receives input from the keyboard for which way the snake should
    #                    move. It uses the arrow keys as standard input. If no new key 
    #                    strokes are recorded, then the snake continues in the direction
    #                    it was previously headed. If the snake has length > 1 and the
    #                    user inputs the direction opposite of the current direction,
    #                    then the snake will die.
    #
    #####################################################################################
    def move(self, snack_location):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_delta = -1 * self.snake_block_size
                    self.y_delta = 0
                elif event.key == pygame.K_RIGHT:
                    self.x_delta = self.snake_block_size
                    self.y_delta = 0
                elif event.key == pygame.K_UP:
                    self.y_delta = -1 * self.snake_block_size
                    self.x_delta = 0
                elif event.key == pygame.K_DOWN:
                    self.y_delta = self.snake_block_size
                    self.x_delta = 0
        head = self.position[0]
        x_cord = head[0]
        y_cord = head[1]
        new_head = (x_cord+self.x_delta, y_cord+self.y_delta)
        self.position.insert(0, new_head)
        if not (new_head[0] == snack_location[0] and new_head[1] == snack_location[1]):
            self.position.pop()
        else:
            self.grow()
            print("No pop!")

    #####################################################################################
    #
    #   Csnake_human:get_position
    #       Returns: self.position
    #
    #####################################################################################
    def get_position(self):
        return self.position
    
    #####################################################################################
    #
    #   Csnake_human:grow
    #       Description: increases self.size by 1
    #
    #####################################################################################
    def grow(self):
        self.size = self.size + 1

    #####################################################################################
    #
    #   Csnake_human:get_size
    #       Returns self.size
    #
    #####################################################################################
    def get_size(self):
        return self.size

    #####################################################################################
    #
    #   Csnake_human:valid_board
    #       Parameters: 1. p_board_size
    #                   2. p_block_size
    #
    #       Description: if the sizes are valid according to the rules below, then the 
    #                    snake is initialized with the input parameters. Otherwise the 
    #                    board_size is set to 800 and the block_size is set to 25
    #
    #       Note: a valid board must:
    #           1. have a board size > block size
    #           2. have a board size that is an integer multiple of block size
    #           3. have a board size < than 800 (otherwise it won't fit on my screen)
    #           Similar rules apply to snake objects
    #
    #####################################################################################
    def valid_board(self, p_board_size, p_block_size):
        valid_parameters = True
        if p_board_size > 800:
            valid_parameters = False
        counter = 0
        while counter != p_board_size and valid_parameters:
            counter = counter + p_block_size
            if counter > p_board_size:
                valid_parameters = False
        return valid_parameters