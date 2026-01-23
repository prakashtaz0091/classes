# Data structures

# List, Tuple, Set
# Dictionary
# user_info = ["Ram Thapa", "9800000000", "9800000090", "kathmandu", 35]

# user_info[0]
# user_info[1]
# user_info = {
#     "name": "Ram Thapa",
#     "phone": "9800000000",
#     "workplace_no": "9800000090",
#     "address": "kathmandu",
#     "age": 35,
# }
# ex = {
#     1: "one",
#     2: "two",
#     3: "three",
#     (12, 3): "Collection of 12 and 3",
#     3.5: "done"
# }

# emotions = {
#     5: "😄",
#     4: "😊",
#     3: "😔",
#     2: "😢",
#     1: "😭"
# }

# life = int(input("What's the life remaining: "))
# print(emotions.get(life))



# key=> Immutable data => string, numbers (int, float), tuple

# print(user_info["name"])
# print(user_info["phone2"])

# print(user_info.get("name"))
# print(user_info.get("phone"))
# print(user_info.get("phone2"))

# if user_info.get("phone2") is not None:
#     print("Yes phone2 exists")
# else:
#     print("There is no any information called phone2")

# print(user_info.get("phone2"))
# print(user_info.get("phone2", 9800000000))

# user_info["phone2"] = "9823458682"
# user_info["phone"] = "9823458682"

# print(user_info)

# print("phone" in user_info.keys())
# print("phone2" in user_info.keys())

# if "phone2" not in user_info.keys():
#     user_info["phone2"] = "98234234234"

# Write a program to ask user infos one at a time and store it

# user_info = {}

# while True:
#     # ask user to input new key or q to quit the program
#     user_input = input("Key? (q for quit) : ")

#     # if user inputs 'q' then break the loop
#     if user_input == "q":
#         break

#     # check if new key doesn't exist then add it to dict
#     if user_input not in user_info.keys():
#         new_value = input("Value? : ")
#         user_info[user_input] = new_value
#     else:  # if new key already exists, show a message
#         print("That key already exist, please enter new one")


# print("Entered infos are")
# print(user_info)

# user_info = {
#     "name": "Ram Thapa",
#     "phone": "9800000000",
#     "workplace_no": "9800000090",
#     "address": "kathmandu",
#     "age": 35,
# }
# print(user_info.values())

# print(user_info.items())

# for item in user_info.items():
#     print(item)

# for key, value in user_info.items():
#     print(key, value)

# deleted_info = user_info.pop("name")
# deleted_info = user_info.popitem()

# print(deleted_info)

# print(user_info)


# user_info = {
#     "name": "Ram Thapa",
#     "phone": "9800000000",
#     "workplace_no": "9800000090",
#     "age": 35,
#     "hobbies": ["cycling", "reading", "writing"],
#     "address": {
#         "parmanent": "kathmandu",
#         "temporary": {
#             "city": "hetauda",
#             "ward no": 12,
#             "street name": "Bhanubhakta chowk",
#             "postal code": 52300,
#         },
#     },
# }

# address = user_info.get("address")
# print(address["temporary"]["city"])
# print(address.get("temporary").get("city"))


# products = [
#     {"name": "Smart watch", "price": 3500},
#     {"name": "Washing machine", "price": 35000},
#     {"name": "Hair dryer", "price": 500},
#     {"name": "Frying pan", "price": 3500},
#     {"name": "Smart watch", "price": 3500},
#     {"name": "Smart watch", "price": 3500},
#     {"name": "Smart watch", "price": 3500},
# ]

# phones = [
#     {
#         "name": "Samsung",
#         "price": 12000,
#         "cpu": "snapdragon",
#         "ram": 12,
#         "rom": 512,
#         "battery capacity": 5400,
#     },
#     {
#         "name": "Samsung",
#         "price": 12000,
#         "cpu": "snapdragon",
#         "ram": 12,
#         "rom": 512,
#         "battery capacity": 5400,
#     },
#     {
#         "name": "Samsung",
#         "price": 12000,
#         "cpu": "snapdragon",
#         "ram": 12,
#         "rom": 512,
#         "battery capacity": 5400,
#     },
#     {
#         "name": "Samsung",
#         "price": 12000,
#         "cpu": "snapdragon",
#         "ram": 12,
#         "rom": 512,
#         "battery capacity": 5400,
#     },
# ]


# {
#     "products": [
#         {
#             "id": 1,
#             "title": "Essence Mascara Lash Princess",
#             "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
#             "category": "beauty",
#             "price": 9.99,
#             "discountPercentage": 7.17,
#             "rating": 4.94,
#             "stock": 5,
#             "tags": ["beauty", "mascara"],
#             "brand": "Essence",
#             "sku": "RCH45Q1A",
#             "weight": 2,
#             "dimensions": {"width": 23.17, "height": 14.43, "depth": 28.01},
#             "warrantyInformation": "1 month warranty",
#             "shippingInformation": "Ships in 1 month",
#             "availabilityStatus": "Low Stock",
#             "reviews": [
#                 {
#                     "rating": 2,
#                     "comment": "Very unhappy with my purchase!",
#                     "date": "2024-05-23T08:56:21.618Z",
#                     "reviewerName": "John Doe",
#                     "reviewerEmail": "john.doe@x.dummyjson.com",
#                 },
#                 {
#                     "rating": 2,
#                     "comment": "Not as described!",
#                     "date": "2024-05-23T08:56:21.618Z",
#                     "reviewerName": "Nolan Gonzalez",
#                     "reviewerEmail": "nolan.gonzalez@x.dummyjson.com",
#                 },
#                 {
#                     "rating": 5,
#                     "comment": "Very satisfied!",
#                     "date": "2024-05-23T08:56:21.618Z",
#                     "reviewerName": "Scarlett Wright",
#                     "reviewerEmail": "scarlett.wright@x.dummyjson.com",
#                 },
#             ],
#             "returnPolicy": "30 days return policy",
#             "minimumOrderQuantity": 24,
#             "meta": {
#                 "createdAt": "2024-05-23T08:56:21.618Z",
#                 "updatedAt": "2024-05-23T08:56:21.618Z",
#                 "barcode": "9164035109868",
#                 "qrCode": "...",
#             },
#             "thumbnail": "...",
#             "images": ["...", "...", "..."],
#         },
#         {
#             "id": 1,
#             "title": "Essence Mascara Lash Princess",
#             "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
#             "category": "beauty",
#             "price": 9.99,
#             "discountPercentage": 7.17,
#             "rating": 4.94,
#             "stock": 5,
#             "tags": ["beauty", "mascara"],
#             "brand": "Essence",
#             "sku": "RCH45Q1A",
#             "weight": 2,
#             "dimensions": {"width": 23.17, "height": 14.43, "depth": 28.01},
#             "warrantyInformation": "1 month warranty",
#             "shippingInformation": "Ships in 1 month",
#             "availabilityStatus": "Low Stock",
#             "reviews": [
#                 {
#                     "rating": 2,
#                     "comment": "Very unhappy with my purchase!",
#                     "date": "2024-05-23T08:56:21.618Z",
#                     "reviewerName": "John Doe",
#                     "reviewerEmail": "john.doe@x.dummyjson.com",
#                 },
#                 {
#                     "rating": 2,
#                     "comment": "Not as described!",
#                     "date": "2024-05-23T08:56:21.618Z",
#                     "reviewerName": "Nolan Gonzalez",
#                     "reviewerEmail": "nolan.gonzalez@x.dummyjson.com",
#                 },
#                 {
#                     "rating": 5,
#                     "comment": "Very satisfied!",
#                     "date": "2024-05-23T08:56:21.618Z",
#                     "reviewerName": "Scarlett Wright",
#                     "reviewerEmail": "scarlett.wright@x.dummyjson.com",
#                 },
#             ],
#             "returnPolicy": "30 days return policy",
#             "minimumOrderQuantity": 24,
#             "meta": {
#                 "createdAt": "2024-05-23T08:56:21.618Z",
#                 "updatedAt": "2024-05-23T08:56:21.618Z",
#                 "barcode": "9164035109868",
#                 "qrCode": "...",
#             },
#             "thumbnail": "...",
#             "images": ["...", "...", "..."],
#         },
#     ],
#     "total": 194,
#     "skip": 0,
#     "limit": 30,
# }

# chauchau_box = ("chauchau1", "chauchau2", "chauchau3", "chauchau4")

# ram, shyam, hari, geeta = chauchau_box
# ram, *geeta = chauchau_box
# *ram, geeta = chauchau_box

# ram, *hari, geeta = chauchau_box

# print("ram got", ram)
# # print(shyam)
# # print(hari)
# print("geeta got ", geeta)
