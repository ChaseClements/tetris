class Tetromino:
    def __init__(self, blocks, x, y):
        self.blocks = blocks
        self.pos_x, self.pos_y = x, y
        self.vel_x = 0
        self.last_y = self.last_x = 0
        self.delay, self.delay_const = 1, 1
        self.active = True

    def update_pos(self, time, tetrominos):
        """
            This function makes the tetromino go down the screen
            at a rate of one block per 1000 // self.delay
            in milliseconds. The function will also move the tetromino
            left and right by one block if the player wishes to.
        """
        if time - self.last_y >= 1000 // self.delay:
            locations = [475]
            for tetro in tetrominos:
                right_corner = tetro.pos_x + tetro.x_size
                if tetro.pos_x <= self.pos_x < right_corner \
                   or tetro.pos_x < self.pos_x + self.x_size <= right_corner:
                    locations.append(tetro.pos_y - tetro.y_size)
            if self.pos_y < min(locations):
                for block in self.blocks:
                    block.pos_y += 25
                self.pos_y += 25
            else:
                self.active = False
            self.last_y = time
        
        if time - self.last_x >= 50:
            if self.vel_x < 0:
                locations = []
                for tetro in tetrominos:
                    if tetro.pos_y == self.pos_y:
                        locations.append(tetro.pos_x)
                        locations.append(tetro.pos_x + tetro.x_size)
                if self.pos_x > 0 and \
                        (self.pos_x + self.x_size <= min(locations + [150]) or \
                        self.pos_x > max(locations + [1])):
                    for block in self.blocks:
                        block.pos_x += self.vel_x
                    self.pos_x += self.vel_x
            elif self.vel_x > 0:
                locations = []
                for tetro in tetrominos:
                    if tetro.pos_y == self.pos_y:
                        locations.append(tetro.pos_x)
                        locations.append(tetro.pos_x + tetro.x_size)
                if self.pos_x + self.x_size < 250 and \
                        (self.pos_x + self.x_size < min(locations + [150]) or \
                        self.pos_x >= max(locations + [1])):
                    for block in self.blocks:
                        block.pos_x += self.vel_x
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

    def start_down(self):
        """
            This function makes the tetromino fall faster while
            the player is pressing the down arrow key.
        """
        self.delay_const = self.delay
        self.delay = 20

    def stop_down(self):
        """
            This function returns the tetromino's down speed
            to what it was before the user pressed the down
            arrow key.
        """
        self.delay = self.delay_const

class Block:
    def __init__(self, surface, position):
        self.surface = surface
        self.pos_x = position[0]
        self.pos_y = position[1]

class Line(Tetromino):
    def __init__(self, blocks):
        super().__init__(blocks, 75, 0)
        self.x_size = 100
        self.y_size = 25

    def shift(self):
        """
            This function changes the line's orientation from
            horizontal to vertical or vice versa.
        """
        pass
