import pygame
import random


class Window:
    def __init__(self, num_rows, num_cols, cell_height, cell_width):
        self.height, self.width = (
            (cell_height * num_rows),
            (cell_width * num_cols),
        )
        self.window = pygame.display.set_mode((self.width, self.height))
        self.maze_surface = pygame.Surface((self.height, self.width))


class Cell:
    def __init__(self, i, j, cell_height, cell_width):
        self.i = i
        self.j = j
        self.height = cell_height
        self.width = cell_width

        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

        self.visited = False

        self.neighbors = []


class Maze:
    def __init__(self, num_rows, num_cols, cell_height, cell_width, window):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.win = window

        self._cells = []
        self._create_grid_array()
        self._walk()

    def generate(self):
        self._draw_cells()

    def _walk(self):
        pass

    def _draw_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                cell = self._cells[i][j]

                x = j * cell.width
                y = i * cell.height

                if cell.has_top_wall:
                    pygame.draw.line(
                        self.win.maze_surface,
                        (0, 0, 0),
                        (x, y),
                        (x + cell.width, y),
                        1,
                    )
                if cell.has_right_wall:
                    pygame.draw.line(
                        self.win.maze_surface,
                        (0, 0, 0),
                        (x + cell.width, y),
                        (x + cell.width, y + cell.height),
                        1,
                    )
                if cell.has_bottom_wall:
                    pygame.draw.line(
                        self.win.maze_surface,
                        (0, 0, 0),
                        (x + cell.width, y + cell.height),
                        (x, y + cell.height),
                        1,
                    )
                if cell.has_left_wall:
                    pygame.draw.line(
                        self.win.maze_surface,
                        (0, 0, 0),
                        (x, y + cell.height),
                        (x, y),
                        1,
                    )

                if cell.visited:
                    pygame.draw.rect(
                        self.win.maze_surface,
                        (128, 128, 128),
                        pygame.Rect(x, y, cell.width, cell.height),
                    )

    def _create_grid_array(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                cell = Cell(i, j, self.cell_height, self.cell_width)
                self._set_neighbors(cell)
                # if j > 0:
                #     cell.has_left_wall = row[j - 1].has_right_wall
                # if i > 0:
                #     cell.has_top_wall = self._cells[i - 1][j].has_bottom_wall
                row.append(cell)
            self._cells.append(row)

    def _set_neighbors(self, cell):
        if cell.i > 0:
            cell.neighbors.append((cell.i - 1, cell.j))
        if cell.i < self.num_rows - 1:
            cell.neighbors.append((cell.i + 1, cell.j))
        if cell.j > 0:
            cell.neighbors.append((cell.i, cell.j - 1))
        if cell.j < self.num_cols - 1:
            cell.neighbors.append((cell.i, cell.j + 1))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    cell_height, cell_width = 50, 50
    num_rows, num_cols = 5, 5
    win = Window(num_rows, num_cols, cell_height, cell_width)
    maze = Maze(num_rows, num_cols, cell_height, cell_width, win)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # clear screen
        win.window.fill((255, 255, 255))
        win.maze_surface.fill((255, 255, 255))

        # render
        maze.generate()

        # display to the canvas
        win.window.blit(
            win.maze_surface,
            (
                ((win.height - win.maze_surface.get_height()) // 2),
                ((win.width - win.maze_surface.get_width()) // 2),
            ),
        )

        pygame.display.update()
        clock.tick(30)

    pygame.quit()


main()
