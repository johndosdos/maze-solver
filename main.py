from graphics import *
from cell import *
from maze import *


def main():
    num_rows = 10
    num_cols = 10
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

    win.wait_for_close()


main()
