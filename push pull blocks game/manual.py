from board_utils import print_board, in_bounds, check_win
from mechanics import activate_device

def play_manual(board):
    while True:
        print_board(board)

        if check_win(board):
            print("You win!")
            return

        inp = input("Enter row,column of device: ")
        if inp == "q":
            return

        try:
            r, c = map(int, inp.split(","))
        except:
            print("Invalid format.")
            continue

        if not in_bounds(r, c, len(board), len(board[0])):
            print("Out of board.")
            continue

        ok, msg = activate_device(board, r, c)
        print(msg)
