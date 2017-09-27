import numpy as np
from config import *


class Board:

    def __init__(self):
        self.grid = []
        self.M = []
        self.Explosion_list = []
        self.Enemy_list = []
        self.game_end = 0
        self.is_bomb = 0
        self.obj_height = 2
        self.obj_length = 4
        self.num_of_rows = 18
        self.num_of_columns = 20
        self.num_of_enemies = 4
        self.hero = ''

    def helper(self, x):
        """ Map for numbers to identities """
        if x == 1:
            return self.obj_length * brick_symbol
        elif x == 2:
            return self.obj_length * wall_symbol
        elif x == 5:
            return self.obj_length * explosion_symbol
        elif x == 7:
            return self.obj_length * bomb_symbol
        else:
            return self.obj_length * space

    def change_grid(self, i, j, k):
        """ A change in M should also be made in the grid """
        """ k decides the change """
        board.M[i][j] = k
        board.grid[2 * i][j] = self.helper(k)
        board.grid[2 * i + 1][j] = self.helper(k)

    def gen_matrix(self):
        row_size = self.num_of_rows
        col_size = self.num_of_columns

        """ Beginning row of game should be all walls. """
        self.M.append([2] * (col_size + 2))

        """We get a list using random . To create more air as compared to bricks
        if the returned value <= .2 we consider it as a brick.
        Thus, Air : Brick = 4 : 1"""
        for i in range(row_size):
            L = list(np.random.random(int(col_size)))
            self.M.append([2] + list(map(lambda x: int(x <= 0.2), L)) + [2])
        
        """ Last Row """
        self.M.append([2] * (col_size + 2))
        
        """ Creating walls at fixed positions. """
        for i in range(1, row_size, 3):
            for j in range(1, col_size, 3):
                self.M[i][j] = 2

        """Ensuring the first four blocks are air for bomber to move"""
        self.M[1][1] = 0
        self.M[1][2] = 0
        self.M[2][1] = 0
        self.M[2][2] = 0
        """Conversion of 1/1 M of numbers to 2/4 grid of characters"""
        for i in self.M:
            for it in range(self.obj_height):
                self.grid.append(list(map(self.helper, i)))

    def gen_grid_from_matrix(self):
        """ Print function for matrix. """
        for i in self.grid:
            for j in i:
                print j,
            print

    def check_valid(self, i, j):
        """ To check if a given set of coordinates are within the board """
        return i > 0 and i <= self.num_of_rows and j > 0 and j \
            <= self.num_of_columns

    def initialize(self):
        """ For using the same board afresh """
        self.grid = []
        self.M = []
        self.Explosion_list = []
        self.Enemy_list = []
        self.game_end = 0
        self.is_bomb = 0


board = Board()

