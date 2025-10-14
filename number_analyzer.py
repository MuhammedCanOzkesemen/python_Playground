def number_analyzer():
    numbers = []
    print("Welcome to the Number Analyzer!")
    print("Type 'stop' to finish.\n")

    while True:
        user_input = input("Enter a number: ").lower()
        if user_input == "stop":
            break
        numbers.append(int(user_input))

    if len(numbers) == 0:
        print("No numbers were entered.")
        return

    even = []
    odd = []

    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    print("\n--- Results ---")
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Even numbers:", even)
    print("Odd numbers:", odd)


number_analyzer()
