import unittest

from maze import Maze
from graphics import Window


class Tests(unittest.TestCase):
    def test_cell_creation(self):
        num_rows = 5
        num_cols = 5
        cell_width = 50
        cell_height = 50
        maze_offset_x = 10
        maze_offset_y = 10
        win = Window(
            (cell_width * num_cols) + 2 * maze_offset_x,
            (cell_height * num_rows) + 2 * maze_offset_y,
        )
        maze = Maze(
            maze_offset_x,
            maze_offset_y,
            num_rows,
            num_cols,
            cell_width,
            cell_height,
            win,
        )
        maze.create_cells()
        maze.break_entrance_and_exit()
        self.assertEqual(maze.cells[0][0].has_top_wall, False)
        self.assertEqual(
            maze.cells[len(maze.cells) - 1][num_cols - 1].has_bottom_wall, False
        )
        maze.break_walls_r(0, 0)


if __name__ == "__main__":
    unittest.main()
