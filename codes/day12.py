# Lambda functions
# def add(a,b):
#     return a+b

# add = lambda a, b: a + b
# Notes:
"""
1. lambda function doesn't has it's own name
2. it can have any number of parameter
3. it can only have one return value
4. it should be written in single line
"""


# print(add(3, 4))

# Higher Order Functions
"""
1. If a function receives another function as a parameter
2. If a function returns another function as a return value
3. Can be both 1 and 2 at the same time
"""

# Map, Filter
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# list, tuple, set, dictionary, string
# new_l = list(filter(lambda num: num != 5, l))
#  5:  0 < 5 -> True
# print(new_l)

# users = ["ram", "hari", "sita", "ramesh"]

# new_users = list(filter(lambda str: str != "hari", users))
# print(new_users)


# Map
#      l = [1, 2, 3, 4, 5]
# R => l*2
# new_l  = [2, 4, 6, 8, 10]
# l = [1, 2, 3, 4, 5]

# l_2 = list(map(lambda num: num * 2 -1, l))

# print(l_2)

# def word_len(word):

#     # logics
#     # logics
#     # logics
#     # logics

#     return len(word)

# l = ["apple", "ball", "cat", "dog"]
# l_count = list(map(lambda word: word_len(word), l))

# print(l_count)


# sorted
# l = [1, 2, 3, 5, 6, 4, 7, 8, 9, 0, 23, -56, -12]

# l_sorted = sorted(l)
# print(l_sorted)

# users = ["ram", "shyam", "hari", "sita", "gita"]

# users_sorted = sorted(users, reverse=True)

# print(users_sorted)

# student_percentage = {"ram": 98, "hari": 78, "gita": 90, "sita": 76}

# student_rank_sorted = sorted(student_percentage.items(), key=lambda item: item[1], reverse=True)

# print(dict(student_rank_sorted))

products = [
    {
        "name": "watch",
        "price": 899
    },
    {
        "name": "laptop",
        "price": 89999
    },
    {
        "name": "mobile",
        "price": 9990
    },
    {
        "name": "t-shirt",
        "price": 999
    }
]

products_low_to_high = sorted(products, key=lambda product:product.get("price"))

products_high_to_low = sorted(products, key=lambda product:product.get("price"), reverse=True)

# print(products_low_to_high)
# print(products_high_to_low)


# let's say, send this to mobile app