# age = 20
# gender = "femle"

# if gender == "male" and age >= 18:
#     print("You are eligible for citizenship")
#     print("Please visit office")
# elif gender == "female" and age >= 16:
#     print("You are eligible for citizenship")
#     print("Please visit office")
# else:
#     print("You are too young to get citizenship")
#     print("Please try again after few years")


# age = 13
# passed_10 = True

# if passed_10:
#     if age >= 15:
#         print("Yes collect the citizenship")
#     else:
#         print("Not eligible")
# else:
#     if age >= 18:
#         print("Yes collect the citizenship")
#     else:
#         print("Not eligible")


# if passed_10 and age >= 15:
#     print("Yes collect the citizenship")
# elif not passed_10 and age >= 18:
#     print("Yes collect the citizenship")
# else:
#     print("Not eligible")


# percentage = 80

# if percentage >= 90 and percentage <= 100:
#     print("A+")
# elif percentage >= 80 and percentage < 90:
#     print("A")
# elif percentage >= 70 and percentage < 80:
#     print("B+")
# elif percentage >= 60 and percentage < 70:
#     print("B")
# elif percentage >= 50 and percentage < 60:
#     print("C+")
# elif percentage >= 40 and percentage < 50:
#     print("C")
# elif percentage >= 30 and percentage < 40:
#     print("D")
# elif percentage >= 20 and percentage < 30:
#     print("E")
# elif percentage >= 0 and percentage < 20:
#     print("NG")
# else:
#     print("Invalid percentage")


# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))  # explicit type conversion

# # user_age = "50" + 5
# # print(type(user_age))

# print("Your name is ", user_name)
# print("Your current age is ", user_age)
# print("After 5 years your age will be ", user_age + 5)
# print("After 10 years your age will be ", user_age + 10)


age = int(input("Enter your age: "))
passed_10 = input("Are you SEE graduate (y/n): ")

if passed_10 == "y":
    if age >= 15:
        print("Yes collect the citizenship")
    else:
        print("Not eligible")
elif passed_10 == "n":
    if age >= 18:
        print("Yes collect the citizenship")
    else:
        print("Not eligible")
else:
    print("Invalid answer for second question, it should be either 'y' or 'n'")
