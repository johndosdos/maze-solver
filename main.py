from graphics import *
from cell import *
from maze import *


def main():
    win = Window(800, 600)

    x = 10
    y = 10
    num_rows = 5
    num_cols = 5
    cell_size_x = 50  # pixel
    cell_size_y = 50  # pixel
    maze = Maze(x, y, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.create_cells()

    win.wait_for_close()


main()
