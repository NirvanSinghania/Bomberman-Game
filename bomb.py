from game_board import board
from config import dx, dy


class Bomb:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.counter = 0
        self.__count_bricks = 0

    def __spread_explosion(self):

        # Adding the areas of attack to the list - Explosion List
        # count_bricks private variable to count the number of bricks affected by bomb

        board.Explosion_list.append([self.x, self.y])
        for i in range(4):
            newx = self.x + dx[i]
            newy = self.y + dy[i]
            if board.check_valid(newx, newy) and board.M[newx][newy] != 2:
                board.Explosion_list.append([newx, newy])
                if board.M[newx][newy] == 1:
                    self.__count_bricks += 1

    def __create_bomb(self):

        # Create the symbol for bomb in output

        board.change_grid(self.x, self.y, 7)

    def __create_explosion(self):

        # for all areas of effect change to explosion symbol

        self.__spread_explosion()
        for i in board.Explosion_list:
            board.change_grid(i[0], i[1], 5)

    def end_bomb(self):

        # Fill all affected areas with air.
        # Increase the score of the bomber due to bricks
        # Re-initialize the variables to that before creation of bomb

        self.counter = 0
        for i in board.Explosion_list:
            board.change_grid(i[0], i[1], 0)
        board.hero.increase_score(self.__count_bricks * 100)
        board.is_bomb = 0
        self.__count_bricks = 0
        board.Explosion_list = []

    def inc(self):

        # The master function which takes the required action on the basis of counter values

        self.counter += 1
        if self.counter <=3:
            self.__create_bomb()
        elif self.counter == 6:
            self.end_bomb()
        elif self.counter == 4:
            self.__create_explosion()


        