# 4 pillars of OOP
# Encapsulation
# Inheritance
# Abstraction
# Polymorphism

# 1. Encapsulation
# Access modifiers
# class A:
#     def __init__(self):
#         self.a = 10  # a=> public
#         self._b = "ram"  # _b is now protected attribute
#         self.__c = "private c"  # __c is now private attribute
#         # self._A__c = "private c" # => name mangling

#     def get_c(self):  # getter method
#         return self.__c

#     @property
#     def c(self):
#         return self.__c


# a1 = A()

# a1.a = 20
# a1._b = "hari"
# print(a1._b)

# print(a1.__c) # wrong => not accessible
# print(a1._A__c)

# print(a1.get_c())

# print(a1.c)


# class BankAccount:
#     def __init__(self, acc_no, first_deposit=0):
#         self.__acc_no = acc_no
#         self.__balance = first_deposit

#     @property
#     def acc_no(self):  # getter
#         return f"XXXXX{self.__acc_no[-4:]}"

#     @acc_no.setter
#     def acc_no(self, new_value):
#         print("you can't set new account no: ", new_value)

#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self, new_value):
#         if not isinstance(new_value, (int, float)):
#             raise Exception("Deposit balance must be a number")
#         if new_value < 500:
#             raise Exception("Deposit balance cannot be less than 500")
#         self.__balance += new_value


# a1 = BankAccount("123456778", 5000)
# # a1.acc_no = "asddf"
# # print(a1.acc_no)

# print("Just after creation of bank account ", a1.balance)
# try:
#     # a1.balance = 2000
#     a1.balance = "assdf"
# except Exception as e:
#     print(e)
# finally:
#     print("After deposit ", a1.balance)


# Inheritance


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         # codes
#         return "Animal Sound !!!"


# class Dog(Animal):  # Animal => super class , Dog => sub class
#     def speak(self):  # method overriding
#         # codes
#         return f"{self.name} barks !!!"


# d = Dog("Tommy")
# print(d.speak())


# class A:
#     pass
#     # def show(self):
#     #     print("this is class A")


# class B:
#     pass
#     # def show(self):
#     #     print("This is class B")


# class C(A, B):  # multiple inheritance
#     pass
#     # def show(self):
#     #     print("This is C class")


# c = C()

# c.show()
# print(C.__mro__)


# Polymorphism


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         # codes
#         return "Animal Sound !!!"


# class Dog(Animal):  # Animal => super class , Dog => sub class
#     def speak(self):  # method overriding
#         # codes
#         return f"{self.name} barks !!!"


# a = Animal("Animal1")
# d = Dog("Tommy")
# a.speak()
# d.speak()

# def speak(obj):
#     print(obj.speak())


# speak(a)
# speak(d)


#  + => kun operator?

# BankAccount = 10 # wrong


class BankAccount:  # Write class name in PascalCase
    def __init__(self, acc_no, first_deposit=0):
        self.__acc_no = acc_no
        self.__balance = first_deposit

    @property
    def acc_no(self):  # getter
        return f"XXXXX{self.__acc_no[-4:]}"

    @acc_no.setter
    def acc_no(self, new_value):
        print("you can't set new account no: ", new_value)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise Exception("Deposit balance must be a number")
        if new_value < 500:
            raise Exception("Deposit balance cannot be less than 500")
        self.__balance += new_value

    def __eq__(self, other):
        return self.__balance == other.__balance


a1 = BankAccount("123456778", 5000)
a2 = BankAccount("123456789", 5000)

print(a1 == a2)
