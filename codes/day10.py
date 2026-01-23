# function to add two numbers
# def add(num1, num2): # Function defination
#     print(num1+num2)


# add(3, 4) # Function call


# def add(num1, num2, num3): # Function defination
#     print(num1+num2+num3)


# add(3, 4, 5) # Function call

# def add(num1, num2, num3, num4): # Function defination
#     print(num1+num2+num3+num4)


# add(3, 4, 5) # Function call


# def add(*args): # * means, any, args means arguments
#     print(args)


# add(2, 3, 4) # Function call


# def add(*numbers): # * means, any, numbers means arguments
#     result = 0
#     #    3      (2, 3, 4) 
#     for num in numbers:
#         result = result + num
#         # result = 5
    
#     print(result)

# add(2, 3, 40, 577) # Function call

# print(sum((999999999, 7777, 3)))


# Positional Argument , welcome_user("hi", "Ram")
# Keyword argument, welcome_user(greeting="hi", name="Ram")

# def add(*numbers): # Any no of arguments (args)
#     print(numbers)


# add(1, 2)
# add(a = 1, b = 3)

# def show_user_info(name, age, phone, address, gender):
#     print(name)
#     print(age)
#     print(phone)
#     print(address)
#     print(gender)
    
    
# show_user_info(name="ram", age=34, phone="98000", address="ktm", gender="Male")
# show_user_info(name="ram", age=34)

# Problem: Above example shows that, number of parameters while defining a function, determines the number of arguments required, This function is not flexible enough to handle varied number of keyword arguments


# Solution: **kwargs
# def show_user_info(**kwargs):
#     # print(kwargs)
#     for key, value in kwargs.items():
#         print(key, value)
    
    
# show_user_info(name="ram", age=34, phone="98000", address="ktm", gender="Male")

# show_user_info(name="ram", age=34)

# Return statement


# def add(a, b):
#     # print(a+b)
#     result = a+b
#     return result
    
# print(add(3, 4))
# print(add(3, 4))

# sum((3, 5))


# Write a menu-driven program let's suppose unit converter
MENU = """
########################
    1. km to m
    2. m to cm
    3. cm to mm
    4. Exit
########################
"""

# def show_answer(ans, units):
#     print(f"Ans: {ans} {units}")
def show_answer(ans, units):
    print("#############################")
    print("")
    print(f"Ans: {ans} {units}")
    print("")
    print("#############################")


def kilometer_to_meter():
    print("----Kilometer to meter converter------")
    
    km_value = float(input("Kilometer ? >>>  "))
    m_value = km_value * 1000

    return m_value



while True:
    print(MENU) # convert this to a familiar function name, called show menu
    user_choice = input("choice: ")
    
    if user_choice == "1":        
        meter_ans = kilometer_to_meter()
        show_answer(ans=meter_ans, units="meters")
        
        
    elif user_choice == "2":
        print("----Meter to centimeter converter------")
        m_value = float(input("Meter ? >>>  "))
        cm_value = m_value * 100
        
        show_answer(ans=cm_value, units="centimeters")
        
    elif user_choice == "3":
        print("----Centimeter to millimeter converter------")
        cm_value = float(input("Centimeter ? >>>  "))
        mm_value = cm_value * 10
        
        show_answer(ans=mm_value, units="millimeters")
        
    elif user_choice == "4":
        print("User choice is 4, that means user wants to exit")
        break
    else:
        print("Please, enter correct choice")