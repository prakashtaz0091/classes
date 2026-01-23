# indexing
# Negative indexing
#    0  1  2  3  4
# l = [1, 2, 4, 2, 3]
#          -3 -2 -1
# l[0]
# l[-1]

# slicing

# sub_list = l[0:3]
# sub_list = l[-3:]
# sub_list = l[:3]
# print(sub_list)

# enumerate
# users = ["ram", "ramesh", "roshan", "geeta"]

# for user in enumerate(users, start=1):
#     print(user)

# zip
# users = ["ram", "ramesh", "roshan", "geeta"]
# phones = ["98123123", "98123125", "98123126", "981231290"]


# for user_info in zip(users, phones):
#     print(user_info)


# Tuple (immutable/unchangeable/concrete)

# t = (1, 2, 3)
# print(t[0])
# t[0] = 5
# print(t[0])

# dance_list = ["ram", "hari"]

# dance_list.append("roshan")
# dance_list.append("dikshya")

# final_dance_list = tuple(dance_list)

# print(dance_list)
# print(final_dance_list)
# (1  , "ram") -> packing
# for stu_name in enumerate(final_dance_list, start=1):
#     print(stu_name)

# stu_name = "ram"
# number, stu_name = (1, "ram")  # unpacking


# for number, stu_name in enumerate(final_dance_list, start=1):
#     print(number, stu_name)


# days_of_week = ("sunday", "monday", "tuesday")
# Tuple -> List
# List, data change
# changed list -> tuple

# temp_days_of_week = list(days_of_week)

# print(type(days_of_week))
# print(type(temp_days_of_week))

# temp_days_of_week.append("wednesday")
# temp_days_of_week.append("thursday")
# temp_days_of_week.append("friday")
# temp_days_of_week.append("saturday")

# days_of_week = tuple(temp_days_of_week)

# print(days_of_week, type(days_of_week))


# Set (Venn-diagram)
# A well defined collection of objects
# Data repeatation is not allowed, or no duplicate data
# I will not rememberize index/order

# list = []
# tuple = ()
# set = {}
# dict = {}
# tuple(), list(), set()
# s1 = set()

# print(s1, type(s1))
# s1 = {1, 2, 4, 5, 6, 5, 6, 2, 2}

# print(s1)
# dance_list = ["ram", "ram", "geeta", "seeta", "shyam", "seeta"]

# clean_dance_list = set(dance_list)

# print(clean_dance_list)
# for stu_name in clean_dance_list:
#     print(stu_name)


# s1 = {"apple", "ball", "cat"}

# s1.add("dog")
# s1.update(["parrot", "cabbage"])
# # s1.update(("parrot", "cabbage"))
# s1.remove("apple")

# s2 = {"new", "mew"}

# ram_hobbies = {"cycling", "travelling", "coding", "football"}

# hari_hobbies = {"travelling", "singing", "dancing", "football"}

# common_hobbies = ram_hobbies.intersection(hari_hobbies)
# common_hobbies = hari_hobbies.intersection(ram_hobbies)
# common_hobbies = hari_hobbies & ram_hobbies

# print(common_hobbies)

# all_hobbies = ram_hobbies.union(hari_hobbies)
# all_hobbies = ram_hobbies | hari_hobbies

# print(all_hobbies)

# ram_only = ram_hobbies - hari_hobbies
# print(ram_only)
# hari_only = hari_hobbies - ram_hobbies
# print(hari_only)

# sym_diff = ram_hobbies.symmetric_difference(hari_hobbies)
# sym_diff = hari_hobbies.symmetric_difference(ram_hobbies)
# sym_diff = hari_hobbies ^ ram_hobbies

# print("Symmetric differnce", sym_diff)

# Write a program to ask users hobbies and store them

# hobbies = set()

# while True:
#     user_input = input("You hobbies (q to quit) : ")

#     if user_input == "q":
#         break

#     hobbies.add(user_input)


# print("Okay, I have remembered your hobbies:")
# for sn, hobby in enumerate(hobbies, start=1):
#     print(sn, hobby)
