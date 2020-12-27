class Tetromino:
    def __init__(self, blocks, tetrominos):
        self.blocks = blocks
        self.vel_x = 0
        self.last_y = self.last_x = 0
        self.delay, self.delay_const = 1, 1
        self.active = True
        self.barriers = set()
        self.__setup_barriers(tetrominos)

    def __setup_barriers(self, tetrominos):
        """
            This method sets up the barriers set for use in the
            update_pos method.
        """
        self.barriers.add((-25, self.blocks[0].pos_y))
        self.barriers.add((250, self.blocks[0].pos_y))
        for tetro in tetrominos:
            for block in tetro.blocks:
                self.barriers.add((block.pos_x, block.pos_y))

    def update_pos(self, time, tetrominos):
        """
            This method makes the tetromino go down the screen
            at a rate of one block per 1000 // self.delay
            in milliseconds. The method will also move the tetromino
            left and right by one block if the player wishes to.
        """
        if time - self.last_y >= 1000 // self.delay:
            self.barriers.add((self.blocks[0].pos_x, 500))
            if all([(b.pos_x, b.pos_y + 25) not in self.barriers \
                                                    for b in self.blocks]):
                for block in self.blocks:
                    block.pos_y += 25
            else:
                self.active = False
            self.last_y = time

        if time - self.last_x >= 50:
            self.barriers.add((-25, self.blocks[0].pos_y))
            self.barriers.add((250, self.blocks[0].pos_y))
            if all([(b.pos_x + self.vel_x, b.pos_y) not in self.barriers \
                                                    for b in self.blocks]):
                for block in self.blocks:
                    block.pos_x += self.vel_x
            self.last_x = time

    def start_horizontal(self, direction):
        """
            This method changes the x velocity of the tetromino
            based on if the user pressed the left or right arrow
            key.
        """
        self.vel_x = direction * 25

    def stop_horizontal(self):
        """
            This method stops the tetrominos x movement by
            lowering it's x velocity to 0.
        """
        self.vel_x = 0

    def start_down(self):
        """
            This method makes the tetromino fall faster while
            the player is pressing the down arrow key.
        """
        self.delay_const = self.delay
        self.delay = 20

    def stop_down(self):
        """
            This method returns the tetromino's down speed
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
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)
        self.horizontal = True
        self.shift_num = 2

    def shift(self):
        """
            This method changes the line's orientation from
            horizontal to vertical or vice versa.
        """
        if self.horizontal:
            for i in range(len(self.blocks)):
                self.blocks[i].pos_x = self.blocks[self.shift_num].pos_x
                self.blocks[i].pos_y += 25 * (i - self.shift_num)
            self.horizontal = False
        else:
            for i in range(len(self.blocks)):
                self.blocks[i].pos_x += 25 * (i - self.shift_num)
                self.blocks[i].pos_y = self.blocks[self.shift_num].pos_y
            if self.shift_num == 1:
                self.shift_num = 2
            else:
                self.shift_num = 1
            self.horizontal = True
