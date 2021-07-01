import unittest
import Game as game
class test_game(unittest.TestCase):
    def setUp():
        game = Game()
        game.show_grid()

    def test_move_up():
        pass

if __name__ == "__main__":
    test_game.unittest()
