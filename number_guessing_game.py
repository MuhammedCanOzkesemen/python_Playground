import random

def choose_difficulty():
    print("Choose difficulty:")
    print("1 - Easy   (1-50)")
    print("2 - Medium (1-100)")
    print("3 - Hard   (1-200)")

    choice = input("Your choice: ")

    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 8
    elif choice == "3":
        return 200, 6
    else:
        print("Invalid choice. Medium selected.")
        return 100, 8


def play_game():
    max_number, attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)
    score = 100

    print(f"\nI picked a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts.\n")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            print("\nCorrect! You won!")
            print(f"Final score: {score}")
            return

        attempts -= 1
        score -= 10

        if guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        print(f"Attempts left: {attempts}\n")

    print("Game over!")
    print(f"The correct number was: {secret_number}")


def main():
    print("NUMBER GUESSING GAME")
    print("--------------------")

    while True:
        play_game()

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()