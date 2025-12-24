from collections import deque
from board_utils import print_board, copy_board, check_win, DIRS
from mechanics import activate_device
import heapq


def dfs(board, depth, max_depth, visited, path):
    state = tuple(tuple(row) for row in board)
    if state in visited:
        return False
    visited.add(state)

    path.append(copy_board(board))

    if check_win(board):
        print("\n🎉 Solved with DFS! Steps:\n")
        for i, step_board in enumerate(path):
            print(f"Step {i}")
            print_board(step_board)
        return True

    if depth >= max_depth:
        path.pop()
        return False

    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in DIRS:
                new_board = copy_board(board)
                ok, _ = activate_device(new_board, r, c)
                if ok:
                    if dfs(new_board, depth + 1, max_depth, visited, path):
                        return True

    path.pop()
    return False

def bfs_solve(start_board):
    queue = deque([start_board])
    visited = {tuple(tuple(row) for row in start_board)}
    step = 0

    while queue:
        board = queue.popleft()
        print(f"\n===== BFS Step {step} =====")
        print_board(board)
        step += 1

        if check_win(board):
            print("Solved with BFS!")
            return

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in DIRS:
                    new_board = copy_board(board)
                    ok, _ = activate_device(new_board, r, c)
                    if ok:
                        state = tuple(tuple(row) for row in new_board)
                        if state not in visited:
                            visited.add(state)
                            queue.append(new_board)

    print("No solution found with BFS.")

def ucs_solve(start_board):
    pq = []  # priority queue
    heapq.heappush(pq, (0, start_board, []))
    # (cost, board, path)

    visited = {}

    step = 0

    while pq:
        cost, board, path = heapq.heappop(pq)

        state = tuple(tuple(row) for row in board)
        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost

        print(f"\n===== UCS Step {step} | Cost = {cost} =====")
        print_board(board)
        step += 1

        new_path = path + [copy_board(board)]

        if check_win(board):
            print("\n🎉 Solved with UCS!")
            print(f"Total Cost = {cost}\n")
            for i, b in enumerate(new_path):
                print(f"Step {i}")
                print_board(b)
            return

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in DIRS:
                    new_board = copy_board(board)
                    ok, _ = activate_device(new_board, r, c)
                    if ok:
                        new_cost = cost + 1  # كلفة الحركة
                        heapq.heappush(
                            pq,
                            (new_cost, new_board, new_path)
                        )

    print("❌ No solution found with UCS.")
