# 2. Looping statement
# print("Good morning")
# print("Namaste")
# print("Namaste")
# print("Namaste")
# print("Namaste")

# For..in loop
# range(50) -> [0, 1, ... 9]
# for _ in range(10):  # _ -> dummy variable
#     # task
#     print("Good morning")
#     # more lines

# for num in range(500):  # num -> actual variable to be used in loop body
#     # task
#     print("Good morning", num + 1)


# range(10) -> here 10 is stopping value
# range(1, 10) -> here 1 is starting value and 10 is stopping value
# range(1, 10, 2) -> here 1 is starting value, 10 is stopping value and 2 is step

# for num in range(1, 11, 2):
#     # task
#     print(num)

# num = int(input("Enter a number: "))


# for number in range(1, 11):
#     print(f"{num} x {number} = {num * number}")
# print(num, "  x ", number, " = ", num * number)

# 2, 4, 6, 8, 10
# for num in range(2, 11, 2):
#     print(num)
# for num in range(1, 10, 2):
#     print(num)

# 10 + (-1), 10-1
# for num in range(1, 100):
#     print(num)

# this is not the part of loop body/block


# Infinite loop (while loop)
# value = 1
# while value < 10:
#     # task
#     print(value)
#     value = value + 1

# for times in range(100):
#     if times == 55:
#         break

#     print("Doing up and down", times + 1)


# while True:
#     raining = input("Is it raining? (yes/no) >>> ")

#     if raining.lower() == "yes":
#         print("take an umbrella")
#         break
#     elif raining.lower() == "no":
#         print("don't take an umbrella")
#         break
#     else:
#         print("Please enter correct response")


# while True:
#     raining = input("Is it raining? (yes/no) >>> ")

#     # check if user entered other than 'yes' or 'no'
#     if not (raining.lower() == "yes" or raining.lower() == "no"):
#         print("Please enter correct response")
#         continue  # skip to next iteration/loop

#     # expected output
#     if raining.lower() == "yes":
#         print("take an umbrella")
#     elif raining.lower() == "no":
#         print("don't take an umbrella")

#     break

# print("End of program")

# result = 0
# for n in range(1, 11):
#     print(n)
#     result = result + n

# print("sum of first 10 natural numbers is ", result)
