'''
This program addresses the game Pentominos
by solving it as a constraint satisfaction problem

Authors: Rebecca Comas, Zoe Moore, Brian Walker
'''

''' P I E C E S '''
'''
F: X X    L: X X  I: X  T: X X X  Y: X    U: X X  P:   X X
     X X       X     X       X       X         X     X X X
     X         X     X       X       X X     X X
               X     X               X
                     X

W: X         X:   X   Z: X X   V: X       N: X
   X X          X X X      X      X          X X
     X X          X        X X    X X X        X
                                               X
'''

''' F U N C T I O N S '''

'''
This function generates an empty pentominos board of size
5 x 5 or of size 5 x 7
row: the number of rows in the board
column: the number of columns in the board
return: the list representing the empty board
'''
def initial_board(row = 5, column = 5):
    if(row == 5 and column == 5):
        board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        '''
        X X X X X
        X X X X X
        X X X X X
        X X X X X
        X X X X X
        '''
    if(row == 5 and column == 7):
        '''
        X X X X X X X
        X X X X X X X
        X X X X X X X
        X X X X X X X
        X X X X X X X
        '''
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    return board

'''
This function prints the given board in a readable output format
board: the input board to be printed
'''
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print('\n')
    print('\n')

'''
This function places the piece F in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_f(board, starting_index):
    '''
    X X
      X X
      X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 3):
        return False
    if(column > len(board[0]) - 3):
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

'''
This function places the piece L in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_l(board, starting_index):
    '''
    X X
      X
      X
      X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 4):
        return False
    if(column > len(board[0]) - 2):
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

'''
This function places the piece I in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_i(board, starting_index):
    '''
    X
    X
    X
    X
    X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 5):
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

'''
This function places the piece T in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_t(board, starting_index):
    '''
    T T T
      T
      T
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 3):
        return False
    if(column > len(board[0]) - 3 or column < 1):
        return False

    # Copy board to prevent accidental overwriting
    b_copy = [ele[:] for ele in board]

    # Place piece, checking to make sure another piece isn't in the way
    if(b_copy[row][column] == 0):
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row][column + 1] == 0):
        column += 1
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row + 1][column - 1] == 0):
        column -= 1
        row += 1
        b_copy[row][column] = 'T'
    else:
        return False
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'T'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

'''
This function places the piece Y in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_y(board, starting_index):
    '''
    X
    X
    X X
    X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 4):
        return False
    if(column > len(board[0]) - 2):
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

'''
This function places the piece U in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_u(board, starting_index):
    '''
    X X
      X
    X X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 3):
        return False
    if(column > len(board[0]) - 2):
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

'''
This function places the piece P in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_p(board, starting_index):
    '''
      X X
    X X X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 2):
        return False
    if(column < 1 or column > len(board[0]) - 2):
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

'''
This function places the piece W in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_w(board, starting_index):
    '''
    X
    X X
      X X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 3):
        return False
    if(column > len(board[0]) - 3):
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

'''
This function places the piece X in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_x(board, starting_index):
    '''
      X
    X X X
      X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row < 1 or row > len(board) - 2):
        return False
    if(column > len(board[0]) - 3):
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

'''
This function places the piece Z in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_z(board, starting_index):
    '''
    X X
      X
      X X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 3):
        return False
    if(column > len(board[0]) - 3):
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

'''
This function places the piece V in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_v(board, starting_index):
    '''
    X
    X
    X X X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 3):
        return False
    if(column > len(board[0]) - 3):
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

'''
This function places the piece N in the specified position on the board,
checking to make sure the piece is only placed if it can properly fit on the board
board: the board to place the piece on
starting_index: the starting location on the board for placing the piece
return: True if the piece was successfully placed on the board, False otherwise
'''
def place_n(board, starting_index):
    '''
    X
    X X
      X
      X
    '''
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > len(board) - 4):
        return False
    if(column > len(board[0]) - 2):
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
    if(b_copy[row + 1][column] == 0):
        row += 1
        b_copy[row][column] = 'N'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

'''
This function makes a deep copy of the Pentominos board to prevent
overwriting any spaces
original: the board that is receiving the copy
new: the new board that needs to be copy into the old board
returns: the board copy
'''
def board_copy(original, new):
    for i in range(len(original)):
        for j in range(len(original[0])):
            original[i][j] = new[i][j]
    return original

'''
This function creates a deep copy of a given Pentominos board and
appends it to a list of subproblems in the backtrace function to
prevent any accidental overwriting of boards
subproblems: the list of subproblems to be expanded in backtrace
board: the Pentominos board that needs to be added
'''
def append_board(subproblems, board):
    new_board = initial_board()

    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[i][j] = board[i][j]

    subproblems.append(new_board)

'''
This function tests a given board to see if every space has a piece; this
is used as the test condition to see if a solution is found
board: the board that is being checked
returns: True if the board is full, False otherwise
'''
def board_full(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return False
    return True

'''
This function tests a given board to see if it can be considered a failed board
by the backtrace function and thus discarded; checks to see if any more pieces can fit
on the board
board: the board that is being tested
returns: True if the board cannot fit any more pieces, False if the board can fit more pieces
'''
def test_failure(board):

    test_board = initial_board()
    test_board = board_copy(test_board, board)

    for i in range(len(test_board)):
        for j in range(len(test_board)):
            board = board_copy(test_board, board)
            if(test_board[i][j] == 0):
                if(place_f(test_board, [i,j]) or place_u(test_board, [i,j]) or place_i(test_board, [i,j]) or place_p(test_board, [i,j]) or place_y(test_board, [i,j]) or place_t(test_board, [i,j]) or place_z(test_board, [i,j]) or place_x(test_board, [i,j]) or place_w(test_board, [i,j]) or place_v(test_board, [i,j]) or place_l(test_board, [i,j]) or place_n(test_board, [i,j])):
                    return False
    return True

'''
This function determines which pieces have not yet been placed on the given
board to expand the board into subproblems in the backtrace function
board: the board to be analyzed
returns: a list of the pieces that have not yet been placed on the given board
'''
def which_piece(board):
    pieces = ['I', 'F', 'U', 'Y', 'P', 'T', 'Z', 'X', 'W', 'V', 'L', 'N']

    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 'I'):
                pieces[0] = 0
            elif(board[i][j] == 'F'):
                pieces[1] = 0
            elif(board[i][j] == 'U'):
                pieces[2] = 0
            elif(board[i][j] == 'Y'):
                pieces[3] = 0
            elif(board[i][j] == 'P'):
                pieces[4] = 0
            elif(board[i][j] == 'T'):
                pieces[5] = 0
            elif(board[i][j] == 'Z'):
                pieces[6] = 0
            elif(board[i][j] == 'X'):
                pieces[7] = 0
            elif(board[i][j] == 'W'):
                pieces[8] = 0
            elif(board[i][j] == 'V'):
                pieces[9] = 0
            elif(board[i][j] == 'L'):
                pieces[10] = 0
            elif(board[i][j] == 'N'):
                pieces[11] = 0
    options = []
    count = 0
    for i in range(len(pieces)):
        if(pieces[i] != 0):
            options.append(pieces[i])

    return options     # if it ends up returning an empty list there will be a problem

'''
This function performs a backtrace on an input Pentominos board to find a solution
in which every space on the board is filled by a piece
original_board: the empty Pentominos board that needs to be filled
returns: the solution board if it exists, False otherwise
'''
def backtrace(original_board):
    stack = []
    stack.append(original_board)
    piece = 0

    while(len(stack) != 0):
        # pop a problem off the stack
        current_board = stack.pop()

        board = initial_board()
        board = board_copy(board, current_board)

        # expand the problem into subproblems
        subproblems = []

        pieces = which_piece(board)
        for k in range(len(pieces)):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board = board_copy(board, current_board)
                    if(pieces[k] == 'I'):
                        if(place_i(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'F'):
                        if(place_f(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'U'):
                        if(place_u(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'Y'):
                        if(place_y(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'P'):
                        if(place_p(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'T'):
                        if(place_t(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'Z'):
                        if(place_z(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'X'):
                        if(place_x(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'W'):
                        if(place_w(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'V'):
                        if(place_v(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'L'):
                        if(place_l(board, [i,j])):
                            append_board(subproblems, board)
                    if(pieces[k] == 'N'):
                        if(place_n(board, [i,j])):
                            append_board(subproblems, board)

        # for each subproblem
        for i in range(len(subproblems)):
            if(board_full(subproblems[i])):
                # if this is a success, halt
                return subproblems[i]
            elif(test_failure(subproblems[i])):
                temp = "wasted space"
                # if this is a failure, discard subproblem
            else:
                stack.append(subproblems[i])
                # otherwise, add it onto the stack

    return False

'''
This is the main code that runs the Pentominos solver:
1 - Create an initial board by calling initial_board()
    No parameters are needed since they unfortunately need to be hard-coded in the function
2 - Call the function backtrace() on the initial board to find a solution
3 - If a solution is found (with the current configuration, it should be), it will be printed

NOTE: finding a solution to a 5 x 7 board takes ~15-20 minutes
'''

board = initial_board()
result = backtrace(board)

if(result):
    print("Solution Board:")
    print_board(result)
else:
    print("No Solution")