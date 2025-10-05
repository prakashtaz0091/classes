class BikeBajaj:  # class name should be written in PascalCase
    company = "Bajaj"

    def __init__(self, name, color):  # constructor method
        # print("Bike is created", self)
        # print("Name of current bike is ", name)
        # print("Color of current bike is ", color)

        # self means -> yo banidai gareko bike
        # self.naam here naam is specifically attached to self/current object, so it's called as instance attribute/variable
        self.naam = name
        # self.name means, yo banidai gareko bike ko name

        # self.ranga here ranga is specifically attached to self/current object, so it's called as instance attribute/variable
        self.ranga = color
        # self.color means, yo banidai gareko bike ko color

    # here, show_features is an instance method, because it's directly related to an object. That means every object will have it's own sperate copy of instance attributes. Or simply, every time we call the show_features method, it will be purely dependent on the object through which it is called.
    def show_features(self):  # eg. self => bike1
        print("Features are:")
        print("Name: ", self.naam)  # eg. self.naam => bike1.naam
        print("Color: ", self.ranga)  # eg. self.ranga => bike1.ranga
        print("Company: ", self.company)  # self.company => BikeBajaj.company

    @classmethod
    def show_company_name(cls):
        print("Company name is: ", cls.company)


bike1 = BikeBajaj("NS-200", "black")
bike2 = BikeBajaj("N-160", "red")


# print(bike1.naam)
# print(bike1.company)

# print(bike2.naam)
# print(bike2.company)

# print(BikeBajaj.company)

# Topic - Summary: To be noted
"""
Attributes are of two types, class attributes and instance attributes.

- Instance attributes are directly related to an object/instance. That means every object will have it's own sperate copy of instance attributes. All the object/instance attributes are isolated from each other.

- Class attributes are related to a class rather than any specific object/instance. That means all the objects/instances will share the same copy of class attributes.

"""


# bike1.show_features()
# bike2.show_features()

# "ram".upper()  #  => "RAM"
# "hari".upper()  # => "HARI"


# bike1.show_company_name()
# BikeBajaj.show_company_name()
# BikeBajaj.show_features()
