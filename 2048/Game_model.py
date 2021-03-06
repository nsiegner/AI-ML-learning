import tkinter as tk
import random as rnd
import numpy as np
from View import *
class Game_model(object):
    changed = False
    score = 0
    def __init__(self, grid=None):
        self.score = 0
        self.grid = [[0]*4 for i in range(4)]
        self.add_tile_2()
        self.add_tile_2()
        if grid != None:
            self.grid = grid




    #an oportunity to change the grid manually
    def set_grid(self, grid):
        self.grid = grid

    #returns the current grid
    def get_grid(self):
        return self.grid

    # the methods to add tiles to the grid
    def add_tile(self):
        i = rnd.randint(0, 10)
        if i == 0 or i == 1:
            self.add_tile_4()
        else:
            self.add_tile_2()

    def add_tile_2(self):
        x = rnd.randint(0, 3)
        y = rnd.randint(0, 3)
        if self.grid[x][y] == 0:
            self.grid[x][y] = 2
        else:
            self.add_tile_2()

    def add_tile_4(self):
        x = rnd.randint(0, 3)
        y = rnd.randint(0, 3)
        if self.grid[x][y] == 0:
            self.grid[x][y] = 4
        else:
            self.add_tile_4()

    # moving each tile in the grid up, starting from the top left to the bottom right corner
    def push_up(self):
        for i in range(1, 4):
            for j in range(4):
                if self.grid[i][j] != 0:
                    if self.grid[0][j] == 0:
                        self.grid[0][j] = self.grid[i][j]
                        self.grid[i][j] = 0
                        if i != 0:
                            self.changed = True
                    elif self.grid[1][j] == 0:
                        self.grid[1][j] = self.grid[i][j]
                        self.grid[i][j] = 0
                        if i != 1:
                            self.changed = True
                    elif self.grid[2][j] == 0:
                        self.grid[2][j] = self.grid[i][j]
                        self.grid[i][j] = 0
                        if i != 2:
                            self.changed = True

    # merge tiles if two tiles of the same value are below each other
    def merge(self):
            for i in range(3):
                for j in range(4):
                    if self.grid[i + 1][j] == self.grid[i][j] and self.grid[i][j] != None:
                        self.grid[i][j] = self.grid[i][j]*2
                        self.grid[i + 1][j] = 0
                        self.set_score(self.grid[i][j])

    #invert the grid
    def invert(self):
        self.grid.reverse()

    # rotate the grid by 90 degrees to the right
    def rotate_right(self):
        a = np.rot90(self.grid, 3)
        self.grid = a.tolist()
    # rotate the grid by 90 degrees to the left
    def rotate_left(self):
        a = np.rot90(self.grid)
        self.grid = a.tolist()

    # move methods
    def move_up(self):
        self.push_up()
        self.merge()
        self.push_up()

    def move_down(self):
        self.invert()
        self.move_up()
        self.invert()

    def move_left(self):
        self.rotate_right()
        self.move_up()
        self.rotate_left()

    def move_right(self):
        self.rotate_left()
        self.move_up()
        self.rotate_right()

    #check if there are any spots in the grid with no tile on them
    def is_full(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False

        return True


    # checks if the game is won, lost or not done jet
    def get_current_state(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 2048:
                    return "Won"

                elif self.grid[i][j] == 0:
                    return "Not done jet"

        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == self.grid[i + 1][j] or self.grid[i][j] == self.grid[i][j + 1]:
                    return "Not done jet"

        for i in range(3):
            if self.grid[i][3] == self.grid[i + 1][3]:
                return "Not done jet"

            elif self.grid[3][i] == self.grid[3][i + 1]:
                return "Not done jet"

        return "Game Over"

    # keeping count of the score of the game
    def set_score(self, value):
        self.score += value*2

    def get_score(self):
        return self.score
