# Decorator
# def decor(func):
#     def wrapper_func():
#         print("This is wrapper func")
#         func()
#         print("This is after actual function call")

#     return wrapper_func


# @decor
# def ex_function():
#     print("This is ex_function")


# ex_function()
import time


# func to calculate, cache data, caching
# def cache(func):
#     results = {}

#     def wrapper(*args, **kwargs):
#         # print(func.__name__)
#         # print(args, kwargs)
#         # make the key for dictionary
#         key = f"{func.__name__}"
#         for arg in args:
#             key = key + f"-{arg}"

#         # check if the key already exist, if so return its value
#         if key in results.keys():
#             print("value found in cache")
#             return results[key]

#         # if key doesn't exist, call the actual func
#         print("value not found in cache, recalculating")
#         result = func(*args, **kwargs)

#         # cache/store the newly calculated result
#         results[key] = result

#         # return the newly calculated result
#         return result

#     return wrapper


# @cache
# def calc(a, b):
#     print("Calculating started...")
#     time.sleep(3)
#     return a + b


# @cache
# def another_calc(x, y, z):
#     print("Another Calculating started...")
#     time.sleep(2)
#     return x - y - z


# # calc(a=4, b=5)
# # print(calc(4, 5))
# # print(calc(4, 5))
# print(another_calc(4, 5, 6))  # calculation hunxa
# print(another_calc(4, 5, 7))  # calculation hunxa
# print(another_calc(4, 5, 6))  # calculation hundaina
loggedin = True
role = "normal"


#
def login_required(func):
    def wrapper(*args, **kwargs):
        if loggedin:
            func(*args, **kwargs)
        else:
            print("You must log in first")

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if role == "admin":
            func(*args, **kwargs)
        else:
            print("You are not authorized to use this page")

    return wrapper


# for eg. /home
def home():
    print("This is home page")


# /admin
@login_required
@admin_required
def admin():
    print("This is admin page")


# /admin/set-password
@login_required
@admin_required
def set_password():
    print("this is password set")


def role_required(roles):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role in roles:
                func(*args, **kwargs)
            else:
                print("You are not authorized to use this page")

        return wrapper

    return decorator


# /checkout
@role_required(["admin", "staff"])
def checkout():
    print("Here are your checkouts")


# @role_required(["admin"])

# home()
# admin()
# set_password()
checkout()
