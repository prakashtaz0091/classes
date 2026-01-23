# a = "ram", whenever we write # (hashtag), the content after that is called as comment, it's not the part of code
# print(a)

# Rules for naming variables
# 1. variable name must start with a letter or an underscore (_)
# recommended that, variable names should be lowercase (i.e. small letters)
# a = 10
# 1a = 10 # since 1a variable name starts with '1', which is not a letter, so it's not a valid variable name

# _1a = 10
# _2a = 10

# x1 = 10
# x2 = 10

# 2. variable name must be a single word

# full name = "Ram Thapa" #wrong

# studentfullname = "Ram Thapa"
# student_full_name = "Ram Thapa"


# 3. reserved words cannot be used as variable names
# if, else, elif, not, or, and
# a = 10
# and = 10


# 4. (good to follow) Variable name must be meaningful

# a = 10
# b = 5
# c = 50

# no_of_students = 10

# Operators
# 1. Arithmetic operators

# x = 5
# y = 3

# print("Addition ", x + y)
# print("Subtraction", x - y)
# print("multiplication", x * y)  # multiplication
# print("division", x / y)  # true division
# print("quotient", x // y)  # integer division (quotient)
# print("remainder", x % y)  # modulo (remainder)
# print("power", x**y)  # power

# print("Add =", x + y, x - y, x * y)
# print(x + y / 2**3 * y)

# Type casting
# x = int(input("Enter the value of x: "))
# y = float(input("Enter the value of y: "))

# result = x + y

# print("Result is ", result)

# Input -> Process -> Output


# Write a program to convert given kilometer value to meter

# km_value = float(input("Kilometer value ? "))

# # using formula, 1 km = 1000 m
# meter_value = km_value * 1000

# print(
#     "According to formula 1 km = 1000 m, ",
#     km_value,
#     "kilometer is equals to ",
#     meter_value,
#     " meters",
# )

# formatted string
# answer = f"""
# ==> According to the formula,
#         1 km  = 1000 m

#         {km_value} km is equals to {meter_value} meters

# """
# print(answer)


# 2. Relational operators (comparision)
# >, <, >=, <=, ==, !=

# print(5 > 2)

# age = int(input("Enter your age: "))
# # Control Flow statement
# if age >= 18:  # this checks if user's age is >= 18
#     print("Yes, you are eligible for citizenship")
# else:
#     print("No, you are not eligible for citizenship")

# the gap after if and else statement in above example is called as indentation


age = int(input("Enter your age: "))
# gender = input("Enter your gender (male/female): ")

# # # Control Flow statement
# if gender == "male":  # this checks if user's age is >= 18
#     if age >= 18:
#         print("Yes, you are eligible for citizenship")
#     else:
#         print("No, you are not eligible for citizenship")
# else:
#     if age >= 16:
#         print("Yes, you are eligible for citizenship")
#     else:
#         print("No, you are not eligible for citizenship")
