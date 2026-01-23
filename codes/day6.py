# Count how many vowels exist in a given string.
# • Hint: Loop through each character.
# • Use if ch in "aeiouAEIOU".  sir yo question solve gardinu na

# VOWELS = "aeiouAEIOU"
# user_input = input("Enter a string: ")
# counter = 0
# found_vowels = ""
# # "prakash" + "Tajpuriya" => "prakashTajpuriya"
# for ch in user_input:
#     if ch in VOWELS:
#         counter = counter + 1
# print("Vowel found : ", ch)
# found_vowels = found_vowels + ch


# print("vowel", ch)
# print("Found vowels, ", found_vowels)


# print("The number of vowels in given string : ", counter)
# print("vowels present in the given string are ", found_vowels)


# Data structures
# List, Tuple, Set, Dictionary

# 1. List (mutable)

# l = [1, 2, 3]
# user = ["ram", "shyam", "seeta", "geeta"]

# jpt = [1, "ram", 1.5, None, True]

# dance_list = ["ram", "hari", "ramesh", "seeta", "geeta", "shrawan", "avisekh"]
#               0      1       2         3         4

# print(dance_list[0])
# print(dance_list[1])
# print(dance_list[2])
# print(dance_list[3])
# print(dance_list[4])

# for index in range(5):
#     print(dance_list[index])

# print(len(dance_list))
# for index in range(len(dance_list)):
#     print(dance_list[index])

# for stu_name in dance_list:
#     print(stu_name)


# dance_list = ["ram", "hari"]

# dance_list[0] = "Ram"
# print(dance_list)
# dance_list.append("geeta")
# dance_list.append("shrawan")

# print(dance_list[0], dance_list[1], sep="-----")
# print(dance_list[0], end=" -- ")
# print(dance_list[1])

# dance_list = ["ram", "hari"]

# dance_list.pop()
# dance_list.pop(10)

# dance_list.insert(0, "ramesh")

# dance_list.remove("ramesh")

# print(dance_list)

# students = []

# s1 = input("1st student: ")
# s2 = input("2nd student: ")

# students.append(s1.capitalize())
# students.append(s2.capitalize())

# print(students)


# dance_list = ["ram", "hari"]

# print("this is name list, ", dance_list)

# user_input = input("Which name do you want to rename: ")

# i = dance_list.index(user_input)

# new_name = input("Write new name: ")
# dance_list[i] = new_name

# print(dance_list)


# i = dance_list.index("Ram")
# print(i)
