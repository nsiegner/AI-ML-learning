import unittest
from Game import *
class test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game()


    def test_move_up(self):
        example1 = [[2, 0, 0, 2],
                    [2, 2, 2, 0],
                    [2, 0, 0, 2],
                    [2, 2, 4, 4]]

        soultion1 = [[4, 4, 2, 4],
                     [4, 0, 4, 4],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

        self.game.set_grid(example1)
        print("move up")
        self.game.show_grid()
        self.game.move_up()
        self.game.show_grid()
        self.assertEqual(soultion1, self.game.get_grid())

    def test_move_down(self):
        example1 = [[2, 2, 4, 4],
                    [2, 0, 0, 2],
                    [2, 2, 2, 0],
                    [2, 0, 0, 2]]

        soultion1 = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [4, 0, 4, 4],
                     [4, 4, 2, 4]]

        self.game.set_grid(example1)
        print("move down")
        self.game.show_grid()
        self.game.move_down()
        self.game.show_grid()
        self.assertEqual(soultion1, self.game.get_grid())

    def test_move_left(self):
        example1 = [[2, 2, 2, 2],
                    [2, 0, 2, 0],
                    [4, 0, 2, 0],
                    [4, 2, 0, 2]]

        soultion1 = [[4, 4, 0, 0],
                     [4, 0, 0, 0],
                     [4, 2, 0, 0],
                     [4, 4, 0, 0]]
        self.game.set_grid(example1)
        print("move left")
        self.game.show_grid()
        self.game.move_left()
        self.game.show_grid()
        self.assertEqual(soultion1, self.game.get_grid())

    def test_move_right(self):
        example1 = [[2, 2, 2, 2],
                    [2, 0, 2, 0],
                    [4, 0, 2, 0],
                    [4, 2, 0, 2]]

        soultion1 = [[0, 0, 4, 4],
                     [0, 0, 0, 4],
                     [0, 0, 4, 2],
                     [0, 0, 4, 4]]

        self.game.set_grid(example1)
        print("move right")
        self.game.show_grid()
        self.game.move_right()
        self.game.show_grid()
        self.assertEqual(soultion1, self.game.get_grid())

    def test_invert(self):
        example1 = [[2, 0, 2, 4],
                    [2, 0, 0, 0],
                    [8, 4, 0, 8],
                    [8, 4, 0, 2]]

        soultion1 = [[8, 4, 0, 2],
                     [8, 4, 0, 8],
                     [2, 0, 0, 0],
                     [2, 0, 2, 4]]
        self.game.set_grid(example1)
        print("invert")
        self.game.show_grid()
        self.game.invert()
        self.game.show_grid()
        self.assertEqual(soultion1, self.game.get_grid())

    def test_rotate_right(self):
        example1 = [[2, 0, 2, 4],
                    [2, 0, 0, 0],
                    [8, 4, 0, 8],
                    [8, 4, 0, 2]]

        soultion1 = [[8, 8, 2, 2],
                     [4, 4, 0, 0],
                     [0, 0, 0, 2],
                     [2, 8, 0, 4]]
        self.game.set_grid(example1)
        self.game.rotate_right()
        self.assertEqual(soultion1, self.game.get_grid())

    def test_rotate_left(self):
        example1 = [[2, 0, 2, 4],
                    [2, 0, 0, 0],
                    [8, 4, 0, 8],
                    [8, 4, 0, 2]]

        soultion1 = [[4, 0, 8, 2],
                     [2, 0, 0, 0],
                     [0, 0, 4, 4],
                     [2, 2, 8, 8]]
        self.game.set_grid(example1)
        self.game.rotate_left()
        self.assertEqual(soultion1, self.game.get_grid())

if __name__ == "__main__":
    unittest.main()
