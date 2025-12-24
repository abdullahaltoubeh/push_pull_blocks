from solver import dfs, bfs_solve, ucs_solve
from manual import play_manual
from levels import get_levels
from board_utils import copy_board
def main():
    levels = get_levels()

    print("\n=== Choose Level ===")
    for lvl in levels:
        print(f"{lvl}) Level {lvl}")

    try:
        level_choice = int(input("Choose level: "))
        board = copy_board(levels[level_choice])
    except:
        print("Invalid level.")
        return

    print("\n=== Choose Solve Method ===")
    print("1) Manual play")
    print("2) Auto solve DFS")
    print("3) Auto solve BFS")
    print("4) Auto solve UCS")

    choice = input("Choose 1 or 2 or 3 or 4: ")

    if choice == "1":
        play_manual(board)

    elif choice == "2":
        dfs(board, 0, 20, set(), [])

    elif choice == "3":
        bfs_solve(board)

    elif choice == "4":
        ucs_solve(board)

    else:
        print("Invalid choice.")
if __name__ == "__main__":
    main()

