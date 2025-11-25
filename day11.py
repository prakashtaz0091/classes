# List comprehension
# [existing list] -> [new_transformed_list]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Normal approach
# sq_nums = []
# for number in numbers:
#     sq_nums.append(number**2)

# List comprehension
# sq_nums = [number**2 for number in numbers]


# Normal approach
# 2 /2 =0
# 4/2 = 0
# 3/2 = 1
# 5/2 = 1
# sq_nums_even = []
# for number in numbers:
#     if number % 2 == 0:  # first check if the number is even
#         sq_nums_even.append(number**2)  # if even, then calculate sq and add to the list

# List comprehension
# sq_nums_even = [number**2 for number in numbers if number % 2 == 0]


# print(sq_nums_even)
#

"""
3/2 = 1.5
3//2 = 1
3 % 2 = 1

2  ) 3 (  1 -> int div
    - 2
    ____
       1


# bitwise operators
011
100
101

"""

# countries = ["india", "Nepal", "China", "Canada"]
# countries_without_c = [country for country in countries if not country.startswith("C")]
# print(countries_without_c)

# num_to_alpha = {
#     1: "a",
#     2: "b",
#     3: "c",
#     4: "d",
#     5: "e",
#     6: "f",
#     7: "g",
#     8: "h",
#     9: "i",
#     10: "j",
# }

# mapping_odd = {key: value for key, value in mapping.items() if key % 2 == 1}

# print(mapping_odd)

# alpha_to_num = {alpha: num for num, alpha in num_to_alpha.items()}

# print(alpha_to_num)


# Exception handling / Error handling
# try:
#     age = int(input("Enter your age: "))
#     print(Age)  # which is not defined
# except ValueError:
#     print("Please provides number as input, not something else.")
# except NameError:
#     print("The value you want to print is never set")
# except Exception:
#     print("Something went wrong")
# else:
#     print(age, " is your current age.")

# # further codes
# print("Program ended successfully")


# while True:
#     try:
#         # resources
#         age = int(input("Enter your age: "))
#     except ValueError as e:
#         print("default error message", e)
#         print("Please enter correct number")
#     except Exception:
#         print("Something went wrong ! Please try again later")
#     else:
#         print(f"So, you are {age} years old!")
#         break
#     finally:
#         # cleanup
#         print("Finally")


# def add(a, b):
#     raise Exception("Addition not possible")
#     return a + b


# try:
#     add(3, 4)
# except Exception as er_msg:
#     print(er_msg)

# File Hanlding
# variables -> data -> RAM -> program end -> data clear
# variables -> data -> RAM -> HDD, SSD -> file handling

# text file handling
# notebook -> read/write
# first open -> do things -> close the file
# text_file = open("demo.txt", "r")
# # print(text_file.read())
# print(text_file.readlines())

# text_file.close()

# with open("demo.txt", "r") as text_file:
#     print(text_file.read())
# do necessary things
# end

# csv
# binary files
