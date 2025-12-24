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



# ---------------------------------------------
# Activate device
# ---------------------------------------------
def activate_device(board, r, c):
    device = board[r][c]
    if device not in DIRS:
        return False, "Cell does not contain a device."

    rows, cols = len(board), len(board[0])

    moved = False

    # 🔑 دعم اتجاه واحد أو عدة اتجاهات
    for dr, dc in DIRS[device]:

        cur_r = r + dr
        cur_c = c + dc

        # تخطي الفراغات والأجهزة
        while in_bounds(cur_r, cur_c, rows, cols) and board[cur_r][cur_c] not in ['O', 'o']:
            if board[cur_r][cur_c] not in ['0', 'T', '<', '>', '^', 'v', '└']:
                break
            cur_r += dr
            cur_c += dc

        if not in_bounds(cur_r, cur_c, rows, cols):
            continue

        # جمع السلسلة
        chain = []
        while in_bounds(cur_r, cur_c, rows, cols) and board[cur_r][cur_c] in ['O', 'o']:
            chain.append((cur_r, cur_c))
            cur_r += dr
            cur_c += dc

        if not chain:
            continue

        if push_chain(board, chain, dr, dc):
            moved = True

    if moved:
        return True, "Push successful."

    return False, "Cannot push."
