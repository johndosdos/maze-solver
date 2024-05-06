from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Simple maze solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()

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


def main():
    win = Window(800, 800)
    win.wait_for_close()


main()
