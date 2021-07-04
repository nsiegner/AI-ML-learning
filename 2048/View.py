import tkinter as tk

class View():
    def __init__(self):
        window = tk.Tk()
        self.frame = tk.Frame(master=window, width=200, height=200)
        self.frame.pack()

    def show_grid(self, grid):
        for i in range(4):
            for j in range(4):
                label = tk.Label(master=self.frame, text=grid[i][j])
                label.place(x=(50*j)+20, y=(50*i)+20)
