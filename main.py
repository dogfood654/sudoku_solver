#            1  2  3  4  5  6  7  8  9
board = [   [0, 7, 0, 0, 0, 0, 0, 0, 9],      # 1
            [5, 1, 0, 4, 2, 0, 6, 0, 0],      # 2
            [0, 8, 0, 3, 0, 0, 7, 0, 0],      # 3
            [0, 0, 8, 0, 0, 1, 3, 7, 0],      # 4
            [0, 2, 3, 0, 8, 0, 0, 4, 0],      # 5
            [4, 0, 0, 9, 0, 0, 1, 0, 0],      # 6
            [9, 6, 2, 8, 0, 0, 0, 3, 0],      # 7
            [0, 0, 0, 0, 1, 0, 4, 0, 0],      # 8
            [7, 0, 0, 2, 0, 3, 0, 9, 6]   ]   # 9

def display_board():
    global board
    for i in range(9):
        print(board[i])

def check_correct():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                print("There is no possible solution!")
                return False
    print("Correct!")
    return True

def possible(y, x, n):
    global board
    # check horizontal
    for i in range(9):
        if board[y][i] == n:
            return False
    # check vertical
    for i in range(9):
        if board[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    # check box
    for i in range(2):
        for j in range(2):
            if board[y0+i][x0+j] == n:
                return False
    return True

def solver():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y][x] = n
                        solver()
                        board[y][x] = 0
                return
    display_board()
    check_correct()

solver()
