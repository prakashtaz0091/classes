from utils import clear_screen
import windows
from permanent import load_students, add_student

STUDENTS = load_students("students.csv")


def registration():
    print("################   Registration started  ##########")
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")

    new_student = [name, age, address]
    STUDENTS.append(new_student)
    add_student("students.csv", new_student)

    print("################   Registration ended  ##########")


def show_all_students():
    for number, student in enumerate(STUDENTS, start=1):
        print(f"""
              -------- Student No: {number} ------------
              Name      :   {student[0]}
              Age       :   {student[1]}
              Address   :   {student[2]}
              ------------------------------------------              
              """)


# main program
while True:
    print(windows.MENU_WINDOW)
    choice = input("Enter your choice (1/2/E) : ")

    if choice == "1":
        # registraton code
        registration()
    elif choice == "2":
        # show all students code
        show_all_students()
    elif choice in "Ee":
        # exit the program
        print(windows.EXIT_WINDOW)
        break
    else:
        clear_screen()
        # say that you entered invalid choice
        print("Invalid choice")
