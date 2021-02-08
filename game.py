import random
import piece


class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = []
        self.piece = None
        self.state = 'play!'


class TetrisArea(Tetris):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.create_area()

    def create_area(self):
        """Create a game board - list of lists,
        where each inner list represents a row."""

        for y in range(self.height-1):
            row = []
            for x in range(self.width):

                # left & right edge
                if x == 0 or x == self.width-1:
                    row.append('*')

                # center
                else:
                    row.append(' ')

            self.area.append(row)

        # bottom edge
        self.area.append(list(self.width * '*'))

    def clear_area(self):
        """Remove '*' value from each field
        in order to enable free reposition of the piece."""

        for y in range(self.height - 1):
            for x in range(1, self.width - 1):
                if self.area[y][x] == 'X':
                    continue
                self.area[y][x] = ' '

    def draw_area(self):
        """Print a game board."""
        print()
        for line in self.area:
            #print(line)                # <- raw, grid version
            print(''.join(line))        # <- eye firendly


class TetrisPiece(TetrisArea):

    def new_piece(self):
        """Crate a new piece."""
        self.piece = piece.Piece(x=random.randint(1, 16), y=0)

    def place_piece(self):
        """Fulfill area (apropriate fields based on the piece
        coordinates) with '*' sign to represent the actual piece."""

        for y in range(4):
            for x in range(4):
                xy_coor = y * 4 + x
                if xy_coor in self.piece.piece_coor():
                    if self.area[y + self.piece.y][x + self.piece.x] == 'X':
                        self.state = 'gameover'
                        break
                    self.area[y + self.piece.y][x + self.piece.x] = '*'


class TetrisUtils(TetrisPiece):

    def junction(self) -> bool:
        """Check if a junction has occurred."""

        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.piece.piece_coor():

                    # bottom
                    if y + self.piece.y > self.height - 2:
                        return True

                    # right side
                    if x + self.piece.x > self.width - 2:
                        return True

                    # left side
                    if x + self.piece.x < 1:
                        return True

                    # past pieces
                    if self.area[y + self.piece.y][x + self.piece.x] == 'X':
                        return True
        return False

    def block_piece(self):
        """Fulfill area fields that represent the actual piece
        with the 'X' sign to mark those fields as blocked.
        Spawn another piece."""

        for y in range(4):
            for x in range(4):
                if y * 4 + x in self.piece.piece_coor():
                    self.area[y + self.piece.y][x + self.piece.x] = 'X'
        self.new_piece()
        if self.junction():
            self.state = 'gameover'


class TetrisMoves(TetrisUtils):

    def move_piece(self, side):
        """Move piece down + left / right / rotate depending on the choosen move.
        Block piece if underneath there is no blank field."""

        old_x = self.piece.x
        old_y = self.piece.y
        old_rotation = self.piece.rotation

        # move or rotate piece depending on side
        if side == 'left':
            self.piece.x -= 1
        elif side == 'right':
            self.piece.x += 1
        elif side == 'clockwise':
            self.piece.rotate_clockwise()
        elif side == 'counter_clockwise':
            self.piece.rotate_counter_clockwise()

        # move down
        self.piece.y += 1

        # if junction, get back to the previous position
        if self.junction():
            self.piece.y = old_y
            if side == 'left' or side == 'right':
                self.piece.x = old_x
            elif side == 'clockwise' or side == 'counter_clockwise':
                self.piece.rotation = old_rotation
            print('\nThis move is not valid! Enter a valid one.')

        # block if the next down move would make a junction
        self.piece.y += 1
        if self.junction():
            self.piece.y -= 1
            self.block_piece()
        else:
            self.piece.y -= 1

    def avaliable_moves(self) -> bool:
        """Flow through all moves & check if any
        of them is avaliable to perform."""

        old_x = self.piece.x
        old_y = self.piece.y
        old_rotation = self.piece.rotation

        left = self._check_move(
            'left', old_x, old_y, old_rotation)
        right = self._check_move(
            'right', old_x, old_y, old_rotation)
        rotate_clock = self._check_move(
            'clockwise', old_x, old_y, old_rotation)
        rotate_counter_clock = self._check_move(
            'counter_clockwise', old_x, old_y, old_rotation)

        return any([left, right, rotate_clock, rotate_counter_clock])

    def _check_move(self, side, old_x, old_y, old_rotation) -> bool:
        """Check if a given move is avaliable to perform."""

        if side == 'left':
            self.piece.x -= 1
        elif side == 'right':
            self.piece.x += 1
        elif side == 'clockwise':
            self.piece.rotate_clockwise()
        elif side == 'counter_clockwise':
            self.piece.rotate_counter_clockwise()

        self.piece.y += 1

        if not self.junction():
            self.piece.x, self.piece.y, self.piece.rotation = \
                old_x, old_y, old_rotation
            return True

        self.piece.x, self.piece.y, self.piece.rotation = \
            old_x, old_y, old_rotation
        return False


class TetrisGame(TetrisMoves):
    pass