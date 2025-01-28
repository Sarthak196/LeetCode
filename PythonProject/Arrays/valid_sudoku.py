def isValidSudoku(board):
    check_row = isValidRow(board)
    check_col = isValidCol(board)
    if check_row and check_col:
        check_subgrid = isValidGrid(board)
        if check_subgrid:
            return True
    return False


def isValidRow(board):
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[i][j] != ".":
                row.append(board[i][j])
        if len(row) != len(set(row)):
            return False
    return True


def isValidCol(board):
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            if board[j][i] != ".":
                col.append(board[j][i])
        if len(col) != len(set(col)):
            return False
    return True


def isValidGrid(board):
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            box = []
            for k in range(3):
                for l in range(3):
                    if board[i + k][j + l] != '.':
                        box.append(board[i + k][j + l])
            if len(box) != len(set(box)):
                return False
    return True

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board)) # True