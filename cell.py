class Cell:
    def __init__(self, p1, p2, window):
        self.p1 = p1
        self.p2 = p2
        self.window = window
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
