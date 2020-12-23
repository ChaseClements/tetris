
class Tetromino:
    def __init__(self, x, y):
        self.pos_x, self.pos_y = x, y
        self.vel_x = 0
        self.last_y = self.last_x = 0
        self.delay = 1

    def update_pos(self, time):
        """
            This function makes the tetromino go down the screen
            at a rate of one block per 1000 // self.delay in
            milliseconds. The function will also move the tetromino
            left and right by one block if the player wishes to.
        """
        if time - self.last_y >= 1000 // self.delay:
            if self.pos_y < 475:
                self.pos_y += 25
            self.last_y = time
        if time - self.last_x >= 10:
            if self.vel_x < 0 and self.pos_x > 1 \
                or self.vel_x > 0 and self.pos_x < 150:
                self.pos_x += self.vel_x
            self.last_x = time

    def start_horizontal(self, direction):
        """
            This function changes the x velocity of the tetromino
            based on if the user pressed the left or right arrow
            key.
        """
        self.vel_x = direction * 25

    def stop_horizontal(self):
        """
            This function stops the tetrominos x movement by
            lowering it's x velocity to 0.
        """
        self.vel_x = 0

class Line(Tetromino):
    def __init__(self, surface):
        Tetromino.__init__(self, 75, -25)
        self.surface = surface

    def shift(self):
        pass
