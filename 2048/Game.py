import tkinter as tk
import View as view
import Random as rnd
class Game(object):


    def __init__(self):
        self.grid = [[None]*4 for i in range(4)]
        add_tile_2()
        add_tile_2()
        view.draw()



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

    def swipe_left():

        new_grid = [[0]*4 for i in range(4)]


        for i in range(4):
            pos = 0
            for j in range(4):
                if grid [i][j] != 0:
                    new_grid[i][pos] = self.grid[i][j]
                    pos += 1

        self.grid = new_grid

    def merge(self):


        for i in range(4):
            for j in range(3):


                if(self.grid[i][j] == self.grid[i][j + 1] and self.grid[i][j] != 0):

                    self.grid[i][j] = self.grid[i][j] * 2
                    self.grid[i][j + 1] = 0


    def invert():
        new_grid = []
        for i in range(4):
            new_grid.append([])
            for j in range(4):
            new_grid[i].append(self.grid[i][3 - j])

        self.grid = new_grid

    def transpose():
        new_grid = []
        for i in range(4):
            new_grid.append([])
            for j in range(4):
                new_grid[i].append(self.grid[i][j])

        self.grid = new_grid

    def move_left():
        self.swipe_left()
        self.merge()
        self.swipe_left()

    def move_right():
        self.invert()
        self.move_left()
        self.invert()

    def move_up():
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down():
        self.transpose()
        self.move_right()
        self.transpose()

    def get_current_state():
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 2048:
                    return "Won"

                elif self.grid[i][j] = 0:
                    return "Not done jet"

        for i in range(3):
            for j in range(3):
                if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]:
                    retrun "Not done jet"

        for i in range(3):
            if grid[i][3] == grid[i + 1][3]:
                return "Not done jet"

            elif grid[3][i] == grid[3][i + 1]:
                return "Not done jet"

        return "Game Over"
