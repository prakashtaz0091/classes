# Exception Handling

# 1a = 5

# try:
#     user_input = int(input("Enter a number: "))
# except:
#     print("Something went wrong")

# try:
#     user_input = int(input("Enter a number: "))
# except Exception as e:
#     print("Something went wrong", e)


# user_input = int(input("Enter a number: "))
# try:
#     user_input = int(input("Enter a number: "))
# except ValueError: # if user enter wrong value
#     print("Please enter numeric value only, eg. 123")
# except Exception as e: # hanlde any error
#     print("Something went wrong", e)


# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#     except ValueError: # if user enter wrong value
#         print("Please enter numeric value only, eg. 123")
#     except Exception as e: # hanlde any error
#         print("Something went wrong", e)
#     else:
#         break


# print("Something running")
# print("Program ends here")

# students = ["ram", "hari"]
# try:
#     students.remove("hari")
# except ValueError:
#     print("The item you are trying to remove, doesn't exist")
# else:
#     print("Removed successfully")
# finally:
#     print("Student removal program completed")

# try:    
#     with open("new.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File doesn't exist")
#     print("Please check the file name or file path")

# Comprehensions
# marks = ['45', '34', '78', '86']

# int_marks = [int(mark) for mark in marks] # list comprehension
# print(marks)
# print(int_marks)

# total = sum(int_marks)

# print(total)
# if num%2==0 -> num/2 ? remainder 0? if 0, even
# nums = [1,2,3,4,5,6,7,8,9]
# even_numbers = [num for num in nums if num%2 == 0]
# odd_numbers = [num for num in nums if num%2 != 0]
#              
# 1. what to keep in new list?
# 2. where does that come from?
# 3 [opt]. on what condition new value should be kept?

# print(even_numbers)
# print(odd_numbers)

# life_to_emotion = {
#     5: "😊",
#     4: "😃",
#     3: "😐",
#     2: "😔",
#     1: "😢"
# }

# emotion_to_life = {
#     value:key
#     for key, value in life_to_emotion.items()
# }

# print(emotion_to_life)

# nums = [1,2,3,4,5,6,7,8,9,10,11.5]

# result = [f"{num} is Even" if num % 2 == 0 else f"{num} is Odd" for num in nums]

# print(result)


# decorator
# def deco(func):
#     def wrapper_func():
#         print("this is before function")
#         func()
#         print("This is after the function")
    
#     return wrapper_func


# @deco
# def just_func():
#     print("this is just a function")
    
    
# just_func()

# Measure execution time
# import time

# start = time.time()

# # some task
# # for i in range(1000000):
# #     pass
# time.sleep(5)

# end = time.time()
# import time

# def show_execution_time(func):
#     def wrapper_func(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Execution time: ", end-start, " seconds")

#     return wrapper_func


# @show_execution_time
# def heavy_task_func(a, b=0):
#     print("Heavy task start")
#     time.sleep(3.5)
#     print("values are ", a, b)
#     print("Heavy task end")


# @show_execution_time
# def a(a, b, c, d):
#     pass

# heavy_task_func(a=0, b=1)


