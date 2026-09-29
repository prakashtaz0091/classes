# num1 = float(input("Enter a number "))
# num2 = float(input("Enter another number "))
# # num1 = "788" -> 788
# # num2 = "877"  -> 877

# result = num1 + num2
# # result = "788" + "877" = "788877" # string concatination
# # 788877

# print(result)

# ask kilometer value to user and convert to meters
# 1 km = 1000 m

# km_value = float(input("Enter km value "))

# m_value = km_value * 1000

# # print(km_value, " km = ", m_value, " meters")

# print(f"{km_value} km = {m_value} meters")

# Rules for naming variables
# 1[Strict]. variable name must start with letter or an underscore

# num1 = 90
# _1num = 90

# 2[Standard]. variable name should be meaningful

# a = 5
# b = 10

# english = 5
# math = 10

# a = 90
# b = 60

# 3[Standard]. variable name must be single word, if it's more than one word, use snake_case
# camelCase => englishFullMarks
# PascalCase => EnglishFullMarks

# english_full_marks = 50
# english_marks = 5
# math_marks = 10

# 4[Strict]. Reserved keywords cannot be used as variable names

# if = 10 # wrong

# determine if user is allowed to apply for citizenship card or not
## Algorithm
# step 1: what is your age? => 18
# step 2: check if user's age is greater than or equals to 18 ?
# step 3: if yes, user is eligible for citizenship card
# step 4: if no, user is currently not eligible for citizenship
# ex.com/admin/dashboard/
# user_role == "admin":

# age = int(input("Enter your age (eg. 20) "))

# if age>=18:
#     print("You are eligible for applying citizenship")
#     print("Congratulations")
# else:
#     print("Sorry, you are too young enough to get citizenship")
#     print("Please try again when you are 18")

# print("Thank you for using our system")
    

# Calcuate grade based on user entered marks
# 1. Ask user obtained marks
# 2. check if marks >= 90 -> A+
# 3. check if marks >= 80 -> A
# 4. check if marks >= 70 -> B+
# 5. check if marks >= 60 -> B
# 6. check if marks >= 50 -> C+
# 7. check if marks >= 40 -> C
# 8. check if marks >= 30 -> D+
# 9. check if marks >= 20 -> D
# 10. check if marks >= 10 -> E
# 11. check if marks >= 0 -> NG

# marks = float(input("Enter marks obtained: "))

# if marks > 100:
#     print("Invalid marks, marks must be (0-100)")
# elif marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B+")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C+")
# elif marks >= 40:
#     print("C")
# elif marks >= 30:
#     print("D")
# elif marks >= 20:
#     print("D+")
# elif marks >= 10:
#     print("E")
# elif marks >= 0:
#     print("NG")
# else:
#     print("Invalid marks, marks must be (0-100)")


## improvised

# marks = float(input("Enter marks obtained: "))
# if marks greater than 100 -> invalid
# if marks less than 0 -> invalid
# 125 # athawa -> OR

# if marks > 100 or marks < 0:
#     print("Invalid marks, marks must be (0-100)")
# elif marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B+")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C+")
# elif marks >= 40:
#     print("C")
# elif marks >= 30:
#     print("D")
# elif marks >= 20:
#     print("D+")
# elif marks >= 10:
#     print("E")
# elif marks >= 0:
#     print("NG")
    
    
# and -> 
# 
english = 40
maths = 60
science = 16

# pass ?? english >= 20, maths >= 20

# if english >= 20 and maths >= 20:
#     print("pass")

# fail ?? english < 20, maths < 20, science < 20

if english<20 or maths<20 or science<20:
    print("fail")