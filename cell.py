from graphics import *


class Cell:
    def __init__(self, p1, p2, win):
        self.p1 = p1
        self.p2 = p2
        self.window = win
        self.center = Point((self.p1.x + self.p2.x) // 2, (self.p1.y + self.p2.y) // 2)
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, canvas, fill_color):
        if self.has_top_wall:
            canvas.create_line(
                self.p1.x, self.p1.y, self.p2.x, self.p1.y, fill=fill_color, width=2
            )
        if self.has_right_wall:
            canvas.create_line(
                self.p2.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
            )
        if self.has_bottom_wall:
            canvas.create_line(
                self.p2.x, self.p2.y, self.p1.x, self.p2.y, fill=fill_color, width=2
            )
        if self.has_left_wall:
            canvas.create_line(
                self.p1.x, self.p2.y, self.p1.x, self.p1.y, fill=fill_color, width=2
            )

    def draw_move(self, to_cell, undo=False):
        line = Line(
            Point(self.center.x, self.center.y),
            Point(to_cell.center.x, to_cell.center.y),
        )
        fill_color = "red"
        if undo:
            fill_color = "gray"
        line.draw(self.window.canvas, fill_color)
