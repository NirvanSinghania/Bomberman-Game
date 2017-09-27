from persons import Person
from game_board import board
from config import *
import random


# Our main character - Bomberman aka Hero!!!

class Hero(Person):

    def __init__(self, x, y):
        self.lives_left = 3
        self.__score = 0
        Person.__init__(self, x, y)

    # Define check_obstacle for a Hero

    def check_obstacle(self, i, j):
        return board.M[i][j] == 0 or board.M[i][j] == 4 or board.M[i][j] == 5 or board.M[i][j] == 7

    def create_hero(self):

        # It creates the hero int the given position

        board.M[self.x][self.y] = 3
        board.grid[2 * self.x][self.y] = man_top
        board.grid[2 * self.x + 1][self.y] = man_down

    # Functions to access the private variable score ( a safe object)

    def increase_score(self, x):
        self.__score += x

    def get_score(self):
        return self.__score


class Enemy(Person):

    def __init__(self, x, y):
        Person.__init__(self, x, y)

    def check_obstacle(self, i, j):
        return board.M[i][j] == 0 or board.M[i][j] == 3 or board.M[i][j] == 5 or board.M[i][j] == 7

    def create_enemy(self):
        board.M[self.x][self.y] = 4
        board.grid[2 * self.x][self.y] = enemy_top
        board.grid[2 * self.x + 1][self.y] = enemy_down

    # The definitions of move for the enemy

    def move(self):

        # Decide to go left,right,up or down using random

        ran = random.randint(0, 3)

        # Get the new co-ordinate using the dx,dy array

        newx = self.x + dx[ran]
        newy = self.y + dy[ran]
        if board.check_valid(newx, newy) and self.check_obstacle(newx, newy):

            # Additional check for bomberman in the new position

            if board.M[newx][newy] == 3:
                board.game_end = 1
            self.clear()
            self.x = newx
            self.y = newy

    # Method Overriding of parent class

    def kill(self):

        # Every time an enemy is killed the score increases and num_of_enemies dedcreases

        board.hero.increase_score(300)
        board.num_of_enemies -= 1
        self.alive = 0

