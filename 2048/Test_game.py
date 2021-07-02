import unittest
from Game import *
class test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game()


    def test_move_up(self):
        example1 = [[2, 0, 0, 2], [2, 2, 2, 0], [2, 0, 0, 2], [2, 2, 4, 4]]
        soultion1 = [[4, 4, 2, 4], [4, 0, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.game.set_grid(example1)
        self.game.move_up()
        self.assertEqual(soultion1, game.grid)

if __name__ == "__main__":
    test_game.setUp()
    test_game.test_move_up()
