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


def remove_piece(board, piece):

    for i in range(0,5):
        for j in range(0,5):
            if board[i][j] == piece:
                board[i][j] = 0
    return True


def board_copy(original, new):
    for i in range(len(original)):
        for j in range(len(original[0])):
            original[i][j] = new[i][j]
    return original


def place_piece(board,index,placed_pieces, skip):
     #Attempts to place pieces at a starting index until successful
     #NOT TESTED

    row = index[0]
    column = index[1]
    board_copy = [ele[:] for ele in board]

    if (place_f(board_copy, [row, column]) and not "f" in placed_pieces and skip != "f"):
        place_f(board, [row, column])
        placed_pieces.append("f")
        print_board(board)
        return True
    elif (place_l(board_copy, [row, column]) and not "l" in placed_pieces and skip != "l"):
        place_l(board, [row, column])
        placed_pieces.append("l")
        print_board(board)
        return True
    elif (place_i(board_copy, [row, column]) and not "i" in placed_pieces and skip != "i"):
        place_i(board, [row, column])
        placed_pieces.append("i")
        print_board(board)
        return True
    elif (place_y(board_copy, [row, column]) and not "y" in placed_pieces and skip != "y"):
        place_y(board, [row, column])
        placed_pieces.append("y")
        print_board(board)
        return True
    elif (place_t(board_copy, [row, column]) and not "t" in placed_pieces and skip != "t"):
        place_t(board, [row, column])
        placed_pieces.append("t")
        print_board(board)
        return True
    return False

def board_full(board):
    full = True
    for i in range(0,5):
        for j in range(0,5):
            if board[i][j] == 0:
                full = False
    return full

def is_empty(board, index):
     # Checks is a spot on the board is empty.
     # NOT TESTED
     if (board[index[0]][index[1]] == 0):
        return True
     return False

def increment_index(starting_index):
    if starting_index[1] + 1 < 5:
        starting_index[1] = starting_index[1] + 1
        return True
    elif starting_index[0] + 1 < 5:
        starting_index[0] = starting_index[0] + 1
        return True
    elif starting_index[0] == 4 and starting_index[1] ==4:
        starting_index[1] = 0
        starting_index[0] = 0
    return False

def decrement_index(starting_index):
    if starting_index[0] - 1 < 0:
        starting_index[0] = starting_index[0] - 1
        return True
    elif starting_index[1] - 1 < 0:
        starting_index[1] = starting_index[1] - 1
        return True
    elif starting_index[0] == 0 and starting_index[1] == 0:
        starting_index[1] = 4
        starting_index[0] = 4
    return False


def solve_puzzle (board, index, placed_pieces, skip):
    """
    Our First Attempt

    if board_full(board):
        return True
    else:
        if is_empty(board,index):
            place_piece(board, index, placed_pieces,skip)
            increment_index(index)
            if (solve_puzzle(board, index, placed_pieces, skip)):
                return True
            else:
                piece = placed_pieces[len(placed_pieces)-1]
                remove_piece(board, piece)
                placed_pieces.remove(piece)
                skip = piece
                decrement_index(index)
                solve_puzzle(board,index,placed_pieces,skip)
        else:
            increment_index(index)
            solve_puzzle(board, index, placed_pieces, skip)
    return False
    """

    """
    Attempt Two

    for i in range(0,5):
        for j in range(0,5):
            if is_empty(board,index):
                place_piece(board, [i,j], placed_pieces, skip)
                if (solve_puzzle(board, [i,j], placed_pieces, skip)):
                    return True
                else:
                    piece = placed_pieces[len(placed_pieces)-1]
                    remove_piece(board, piece)
                    placed_pieces.remove(piece)
                    skip = piece
    """


"""

n queens backtracking example
bool solveNQUtil(int board[N][N], int col)
{
    /* base case: If all queens are placed
      then return true */
    if (col >= N)
        return true;

    /* Consider this column and try placing
       this queen in all rows one by one */
    for (int i = 0; i < N; i++) {
        /* Check if the queen can be placed on
          board[i][col] */
        if (isSafe(board, i, col)) {
            /* Place this queen in board[i][col] */
            board[i][col] = 1;

            /* recur to place rest of the queens */
            if (solveNQUtil(board, col + 1))
                return true;

            /* If placing queen in board[i][col]
               doesn't lead to a solution, then
               remove queen from board[i][col] */
            board[i][col] = 0; // BACKTRACK
        }
    }

    /* If the queen cannot be placed in any row in
        this colum col  then return false */
    return false;
}
"""



"""
To test the solve_puzzle function
placed_pieces = []
board = initial_board()
print_board(board)
solve_puzzle(board, [0,0], placed_pieces, "A")
"""


board = initial_board()
print_board(board)
place_f(board, [0,0])
place_y(board, [1,0])
place_i(board, [0,4])
place_l(board, [0,2])
place_t(board, [2,2])
print_board(board)
