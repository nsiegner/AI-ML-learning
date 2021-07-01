import tkinter as tk
import Game as game
class View():

    def __init__(self, grid):
        window = tk.Tk()
        show_grid()
        self.grid = grid


    def show_grid():
        for i in range(4):
            for j in range(4):
                frame = tk.Frame(master=window,relief=tk.RAISED, borderwidth=1)
                frame.grid(row=i,column=j)
                tile = tk.Label(master=frame, text=self.grid[i][j].get_value())
                tile.pack()



if __name__ == __main__():
    window = tk.Tk()
