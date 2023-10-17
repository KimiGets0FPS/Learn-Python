from termcolor import cprint


default_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
row_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]


def fen_to_board(fen):
    board = fen.split("/")
    output = []
    for i in range(len(board)):
        column = ""
        for j in range(len(board[i])):
            if ord(board[i][j]) >= 65:
                column += board[i][j] + " "
            else:
                column += ' '.join(list('.' * int(board[i][j])))
        output.append(column)
    return output


def main():
    default_p2move = True  # True is white, False is black
    current_board = default_board
    while True:
        print(f"{'White' if default_p2move else 'Black'} to move")
        current_display = fen_to_board(current_board)
        cprint(f". {''.join(row_numbers)}", color="green")
        for i in range(len(current_display)):
            cprint(column_letters[i], color="green", end=" ")
            print(current_display[i])
        move = input("Your move: ")


if __name__ == "__main__":
    main()
