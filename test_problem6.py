import unittest

from problem6 import Maze


class TestProblem6(unittest.TestCase):

    def test_find_path(self, ):
        print('test_find_path :: assertion test')
        input_1 = [
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 2],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(Maze(0, 0, maze=input_1).find_path(), {'found': True, 'destination': (3, 7)})
        self.assertEqual(Maze(5, 2, maze=input_1).find_path(), {'found': True, 'destination': (3, 7)})

        input_2 = [
            [0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1],
            [2, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(Maze(0, 0, maze=input_2).find_path(), {'found': True, 'destination': (4, 0)})

        print('test_find_path :: assertion test:: x, y point in a wall')
        self.assertEqual(Maze(1, 1, maze=input_2).find_path(), {'found': False, 'destination': None})

        # destination matched with start_x and start_y
        input_4 = [[2]]
        self.assertEqual(Maze(0, 0, maze=input_4).find_path(), {'found': True, 'destination': (0, 0)})

        print('test_find_path :: assertion test:: non reachable destination')
        input_5 = [
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1, 2],
            [0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(Maze(0, 0, maze=input_5).find_path(), {'found': False, 'destination': None})
        self.assertEqual(Maze(0, 7, maze=input_5).find_path(), {'found': False, 'destination': None})

        print('test_find_path :: assertion test:: no destination')
        input_6 = [
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(Maze(0, 0, maze=input_6).find_path(), {'found': False, 'destination': None})
        self.assertEqual(Maze(6, 7, maze=input_6).find_path(), {'found': False, 'destination': None})

        with self.assertRaises(IndexError):
            self.assertEqual(Maze(10, 10, maze=input_1).find_path(), {'found': True, 'destination': (3, 7)})

    def test_traverse(self):
        print('test_traverse :: assertion test')
        input_1 = [
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 2],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        input_4 = [[2]]

        self.assertTrue(Maze(6, 0, maze=input_1).traverse(0, 0))
        self.assertTrue(Maze(0, 0, maze=input_4).traverse(0, 0))
        self.assertTrue(Maze(0, 0, maze=input_1).traverse(0, 0))


if __name__ == '__main__':
    unittest.main()
