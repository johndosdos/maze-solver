from graphics import *
from cell import *


def main():
    win = Window(800, 600)
    cell1 = Cell(Point(10, 10), Point(100, 100))
    cell2 = Cell(Point(100, 10), Point(190, 100))
    win.draw_cell(cell1, "white")
    win.draw_cell(cell2, "white")
    win.wait_for_close()


main()
