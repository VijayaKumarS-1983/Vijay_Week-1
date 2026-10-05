# grade_manager.py

def calculate_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    elif 0 <= mark < 60:
        return "E"
    else:
        return None  # invalid mark


def show_results(students):
    if not students:
        print("\nNo students added yet.\n")
        return

    print("\nResults:")
    print(f"{'Name':<20}{'Mark':<10}{'Grade':<10}")
    print("-" * 40)

    marks = []
    for name, mark in students:
        grade = calculate_grade(mark)
        print(f"{name:<20}{mark:<10}{grade:<10}")
        marks.append(mark)

    avg = sum(marks) / len(marks)
   #print("\t\nClass Average:\t", round(avg, 2))
    #print("\tHighest Mark:\t", max(marks))
    #print("\tLowest Mark:\t", min(marks))
    print(f"\nClass Average: {avg:<8.1f} Highest Mark: {max(marks)} Lowest Mark: {min(marks)}\n")
    


def add_student(students):
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        mark = int(input("Enter student mark (0–100): ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    grade = calculate_grade(mark)
    if grade is None:
        print("Invalid mark. Must be between 0 and 100.")
        return

    students.append((name, mark))
    print(f"Added {name} with mark {mark}.\n")


def menu():
    students = []
    while True:
        print("Menu: [1] Add Student  [2] Show Results  [3] Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_results(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    menu()
