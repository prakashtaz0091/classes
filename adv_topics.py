# nums_list = [1, 2, 3, 4, 5]

# squares = [1, 4, 9, 16, 25]
# for num in nums_list:
#     squares.append(num**2)

# squares = [num**2 for num in nums_list]  # list comprehension


# squares = set()
# for num in nums_list:
#     squares.add(num**2)
# print(squares)

# squares_set = {num**2 for num in nums_list}

# {1, 4, 9, 16, 25}
# {1: 1, 2: 4, 3: 9, 4: 16}
# num_squares = {}
# for num in nums_list:
#     num_squares[num] = num**2

# print(num_squares)

# num_squares = {num: num**2 for num in nums_list}
# print(num_squares)

# squares = [num**2 for num in nums_list if num > 2]  # list comprehension
# print(squares)


# Lambda functions
# def square(x): # basic/normal function
#     return x**2

# square = lambda x: x**2

# print(square(5))

# Higher order functions
# function as an argument -> int, string, list, tuple, set, dict

# kunai (any ) function-> function as an argument or return value


# def add(a, b):
#     return a + b
# all_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# even_nums = list(filter(lambda num: num % 2 == 0, all_nums))
# print(even_nums)

# odd_nums = list(filter(lambda num: num % 2 == 1, all_nums))
# print(odd_nums)

# squares_all_nums = list(map(lambda num: num**2, all_nums))
# print(squares_all_nums)


# Decorator
# def decorator_daju(gift):
#     def wrapped_gift():
#         print("Before function call")
#         gift()
#         print("After function call")

#     return wrapped_gift


# @decorator_daju
# def say_hello():
#     print("Hello!")


# say_hello()


# def run_twice(func):
#     def wrapper():
#         func()
#         func()

#     return wrapper


# @run_twice
# def say_hello():
#     print("Hello!")


# # say_hello()


# # @run_twice
# def say_hi():
#     print("Hi!")


# say_hi()

# from custom_package.helpers import log_execution_time


# @log_execution_time
# def say_hello():
#     # time.sleep(2)
#     print("Hello!")


# say_hello()


# numbers = [1, 2, 3, 4]
# def numbers():
#     return 1, 2, 3, 4


# print(numbers())


# def my_gen():
#     yield 4
#     yield 3
#     yield 2
#     yield 1


# number = my_gen()

# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))

# for val in my_gen():
#     print(val)


# def my_gen():
#     while True:
#         yield 1  # gives 1 and pause


# number = my_gen()

# for _ in range(1000):
#     print(next(number))


# def even_number_generator():
#     first_even = 2
#     while True:
#         yield first_even
#         first_even += 2


# even_number = even_number_generator()

# for _ in range(1000):
#     print(next(even_number))


# def primes_generator():
#     """Infinite prime number generator (yields 2,3,5,7,11,...)."""
#     primes = []  # discovered primes for trial-division
#     candidate = 2
#     while True:
#         is_prime = True
#         # only test divisors up to sqrt(candidate)
#         limit = int(candidate**0.5) + 1
#         for p in primes:
#             if p > limit:
#                 break
#             if candidate % p == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(candidate)
#             yield candidate
#         candidate += 1 if candidate == 2 else 2  # skip even numbers after 2


# prime_number = primes_generator()

# for _ in range(1000):
#     print(next(prime_number))


# file = open("new.txt", "r")
# print(type(file))
# print(hasattr(file, "__iter__"))
# for line in file:
#     print(line)
