# playing with lists and random 

import random

print("=== Random Fun ===")

names = ["Can", "Ola", "Ali", "Ece", "Bartek", "Merve"]
print("All names:", names)

# pick random person
winner = random.choice(names)
print("Winner is ", winner)

# pick 3 random people (no repeat)
team = random.sample(names, 3)
print("Team:", team)

# random numbers
numbers = list(range(1, 11))
print("Numbers ", numbers)

random.shuffle(numbers)
print("Shuffled:", numbers)

# mini lottery
lottery = random.sample(range(1, 50), 6)
print("Lottery numbers:", sorted(lottery))

# small guessing part
guess = int(input("Guess a number 1-10: "))
secret = random.randint(1, 10)

if guess == secret:
    print("You got it")
else:
    print("Nope! Secret was", secret)
