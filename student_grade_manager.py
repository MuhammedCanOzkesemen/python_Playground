import json
import os

FILE_NAME = "students.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_student(data):
    name = input("Student name: ").strip()

    if name in data:
        print("Student already exists.")
        return

    data[name] = []
    save_data(data)
    print("Student added successfully.")


def add_grade(data):
    name = input("Student name: ").strip()

    if name not in data:
        print("Student not found.")
        return

    try:
        grade = float(input("Grade: "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return

        data[name].append(grade)
        save_data(data)
        print("Grade added successfully.")

    except ValueError:
        print("Invalid grade.")


def show_students(data):
    if not data:
        print("No students found.")
        return

    for name, grades in data.items():
        if grades:
            average = sum(grades) / len(grades)
            print(f"{name} | Grades: {grades} | Average: {average:.2f}")
        else:
            print(f"{name} | No grades yet")


def search_student(data):
    name = input("Student name: ").strip()

    if name not in data:
        print("Student not found.")
        return

    grades = data[name]

    if grades:
        average = sum(grades) / len(grades)
        print(f"Name: {name}")
        print(f"Grades: {grades}")
        print(f"Average: {average:.2f}")
        print(f"Highest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")
    else:
        print(f"{name} has no grades yet.")


def delete_student(data):
    name = input("Student name: ").strip()

    if name not in data:
        print("Student not found.")
        return

    del data[name]
    save_data(data)
    print("Student deleted successfully.")


def class_statistics(data):
    all_grades = []

    for grades in data.values():
        all_grades.extend(grades)

    if not all_grades:
        print("No grades available.")
        return

    average = sum(all_grades) / len(all_grades)

    print(f"Class average: {average:.2f}")
    print(f"Highest grade: {max(all_grades)}")
    print(f"Lowest grade: {min(all_grades)}")
    print(f"Total grades: {len(all_grades)}")


def menu():
    data = load_data()

    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add student")
        print("2. Add grade")
        print("3. Show all students")
        print("4. Search student")
        print("5. Delete student")
        print("6. Class statistics")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            add_grade(data)
        elif choice == "3":
            show_students(data)
        elif choice == "4":
            search_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            class_statistics(data)
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


menu()