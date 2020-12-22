
class Tetromino:
    def __init__(self, x, y):
        self.pos_x, self.pos_y = 75, 0
        self.vel_x, self.vel_y = 1, 1

    def update_pos(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

class Line(Tetromino):
    def __init__(self, surface):
        Tetromino.__init__(self, 75, 0)
        self.surface = surface

    def shift(self):
        pass
