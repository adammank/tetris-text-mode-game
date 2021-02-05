POSSIBLE_MOVES = {'a', 'd', 'w', 's'}

PIECE_COORDINATES = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[1, 5, 9, 10], [4, 5, 6, 8], [0, 1, 5, 9], [2, 4, 5, 6]],
    [[1, 5, 8, 9], [0, 4, 5, 6], [1, 2, 5, 9], [4, 5, 6, 10]],
    [[1, 4, 5, 8], [0, 1, 5, 6]],
    [[1, 2, 5, 6]]
]

#   Each list contains coordinates of a certain piece
# within, the first list represents the basic piece.
# The next ones are the rotate versions.
#
#
# Based on the 4x4 map:
#
#   0,   1,   2,   3,
#   4,   5,   6,   7,
#   8,   9,   10,  11,
#   12,  13,  14,  15
#
# So f.g:   PIECE_COORDINATES[2][0]   would be:
#
#       1
#       5
#    8  9
#
# Which stands for piece:
#
#       *
#       *
#      **