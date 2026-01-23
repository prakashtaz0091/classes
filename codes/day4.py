# Find greater number between two numbers
#  number1  and   number2
# compare number1 > number2 ??? number1 is greater
# otherwise  number2 is greater

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if number1 == number2:
#     print(number1, " is equals to ", number2)
# elif number1 > number2:
#     print(number1, " is greater than ", number2)
# else:
#     print(number2, " is greater than ", number1)


# Forms of if-statement

# marks = 90
# 1.   if statement
# if marks >= 40:
#     print("You passed the examination")

# 2. if else statement
# if marks >= 40:
#     print("You passed the examination")
# else:
#     print("You failed the examination")

# marks = 101
# # 3. if elif else statement
# if marks > 100:
#     print("Marks cannot be greater than FM (full marks, i.e. 100)")
# elif marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B+")
# else:
#     print("Invalid marks")

# Try adding more elif conditions to calculate grade till grade E


# if marks >= 90:
#     print("A+")
# if 80 <= marks < 90:
#     print("A")
# if 70 <= marks < 80:
#     print("B+")


# single truth
# if elif elif else

# mulitple truth, multiple solutions
# if statement

# Arithmetic , Relational (comparision)

# 3. Logical operators
# and, or , not

# use when you want to combine two or more than two relational operations

# age = int(input("Enter your age: "))
# gender = input("Enter your gender (male/female): ")

# if gender == "male" and age >= 18:  # check if male and age >= 18
#     print("Yes, you are eligible for citizenship")
# elif gender == "female" and age >= 16:  # check if female and age >= 16
#     print("Yes, you are eligible for citizenship")
# else:
#     print("No, you are not eligible for citizenship")


# if (gender == "male" and age >= 18) or (
#     gender == "female" and age >= 16
# ):  # check if (male and age >= 18) or (female and age>=16)
#     print("Yes, you are eligible for citizenship")
# else:
#     print("No, you are not eligible for citizenship")


# and operator => Final result is True only when all the relations are True
# or operator => Final result is True, if atleast one of the relation is True, In other words, final result is False only when all the relations are False

# (gender == "male" and age >= 18)
#       True        and   True     => True
#       False       and   True     => False
#       True        and   False     => False
#       False       and   False     => False


# (gender == "male" or age >= 18)
#       True        or   True     => True
#       False       or   True     => True
#       True        or   False     => True
#       False       or   False     => False

# Marks obtained by student
# maths_marks = 40  # PM = 32
# science_marks = 50  # PM = 32
# english_marks = 60  # PM = 32
# computer_marks = 17  # PM = 18

# if (
#     maths_marks >= 32
#     and science_marks >= 32
#     and english_marks >= 32
#     and computer_marks >= 18
# ):  # to check if the student has passed the exam
#     print("Student passed the examination")
# else:
#     print("Student failed the examination")


# if (
#     maths_marks < 32 or science_marks < 32 or english_marks < 32 or computer_marks < 18
# ):  # to check if the student has failed the exam
#     print("Student failed the examination")
# else:
#     print("Student passed the examination")

# failed_in_math = maths_marks < 32
# failed_in_english = english_marks < 32
# failed_in_science = science_marks < 32
# failed_in_computer = computer_marks < 18


# if (
#     failed_in_math or failed_in_english or failed_in_science or failed_in_computer
# ):  # to check if the student has failed the exam
#     print("Student failed the examination")
# else:
#     print("Student passed the examination")


# not operator => it simply toggles the boolean value
# True/False
# not True => False
# not False => True

# is_raining = True

# # if is_raining:  # 1 way
# #     print("Hide the cloths")
# # else:
# #     print("Reveal the cloths")

# if not is_raining:
#     print("Reveal the cloths")
# else:
#     print("Hide the cloths")


# Membership operator
# sentence = "Ram is a good boy"

# print("good" in sentence)
# print("is" in sentence)
# print("boy" in sentence)
# print("good boy" in sentence)

# print("boy good" in sentence)

# users = "ram shyam hari geeta seeta"

# username = input("Username : ")
# # "prakash" in "ram shyam hari geeta seeta"
# # "ram" in "ram shyam hari geeta seeta"
# if username in users:
#     print("welcome to the system sir.")
# else:
#     print("You are not the member. Please signup to join us")


# Identity operator
# is

# a = 10
# b = a

# print(a == b)

# a = "ram"
# b = "ram"

# print(a is b)
