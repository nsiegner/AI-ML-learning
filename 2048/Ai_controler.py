import numpy as np
import logging as log
from Game_model import *


class Ai_controler():
    def __init__(self):
        self.board = Game_model()
        log.basicConfig(filename="logfile.log", level=log.INFO)

    def ai_move(self):
        while Game_model.get_current_state == "Not done jet":
            log.info(self.board.get_grid())
            self.board.move_up()
            if self.board.changed != True:
                self.board.move_right()
                if self.board.changed != True:
                    self.board.move_down()
                    if self.board.changed != True:
                        self.board.move_left()

if __name__ == "__main__":
    ai = Ai_controler()
    ai.ai_move()
