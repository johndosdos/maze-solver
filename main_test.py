import unittest

import unittest.test
from maze import Maze


class Tests(unittest.TestCase):
    def test_cell_creation(self):
        num_rows = 5
        num_cols = 5
        maze = Maze(0, 0, num_rows, num_cols, 50, 50)
        maze.create_cells()
        self.assertEqual(len(maze.cells), num_rows)
        self.assertEqual(len(maze.cells[0]), num_cols)


if __name__ == "__main__":
    unittest.main()
