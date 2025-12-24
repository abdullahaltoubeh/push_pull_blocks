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



def pull_chain(board, chain, dr, dc):
    rows, cols = len(board), len(board[0])

    first_r, first_c = chain[0]
    target_r = first_r - dr
    target_c = first_c - dc

    if not in_bounds(target_r, target_c, rows, cols):
        return False

    if board[target_r][target_c] not in ['0', 'T']:
        return False

    for r, c in chain:
        board[r - dr][c - dc] = board[r][c]

    last_r, last_c = chain[-1]
    board[last_r][last_c] = '0'

    return True



# ---------------------------------------------
# Activate device
# ---------------------------------------------
def activate_device(board, r, c):
    device = board[r][c]
    if device not in DIRS:
        return False, "Cell does not contain a device."

    rows, cols = len(board), len(board[0])

    movable = {'O', 'o', '^', 'v', '<', '>', '└', 'P^', 'Pv'}

    moved = False

    # 🔑 دعم اتجاه واحد أو عدة اتجاهات
    for dr, dc in DIRS[device]:

        cur_r = r + dr
        cur_c = c + dc

        # تخطي الفراغات والأهداف
        while in_bounds(cur_r, cur_c, rows, cols) and board[cur_r][cur_c] in ['0', 'T']:
            cur_r += dr
            cur_c += dc

        if not in_bounds(cur_r, cur_c, rows, cols):
            continue

        if board[cur_r][cur_c] not in movable:
            continue

        # جمع السلسلة
        chain = []
        while in_bounds(cur_r, cur_c, rows, cols) and board[cur_r][cur_c] in movable:
            chain.append((cur_r, cur_c))
            cur_r += dr
            cur_c += dc

        if not chain:
            continue

        if device in ['P^', 'Pv']:
            if pull_chain(board, chain, dr, dc):
                moved = True
        else:
            if push_chain(board, chain, dr, dc):
                moved = True

    if moved:
        if device in ['P^', 'Pv']:
            return True, "Pull successful."
        return True, "Push successful."

    if device in ['P^', 'Pv']:
        return False, "Cannot pull."
    return False, "Cannot push."
