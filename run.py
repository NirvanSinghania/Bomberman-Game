import numpy as numpy
import os
import random
import time

from input_output import char
from game_board import board, Board
from hero_enemy import Hero, Enemy
from bomb import Bomb
from config import *


# Helper function to randomly get an empty location in the grid

def get_empty_element():
    L = []
    for i in range(len(board.M)):
        for j in range(2, len(board.M[0])):
            if board.M[i][j] == 0:
                L.append([i, j])

    x = random.randint(0, len(L) - 1)
    return L[x]


# Helper function to create enemies in a randomly chosen location

def initialize_enemies():
    k = get_empty_element()
    e = Enemy(k[0], k[1])
    e.create_enemy()
    board.Enemy_list.append(e)
    board.M[k[0]][k[1]] = 4


# Initialie level of the game as 0

level = 0


def NewFrame():

    # Clear the screen before rendering new frame

    os.system('clear')

    # First the Hero is created on the grid based on its updated position

    board.hero.create_hero()

    # Next the enemies which are alive are created

    for i in board.Enemy_list:

        if i.alive == 1:

            i.move()
            i.create_enemy()

    # Print the matrix

    board.gen_grid_from_matrix()

    print 'Score : ' + str(board.hero.get_score()) \
        + '  Number of lives left : ' + str(board.hero.lives_left)
    global level
    print 'Level ' + str(level + 1)


# For different levels different enemy numbers and frame rates

enemynumber = [4, 5, 6]
frame = [1, 0.5, 0.3]

temp = 3

# Checker variable for "q" keypress

is_quit = 0

while level < 3:

    # Initialization of board and input based on level

    board.initialize()
    board.num_of_enemies = enemynumber[level]
    char.set_frame_rate(frame[level])

    # Printing current level for the first time

    os.system('clear')
    board.gen_matrix()

    # Initialize hero variable of board as an instance of our bomberman(Hero)

    board.hero = Hero(2, 1)

    # Number of lives initially 3

    board.hero.lives_left = temp
    board.hero.create_hero()
    for i in range(board.num_of_enemies):
        initialize_enemies()
    board.gen_grid_from_matrix()

    # Initializing a disabled bomb

    mybomb = Bomb(0, 0)

    while True:

        # Check if the hero lost his life

        if board.game_end == 1:
            board.hero.lives_left -= 1

            # if no lives left end the game

            if board.hero.lives_left == 0:
                break
            else:

                # Start afresh

                board.game_end = 0

                # Give the hero a new position to start

                board.hero.clear()
                m = get_empty_element()
                board.hero.x = m[0]
                board.hero.y = m[1]
                board.hero.alive = 1

                global mybomb
                # If the bomb was previously active it should be disabled now

                if board.is_bomb == 1:
                    mybomb.end_bomb()
                    board.is_bomb = 0
                mybomb.counter = 0

                # Wait introduced to give player some time after losing life

                starttime = time.time()
                while time.time() - starttime < 2:
                    lol = 1
                NewFrame()

        # If the player has cleared all the enemies take subsequent action

        if board.num_of_enemies == 0:
            break

        # Actions based on keypress

        c = char.getch()
        if c is not None:
            keycode = ord(c)

            # End game manually

            if keycode == ord("q"):

                # global is_quit

                is_quit = 1
                break

            # movement keys

            if keycode == 119:
                board.hero.move_up()
            elif keycode == 100:
                board.hero.move_right()
            elif keycode == 115:
                board.hero.move_down()
            elif keycode == 97:
                board.hero.move_left()
            elif keycode == ord("b") and board.is_bomb == 0:

                # handling bomb creation

                mybomb = Bomb(board.hero.x, board.hero.y)
                board.is_bomb = 1

        # managing bomb if one has been planted using its master function

        if board.is_bomb == 1:

            global mybomb

            mybomb.inc()
            board.hero.check_in_explosion()
            for i in board.Enemy_list:
                if i.alive == 1:
                    i.check_in_explosion()

        # Checking if hero is alive or in safe position or not

        if board.M[board.hero.x][board.hero.y] == 4 or board.hero.alive == 0:
            board.game_end = 1

        NewFrame()

    # Actions between levels and events

    if is_quit == 1:
        break

    # We took level as 0-based

    if level == 3:
        print 'You Won'
        break

    if board.hero.lives_left == 0:
        print 'You Lost'
        break

    # Remember we initialize heros lives using temp to communicate between levels

    temp = board.hero.lives_left
    level += 1

