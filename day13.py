# print(type(5))
# print(type(range(10)))

# import time

# print(type(time))


# class MyDataType:  # class define
#     pass


# d1 = MyDataType()

# print(type(d1))

# person 1 details
person1_name = "Ram"
# person1_age = 32
# person1_phone = "980000000"
# person1_address = "KTM"


# # person 2 details
# person2_name = "Hari"
# person2_age = 23
# person2_phone = "980000000"
# person2_address = "KTM"


# def asdf


# class Person:
#     pass


# p1 = Person()  # creating new Person object
# p1.name = "Ram"
# p1.age = 32


# # p1 ->  name
# #    |-> age


# p2 = Person()  # creating new Person object
# p2.name = "Hari"
# p2.age = 23


# print(p1.name, p1.age)


# self keyword means, current object/instance
# class Person:

#     def __init__(self, name, age):  # this is not a normal function/method
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)


# p1 = Person("ram", 32)  # p1 is object/instance of Person class
# print(p1.phone)
# p2 = Person("hari", 23)

# # print(p1.name, p1.age)
# # print(p2.name, p2.age)

# p1.show_info()
# p2.show_info()


# till now, the variables .name .age are special variables related to an object, they are called as data members/attributes


# name = "Ram"
# name.show_info() -> methods
# print(name.startswith("S"))
# startswith is a method of class str
# 5.startswith("s")


# Attributes are of two types
# 1. object/instance attribute
# 2. class attribute


class Student:
    school = "ABC school"  # class attribute or class data member

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_stu_info(self):
        print("Student info")
        print("Name: ", self.name)
        print("Age: ", self.age)

    @classmethod
    def show_school_name(cls):
        print("School Name: ", cls.school)


s1 = Student("Ram", 12)
s2 = Student("hari", 14)

# print(s1.school)
# print(s2.school)
s1.show_stu_info()

# print(Student.school)
# print(Student.name)
# print(Student.age)

Student.show_school_name()

"""
1. object & class
2. contructor method __init__
3. self -> it means, current object, for eg. s1.show_info(), self means s1
4. method -> function defined inside a class. This function is only applicable or available for class related objects
5. data member -> variable, but related to class or object
6. attribute -> data members or methods
7. instance -> it means object, nothing more nothing less
8. object attribute -> those data members or methods which are related to each and every object 
9. class attribute -> those data members or methods which are related directly to class, rather than any object. Class attribute can be accessed directly with class name, we don't need any objects for that.
"""
