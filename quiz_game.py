questions = {
    "What is 2+2? ": "4",
    "Capital of France? ": "paris",
    "Python is a (language/animal)? ": "language"
}

score = 0

for q, a in questions.items():
    answer = input(q).lower()
    if answer == a:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print(f"Final score: {score}/{len(questions)}")