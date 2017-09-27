from game_board import board


class Person:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = 1

    def clear(self):
        """ Fill air in place of Person's position"""
        board.change_grid(self.x, self.y, 0)

    """ Movement functions for the Person """
    def move_right(self):
        if board.check_valid(self.x, self.y + 1) and self.check_obstacle(self.x, self.y + 1):
            self.clear()
            self.y += 1

    def move_left(self):
        if board.check_valid(self.x, self.y - 1) and self.check_obstacle(self.x, self.y - 1):
            self.clear()
            self.y -= 1

    def move_up(self):
        if board.check_valid(self.x - 1, self.y) and self.check_obstacle(self.x - 1, self.y):
            self.clear()
            self.x -= 1

    def move_down(self):
        if board.check_valid(self.x + 1, self.y) and self.check_obstacle(self.x + 1, self.y):
            self.clear()
            self.x += 1

    """ Explicit destructor for Person . It changes the value of alive variable"""
    def kill(self):
        self.alive = 0

    def check_in_explosion(self):
        L = [self.x, self.y]
        if L in board.Explosion_list:
            self.kill()


