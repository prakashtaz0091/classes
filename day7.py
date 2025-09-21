# a = "hello"
# b = 10
# # print("%s is a string,   %d is an integer" % ("hello", 10))
# # print("%s is a string,   %d is an integer" % (a, b))
# print(f"{a} is a string,   {b} is an integer")


# number = float(input("Enter a number: "))

# # 1. number needs to be checked if it is positive
# # 2. number needs to be checked if it is negative
# # 3. Else it is 0

# if number > 0:
#     print(f"{number} is positive")
# elif number < 0:
#     print(f"{number} is negative")
# else:
#     print(f"{number} is 0")


# a = 5
# b = 7

# a, b = b, a
# temp = a  # put the value of a into temp, temp = 5
# a = b  # put value of b into a, a = 7
# b = temp  # put value of a into b, b = a, b = 5


# a = a + b  # 12
# b = a - b  # 5
# a = a - b  # 7


# print(a, b)


# Function return statement
# 1. void function -> no return statement -> yesle None, Nothing
# 2. return statement -> yesle value return garxa


# def add(a, b):
#     # print(a + b)
#     return a + b


# result = add(10, 20)
# print(result)

# ex = "RAM"
# ex = ex.lower()  # takes "RAM" and returns "ram"
# print(ex)


# Console Calulator


# def show_calculator_menu():
#     MENU = """
#     1. Add
#     2. Subtract
#     3. Multiply
#     4. Divide
#     5. Exit
#     """
#     print(MENU)


# def get_result(choice, num1, num2):
#     # 4. Check for operations
#     if choice == "1":
#         # add operation
#         return num1 + num2
#     elif choice == "2":
#         # subtract operation
#         return num1 - num2
#     elif choice == "3":
#         # multiply operation
#         return num1 * num2
#     elif choice == "4":
#         # divide operation
#         return num1 / num2


# def show_formatted_result(result):
#     print("#############---Result---############")
#     print(result)
#     print("#############---Result---############")


# # Main program/loop
# while True:
#     # 1. Show calculator menu so that user can choose operation
#     show_calculator_menu()

#     # 2. Take input from user, to get the operation choice
#     choice = input("Enter your choice: ")

#     # 3. If user wants to exit, break the loop
#     if choice == "5":
#         break

#     # 4. Since user don't want to end the program, we know he wants to do operation, and needs to input at least two numbers
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     # 5. Calculate the result
#     result = get_result(choice, num1, num2)

#     # 6. Display the result
#     show_formatted_result(result)


# Data Structures

# 1. list (simply collection of objects/data items)
# student1 = "ram"
# student2 = "hari"
# students = [] # way to create empty list
# students = ["ram", "hari", "sita", "gita"]
# index       0      1        2      3
# print(type(students))
# print(students)
# print(len(students))  # len returns the length/no of data items
# len("ram") -> 3

# to iterate over the list
# in other words, if we need to perform same operation for each item in the list, we will use for loop.
# for student in students:
#     print(student)


# students.append("Roshan") # to add item at last position of list
# students.insert(0, "Roshan")  # to add item at specific position of list
# print(students)

# removed_name = students.pop()

# # another_name = students.pop(2)
# # students.remove("hari")
# # students.remove("ram")

# # del students[2]

# print(students)
# print("Removed name is", removed_name)
# print("Another name is", another_name)


# s = students[0]  # -> "ram"
# s2 = students[1]  # -> "hari"

# print(students[-1])
# print(students[-2])
# print(students[-3])


# students = ["ram", "hari", "sita", "gita"]


# for number, student in enumerate(students, start=1):
#     print(f"{number}. {student}")


# Collecting names of students those who wants to perform

students_name_list = []


def show_menu():
    MENU = """
    1. Add Student Name
    2. Remove Student Name
    3. Show Student Names
    4. Exit  
    """
    print(MENU)


def add_new_student():
    name = input("Enter student name: ")
    students_name_list.append(name)


def remove_student():
    name = input("Enter student name to remove: ")
    students_name_list.remove(name)


def show_all_students_name():
    print("#" * 40)
    print("#" * 10, "Student Names", "#" * 10)
    for number, student in enumerate(students_name_list, start=1):
        print(f"{number}. {student}")

    print("#" * 40)


while True:
    # 1. Show menu
    show_menu()

    # 2. Take input from user
    choice = input("Enter your choice: ")

    # 3. If user wants to exit, break the loop
    if choice == "4":
        print("Completed adding student names")
        print("Program end ...")
        break

    # if user want to add student
    if choice == "1":
        # Add student
        add_new_student()
    elif choice == "2":
        # Remove student
        remove_student()
    elif choice == "3":
        # Show student
        show_all_students_name()
