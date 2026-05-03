import random

WIDTH = 10
HEIGHT = 10

player = [0, 0]
goal = [WIDTH - 1, HEIGHT - 1]

walls = []

for _ in range(20):
    w = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
    if w != player and w != goal:
        walls.append(w)


def print_maze():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] == player:
                print("P", end="")
            elif [x, y] == goal:
                print("G", end="")
            elif [x, y] in walls:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def move(direction):
    if direction == "w":
        player[1] -= 1
    elif direction == "s":
        player[1] += 1
    elif direction == "a":
        player[0] -= 1
    elif direction == "d":
        player[0] += 1


def valid_move():
    x, y = player
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return False
    if [x, y] in walls:
        return False
    return True


def game():
    print("MAZE ESCAPE GAME")
    print("Reach G to win (W A S D to move)\n")

    while True:
        print_maze()

        move_input = input("Move: ").lower()
        old_pos = player.copy()

        move(move_input)

        if not valid_move():
            player[0], player[1] = old_pos

        if player == goal:
            print("You escaped the maze!")
            break


if __name__ == "__main__":
    game()