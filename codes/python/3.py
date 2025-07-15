# character = input("Enter a character: ")
# # len(character)
# if character.isalpha():
#     print("This is alphabet")
# elif character.isdigit():
#     print("This is a digit")
# else:
#     print("This is a special character")


# password = input("Enter your password: ")
# score = 0

# if len(password) >= 8:
#     if not password.isalpha():  # confirms that all characters are not alpha
#         score = score + 1
#     if not password.isnumeric():  # confirms that all characters are not numbers
#         score = score + 1
# else:
#     print("Password must be at least 8 characters long")

# print("Your password strength is ", score)


# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")
# print("I'm sorry")


# For loop
# for _ in range(10):  # range(10) -> [0,1,2,3,....,9]
#     print("I'm sorry")


"""Multi-line Comment
2x1=2
2x2=4
2x3=6
...
2x10=20
"""

# "ram "

# for number in range(1, 110):
#     # print("2x", number, "=", 2 * number)
#     # line = f"2 x {number} = {2 * number}"
#     # 2 x 1 = 2
#     # print(line)
#     print(f"2 x {number} = {2 * number}")

# receiver = input("Receiver's Name: ")
# sender = input("Sender's Name: ")

# message = f"""
# Dear {receiver},
# Namaste

# I hope ....


# Kind Regards,
# {sender}
# """

# print("Final Message is: ")
# print(message)

# for number in range(2, 11, 2):  # [1,3, 5, 7, 9 ]
#     print(number)

# num = int(input("For which number you wanna print multiplication table: "))

# for multiple in range(1, 11):
#     print(f"{num} x {multiple} = {num * multiple}")

"""
table from 1, to 50
1x1 = 1 ...... 1x10 = 10
.
.
.
50x1 = 50......50x10=500


"""
# Task -> repeat 2 times
# for number in range(1, 11):
#     print(f"2 x {number} = {2 * number}")

# print("######################################")

# start_table = int(input("Start from: "))
# to_table = int(input("To : "))

# for num in range(start_table, to_table + 1):
#     for number in range(1, 11):
#         print(f"{num} x {number} = {num * number}")

#     print("######################################")


# Infinite loop
# num = 0
# while num < 11:  # 11<11 => False => stop
#     print(num)
#     num = num + 1


# angry = True  # someone is angry/sad

# while angry:  # loop runs when condition is True
#     print("I'm sorry")
#     response = input("Are you happy now (y/n): ")

#     if response == "y":
#         angry = False


# print("Thank you")


# while True:  # loop runs when condition is True
#     print("I'm sorry")
#     response = input("Are you happy now (y/n): ")

#     if response == "y":
#         break
# print("Thank you")


for day in range(1, 8):
    if day == 3:  # 7=>saturday
        print("Today is Tuesday aka Holiday")
        continue

    print(f"############---Day-{day}--########")
    print("Morning=> Wakeup")
    print("8'o clock => Ready for office")
    print("2'o clock => lunch")
    print("5'o clock => Pack for home")
    print("Arrive home...")

    print("-----------------------------------")
