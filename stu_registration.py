import csv
import os
from tabulate import tabulate


def clear_screen():
    if os.name == "nt":  # nt = windows
        os.system("cls")
    else:
        os.system("clear")


def show_menu():
    MENU = """
        1. Add student
        2. Show all student
        Q. Quit

    """
    print(MENU)


def add_student():
    while True:
        # Add student
        print("#" * 40)
        print("#" * 10, "Add Student", "#" * 10, "\n")

        stu_class = input("Class: ")
        stu_rollno = input("Roll No: ")
        stu_name = input("Name: ")
        stu_age = input("Age: ")

        with open("students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([stu_class, stu_rollno, stu_name, stu_age])

        clear_screen()

        print("#" * 40)
        print("#" * 10, "Student added successfully", "#" * 10, "\n")

        user_choice = input(" Press enter to add another, N to exit: ")
        if user_choice.lower() == "n":
            break

    clear_screen()


def show_students():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        print(tabulate(rows, headers="firstrow", tablefmt="heavy_grid"))


while True:
    # 1. Show menu
    show_menu()

    user_choice = input("Enter your choice: ")

    # 2. Clear screen
    clear_screen()

    if user_choice in ("Q", "q"):
        print("Thank you for using our program")
        print("Program end ...")
        break

    if user_choice == "1":
        add_student()
    elif user_choice == "2":
        show_students()
