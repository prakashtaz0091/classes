# name1 = "ram"
# name2 = "shyam"
# name3 = "hari"

# Data Structures (collection of data but in an organized manner)
# 1. List (items can be of any data type)
#   - add item
#   - remove or delete item
#   - modify existing item
#   - insert item in specific index

# index    0      1       2
# names = ["ram", "shyam", "hari"]
# print(names)

# names.append("seeta")  # adds item to end of list
# names.remove("am")  # removes item by value

# removes item by index (index simply means position, but remember count starts from 0)
# removed_name = names.pop(0)
# removed_name = names.pop(5)
# print("Removed name is ", removed_name)
# del names[5]

# names[1] = "SHYAM"
# names.insert(1, "seeta")

# print(names)

# names = ["ram", "shyam", "hari"]

# for name in names:
#     print(f"{name} is a good student")


# # prints multiplication table for 1 number
# for multiple in range(1, 11):
#     print(f"5 x {multiple} = {5 * multiple}")


# tables = []
# while True:
#     user_input = int(input("Table for ?? (0 for done): "))

#     # check if user has input 0
#     if user_input == 0:
#         print("Okay, generating the tables....")
#         break  # break the while loop

#     tables.append(user_input)
#     print("Noted: ", tables)


# for number in tables:
#     print("#######################################")
#     # prints multiplication table for 1 number
#     for multiple in range(1, 11):
#         print(f"{number} x {multiple} = {number * multiple}")

#     print("#######################################")


# 2. Tuple (collection of items, but it's immutable)
# Immutable means, cannot be mutated, in simpler terms
# Once we create the collection we can't modify it

# final_namelist = ("ram", "shyam", "hari")
# final_namelist.append("seeta") # wrong
# final_namelist[0] = "RAM" # wrong
# final_namelist[5]
# print(final_namelist[0], final_namelist[1])


# final_namelist = ("ram", "shyam", "hari")
# final_namelist_temp = list(final_namelist)

# print("final_namelist type", type(final_namelist))

# final_namelist_temp.append("seeta")

# final_namelist = tuple(final_namelist_temp)
# # print("Temp", type(final_namelist_temp))

# print(final_namelist)

# 3. Set (it doesn't stores duplicates, it doesn't remember order of items)
# namelist = ["ram", "ram", "hari"]
# print(namelist)

# # namelist_set = {"ram", "ram"}
# namelist_set = set(namelist)

# print(namelist_set)

# set_a = {1, 2, 4, 5, 6}
# set_b = {2, 3, 5, 7}

# commons = set_a.intersection(set_b)

# print(commons)


# dance_list = ["ram", "hari", "seeta", "geeta"]
# singing_list = ["ram", "geeta", "ramesh", "roshan"]

# both = set(dance_list).intersection(set(singing_list))
# both = set(dance_list) & set(singing_list)

# all_participants = set(dance_list).union(set(singing_list))
# all_participants = set(dance_list) | set(singing_list)

# dance_only = set(dance_list) - set(singing_list)
# singing_only = set(singing_list) - set(dance_list)

# participants_in_one = all_participants - both
# participants_in_one = set(dance_list).symmetric_difference(set(singing_list))
# participants_in_one = set(dance_list) ^ set(singing_list)

# print(participants_in_one)


# set_a = {1, 2, 4}

# set_a.add(5)
# set_a.remove(1)

# print(set_a)


# 4. Dictionary (key, value pair)
# word -> meaning
# another_word -> meaning

# person1 = {
#     "name": ["ram", "kumar", "thapa"],
#     "address": {
#         "temporary": "Kathmandu",
#         "permanent": {
#             "postal_code": 52700,
#             "place_name": "Chandani Chowk",
#             "house_no": 50,
#             "coordinates": {"lat": 23.456767, "long": 45.23423},
#         },
#     },
#     "phone": "980000000",
#     "occupation": "developer",
# }


# print(person1["address"]["permanent"]["coordinates"]["lat"])
# print(person1["address"]["permanent"]["coordinates"]["long"])

# print(person1["name"])
# print(person1["address"])
# print(person1["phone"])
# print(person1["occupation"])

# person1["roll_no"] = 1
# person1["address"] = "Pokhara"

# print(person1["roll_no"])
# print(person1)


# print(person1.keys())
# print(person1.values())
# print(person1.items())

# print("name" in person1.keys())
# print("kathmandu" in person1.values())

# for key, value in person1.items():
#     # print(item)
#     print(key)
#     print(value)
