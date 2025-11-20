# Function
# DRY -> Don't Repeat Yourself
# def greetings():  # function defination
#     print("welcome")
#     print("to")
#     print("our")
#     print("website")
#     print("Hi")
#     print("Ram")


# greetings()


# here name, greet_word are variables but, since they are used in a function inside () during function defination, they are called as parameters or in short params
# def greetings(name, greet_word):  # function defination
#     print("welcome")
#     print("to")
#     print("our")
#     print("website")
#     print(greet_word)
#     print(name)


# print(name, greet_word)

# greetings("Ram", "Good morning !")
# here when we pass/provide actual data/values to function params during function call, they are called as arguments

# greetings(name="Ram", greet_word="Good morning !")
# greetings(greet_word="Good morning !", name="Ram")
# greetings("Good morning !", "Ram")
# greetings("Hari")


# greet_word = "Hi"
# greet_word = "Good evening !"

# print(greet_word)


# greet_word="Hi" , here in this example when we give a value/default value to a parameter, default parameter
# default parameter/s should always come after positional parameter or simply after non-default parameters
# def greetings(name, greet_word="Hi"):  # function defination
#     print("welcome")
#     print("to")
#     print("our")
#     print("website")
#     print(greet_word)
#     print(name)


# greetings("ram")


# def multiplication_table(number):
#     print("#######################################")
#     # prints multiplication table for 1 number
#     for multiple in range(1, 11):
#         print(f"{number} x {multiple} = {number * multiple}")

#     print("#######################################")


# multiplication_table(56)
# multiplication_table(67)
# multiplication_table(89)
# multiplication_table(98)

# print("asldkfj")
# input()
# 3 < -len("ram")


# def add(a, b):
#     print(a + b)
# def add(a, b):
#     result = a + b
#     return result


# add_result = add(4, 5)

# we can use add_result in further processing


# def neb_worker1(documents):
#     # processing to generate transcript, provisional and migration certificates
#     return "Receipt"


# def neb_worker2(receipt):
#     # search certificates for the receipt
#     return "Transcript", "Provisional", "Migration"


# receipt = neb_worker1("11th marks sheet, 12th mark sheet, letter")
# print(receipt)
# # after 7 days
# certificates = neb_worker2(receipt)
# # here certificates is group of 3 items, in tuple data type

# # c1, c2, c3 = certificates  # unpacking
# # print(c1)
# # print(c2)
# # print(c3)

# c1, *c2 = certificates  # unpacking


# print(certificates)


# def add(a, b):
#     print(a + b)


# result = add(4, 5)

# if result is not None:
#     print("result", result)
#     print("result", result)

# else:
#     print("Function didn't returned any value")
