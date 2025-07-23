# def test_decor(func):  # decorator function
#     def wrapper_func():
#         print("This is before test function")
#         func()
#         print("This is after test function")

#     return wrapper_func


# @test_decor
# def test():
#     print("This is test function")


# test()


# def admin_required(func):
#     def wrapper(*args, **kwargs):
#         user_role = "staff"
#         if user_role == "admin":
#             func(*args, **kwargs)
#         else:
#             print("You are not authorized to view this page")
#             home_view()

#     return wrapper


# def login_required(func):
#     def wrapper(*args, **kwargs):
#         user_logged_in = True
#         if user_logged_in:
#             func(*args, **kwargs)
#         else:
#             login_view()

#     return wrapper


# @login_required
# def home_view():
#     print("this is home page")


# @login_required
# @admin_required
# def admin_view():
#     print("this is admin page")


# def login_view():
#     print("This is login page")


# # eg: https://domain-name.com/home/
# # home_view()

# # eg: https://domain/admin/
# admin_view()
# import time
# import csv


# def execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         time_taken = end_time - start_time
#         print(f"{func.__name__} took {time_taken} seconds ")

#     return wrapper


# def execution_time(accurate=False):
#     def execution_time_wrapper(func):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             func(*args, **kwargs)
#             end_time = time.time()
#             time_taken = end_time - start_time
#             if accurate:
#                 print(f"{func.__name__} took {time_taken} seconds ")
#             else:
#                 print(f"{func.__name__} took {time_taken:.2f} seconds ")

#         return wrapper

#     return execution_time_wrapper


# @execution_time
# def tc_task():
#     time.sleep(5)
#     print("Task is completed")


# @execution_time(accurate=False)
# def read_students():
#     time.sleep(4)
#     with open("students.csv", "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)


# # tc_task()
# read_students()


# Generator
# def test_gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6


# gen_obj = test_gen()

# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# # print(next(gen_obj))
# for value in gen_obj:
#     print(value)


# def inf_even_num_gen():
#     even = 2
#     while True:
#         yield even  # pause
#         even = even + 2


# even_number = inf_even_num_gen()

# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))
# # print(next(even_number))

# for _ in range(1000):
#     print(next(even_number))


# def password_gen(filename):
#     with open(filename, "r") as file:
#         for line in file:
#             yield line.strip()


# password = password_gen("passwords.txt")

# # print(next(password))
# # print(next(password))
# # print(next(password))
# pass_to_crack = "admin1234"
# while True:
#     try:
#         p = next(password)
#         if p == pass_to_crack:
#             print(f"Cracked !!! password is {p}")
#             break
#     except StopIteration:
#         print("Dictionary scan completed, password not cracked")
#         break


# Lamda function (anon-function, one-liner function, any no. of args but can return only one value)
# def test(a, b):
#     return a + b

# test = lambda a, b: (a + b, a - b)
# const asdf = ()=>asd
# print(test(5, 6))

# Filter (higher order function)
# numbers = [1, 2, 3, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print(odd_numbers)
# print(even_numbers)

# Map
# a = [1, 2, 3]
# b = list(map(lambda x: x**2, a))

# print(b)


# a = [1, 2, 3]  # roll no.s
# b = ["ram", "hari", "shyam"]  # student names

# for rollno, name in zip(a, b):
#     print(rollno, name)


# comprehensions
# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2 = [num**2 for num in l1]
# l2 = [num for num in l1 if num % 2 == 1]

# print(l2)

d1 = {"name": "ram", "roll_no": 20, "address": "ktm"}

# # d2 = {key: value for key, value in d1.items() if len(key) > 6}
# d2 = {value: key for key, value in d1.items()}

# print(d2)

# gen = (num for num in range(2))
# print(gen)

d1_sorted = sorted(d1, key=lambda item: item[0])
print(d1_sorted)
