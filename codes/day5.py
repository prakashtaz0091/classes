# final_participants = ("ram", "hari", "geeta")

# final_participants.append("roshan")
# print(type(final_participants))

# order status -> received/packed/in-transit/reached-destination/delivered
# variable -> which can be changed
# constant -> which are not meant to be change
# const a = 5;

# ORDER_STATUS_CHOICES = (
#     "received",
#     "accepted", 
#     "packed",
#     "in-transit",
#     "reached-destination",
#     "delivered"
# )

# ORDER_STATUS_CHOICES = 0

# print(ORDER_STATUS_CHOICES)

# print(ORDER_STATUS_CHOICES[0])
# print(ORDER_STATUS_CHOICES[1])

# for status in ORDER_STATUS_CHOICES:
#     print(status)

# Set Data structure
# list []
# tuple ()
# set {}
# ram_hobbies = {"reading", "writing", "football", "cricket", "coding", "football"}
# hari_hobbies = {"football", "coding", "singing", "travelling"}

# print(ram_hobbies)


# common = ram_hobbies.intersection(hari_hobbies)
# common = hari_hobbies.intersection(ram_hobbies)
# common = hari_hobbies & ram_hobbies

# print(common)

# all_hobbies = ram_hobbies.union(hari_hobbies)
# all_hobbies = ram_hobbies | hari_hobbies
# print(all_hobbies)

# ram_only = ram_hobbies.difference(hari_hobbies)
# hari_only = hari_hobbies.difference(ram_hobbies)
# hari_only = hari_hobbies - ram_hobbies

# print(ram_only)
# print(hari_only)

# class_8 = {"vedetar", "tinjure", "pokhara"}
# class_9 = {"shree antu", "damauli", "ABC", "pokhara"}
# class_10 = {"chitwan", "Rara", "Api", "pokhara"}

# common = class_8 & class_9 & class_10
# print(common)

# Dictionary, key-value pairs
# oxford_dict = {
#     "abc": "this is abc meaning", 
#     "bcd": "this is binary coded decimal",
#     "oct": "this is in short octal number system"
# }

# user_input = input("Keyword: ")

# if user_input in oxford_dict.keys(): # False
#     print(oxford_dict[user_input])
# else:
#     print("Sorry, the keyword you are trying to look for, doesn't exist")

# print("Program end")

# products = [
#     {
#         "name": "Mobile Phone", 
#         "price": 34000,
#         "ram": 12,
#         "rom": 256,
#         "battery-capacity": "8000 mAh"
#     },
#     {
#         "name": "Mobile Phone", 
#         "price": 34000,
#         "ram": 12,
#         "rom": 256,
#         "battery-capacity": "8000 mAh"
#     },
#     {
#         "name": "Mobile Phone", 
#         "price": 34000,
#         "ram": 12,
#         "rom": 256,
#         "battery-capacity": "8000 mAh"
#     },
#     {
#         "name": "Mobile Phone", 
#         "price": 34000,
#         "ram": 12,
#         "rom": 256,
#         "battery-capacity": "8000 mAh"
#     },
# ]

# cache
# operation -> 10s
# operation -> 10s
# operation -> 10s

# cache = {
#     "qsn1": 29,
#     "qsn2": 56,
# }
# cache["qsn3"] = 78

# while True:
#     user_input = input("Which qsn? ")

#     if user_input in cache.keys():
#         print(cache[user_input])
#     else:
#         # simulate 10s operation
#         print("Starting calculation")
#         ans = 78
#         cache[user_input] = ans
#         print("Calculation complted and ans cached")
#         print(ans)

# dict_ex = {
#     1: "One",
#     2: "Two",
#     3: "Three" 
# }

# dict_ex.pop(1)
# dict_ex.popitem()
# print(dict_ex)

# student = {
#     "name": {
#         "first_name": "Prakash", 
#         "last_name": "Tajpuriya"
#     },
#     "address": {
#         "temporary": {
#           "landmark": "Something chowk",
#           "pincode": 2384234,
#           "street": "alsdkfj",
#           "house_no": 1212  
#         },
#         "parmanent":{
#           "landmark": "Something chowk",
#           "pincode": 2384234,
#           "street": "alsdkfj",
#           "house_no": 1212  
#         },
#     },
#     "education": [
#         {
#             "level": "SEE",
#             "core_subject": ["Math", "Science"],
#             "institution": {
#                 "name": "ABC school",
#                 "address": "Kathmandu"
#             },
#             "score": "A"
#         },
#         {
#             "level": "+2",
#             "core_subject": ["Math", "Science"],
#             "institution": {
#                 "name": "XYZ school",
#                 "address": "Kathmandu"
#             },
#             "score": "B"
#         },
#         {
#             "level": "Bachelors",
#             "core_subject": ["computer science"],
#             "institution": {
#                 "name": "QWE school",
#                 "address": "Kathmandu"
#             },
#             "score": "B+"
#         },
#     ] 
# }


# print(student["education"][0])
# print(student["education"][1])
# print(student["education"][2]["institution"])

# Mutable
# Immutable

