import random
import constants


class Piece:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece_type = random.choice(constants.PIECE_COORDINATES)
        self.rotation = 0

    def piece_coor(self):
        """Return list of a piece coordinates."""
        return self.piece_type[self.rotation]

    def rotate_clockwise(self):
        self.rotation = (self.rotation + 1) % len(self.piece_type)

    def rotate_counter_clockwise(self):
        self.rotation = (self.rotation + -1) % len(self.piece_type)