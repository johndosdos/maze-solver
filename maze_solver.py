from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Simple maze solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH)

        self.is_running = False

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell, fill_color):
        cell.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
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


def main():
    win = Window(800, 600)
    cell1 = Cell(Point(10, 10), Point(100, 100))
    cell2 = Cell(Point(100, 10), Point(190, 100))
    win.draw_cell(cell1, "white")
    win.draw_cell(cell2, "white")
    win.wait_for_close()


main()
