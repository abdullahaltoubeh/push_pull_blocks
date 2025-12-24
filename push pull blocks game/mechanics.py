from board_utils import in_bounds, DIRS

def push_chain(board, chain, dr, dc):
    rows, cols = len(board), len(board[0])

    last_r, last_c = chain[-1]
    target_r = last_r + dr
    target_c = last_c + dc

    if not in_bounds(target_r, target_c, rows, cols):
        return False

    if board[target_r][target_c] not in ['0', 'T']:
        return False

    for r, c in reversed(chain):
        board[r + dr][c + dc] = board[r][c]

    first_r, first_c = chain[0]
    board[first_r][first_c] = '0'

    return True

def activate_device(board, r, c):
    device = board[r][c]
    if device not in DIRS:
        return False, "Cell does not contain a device."

    dr, dc = DIRS[device]
    rows, cols = len(board), len(board[0])

    cur_r = r + dr
    cur_c = c + dc

    while in_bounds(cur_r, cur_c, rows, cols) and board[cur_r][cur_c] not in ['O', 'o']:
        if board[cur_r][cur_c] not in ['0', 'T', '<', '>', '^', 'v']:
            return False, "No block in that direction."
        cur_r += dr
        cur_c += dc

    if not in_bounds(cur_r, cur_c, rows, cols):
        return False, "No block found."

    chain = []
    while in_bounds(cur_r, cur_c, rows, cols) and board[cur_r][cur_c] in ['O', 'o']:
        chain.append((cur_r, cur_c))
        cur_r += dr
        cur_c += dc

    if not push_chain(board, chain, dr, dc):
        return False, "Cannot push."

    return True, "Push successful."
