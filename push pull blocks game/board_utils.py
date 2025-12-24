DIRS = {
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '>': [(0, 1)],

    # جهاز PUSH باتجاهين (أعلى + يمين)
    '└': [(-1, 0), (0, 1)],

    # أجهزة PULL
    'P^': [(1, 0)],
    'Pv': [(-1, 0)]
}

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def copy_board(board):
    return [row[:] for row in board]

def check_win(board):
    for row in board:
        for cell in row:
            if cell == 'T':
                return False
    return True
