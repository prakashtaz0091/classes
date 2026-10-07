# logged_in = True

# def login_required(func):
#     def wrapper_func():
#         if logged_in:
#             func()
#         else:
#             print("Please login to access this page")
    
#     return wrapper_func
        


# @login_required
# def home():
#     #1
#     #2
#     # 
#     #3
#     #4
#     #5
    
#     html = "This is homepage"
#     return html


# home()
# print(home())

# @login_required
# def admin():
#     html = "This is admin"
#     return html
# # def home():
# #     html = "This is homepage"
# #     return html

# admin()


# @login_required
# def home():
#     print('Homepage')
    
# home = login_required(home)

# # print(a)
# home()

# Exception Handling

# try:
#     user_input = int(input("Enter a number: "))
# except ValueError:
#     print("Something went wrong")
# else:
#     print(user_input)

# try:
#     # otp verify
#     print("Trying to verify otp")
#     raise Exception("OTP verification failed")
# except Exception:
#     # message
#     print("OTP verification failed, please request a new OTP")
# else:
#     print("OTP verified")


# print("End of program")


# Student.DoesNotExist => 


# Iterator

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     print(num)

# print(nums.__iter__)

# a = 1

# print(a.__iter__)


# nums_iter = iter(nums)
# print(type(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))

# while True:
#     try:
#         num = next(nums_iter)
#     except StopIteration:
#         break
#     else:
#         print(num)


# Generator, range(100000000)
# def crange(stop):
#     start = 0
#     while start < stop:
#         # print(start)
#         yield start
#         start += 1


# crange_gen = crange(10)

# # print(crange_gen.__iter__)

# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))
# print(next(crange_gen))

# print(crange(10))

# with open("passwords.txt", "r") as file:
#     for line in file:
#         print(line)
    # content = file.readlines()
    # print(content)


# students = Student.objects.all()

# for student in students:


