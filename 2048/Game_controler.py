from Game_model import *
from View import *


class Game_controller():
    def __init__(self):
        self.model = Game_model()

        self.window = View()

        self.main_loop()

    #defining the main loop which is run everytime the player trys to make a move
    def main_loop(self):
        self.window.show_grid(self.model.grid)
        new_grid = self.model.grid
        self.model.changed = False
        x = input("which direction you want to go in:").lower()
        if x == "w":
            self.model.move_up()
        elif x == "s":
            self.model.move_down()
        elif x == "a":
            self.model.move_left()
        elif x == "d":
            self.model.move_right()
        else:
            pass
        if self.model.is_full() != True and self.model.changed == True:
            self.model.add_tile()

        if self.model.get_current_state() == "Not done jet":
            self.main_loop()
        elif self.model.get_current_state() == "Won":
            print("You have won")
        elif self.model.get_current_state() == "Game Over":
            print("Game Over")


if __name__ == "__main__":
    game = Game_controller()
