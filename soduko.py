# THIS IS A SODUKO SOLVER ALGORITHM
# THE MAIN IDEA IS TO BACKTRACK

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

def print_board(board):

    for row in range(len(board)):
        if row % 3 and row != 0:
            print("- - - - - - - - - - - - - ")

        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print(" | ", end="")

            if column == 0:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ")


def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)
            

def hello(das):
    print(das)


print_board(board)