# 1. Polymorphism
# 2. Abstraction
# 3. Encapsulation
# 4. Inheritance


# class BikeBajaj:  # class name should be written in PascalCase
#     company = "Bajaj"

#     def __init__(self, name, color):  # constructor method
#         # print("Bike is created", self)
#         # print("Name of current bike is ", name)
#         # print("Color of current bike is ", color)

#         # self means -> yo banidai gareko bike
#         # self.naam here naam is specifically attached to self/current object, so it's called as instance attribute/variable
#         self.naam = name  # here, self.naam is a public instance attribute
#         # self.name means, yo banidai gareko bike ko name

#         # self.ranga here ranga is specifically attached to self/current object, so it's called as instance attribute/variable
#         self.ranga = color
#         # self.color means, yo banidai gareko bike ko color

#     # here, show_features is an instance method, because it's directly related to an object. That means every object will have it's own sperate copy of instance attributes. Or simply, every time we call the show_features method, it will be purely dependent on the object through which it is called.
#     def show_features(self):  # eg. self => bike1
#         print("Features are:")
#         print("Name: ", self.naam)  # eg. self.naam => bike1.naam
#         print("Color: ", self.ranga)  # eg. self.ranga => bike1.ranga
#         print("Company: ", self.company)  # self.company => BikeBajaj.company


# b1 = BikeBajaj("NS", "Black")

# b1.naam = "NS-200"

# print(b1.naam)


# class BankAccount:
#     def __init__(self, person_name):
#         self.account_holder = person_name
#         # self._balance = 0
#         # single _ (underscore) in front of attribute name denotes as protected
#         self.__balance = 0
#         # double __ (underscore) in front of attribute name denotes as private, and it's strict
#         # python changes self.__balance to self._BankAccount__balance, this is called as name mangling

#     @property
#     def balance(self):  # getter
#         return f"Rs. {self.__balance}"

#     @balance.setter
#     def balance(self, amount):  # setter
#         if not isinstance(amount, int):
#             return

#         if amount < 0:
#             return

#         self.__balance = amount


# a1 = BankAccount("Ram")

# # a1.__balance = "laksdjflk"

# # print(a1.__balance)  # a1.__balance (i.e. doesn't exist) => a1._BankAccount__balance
# # print(a1._BankAccount__balance)

# a1.balance = "alsdkfjlsd"

# print(a1.balance)

# OTP has been sent to 98*********87


# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address


# # Person class -> Parent class , and Student class -> Child class
# class Student(Person):  # Person class -> Super class, and Student class -> Sub class
#     def __init__(self, name, address, school, grade):
#         super().__init__(name, address)
#         self.school = school
#         self.grade = grade


# # p1 = Person("Hari", "ktm")
# s1 = Student("Ram", "ktm", "NVM", 10)


# # print(p1.name, p1.address)
# print(s1.name, s1.address, s1.school, s1.grade)


# class Employee(Person):
#     def __init__(self, name, address, company, position):
#         super().__init__(name, address)
#         self.company = company
#         self.position = position


"""
class Person:
    def __init__


class Student(Person):
    def __init__ X

    def __init__


# Here, first, when there was not any init method in Student class, then the init method of Person class existed, and when we defined new init method in Student class, the new init method replaces the functionality of copied init method, this concept is called as method overriding

a = 5
a = 10


models.Model


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


"""


# class A:
#     pass
#     # def show(self):
#     #     print("Show of A")


# class B:
#     pass
#     # def show(self):
#     #     print("Show of B")


# class C(A, B):
#     pass


# c = C()

# c.show()
# print(C.__mro__)

# MRO -> Method Resolution Order

# -
