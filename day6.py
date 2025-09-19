# def show_welcome_message():  # function definition
#     print("Hi")
#     print("Good morning")
#     print("Welcome to the office")
#     print("Have a nice day")

# # function call or calling a function
# show_welcome_message()


# print(2 + 3) # standard/built-in function
# input()
# int()
# float()
# str()
# range()
# .lower()
# show_welcome_message()
# x = 1  # global scope


# def show_welcome_message(name):  # function definition
#     # here name is local variable, which is defined during function creation, it is called as parameter, formal parameter
#     print("Hi, ", name)


# name = input("Enter your name: ")  # < ram
# show_welcome_message(
#     "ram", "hari"
# )  # here "ram" is called as argument, actual parameter


# def show_welcome_message(name, greet):  # function definition
#     print(greet, name)


# show_welcome_message("hari", "Namaste")
# show_welcome_message("ram", "Good morning")
# show_welcome_message("Good morning", "Ram")  # here both as positional arguments
# show_welcome_message(greet="Good morning", name="Ram")  # here both as keyword arguments


# default parameter
# def show_welcome_message(name, greet="Hi"):
#     # here greet has a default value, hence called as default parameter
#     print(greet, name)


# # show_welcome_message("ram", "Good morning")
# show_welcome_message("ram")


# problem -> We need to keep n number of parameter to receive n number of argument
# def add(a, b, c):
#     print(a + b + c)


# add(10, 2, 3, 10)

# range(5) -> [0,1,2,3,4]

# Solution -> *args
# def add(*args):  # *args -> any number of positional arguments
#     # print(args)  # -> tuple -> simply understand it as collection of data items

#     # in this eg. args contains (10, 2, 3, 6, 7), and this for loop will execute 5 times, each time data will be stored in a loop variable called number

#     result = 0
#     for number in args:
#         # print(number)
#         result = result + number

#     print(result)


# add(10, 2, 3, 6, 7, 234234, 2349812, 12, 3)


# def add(*numbers):  # *args -> any number of positional arguments
#     # print(args)  # -> tuple -> simply understand it as collection of data items

#     # in this eg. args contains (10, 2, 3, 6, 7), and this for loop will execute 5 times, each time data will be stored in a loop variable called number

#     result = 0
#     for number in numbers:
#         # print(number)
#         result = result + number

#     print(result)


# add(10, 2, 3, 6, 7, 234234, 2349812, 12, 3)


# **kwargs -> kw-> keyword args-> arguments
# def example(**user_info):  # **kwargs means any number of keyword arguments
#     print(user_info)  # kwargs, this is called as dictionary


# example(name="ram", age=18, isstudent=True)
