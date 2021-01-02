class Player:
    def __init__(self):
        self.score = 0
        self.lines = 0
        self.level = 0
        self.dis_score = None
        self.dis_lines = None
        self.dis_level = None

    def display_score(self):
        return 'Score: ' + str(self.score)

    def display_lines(self):
        return 'Lines: ' + str(self.lines)

    def display_level(self):
        return 'Level: ' + str(self.level)
