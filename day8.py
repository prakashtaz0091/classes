# ATM pin max attempt check

# actual_pin = 1234
# counter = 3
# print("You have 3 attempts to login")
# while counter > 0:
#     user_pin = int(input("Enter your pin >>> "))
#     if user_pin == actual_pin:
#         print("Login successful")
#         break
#     else:
#         print("Incorrect pin")
#         counter -= 1
#         print(f"You have {counter} attempts left.")
# else:
#     print(
#         "You have exhausted all attempts. Your account has been locked. Please contact nearest branch"
#     )

# if counter == 0:
#     print(
#         "You have exhausted all attempts. Your account has been locked. Please contact nearest branch"
#     )


# 2. Tuple
# tuple -> immutable -> once created, cannot be changed
# list -> mutable -> can be changed


# students = ["ram", "hari", "sam"]
# final_student_list = tuple(students)

# print(type(students))
# print(type(final_student_list))
# print(students)
# print(final_student_list)

# final_student_list.pop() # wrong
# final_student_list.remove("ram") # wrong
# for student_name in final_student_list:
#     print(student_name)
# students.remove("ram")
# print(students)
# print(final_student_list)
# print(final_student_list[0])
# print(final_student_list[1])
# print(final_student_list[2])


# days_of_week = (
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday",
# )


# def add_nums(*args):
#     print(args)
#     print(type(args))


# add_nums(10, 20, 30, 40, 50)


# def ex():
#     return 5, 6, 7, 8


# result = ex()  # (5, 6, 7, 8) -> tuple
# print(result)
# print(type(result))


# tx = (1, 2)
# tx_l = list(tx)

# a = 10
# b = 6

# a, b = b, a  # (6, 10)

# a, *middles, b = (1, 2, 3, 4)  # Unpacking
# *middles, a, b = (1, 2, 3, 4)  # Unpacking
# a, *middles, b = (1, 2, 3, 4, 5)  # Unpacking

# print(a)
# print(middles)
# print(b)

# slicing
# l = [1, 2, 3, 4, 5, 6, 6]
# # l1 = l[0:3]  # takes sub list from l
# l1 = l[:3]  # takes sub list from l
# # l2 = l[3:6]
# l2 = l[3:]

# print(l1)
# print(l2)


# 3. Set
# set -> collection of unique elements
# set -> unordered # no indexing can be done
# set -> mutable
# set -> unindexed

# list-> [], tuple-> (), set-> {}, dict-{}

# seta = {1, 2, 3}
# print(type(seta))
# seta =  # wrong , this is empty dictionary
# seta = set()  # empty set
# print(type(seta))

# students_list = ["ram", "shyam", "hari", "gita", "ram"]

# cleaned_students_list = set(students_list)
# print(type(cleaned_students_list))
# print(cleaned_students_list)


# ram_interests = {"reading", "writing", "coding"}
# hari_interests = {"reading", "coding", "travelling"}
# ex = {"reading", "travelling", "cooking"}


# common_interests = ram_interests.intersection(hari_interests).intersection(ex)
# common_interests = ram_interests & hari_interests & ex

# print(common_interests)
# all_interests = ram_interests.union(hari_interests)
# all_interests = ram_interests | hari_interests
# print(all_interests)


# ram_only_interests = ram_interests.difference(hari_interests)
# ram_only_interests = ram_interests - hari_interests

# print(ram_only_interests)

# hari_only_interests = hari_interests.difference(ram_interests)
# hari_only_interests = hari_interests - ram_interests

# print(hari_only_interests)

# except_common = ram_interests.symmetric_difference(hari_interests)

# print(except_common)


# Dictionary
# data -> 1 single data -> 2 parts, key and value
# key -> unique
# value -> can be duplicate

# person = {
#     "name": "ram",
#     "age": 20,
#     "phone": "1234567890",
#     "address": "abc",
#     "college": "xyz",
# }

# print(person["name"])
# print(person["age"])
# print(person["college"])
# for detail in person.items():
#     print(type(detail), detail)
# for key, value in person.items():
#     print(key, value)

# print(person.values())
# print(person.keys())
# print(person.items())

# print("address" in person.keys())
# print("ram" in person.values())

# person["age"] = 30
# person["rollno"] = 1

# print(person)
