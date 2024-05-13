from cell import *
from graphics import Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

    def create_cells(self):
        self.cells = []
        for i in range(self.num_rows):
            rows = []
            for j in range(self.num_cols):
                cols = []
                p1 = Point(
                    self.x1 + (j * self.cell_size_x), self.y1 + (i * self.cell_size_y)
                )
                p2 = Point(
                    self.x1 + ((j + 1) * self.cell_size_x),
                    self.y1 + (i + 1) * self.cell_size_y,
                )
                cell = Cell(p1, p2, self.win)
                cols.append(cell)
                rows.append(cols)
            self.cells.append(rows)

    def draw_cell(self, i, j):
        pass

    def animate(self):
        pass
