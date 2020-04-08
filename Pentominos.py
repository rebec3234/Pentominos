import copy
'''
This program addresses the game Pentominos
by solving it as a constraint satisfaction problem

Authors: Rebecca Comas, Zoe Moore, Brian Walker
'''

''' P I E C E S '''
'''
F: X X    L: X X  I: X  T:   X    Y: X
     X X       X     X       X       X
     X         X     X     X X X     X X
               X     X               X
                     X
'''

''' F U N C T I O N S '''

def initial_board():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    return board

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

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 2):
        return False
    if(column > 2):
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

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 1):
        return False
    if(column > 3):
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

def place_t(board, starting_index):
    # Starting position of piece
    row = starting_index[0]
    column = starting_index[1]

    # Check that piece doesn't extend past boundaries of 5 x 5 board
    if(row > 2):
        return False
    if(column > 3 or column < 1):
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
    if(b_copy[row - 1][column + 1] == 0):
        row -= 1
        column += 1
        b_copy[row][column] = 'Y'
    else:
        return False

    # If there are no piece conflicts, replace original board with updated board
    board = board_copy(board, b_copy)
    return True

def increment_index(starting_index):
    if starting_index[1] + 1 < 5:
        starting_index[1] = starting_index[1] + 1
        return True
    elif starting_index[0] + 1 < 5:
        starting_index[0] = starting_index[0] + 1
        return True
    return False

def board_copy(original, new):
    for i in range(len(original)):
        for j in range(len(original[0])):
            original[i][j] = new[i][j]
    return original

def place_piece(board,row,column):
     #Attempts to place pieces at a starting index until successful
     #NOT TESTED
     if (place_f(board, [row, column])):
          place_f(board, [row, column])
          return True
     elif (place_l(board, [row, column])):
          place_l(board, [row, column])
          return True
     elif (place_i(board, [row, column])):
          place_i(board, [row, column])
          return True
     elif (place_t(board, [row, column])):
          place_t(board, [row, column])
          return True
     elif (place_y(board, [row, column])):
          place_y(board, [row, column])
          return True
     return False

def is_empty(board, index):
     # Checks is a spot on the board is empty.
     # NOT TESTED
     if (board[index[0]][index[1]] == 0):
          return True
     return False

## A main program that places pieces on the board until it runs out of starting spots.
## Things that need to be added: 
## -A function to test if the board is full
## -A function to backtrack if no piece can be placed and the board is not full
# NOT TESTED
board = initial_board()
starting_index = [0,0]
while (starting_index[0] <= len(board)):
     while (starting_index[1] <= len(board[0])):
          if(is_empty(board, starting_index) and place_piece(board,starting_index[0],starting_index[1])):
             place_piece(board,starting_index[0],starting_index[1])
          increment_index(starting_index[1])    
print_board(board)

