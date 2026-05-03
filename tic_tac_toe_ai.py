import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_full():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Choose position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Spot taken.")
        except:
            print("Invalid input.")

def ai_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"

def game():
    print("TIC TAC TOE\nYou = X | AI = O")

    while True:
        print_board()
        player_move()

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        if is_full():
            print_board()
            print("Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

if __name__ == "__main__":
    game()