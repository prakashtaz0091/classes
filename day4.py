# Control flow
# # Conditional statements
# # Looping statement

# 1. Finite looping (for _ in )

# print("Welcome home !!!")
# print("Welcome home")
# print("Welcome home")
# print("Welcome home")
# print("Welcome home")

# for i in range(5):
#     print("Welcome home !!!")


# What is i?
# range(5) => [0,1,2,3,4]
# for i in range(5):
#     print("Welcome home !!!", i)

# range(1, 5) => 1 is starting value, 5 is stopping value, 5 is excluded
# for i in range(1, 5):
#     print("Welcome home !!!", i)


# range(1, 5, 2) => 1 is starting value, 5 is stopping value, 5 is excluded, 2 is called step value
# for i in range(1, 5, 2):
#     print("Welcome home !!!", i)


# Multiplication table
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

# for num in range(1, 11):
#     print("2x", num, "=", num*2)

# for num in range(1, 11):
#     print("3 x", num, "=", num*3)

# for num in range(1, 11):
#     print(f" 3 x {num} = {3*num} ")

# for num in range(1, 11):
#     print(f" 4 x {num} = {4*num} ")

# Example. print mul table for user given number
# number = int(input("Enter a number for mul table: "))

# for num in range(1, 11):
#     print(f" {number} x {num} = {number*num} ") 


# number = int(input("Enter a number for mul table: "))

# for num in range(10, 0, -1):
#     print(f" {number} x {num} = {number*num} ") 

# sentence = "We love Nepal" # sequence of characters
# vowels = "aeiouAEIOU"

# each_char in vowels
# 'W' in "aeiouAEIOU" => False
# 'e' in "aeiouAEIOU" => True

# 'in' is an operator, it's called as membership operator

# for each_char in sentence:
#     # check if it's a vowel
#     if each_char in vowels:
#         print(each_char)



# sentence = "We love Nepal. We speak Nepali" # sequence of characters
# vowels = "aeiouAEIOU"
# count = 0

# for each_char in sentence:
#     # check if it's a vowel
#     if each_char in vowels:
#         print(each_char)
#         count += 1


# print("No of vowels in sentence is ", count)
# _ => underscore
# for _ in range(5):
#     print("Welcome home !!!")


# Infinite looping (while loop)

# line_xa = True  # Yes

# # Fan loop
# while line_xa:
#     print("Fan ghumdaixa")
    
#     user_answer = input("Line xa ?? (yes/no): ")

#         # "no" == "no" => True
#     if user_answer == "no":
#         line_xa = False # which means line gayo


# Account block
# dummy_password = "admin123"
# MAX_ATTEMPTS = 3
# user_attempt = 0

# while user_attempt < MAX_ATTEMPTS:
#     user_password = input("Enter your password: ")
    
#     if user_password != dummy_password:
#         print("Wrong password !!")
#         user_attempt += 1
#         print("Attempts left: ", MAX_ATTEMPTS-user_attempt)
#     else:
#         print("Login successful")
#         break
# else:
#     print("You have entered wrong password for all the attempts")
#     print("So your account has been temorarily blocked. Please visit the office for re-activation")

# print("Program end")

# Account block new variant
dummy_password = "admin123"
MAX_ATTEMPTS = 3
user_attempt = 0

while user_attempt < MAX_ATTEMPTS:
    user_password = input("Enter your password: ")

    if user_password != dummy_password:
        print("Wrong password !!")
        user_attempt += 1
        print("Attempts left: ", MAX_ATTEMPTS-user_attempt)
        continue # skip code below
    
    print("Login successful")
    break
    
print("Program end")
