# Advanced concepts

# 1. comprehension (list, set, dict)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
        
        
# print(even_numbers)

# even_numbers = [number for number in numbers if number % 2 == 0]

# print(even_numbers)

# users = [
#     {
#         "name": "Ram", 
#         "email": "ram@gmail.com"
#     },
#     {
#         "name": "hari", 
#         "email": "hari@gmail.com"
#     },
#     {
#         "name": "geeta", 
#         "email": "geeta@gmail.com"
#     },
#     {
#         "name": "saugat", 
#         "email": "saugat@gmail.com"
#     },
#     {
#         "name": "Roshan", 
#         "email": "ram@gmail.com"
#     }
# ]


# send_mail(["ram@gmail.com", "saugat@gmail.com"])

# emails = [user["email"] for user in users]
# emails = {user["email"] for user in users}

# print(emails)

# 2. Higher order functions
# function -> paramters and arguments

# filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

# def odd_filter(x):
#     # if x%2 == 1:
#     #     return True
#     # else:
#     #     return False
#     return x%2 == 1 # 1%2 == 1 => 1 == 1 => True

# print(odd_filter(1))
# print(odd_filter(2))

# odd_numbers = filter(odd_filter, numbers)

# print(odd_numbers)

# odd_numbers_list = list(odd_numbers)

# print(odd_numbers_list)

# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))


# users = [
#     {
#         "name": "Ram", 
#         "email": "ram@gmail.com"
#     },
#     {
#         "name": "hari", 
#         "email": "hari@gmail.com"
#     },
#     {
#         "name": "geeta", 
#         "email": "geeta@gmail.com"
#     },
#     {
#         "name": "saugat", 
#         "email": "saugat@gmail.com"
#     },
#     {
#         "name": "Roshan", 
#         "email": "ram@gmail.com"
#     }
# ]

# def get_email(user):
#     return user["email"]

# emails = map(get_email, users)

# print(set(emails))


# sorted

# numbers = [3, 5, 1, 0, 10]

# numbers.sort()

# print(numbers)

# students = [
#     {
#         "name": "ram", 
#         "total_marks": 345
#     },
#     {
#         "name": "roshan",
#         "total_marks": 500,
#     },
#     {
#         "name": "harry",
#         "total_marks": 150,
#     }
# ]

# def get_total_marks(student):
#     return student["total_marks"]

# print(get_total_marks({
#         "name": "harry",
#         "total_marks": 150,
#     }))

# ranked_list = sorted(students, key=get_total_marks, reverse=True)

# print(ranked_list)

# lambda function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

# odd_numbers = filter(lambda x:x%2 == 1, numbers)

# print(list(odd_numbers))



