import tkinter as tk
import random as rnd
import numpy as np
class Game(object):


    def __init__(self):
        self.grid = [[0]*4 for i in range(4)]
        self.add_tile_2()
        self.add_tile_2()

        self.main_loop()

    def main_loop(self):
        self.show_grid()
        new_grid = self.grid

        x = input("which direction you want to go in:").lower()
        if x == "w":
            self.move_up()
        elif x == "s":
            self.move_down()
        elif x == "a":
            self.move_left()
        elif x == "d":
            self.move_right()
        else:
            pass

        if self.is_full() != True and new_grid != self.grid:
            self.add_tile()

        if self.get_current_state() == "Not done jet":
            self.main_loop()
        elif self.get_current_state() == "Won":
            print("You have won")
        elif self.get_current_state() == "Game Over":
            print("Game Over")



    def set_grid(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid

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
                    if self.grid[i + 1][j] == self.grid[i][j] and self.grid[i][j] != None:
                        self.grid[i][j] = self.grid[i][j]*2
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
                if self.grid[i][j] == 0:
                    return False

        return True


    def show_grid(self):
        print("\n")
        for i in range(4):
            print(self.grid[i][0], self.grid[i][1], self.grid[i][2], self.grid[i][3])
        print("\n")

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

if __name__ == "__main__":
    game = Game()
