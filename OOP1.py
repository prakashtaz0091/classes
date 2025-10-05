# print(type(5))

# print(type("RAM"))

# True.lower()
# print("RAM".lower())

# [].append(5)
# ().append(5)


# Object is also called as instance


# class Bike:  # class name should be written in PascalCase
#     def __init__(self):  # constructor method
#         print("Bike is created")


# mt_15 = Bike()  # it helps to create an object of class Bike
# ns_200 = Bike()

# True.lower()
# mt_15.self_start()
# print(type(mt_15))


class Bike:  # class name should be written in PascalCase
    def __init__(self, name, color):  # constructor method
        # print("Bike is created", self)
        # print("Name of current bike is ", name)
        # print("Color of current bike is ", color)

        # self means -> yo banidai gareko bike
        self.naam = name
        # self.name means, yo banidai gareko bike ko name
        self.ranga = color
        # self.color means, yo banidai gareko bike ko color

    def self_start(self):
        print("Starting.....")
        # actual game, engine sound play

    def kill_switch(self):
        print("....Stopping the engine")


mt_15 = Bike("MT-15", "Black")
ns_200 = Bike("NS-200", "Red")

# print("Name of this bike", mt_15.naam)
# print("Color of this bike", mt_15.ranga)


# print("Name of this bike", ns_200.naam)
# print("Color of this bike", ns_200.ranga)

# import time

# engine_start_button  => click => mt_15.self_start()

# # time.sleep(5)
# kill_switch => click => mt_15.kill_switch()
# # mt_15.ranga


# Summary
"""
OOP is just a modern concept, which helps in better code organization, readability and maintainability. It provides better code organization than that of functions, since function specially wraps/groups the logical parts, Class helps to group the data and function/method/behaviour together.

1. Class -> New Datatype -> with full control other data and it's behavior
2. Object -> Also called as instance -> Is the actual value/data of the class, Every object has data and behaviour, mentioned/defined in it's class
3. Constructor -> It's a special method that helps to create an object. That's why it's called as constructor. If we don't write the constructor method, python will use a empty default constructor method.  So, most of the time, when we define __init__ i.e. a constructor, we probably want to modify the process of creating the object.
4. self -> It represents the current object, which is being created. It's not a keyword, it's a convention. Whenever we need to set data/attributes to the current object, we use self. for eg. self.name and self.color in above example
"""


# import math

# print(type(math))
# functions
# math class -> methods
# math -> add, sub


# class math:
#     def add()

#     def sub()


# math.add()

# math.sub()


# def asdf():
#     pass


# print(type(asdf))
