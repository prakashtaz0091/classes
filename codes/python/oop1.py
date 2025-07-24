# print(type(5))
# print(type("ram"))
# print(type([1, 2, 3]))


# class House:
#     pass


# ram_house = House()

# print(type(ram_house))


# class Book:
#     pass


# book1 = Book()  # instantiation -> instance of Book Class
# book1.name = "Harry Potter"  # property eg. name, attribute
# book1.price = 2000


# book2 = Book()
# book2.name = "Titanic"
# book2.price = 2000


# print(book2.name, book2.price)
# def test(): # general function , not related to any specific class, so simply call this as function


class Book:
    # pass
    def __init__(self, name, price):  # initialize  # method
        print("Creating new object of Class Book")
        self.name = name
        self.price = price


# book1 = Book()
# book1.name = "Harry Potter"

# book2 = Book()
# book2.price = 2000

# book1 = Book("Harry Potter")  # instantiation -> instance of Book Class
# book1.show_info() # wrong
# print(book1.name)
# book2 = Book()  # instantiation -> instance of Book Class
# book1.name = "Harry Potter"  # property eg. name, attribute
# book1.price = 2000


# book2 = Book()
# book2.name = "Titanic"
# book2.price = 2000


# print(book2.name, book2.price)


# book1 = Book("asdf", 2000)
# book2 = Book("qwer", 3400)


# print(book1.name, book1.price)


# class Bike:
#     def __init__(self, name, cc, color="not set"):
#         self.name = name
#         self.cc = cc
#         self.color = color

#     def show_info(self):
#         print(f"Name : {self.name}")
#         print(f"CC : {self.cc}")
#         print(f"Color : {self.color}")


# mt15 = Bike("mt-15", cc=155.5)
# mt15.color = "white"
# pulsar150 = Bike("pulsar 150", 151, "black")


# mt15.show_info()
# pulsar150.show_info()
# Bike.show_info(pulsar150)

# print(mt15.name, mt15.cc, mt15.color)
# print(pulsar150.name, pulsar150.cc, pulsar150.color)


# l1 = [1, 2, 3]
# l1.append(4)
# print(l1)

# d1 = {"name": "ram", "age": 20}

# d1.append()

# 5.upper()
# print("ram".upper())


class Student:
    school = "Himalaya School"  # class attribute
    registration_count = 0

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

        Student.registration_count += 1

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

    @classmethod
    def show_reg_count(cls):
        print(f"Registration Count : {cls.registration_count}")


ram = Student("ram", 20)

hari = Student("hari", 21)

ram.show_info()
hari.show_info()
ram.show_reg_count()
# Student.show_reg_count()

# print(Student.school)
# print(ram.school)
# print(Student.registration_count)
