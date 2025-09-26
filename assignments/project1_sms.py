import csv

students = []  # List to hold student dictionaries

# ------------------- Functions -------------------


def load_from_csv():
    """Load student records from students.csv"""
    pass


def save_to_csv():
    """Save student records to students.csv"""
    pass


def add_student():
    """Take input and add new student"""
    pass


def remove_student():
    """Remove student by name"""
    pass


def show_students():
    """Display all students"""
    pass


def search_student():
    """Search for a student by name"""
    pass


def show_menu():
    print("""
    1. Add Student
    2. Remove Student
    3. Show All Students
    4. Search Student
    5. Save and Exit
    """)


# ------------------- Main Program -------------------

load_from_csv()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        show_students()
    elif choice == "4":
        search_student()
    elif choice == "5":
        save_to_csv()
        print("Data saved. Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")
