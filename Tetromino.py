class Tetromino:
    def __init__(self, blocks, tetrominos):
        self.blocks = blocks
        self.vel_x = 0
        self.last_y = self.last_x = 0
        self.delay, self.delay_const = 1, 1
        self.active = True
        self.drop_point = True
        self.__setup_barriers(tetrominos)

    def __setup_barriers(self, tetrominos):
        """
            This method sets up the barriers set for use in the
            update_pos method.
        """
        self.barriers = set()
        for tetro in tetrominos:
            for block in tetro.blocks:
                self.barriers.add((block.pos_x, block.pos_y))
        for x in range(-50, 275, 25):
            self.barriers.add((x, 500))
        for y in range(-50, 525, 25):
            self.barriers.add((-25, y))
            self.barriers.add((250, y))

    def update_pos(self, time, tetrominos):
        """
            This method makes the tetromino go down the screen
            at a rate of one block per 1000 // self.delay
            in milliseconds. The method will also move the tetromino
            left and right by one block if the player wishes to.
        """
        if time - self.last_y >= 1000 // self.delay:
            if all([(b.pos_x, b.pos_y + 25) not in self.barriers \
                                                    for b in self.blocks]):
                for block in self.blocks:
                    block.pos_y += 25
            else:
                self.active = False
            self.last_y = time

        if time - self.last_x >= 50:
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

    def drop(self):
        """
            Thid method makes the tetromino fall to the closest barrier.
        """
        while all([(b.pos_x, b.pos_y + 25) not in self.barriers for b in self.blocks]):
            for block in self.blocks:
                block.pos_y += 25
        self.active = False

    def shift(self):
        """
            This method changes the tetromino's orientation.
        """
        def rotate_block(block, direction):
            """
                This inner method rotates the position of any block
                clockwise or counterclockwise by 90 degrees with respect
                to the pivot.
            """
            rot_matrix = ((0, 1 * direction), (-1 * direction, 0))
            pos = (block.pos_x - pivot.pos_x, block.pos_y - pivot.pos_y)
            new_x = rot_matrix[0][0] * pos[0] + rot_matrix[0][1] * pos[1]
            new_y = rot_matrix[1][0] * pos[0] + rot_matrix[1][1] * pos[1]
            block.pos_x = new_x + pivot.pos_x
            block.pos_y = new_y + pivot.pos_y
        pivot = self.blocks[1]
        for block in self.blocks:
            rotate_block(block, 1)
        if any([(b.pos_x, b.pos_y) in self.barriers for b in self.blocks]):
            for block in self.blocks:
                rotate_block(block, -1)

    def fall(self, num_lines, lines):
        """
            This method will allow make the tetromino fall by the
            amount of rows that were just completed.
        """
        for b in self.blocks:
            if b.active:
                num_lines = 0
                for y in lines:
                    if b.pos_y < y:
                        num_lines += 1
                b.pos_y += 25 * num_lines

class Block:
    def __init__(self, surface, position):
        self.surface = surface
        self.active = True
        self.pos_x = position[0]
        self.pos_y = position[1]

    def remove_block(self):
        """
            This method makes the block disappear from the screen
            and sets self.active to False.
        """
        self.active = False
        self.pos_x = -500
        self.pos_y = -500

class L(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

class J(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

class S(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

class Z(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

class I(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

class T(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

class O(Tetromino):
    def __init__(self, blocks, tetrominos):
        super().__init__(blocks, tetrominos)

    def shift(self):
        """
            This method overrides the shift method in the
            parent class because squares cannot be shifted.
        """
        return
