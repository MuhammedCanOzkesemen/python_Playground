import random

words = ["python", "developer", "machine", "algorithm", "system"]
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ")

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

else:
    print("You lost! Word was:", word)