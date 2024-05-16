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
        self.cells = []

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
                self.animate()

    def animate(self):
        self.win.redraw()
        self.win.root.after(50)

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
