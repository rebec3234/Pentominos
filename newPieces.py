import copy
'''
This program addresses the game Pentominos
by solving it as a constraint satisfaction problem

Authors: Rebecca Comas, Zoe Moore, Brian Walker
'''

''' P I E C E S '''
'''
F: X X    L: X X  I: X  T:   X    Y: X    U: X X  P:   X X
     X X       X     X       X       X         X     X X X
     X         X     X     X X X     X X     X X
               X     X               X
                     X

W: X X      X:   X   Z: X X   V: X       N: X
     X X       X X X      X      X          X
       X X       X        X X    X X X      X X
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

def board_copy(original, new):
    for i in range(len(original)):
        for j in range(len(original[0])):
            original[i][j] = new[i][j]
    return original

def append_board(subproblems, board):
    new_board = initial_board()

    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[i][j] = board[i][j]

    subproblems.append(new_board)

def board_full(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return False
    return True

def test_failure(board):

    test_board = initial_board()
    test_board = board_copy(test_board, board)

    for i in range(len(test_board)):
        for j in range(len(test_board)):
            board = board_copy(test_board, board)
            if(test_board[i][j] == 0):
                if(place_f(test_board, [i,j]) or place_u(test_board, [i,j]) or place_i(test_board, [i,j]) or place_p(test_board, [i,j]) or place_y(test_board, [i,j]) or place_t(test_board, [i,j]) or place_z(test_board, [i,j]) or place_x(test_board, [i,j]) or place_w(test_board, [i,j]) or place_v(test_board, [i,j]) or place_l(test_board, [i,j]), place_n(test_board, [i,j])):
                    return False
    return True

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
    flag = -1
    count = 0
    while(flag == -1 and count < 5):
        if(pieces[count] != 0):
            flag = count
        count += 1

    return flag     # if it ends up returning -1 there will be a problem



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
        for i in range(len(board)):
            for j in range(len(board[0])):
                board = board_copy(board, current_board)
                count = which_piece(board)
                if(count == 0):
                    if(place_i(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 1):
                    if(place_f(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 2):
                    if(place_u(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 3):
                    if(place_y(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 4):
                    if(place_p(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 5):
                    if(place_t(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 6):
                    if(place_z(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 7):
                    if(place_x(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 8):
                    if(place_w(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 9):
                    if(place_v(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 10):
                    if(place_l(board, [i,j])):
                        append_board(subproblems, board)
                if(count == 11):
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

        # print("Iteration" + str(count))
        # for i in range(len(subproblems)):
        #     print_board(subproblems[i])

        # print("Stack" + str(count))
        # for i in range(len(stack)):
        #     print_board(stack[i])

    return False



board = initial_board()
result = backtrace(board)

print_board(result)

# place_f(board, [0,0])
# place_y(board, [1,0])
# place_i(board, [0,4])
# place_l(board, [0,2])
# print_board(board)

# place_f(board, [1,0])
# place_i(board, [0,4])
# place_l(board, [0,2])
# print_board(board)

# if(test_failure(board)):
#     print("WORKS")

# if(board_full(board)):
#     print("DONE")
