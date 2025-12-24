from solver import dfs, bfs_solve
from manual import play_manual

def main():
    board = [
        ['>', '0', '0', '0', 'T'],
        ['0', '0', 'o', '0', '0'],
        ['0', '0', '^', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]

    print("1) Manual play")
    print("2) Auto solve DFS")
    print("3) Auto solve BFS")

    choice = input("Choose 1 or 2 or 3: ")

    if choice == "1":
        play_manual(board)
    elif choice == "2":
        dfs(board, 0, 12, set(),[])
    elif choice == "3":
        bfs_solve(board)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
