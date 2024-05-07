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
