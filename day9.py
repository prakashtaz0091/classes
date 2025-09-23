# import math as m
# from math import gcd, lcm, factorial, sqrt, isqrt, pi, e, log, log10, log2
# from math import *

# del lcm

# # result = math.gcd(12, 6, 23, 45, 60)
# # result = m.gcd(12, 6, 23, 45, 60)
# result = gcd(12, 6, 23, 45, 60)
# print(result)
# a = 10
# del a

# import time


# for i in range(10):
#     print(i)
#     time.sleep(1)


# import datetime


# print(datetime.datetime.now())
# def find_age(birth_date):
#     today = datetime.date.today()
#     # print(today, birth_date, type(today), type(birth_date))
#     age = today - birth_date
#     print(age)
#     return age.days // 365


# user_birthdate = input("Enter your birth date: (yyyy-mm-dd) ")
# user_birthdate = datetime.datetime.strptime(user_birthdate, "%Y-%m-%d").date()
# age_in_years = find_age(user_birthdate)

# print(f"You are currently {age_in_years} years old")

# import random

# random_number = random.randint(1, 6)
# print(random_number)

# cards_list = [1, 2, 3, 4, 5, 6]
# random.shuffle(cards_list)

# print(cards_list)

# import helpers
# from helpers import add, multiply, factorial
# from custom_package.helpers import add, multiply, factorial


# print(add(1, 2, 3, 4, 5))
# print(multiply(1, 2, 3, 4, 5))
# print(factorial(5))


# Exception Handling


# In this line of code, there might be an error, while converting to integer
# number = int(input("Enter a number: "))

# while True:
#     try:
#         number = int(input("Enter a number: "))
#         break
#     except:
#         print("Invalid input")

# try:
#     number = int(input("Enter a number: "))
#     # number / 0
# except ValueError:
#     print("You have entered wrong input, please enter numbers only")
# except ZeroDivisionError:
#     print("You are trying to divide by zero, please enter another number")
# except Exception as e:
#     print("Something went wrong. Please try again later.", e)
# finally:
#     print("End of program")
# stop the loader


