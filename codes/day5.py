# Not operator
# data = "This is data from api call"

# if data is not None:
#     print("Data received")
# else:
#     print("No data received")


# if data is None:
#     print("No data received")
# else:
#     print("Data received")

# string data maa sub-string exist garxa ki gardaina
# Kunai data structure, kunai data exist garxa ki gardaina

# fruits = "apple, grapes"
# user_input = input("Enter a sub-string: ")

# if user_input in fruits:
#     print("Yes it exists")
# else:
#     print("The sub-string you entered doesn't exist")


# Variables and datatypes (basic)
# Rules for naming variables
# Operator (Arithematic, Relational, Logical, Identity, Membership)
# Control Flow Statement - Conditional Statement
# Control Flow Statement - Looping statement

# Looping Statement
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# range(10) => 0, 1, 2, ..... 8, 9
# range(5) => 0, 1, 2, .....4
# range_5 = "0, 1, 2, 3, 4"

# for i in range(10):
#     print("Welcome", i)

# range(1, 10) => here, first value i.e. 1 is called starting value, second value i.e. 10 is called stopping value
# for i in range(3, 10):
#     print("Welcome", i)

# range(1, 10, 2)
# first value i.e. 1 => starting value
# second value i.e. 10 => stopping value
# last value i.e 2 => stepping value
# for i in range(1, 10, 3):
#     print("Welcome", i)

# 10+(-1) = 9
# for i in range(10, -5, -1):
#     print("Welcome", i)

# print("2x1=2")
# print("2x2=4")
# print("2x3=6")
# print("2x4=8")
# print("2x5=10")
# print("2x6=12")
# print("2x7=14")
# print("2x8=16")
# print("2x9=18")
# print("2x10=20")

# Kunai string data xa, jun maa kei kura haru dynamic xan
# for i in range(1, 11):
#     print(f"3 x {i} = {i*3}")

# "102" => int("102") => 102*2
# number = int(input("Multiplication table for: "))
# upto = int(input("Multiplication till ?? : "))

# for i in range(1, upto + 1):
#     print(f"{number} x {i} = {i*number}")


# While loop
# number = 10
# i = 11
# limit = 10
# step_value = 2
# while i <= limit:
#     print(f"{number} x {i} = {i*number}")
#     i = i + step_value


# while True:
#     day = input("What day is today?: ")

#     if day == "saturday":
#         print("Yeah, Today is holiday.")
#         print("Enjoy!")
#         break

#     print("Go to school ")
# life = 10

# while True:
#     day = input("What day is today?: ")

#     if day == "saturday":
#         print("Yeah, Today is holiday.")
#         print("Enjoy!")
#         continue  # skip the lines below

#     print("Go to school ")
#     print("Go to school ")
#     print("Go to school ")
#     print("Go to school ")
#     print("Go to school ")

#     life = life - 1
#     if life == 0:
#         break

# print("Welcome to heaven")
# while True:
#     print("Inifinite")
# stockstatus = input("Is the item in stock (yes/no): ")
# if stockstatus == "yes":
#     while True:
#         paymentstatus = input("Is the payment successful (success/failed): ")
#         if paymentstatus == "success":
#             print("Order placed")
#             break
#         else:
#             print("Order failed")
# else:
#     print("Order failed")
# import os
# import time
# import random


# for i in range(100):
#     os.system("clear")
#     print(f"Downlading... {i}%")
#     print("|" * i)
#     time.sleep(random.random())
