# numbers = [100,101, 99,20]

"""
Problem: Find the second_largest among items in list, without sorting them
Algorithm: Step by step solution to a problem

1. set first item as largest as well as second_largest
2. Loop through all them items in list, let item be called as num
3. compare if num greater than current largest, set second_largest = largest and largest = num, otherwise go to step 4
4. compare if num is greater than second_largest, set second_largest = num
5. Repeat step 3 and 4 until loop ends
6. Show largest and second_largest
"""


# largest = numbers[0]  #101
# second_largest = numbers[1] #102

# for num in numbers: 
#     #  101   102
#     if num > largest: # set if greater than current largest
#         second_largest = largest
#         largest = num
        
#     #    101 > 102
#     # elif num > second_largest and num != largest: # set second_largest
#     #     second_largest = num
#     elif num > second_largest or second_largest == largest: # set second_largest
#         second_largest = num


# if largest > second_largest:
#     print("Second largest: ", second_largest)
# else:
#     print("Second largest: ", largest)
       

# print("Largest: ", largest)
# print("Second largest: ", second_largest)


# list = [1,2,3,4,6]
# list[-2]


# SET
# Collection of data, unique, unordered

# ram_hobbies = {} # wrong , this is considered as dict
# ram_hobbies = set()
# ram_hobbies = {"cycling", "reading", "writing", "football", "reading"}
#                  0         1   
# Note: set doesn't support indexing, because it's unordered, means, items don't stay in same position
# print(type(ram_hobbies))

# ram_hobbies = {"cycling", "reading", "writing", "football", "reading"}
# hari_hobbies = {"cycling", "adventure trip", "cricket", "writing"}

# print(ram_hobbies)

# commons = ram_hobbies.intersection(hari_hobbies)
# commons2 = hari_hobbies.intersection(ram_hobbies)
# print(commons2)

# commons = ram_hobbies & hari_hobbies

# print(commons)

# all_hobbies = ram_hobbies.union(hari_hobbies)
# all_hobbies = ram_hobbies | hari_hobbies

# print(all_hobbies)

# set difference
# ram_only_hobbies = ram_hobbies.difference(hari_hobbies)
# ram_only_hobbies = ram_hobbies - hari_hobbies  # A - B
# hari_only_hobbies = hari_hobbies - ram_hobbies  # B - A

# print(hari_only_hobbies)

# symmetric set difference

# sym_diff = ram_hobbies.symmetric_difference(hari_hobbies)
# sym_diff = ram_hobbies ^ hari_hobbies

# print(sym_diff)

# add data


# ram_hobbies = {"cycling", "reading", "writing", "football", "reading"}

# ram_hobbies.add("rafting")

# # ram_hobbies.remove("cycling")
# # ram_hobbies.remove("cycling")

# # ram_hobbies.discard("swimming")
# ram_hobbies.update(["swmming", "dancing"])


# print(ram_hobbies)

# Dictionary, (collection key,value pairs)
# person_info = {
#     "name":"ram",
#     "age": 23,
#     "hobbies": {"cycling", "reading", "writing", "football", "reading"},
#     "address": "Jhapa",
# }

# print(person_info)
# print(person_info["address"])
# print(person_info["hobbies"])


# print(person_info.keys())
# print(person_info.values())
# result = "name" in person_info.keys()
# print("name", 5)
# print("name" in person_info.keys())

# print(person_info["adddress"])
# print(person_info.get("adddress", "No value found"))

# print(person_info.items())
# for item in person_info.items():
#     print(item)

# for key, value in person_info.items():
#     print(key, value)

# person_info["salary"] = "1200000"
# person_info["address"] = "KTM"

# person_info.pop("address")
# person_info.popitem()

# del person_info["address"]

# print(person_info)
# Note: keys in dict can be any immutable data types
# person_info = {
#     "name":"ram",
#     "age": 23,
#     "hobbies": {"cycling", "reading", "writing", "football", "reading"},
#     "address": {
#         "permanent": "ktm",
#         "temporary": {
#             "city": "biratnagar",
#             "street": "st_10001",
#             "landmark": "Himal Chowk"
#         }
#     }
# }


# user_addresses = {
#     "count": 2,
#     "results": [
#         {
#             "id": "44CF56D160B74ECB2E88015A30AEBCBEB5C32D077F1E1FF31E90239094EC6220",
#             "tenant": "8211E664A69C354AA43A154B1B56186D4BB6FDA9AD1B61AD3C5621F6EB228026",
#             "add_type": "C9481FE978C549D8F6DA50BAA9011F2BF8020E21FD0F8B4A800737343AC4D64F",
#             "address_line": "97F7+8CC, Tirakharda, Bihar 854328, India",
#             "pincode": "854328",
#             "to_name": "Prakash",
#             "contact_num": "9824946516",
#             "city": "Tirakharda",
#             "state": "Bihar",
#             "country": "8089363FD88E1367076D697CA8D2E9CF4E47B7124DD2A1B75D371F8537EFBBD5",
#             "landmark": "new new",
#             "is_default": 1,
#             "alt_num": "9824946516",
#             "latitude": "26.3733403",
#             "longitude": "87.2635331",
#             "country_name": "India",
#             "add_type_name": "Office"
#         },
#         {
#             "id": "1963BE6D8AA4D05B1D2542476A3958D194E58CE003005D01D48E594674F4A7C9",
#             "tenant": "8211E664A69C354AA43A154B1B56186D4BB6FDA9AD1B61AD3C5621F6EB228026",
#             "add_type": "4CBB5E3F547C9A5AE9C349415127A23C9AFD186840ACEFC4A1F0E847EA5E135A",
#             "address_line": "H.No. 12, Block B, 3rd floor",
#             "pincode": "122001",
#             "to_name": "new address",
#             "contact_num": "9824946516",
#             "city": "Gurugram",
#             "state": "Haryana",
#             "country": "8089363FD88E1367076D697CA8D2E9CF4E47B7124DD2A1B75D371F8537EFBBD5",
#             "landmark": "Sector 4",
#             "is_default": 0,
#             "alt_num": "",
#             "latitude": None,
#             "longitude": None,
#             "country_name": "India",
#             "add_type_name": "Other"
#         }
#     ]
# }


# print(user_addresses["results"][0]["pincode"])