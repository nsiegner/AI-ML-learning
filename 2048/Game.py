import tkinter as tk
import random as rnd
import numpy as np
class Game(object):


    def __init__(self):
        self.grid = [[None]*4 for i in range(4)]
        self.add_tile_2()
        self.add_tile_2()

        '''if input("do you want to play?").lower() == "yes":
            self.main_loop()
        else:
            pass

    def main_loop(self):
        grid_before = self.grid
        self.show_grid()
        x = input("Which direction you want to go?")
        if x.lower() == "w":
            self.move_up()
        elif x.lower() == "s":
            self.move_down()
        elif x.lower() == "a":
            self.move_left()
        elif x.lower() == "d":
            self.move_right()
        else:
            pass
        if grid_before != self.grid:
             if self.is_full != True:
                 self.add_tile()

        if self.get_current_state() == "Not done jet":
            self.main_loop()
        elif self.get_current_state() == "Won":
            pass
        elif self.get_current_state() == "Game Over":
            pass'''

    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid

    def add_tile(self):
        for i in range(10):
            if i == 0 or i == 1:
                self.add_tile_4()
            else:
                self.add_tile_2()

    def add_tile_2(self):
        x = rnd.randint(0, 3)
        y = rnd.randint(0, 3)
        if self.grid[x][y] == None:
            self.grid[x][y] = 2
        else:
            self.add_tile_2()

    def add_tile_4(self):
        x = rnd.randint(0, 3)
        y = rnd.randint(0, 3)
        if self.grid[x][y] == None:
            self.grid[x][y] = 4
        else:
            self.add_tile_4()

    def push_up(self):
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

    def merge(self):
            for i in range(3):
                for j in range(4):
                    if self.grid[i + 1][j] == self.grid[i][j]:
                        self.grid[i][j] *= 2
                        self.grid[i + 1][j] = 0

    def invert(self):
        self.grid.reverse()

    def rotate_right(self):
        a = np.rot90(self.grid, 3)
        self.grid = a.tolist()

    def rotate_left(self):
        a = np.rot90(self.grid)
        self.grid = a.tolist()

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

    def is_full(self):
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 0:
                    return False

        return True


    def show_grid(self):
        for i in range(4):
            print(self.grid[i][0], self.grid[i][1], self.grid[i][2], self.grid[i][3])
        print("\n")

    def get_current_state(self):
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
