#########################################################################################
#
#                                       Game Class
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: Allow for the game to be played by any snake object
#
#   Class attributes:
#       1. board_size...the size of the game board
#       2. block_size...the size of one block
#       3. snack........a tuple that stores the (x,y) coordinates of the snack
#
#   Methods:
#       - __init__......initializes the game board
#       - game_over.....determines when the game is over
#       - print_snake...prints the snake to the screen
#       - print_snack...prints the snack to the screen
#       - print_grid....prints gridlines on the board
#       - play_game.....plays 1 full round of the game
#
#       - set_snack.....determines the location of the snack
#       - valid_board...determines if the board dimensions and block size are valid inputs
#
#########################################################################################
from snake_human import Csnake_human
#from snake_network import Csnake_network
import pygame
import random
import time

class Cgame:
    #####################################################################################
    #
    #   Cgame:__init__
    #       Parameters: 1. p_size.........sets the size of the game board
    #                   2. p_snake_size...sets the size of a snake chunk
    #
    #       Description: Assigns member variables
    #
    #####################################################################################
    def __init__(self, p_size, p_snake_size):
        self.valid_board(p_size,p_snake_size)

    #####################################################################################
    #
    #   Cgame:game_over
    #       Parameters: 1. p_snake...used to determine if the snake is in a legal position
    #
    #       Returns: True: if the snake is out of bounds or has eaten itself
    #                False: all other conditions
    #
    #####################################################################################
    def game_over(self, p_snake):
        head = p_snake.get_position()[0]
        if head[0] < 0 or head[1] < 0 or head[0] >= self.board_size or head[1] >= self.board_size:
            return True
        is_head = True
        for chunk in p_snake.get_position():
            if chunk == head and not is_head:
                #print("exit  2")
                return True
            if is_head:
                is_head = False
        return False

    #####################################################################################
    #
    #   Cgame:print_snake
    #       Parameters: 1. p_snake...used to get snake.position
    #
    #       Description: prints a green circle with a diameter defined by block_size at
    #                    each location in snake.position
    #
    #####################################################################################
    def print_snake(self, p_snake):
        green  = (0,255,0)
        print(p_snake.get_size(), end = ": ")
        for chunk in p_snake.get_position():
            assert(isinstance(chunk,tuple))
            pygame.draw.circle(self.display, green, (int(chunk[0]+(self.block_size/2)), int(chunk[1]+(self.block_size/2))), int(self.block_size/2))#, int(self.block_size)])
            print("("+str(chunk[0])+","+str(chunk[1])+") ", end = "")
        print("")
        # vision lines
        red = (255,0,0)
        pygame.draw.line(self.display, red, (p_snake.get_position()[0][0]+(self.block_size/2),0), (p_snake.get_position()[0][0]+(self.block_size/2), self.board_size))
        pygame.draw.line(self.display, red, (0, p_snake.get_position()[0][1]+(self.block_size/2)), (self.board_size, p_snake.get_position()[0][1]+(self.block_size/2)))

    #####################################################################################
    #
    #   Cgame:print_snack
    #       Parameters: 1. p_snake...used to get snake.position
    #
    #       Description: prints a red square with a length defined by block_size at the 
    #                    location of the snack
    #
    #####################################################################################
    def print_snack(self, p_snake):
        red = (255,0,0)
        print("snack: ("+str(self.snack[0])+","+str(self.snack[1])+") ", end = "")
        if p_snake.get_position()[0] == self.snack:
            self.set_snack(p_snake)
        pygame.draw.rect(self.display, red, [self.snack[0], self.snack[1], self.block_size, self.block_size])

    #####################################################################################
    #
    #   Cgame:print_grid
    #       Description: prints grid lines seperated by a distance of self.block_size
    #
    #       Note: As a general note on the game layout, all snake chuncks and snacks will
    #             be within squares defined by the gridlines. NOT at the intersection of
    #             gridlines
    #
    #####################################################################################
    def print_grid(self):
        line_color = (0,0,100)
        step = 0
        while step <= self.board_size:
            pygame.draw.line(self.display, line_color, (0, step), (self.board_size, step))
            pygame.draw.line(self.display, line_color, (step, 0), (step, self.board_size))
            step = step + self.block_size

    #####################################################################################
    #
    #   Cgame:play_game
    #       Parameters: 1. p_snake...the snake object to be used in the game
    #
    #       Description: playes 1 full round of the snake game until the snake dies
    #
    #####################################################################################
    def play_game(self, p_snake):
        self.display = pygame.display.set_mode((self.board_size, self.board_size))
        pygame.display.set_caption('Snake Game')
        clock = pygame.time.Clock()
        end = False
        self.set_snack(p_snake)
        self.print_snake(p_snake)
        self.print_snack(p_snake)
        self.print_grid()
        pygame.display.update()
        while not end:
            p_snake.move(self.snack)
            end = self.game_over(p_snake)
            if not end:
                black = (0,0,0)
                self.display.fill(black)
                self.print_grid()
                self.print_snack(p_snake)
                self.print_snake(p_snake)
            pygame.display.update()
            clock.tick(10)
        print("Game Over")
        return p_snake.get_size()

    #####################################################################################
    #
    #   Cgame:valid_board
    #       Parameters: 1. p_board_size
    #                   2. p_block_size
    #
    #       Description: if the sizes are valid according to the rules below, then the 
    #                    game is initialized with the input parameters. Otherwise the 
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
        if valid_parameters:
            self.block_size = p_block_size
            self.board_size = p_board_size
        else:
            self.block_size = 25
            self.board_size = 800

    #####################################################################################
    #
    #   Cgame:set_snack
    #       Parameters: 1. p_snake
    #
    #       Description: places a snack in an appropriate location
    #
    #####################################################################################
    def set_snack(self, p_snake):
        blocks_per_side = self.board_size/self.block_size
        in_snake = True
        while in_snake:
            in_snake = False
            self.snack = (round(random.randrange(0,blocks_per_side))*self.block_size,round(random.randrange(0,blocks_per_side))*self.block_size)
            for chunk in p_snake.get_position():
                if chunk == self.snack:
                    in_snake = True

board_size = 782
p_block_size = 27
game_board = Cgame(board_size, p_block_size)#,500)
joshua = Csnake_human(board_size, p_block_size)
game_board.play_game(joshua)
