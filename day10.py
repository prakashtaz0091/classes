# Modules
# token -> statement -> function -> module -> package -> library -> framework


# import math

# Ref: https://docs.python.org/3/library/math.html
# result = math.sqrt(25)
# result = math.cbrt(25)
# result = math.ceil(2.5)
# result = math.floor(2.5)
# result = math.pow(2, 5)
# result = math.sin(90)
# result = math.cos(90)
# print(result)


# import time

# i = 10
# while i >= 0:
#     print(i)
#     time.sleep(1)
#     i = i - 1


# from datetime import datetime, date

# today = date.today()

# date(2001, 07, 14)
# # print(type(today))
# # print(today.strftime("%d/%m/%Y"))

# birthday_input_text = input("Enter your birth date (dd/mm/YY) : ")

# birthday = datetime.strptime(birthday_input_text, "%d/%m/%Y").date()
# today => date
# birthday => date

# result = today - birthday

# years = result.days // 365

# months = (result.days % 365) // 30

# days = (result.days % 365) % 30

# print(years, " years")
# print(months, " months")
# print(days, " days")


# Custom modules
# import c_math

# print(c_math.add(4, 5))
# print(c_math.sub(4, 5))

# from c_math import add, sub, mul

# print(add(4, 5))
# print(sub(4, 5))
# print(mul(4, 5))


# from c_math import int_div as idiv

# print(idiv(40, 5))

# import c_math as cm

# cm.add
# cm.sub

# from o_math import c_math as cm
# from o_math import s_math as sm

#  compiler           interpreter
# py -> intermediate code ->  run


# tabulate -> library -> download/install
# pip install tabulate


# 1 project -> 1 Virtual environment

# computer -> more than 1 project?
# project 1 -> tabulate
# project 2 -> lib2
# project 3 -> lib3, lib4

# tabulate, lib2, lib3, lib4

# os full -> full environment
# project 1 -> 1 seperate environment -> virtual environment

# virtual env -> special folder -> pip install tabulate -> tabulate

# 1. Linux/MacOS
# step 1: virtual environment banaune
# command:   python3 -m venv env
# step 2: activate virtual environment to use it
# command:   source env/bin/activate
# step 3: now we can install any library or packages, it will automatically reside in virtual environment folder


# 2. Windows
# step 1: virtual environment banaune
# command:   python3 -m venv env
# step 2: activate virtual environment to use it
# command:   env\Scripts\activate
# step 3: now we can install any library or packages, it will automatically reside in virtual environment folder


###############################
###############################
###############################
###############################
###############################
###############################
# from tabulate import tabulate

# # Mini Student Tracker
# MENU = """
#     1. Add Student Data
#     2. Show all students data
#     3. Remove student data
#     Q. Quit
# """
# students = []


# def show_menu():
#     print(MENU)


# def show_all_students_data():
#     headers = ["Student Name", "Age"]
#     table = []
#     for student in students:
#         table.append(student.values())

#     print(tabulate(table, headers, tablefmt="heavy_grid"))


# def add_student():
#     name_input = input("Enter name: ")
#     age_input = input("Enter age: ")

#     new_student = {"name": name_input, "age": age_input}
#     students.append(new_student)


# def remove_student():
#     name_to_remove = input("Enter student name to remove: ")
#     for student in students:
#         # check if student name is stu_name_to_remove
#         if student["name"] == name_to_remove:
#             students.remove(student)
#             break


# # Main loop
# while True:
#     # 1. Show menu to the user
#     show_menu()

#     # 2. Take input from user
#     user_choice = input("Enter your choice (1/2/3/Q) >>> ")

#     # if user_choice == "Q" or user_choice == "q":
#     if user_choice in ("Q", "q"):
#         print("Thank you for using our program")
#         break

#     elif user_choice == "1":
#         add_student()
#         # ask if user wants to enter another student data
#         # if yes=> run add_student() again. Hint, use while loop

#     elif user_choice == "2":
#         show_all_students_data()

#     elif user_choice == "3":
#         remove_student()

#     else:
#         print("Invalid input ! Please read the instructions carefully ")
