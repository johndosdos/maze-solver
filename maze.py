from cell import *
from graphics import Point
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.seed = seed
        if self.seed is not None:
            self.seed = random.seed(seed)

    def create_cells(self):
        for i in range(self.num_rows):
            rows = []
            for j in range(self.num_cols):
                p1 = Point(
                    self.x1 + (j * self.cell_size_x), self.y1 + (i * self.cell_size_y)
                )
                p2 = Point(
                    self.x1 + ((j + 1) * self.cell_size_x),
                    self.y1 + (i + 1) * self.cell_size_y,
                )
                cell = Cell(p1, p2, self.win)
                rows.append(cell)
                self.draw_cell(cell)
            self.cells.append(rows)

    def draw_cell(self, cell, fill_color="white"):
        cell.draw(self.win.canvas, fill_color)
        self.animate(20)

    def animate(self, time):
        self.win.redraw()
        self.win.root.after(time)

    def break_entrance_and_exit(self):
        entry_cell = self.cells[0][0]
        exit_cell = self.cells[len(self.cells) - 1][self.num_cols - 1]

        entry_cell.has_top_wall = False
        self.delete_wall(entry_cell, "top")
        exit_cell.has_bottom_wall = False
        self.delete_wall(exit_cell, "bottom")

        self.win.redraw()

    def delete_wall(self, cell, wall_id):
        self.win.canvas.delete(cell.wall_ids[wall_id])
        del cell.wall_ids[wall_id]

    def break_walls_r(self, row, col):
        stack = [(row, col)]
        visited = set()

        while stack:
            cur_row, cur_col = stack.pop()
            visited.add((cur_row, cur_col))
            neighbors = []
            if cur_row > 0:
                neighbors.append((cur_row - 1, col, "top"))
            if cur_col < self.num_cols - 1:
                neighbors.append((cur_row, col + 1, "right"))
            if cur_row < self.num_rows - 1:
                neighbors.append((cur_row + 1, col, "bottom"))
            if cur_col > 0:
                neighbors.append((cur_row, col - 1, "left"))

            for new_row, new_col, wall_id in neighbors:
                if (new_row, new_col) not in visited:
                    self.delete_wall(self.cells[new_row][new_col], wall_id)
                    self.animate(100)
                    stack.append((new_row, new_col))
        # cur_cell = self.cells[row][col]

        # while (row >= 0 and row < len(self.cells)) or (
        #     col >= 0 and col < len(self.cells[row])
        # ):
        #     adjs = []

        #     if row > 0:
        #         adjs.append((row - 1, col, "top"))
        #     if col < self.num_cols:
        #         adjs.append((row, col + 1, "right"))
        #     if row < self.num_rows:
        #         adjs.append((row + 1, col, "bottom"))
        #     if col > 0:
        #         adjs.append((row, col - 1, "left"))

        #     rand_int = random.randrange(0, len(adjs))
        #     new_row = adjs[rand_int][0]
        #     new_col = adjs[rand_int][1]
        #     wall_id = adjs[rand_int][2]
        #     self.delete_wall(cur_cell, wall_id)
        #     self.animate(100)
        #     self.break_walls_r(new_row, new_col)
