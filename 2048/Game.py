import tkinter as tk
import random as rnd
class Game(object):


    def __init__(self):
        self.grid = [[None]*4 for i in range(4)]
        self.add_tile_2()
        self.add_tile_2()
        


    def set_grid(self, grid):
        self.grid = grid



    def add_tile_2(self):
        x = rnd.randint(0, 3)
        y = rnd.randint(0, 3)
        if self.grid[x][y] == None:
            self.grid[x][y] = 2
        else:
            add_tile_2()

    def add_tile_4(self):
        x = rnd.randint(0, 3)
        y = rnd.randint(0, 3)
        if self.grid[x][y] == None:
            self.grid[x][y] = 4
        else:
            add_tile_4()

    def push_up():
        for i in range(1, 4):
            for j in range(4):
                if self.grid[i][j] != 0:
                    if self.grid[0][j] == 0:
                        self.grid[0][j] = self.grid[i][j]
                        self.grid[i][j] = 0
                    elif self.grid[1][j] == 0:
                        self.grid[1][j] = self.grid[i][j]
                        self.grid[i][j] = 0
                    elif self.grid[2][j] == 0:
                        self.grid[2][j] = self.grid[i][j]
                        self.grid[i][j] = 0

    def merge():
            for i in range(3):
                for j in range(4):
                    if self.grid[i + 1][j] == self.grid[i][j]:
                        self.grid[i][j] *= 2
                        self.grid[i + 1][j] = 0

    def move_up():
        self.push_up()
        self.merge()
        self.push_up()

    def get_current_state():
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 2048:
                    return "Won"

                elif self.grid[i][j] == 0:
                    return "Not done jet"

        for i in range(3):
            for j in range(3):
                if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]:
                    return "Not done jet"

        for i in range(3):
            if grid[i][3] == grid[i + 1][3]:
                return "Not done jet"

            elif grid[3][i] == grid[3][i + 1]:
                return "Not done jet"

        return "Game Over"
