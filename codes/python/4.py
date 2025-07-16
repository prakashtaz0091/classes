# multiplication_table_of_2()


# def multiplication_table_of_2():  # defining a function or simply function defination
#     # prints the multiplication table of 2
#     for num in range(1, 11):
#         print(f"2 X {num} = {2 * num}")


# multiplication_table_of_2()  # calling a function or simply say, function call
# multiplication_table_of_2()
# multiplication_table_of_2()


# print()
# input()
# int()
# type()

# greeting = "Welcome here" => has initial value or default value set, so it's called as default paramter
# def greet_user(name, greeting="Welcome here"):  # parameters
#     # print("Welcome here, ", name)
#     message = f"{greeting}, {name}"
#     print(message)


# name = input("Enter your name: ")
# # greet_user(name, "Good evening")  # arguments
# # greet_user("Good evening", name)  # arguments
# # greet_user(greeting="Good evening", name=name) # keyword argument
# greet_user(name, "Good morning")


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Reminder: Always keep, default arguments/parameter after positional parameter/arguments
# def greet_user(greeting="Welcome here", name):  # parameters
#     # print("Welcome here, ", name)
#     message = f"{greeting}, {name}"
#     print(message)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# LIMITATION----------------------------
# def add_all_nums(a, b, c, d):
#     print("Addition Result: ", a + b + c + d)


# add_all_nums(2, 3, 4, 5)
# LIMITATION----------------------------


# def add_all_nums(*numbers):  # any number of positional arguments
#     # print(numbers)
#     addition_result = 0
#     for number in numbers:
#         addition_result = addition_result + number
#         # print("current addition result: ", addition_result)

#     print("Final result: ", addition_result)


# add_all_nums(2, 3, 3, 4, 4, 5, 3, 45, 23423)


# def show_details(**kwargs):
#     # print(kwargs)
#     for keyword, value in kwargs.items():
#         print(f"{keyword} => {value}")


# show_details(name="Ram", college="MMC", address="KTM")


# def asdf(a, b, /, m):
#     print(a, b, m)


# asdf(2,b=2, 2)


# number = 10_00_000
# print(number)
