from graphics import *
from cell import *


def main():
    win = Window(800, 600)

    cell_1 = Cell(Point(10, 10), Point(100, 100), win)
    cell_2 = Cell(Point(100, 10), Point(190, 100), win)
    cell_3 = Cell(Point(190, 10), Point(280, 100), win)
    cell_4 = Cell(Point(190, 100), Point(280, 190), win)

    win.draw_cell(cell_1, "white")
    win.draw_cell(cell_2, "white")
    win.draw_cell(cell_3, "white")
    win.draw_cell(cell_4, "white")

    cell_1.draw_move(cell_3)
    cell_3.draw_move(cell_4)

    win.wait_for_close()


main()
