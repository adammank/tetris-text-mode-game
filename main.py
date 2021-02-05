import constants
from game import TetrisGame


if __name__ == '__main__':

    print(
        '\nMoves: ',
        '\n\ta = move piece left + down,'
        '\n\tb = move piece right + down,',
        '\n\tw = rotate piece counter clockwise + down',
        '\n\ts = rotate piece clockwise + down'
    )

    game = TetrisGame(width=20, heigth=20)
    game.new_piece()
    game.place_piece()
    game.draw_area()

    while game.state == 'play!':

        print('Select your move!')
        move = input()
        while move not in constants.POSSIBLE_MOVES:
            print('Incorrect move, try to select again!')
            move = input()

        if game.avaliable_moves():

            if move == 'a':
                game.move_piece(side='left')
            elif move == 'd':
                game.move_piece(side='right')
            elif move == 'w':
                game.move_piece(side='counter_clockwise')
            elif move == 's':
                game.move_piece(side='clockwise')

        else:
            game.block_piece()

        # Remove last piece from the area
        game.clear_area()

        # Place piece with its new position
        game.place_piece()

        # Print game board in the nice format
        game.draw_area()

        if game.state == 'gameover':
            print(
                '\n\tGame has finished!'
                '\n(lack of avaliable moves to perform / piece has tried to spawn at the position of the past one)'
                '\nHave a nice day!'
            )
