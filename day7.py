# Function
# Function is a block code that represents a specific task
# Function is variable that stores group of code

# a = 10

# def welcome_message():  # Function defination
#     print("Welcome, Ram")
#     print("Please check your email, and verify the account")


# welcome_message()  # function call
# welcome_message()
# welcome_message()
# welcome_message()
# welcome_message()

# name is just a variable, but in this context, it is called as parameter, or simply param
# def welcome_message(name, greeting): 
#     print(greeting, name)
#     print("Please check your email, and verify the account")


# Actual data sent for a parameter, for eg. "Ram", is called as agrument. But in general it can simply be called as param/eter
# welcome_message("Ram", "Good morning")
# welcome_message("Hari", "Good afternoon")


# If a parameter has a default value, it's called as default parameter
# def welcome_message(name, greeting="Welcome"): 
#     print(greeting, name)
#     print("Please check your email, and verify the account")


# welcome_message("Ram", "good morning")
# welcome_message("Ram", "good morning")
# welcome_message("good morning", "Ram")
# welcome_message(greeting="good morning", name="Ram")
# greeting="good morning", this usage is called as keyword-argument

# Code below show a syntax error (means grammaritical error)
# non-default params should be written first
# def welcome_message(greeting="Welcome", name): 
    # print(greeting, name)
    # print("Please check your email, and verify the account")


# 
# def add(a, b):
#     return a+b

# result = add(4, 5)

# print("result", result)

# first overload concept
# add(int a, int b)
# add(float a, float b)
# def add(a, b):
#     r = 0
#     if isinstance(a, (list)):
#         for value in a:
#             r += value
#     else:
#         r += a
        
#     r += b
#     return r

# result = add([1, 2, 3], 5.5)
# result2 = add(4, 5.5)

# print("result", result)
# print("result2", result2)


# send_email_to_loggedin_user("1", "2", "3")

# def add(*numbers, start=0):
#     for value in numbers:
#         start += value

#     return start

# print(add(1, 2, 3, 4, 5, 6, start=5))

# result = sum([1, 2, 3, 4, 5, 6], start=5)

# print(result)

# same as sum function
# def add(numbers, start=0):
#     for value in numbers:
#         start += value

#     return start

# print(add([1, 2, 3, 4, 5, 6], start=5))

# def show_info(**info):
#     print(info)
    
    
# show_info(name="ram", age="23", address="ktm" )


# Note: single * in param, means, any no. of positional arguments
# double ** in param, means, any no. of keyword arguments

# def some_func(p1, p2=0, **kwargs):
#     #laskdjfl
#     #laskdjfl
#     #laskdjfl
#     #laskdjfl
#     if True:
#         return 0
#     elif laskdfj:

    #     return laskd
    # laskdjflkasdf


# def calcuate_grade(sub_marks):
#     if sub_marks>100:
#         print("Marks greater than 100 not allowed")
#     if sub_marks > 90:
#         print("A+")
#     elif sub_marks > 80:
#         print("A")
#     elif sub_marks > 70:
#         print("B+")
#     elif sub_marks > 60:
#         print("B")
#     elif sub_marks > 50:
#         print("C+")
#     elif sub_marks > 40:
#         print("C")
#     elif sub_marks > 30:
#         print("D")
#     elif sub_marks > 20:
#         print("E")
#     elif sub_marks > 0:
#         print("NG")
#     else:
#         print("Negative marks not allowed")


# eng_marks = int(input("Enter english marks: "))

# calcuate_grade(eng_marks)


# sc_marks = int(input("Enter science marks: "))

# calcuate_grade(sc_marks)




# while True:
#     print(MENU)
    
#     user_choice = input("Enter your choice (1-3/Q) >>> ").upper()
#     # print("userchoice", user_choice)
    
#     if user_choice == "1":
#         add_new_participant()
        
#     elif user_choice == "2":
#         remove_participant()
        
#     elif user_choice == "3":
#         show_participants()

#     elif user_choice == "Q":
#         print("Thank you for using our program")
#         break
#     else:
#         print("Please enter right choice. (1-3/Q)")
        