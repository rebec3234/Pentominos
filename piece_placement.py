def initial_board():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    return board

def board_copy(original, new):
    for i in range(len(original)):
        for j in range(len(original[0])):
            original[i][j] = new[i][j]
    return original

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print('\n')
    print('\n')

def place_f(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    board_rows = 5
    board_cols = 5
    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > board_rows - 3):
        return False
    if(column > board_cols - 3):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'F'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'F'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'F'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'F'
    else:
        return False
    if(b_copy[row - 1][column + 1] == 0):
        row -= 1
        column += 1
        b_copy[row][column] = 'F'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_l(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    board_rows = 5
    board_cols = 5
    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > board_rows - 4):
        return False
    if(column > board_cols - 2):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'L'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'L'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'L'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'L'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'L'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_t(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    board_rows = 5
    board_cols = 5
    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > board_rows - 3):
        return False
    if(column > board_cols - 2 or column < 1):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row][column - 1] == 0):
        column -= 1
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row][column + 2] == 0):
        column += 2
        b_copy[row][column] = 'T'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_y(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    board_rows = 5
    board_cols = 5
    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > board_rows - 4):
        return False
    if(column > board_cols - 2):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row - 1][column + 1] == 0):
        row -= 1
        column += 1
        b_copy[row][column] = 'Y'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

"""
Below haven't been updated based on board size
"""

def place_u(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 2):
        return False
    if(column > 3):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'U'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'U'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'U'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'U'
    else:
        return False
    if(b_copy[row][column - 1] == 0):
        column -= 1
        b_copy[row][column] = 'U'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_p(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 3):
        return False
    if(column < 1 or column > 3):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'P'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'P'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'P'
    else:
        return False
    if(b_copy[row][column - 1] == 0):
        column -= 1
        b_copy[row][column] = 'P'
    else:
        return False
    if(b_copy[row][column - 1] == 0):
        column -= 1
        b_copy[row][column] = 'P'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_w(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 2):
        return False
    if(column > 2):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'W'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'W'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'W'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'W'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'W'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_z(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 2):
        return False
    if(column > 2):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'Z'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'Z'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Z'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Z'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'Z'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_v(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 2):
        return False
    if(column > 2):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'V'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'V'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'V'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'V'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'V'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_n(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 1):
        return False
    if(column > 3):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'N'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'N'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'N'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'N'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'N'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_x(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row < 1 or row > 3):
        return False
    if(column > 2):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'X'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'X'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'X'
    else:
        return False
    if(b_copy[row - 1][column - 1] == 0):
        row -= 1
        column -= 1
        b_copy[row][column] = 'X'
    else:
        return False
    if(b_copy[row + 2][column] == 0):
        row += 2
        b_copy[row][column] = 'X'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_i(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 0):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'I'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_i_sideways(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(column > 0):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'I'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'I'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def place_y_up(board, starting_index):
    # Starting position of piece
    """
    X
    X X
    X
    X
    """
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 1):
        return False
    if(column > 3):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'Y'
    else:
        return False
    if(b_copy[row - 2][column + 1] == 0):
        row -= 2
        column += 1
        b_copy[row][column] = 'Y'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

board = initial_board()

place_i_sideways(board, [0,0])
print_board(board)
board = initial_board()
place_i_sideways(board, [1,0])
print_board(board)
board = initial_board()
place_i_sideways(board, [2,0])
print_board(board)
board = initial_board()
place_i_sideways(board, [3,0])
print_board(board)
board = initial_board()
place_i_sideways(board, [4,0])
print_board(board)
