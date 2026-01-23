"""
1. Programming is playing with data
2. Data types? 
3. Variables and rules for naming variables
4. Operations -> operators input output
5. Control Flow Statements -> if, if else, if elif else, for in loop, while loop
6. Data structures-> List, Tuple, Set, Dictionary
7. Function
"""

# Function
# Employee->Training -> Function Defination -> Defining a function
# Employee->Actual Work -> Function call -> Calling a function


# def welcome_user(): # Function defination
#     print("Hello, user")
#     print("Welcome to the python world, let's begin")


# welcome_user() # Function call


# def welcome_user(name): # Function defination
#     print("Hello, ", name)
#     print("Welcome to the python world, let's begin")


# welcome_user("ram") # Function call
# welcome_user("hari") # Function call
# welcome_user("shyam") # Function call


# def welcome_user(name, greeting): # Function defination
#     print(greeting, name)
#     print("Welcome to the python world, let's begin")


# welcome_user("ram", "Good morning, ") # Function call
# welcome_user("hari", "Hi, ") # Function call
# welcome_user("shyam", "Good Evening, ") # Function call



# def welcome_user(name, greeting="Hello, "): # Function defination
#     print(greeting, name)
#     print("Welcome to the python world, let's begin")


# welcome_user("ram") # Function call
# welcome_user("hari", "Hi, ") # Function call
# welcome_user("shyam") # Function call

# welcome_user() # Function call


# Note: The variables name and greeting in above function defination examples are called as parameters in short params
# Note: The values that we pass to function call such as "ram", "Good evening " are called as arguments in short args
# In other terms of programming world, params are also referred as formal parameters and args are also called as actual parameters
# In above example, we are passing args according to position, so they are called as positional arguments
# In above example, we have written a parameter, greeting="Hello", Here greeting is a variable/parameter/formal_parameter we know it, but the value we passed right after the parameter in function defination i.e. "Hello", is called default parameter, since greeting has a default value called "Hello", when no args is passed



# def welcome_user(name, greeting="Hello, "): # Function defination
#     print(greeting, name)
#     print("Welcome to the python world, let's begin")


# welcome_user("Hi", "ram")
# welcome_user(greeting="Hi", name="ram")
# Here we used both parameter's name as well as value to pass in a function call, this type of arguments are called as keyword arguments

# def welcome_user(name, pro_lang="python", greeting="Hello, "):
#     print(greeting, name)
#     print(f"Welcome to the {pro_lang} world, let's begin")


# welcome_user("ram", greeting="Hi")
# welcome_user("hari", pro_lang="C")
