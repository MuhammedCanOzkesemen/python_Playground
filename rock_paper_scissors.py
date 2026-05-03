import random

player_score = 0
computer_score = 0

for round in range(5):
    input("Press Enter to roll dice...")

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print(f"You: {player} | Computer: {computer}")

    if player > computer:
        player_score += 1
        print("You win this round")
    elif computer > player:
        computer_score += 1
        print("Computer wins this round")
    else:
        print("Draw")

print("\nFinal Score")
print(f"You: {player_score} - Computer: {computer_score}")