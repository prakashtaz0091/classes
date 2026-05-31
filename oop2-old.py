# class Student:
#     school_name = "TMK"
#     annual_fees = 90000
    
#     # here __init__ is called as constructor, it's a special function
#     def __init__(self, name, age, address, paid_fees=0):
#         # self.name -> name is a public attribute
#         self.name = name
#         self.age = age
#         self.address = address
#         # self.paid_fees = paid_fees
#         # self._paid_fees = paid_fees # protected attribute
#         self.__paid_fees = paid_fees # private attribute

#     @property
#     def paid_fees(self): # getter
#         return self.__paid_fees*100
    
#     @paid_fees.setter
#     def paid_fees(self, new_value):
#         print("Trying to set new value")
        
#         if not isinstance(new_value, int):
#             raise Exception("Please enter postive numbers only")
#         if new_value < 0:
#             raise Exception("You are not allowed to set negative value")
        
#         self.__paid_fees = new_value
#         print("New value set")
    
    
#     # method => all functions defined inside a class are called as methods
#     def show_info(self):
#         print(f"""
#             ----------------------------------
#                 Name: {self.name}  
#                 Age: {self.age}  
#                 Address: {self.address} 
#                 Annual fees : {self.annual_fees} 
#                 Paid fees : {self.__paid_fees} 
#             ----------------------------------
#             """)
        
#     def show_remaining_fees(self):
#         print(f"""
#             -----------REMAINING FEES---------
#                 Name: {self.name}  
#                 Total fees: Rs. {self.annual_fees}
#                 Paid: Rs. {self.__paid_fees}
#             ------------------------------------
#                 Remaining: Rs. {self.annual_fees} - Rs. {self.__paid_fees}
#                         => Rs. {self.annual_fees-self.__paid_fees}
#             ----------------------------------
#             """)
    
#     @classmethod
#     def update_annual_fees(cls, new_value):
#         cls.annual_fees = new_value
#         print("Annual fees updated successfully")
    


# student1 = Student("ram", 20, "ktm", 20000)
# student2 = Student("hari", 20, "ktm")

# student1.show_info()
# student2.show_info()

# Student.update_annual_fees(1_00_000)

# student1.paid_fees = 100000
# student1.name = "JPT"
# student1.paid_fees = -100000
# student1.paid_fees = "abcd"
# student1._paid_fees = -100000
# student1.__paid_fees = "abcd"
# student1.__paid_fees = 12341234


# print(student1.__paid_fees)
# print(student1._Student__paid_fees) # __paid_fees -> _Student__paid_fees # name mangling

# student1.show_info()
# student2.show_info()

# student1.show_remaining_fees()
# student2.show_remaining_fees()

# Access modifiers

# student1.paid_fees = -100000 # protected from this situation
# student1.paid_fees = "abc"
# student1.paid_fees = -10000
# student1.paid_fees = 10000
# print(student1.paid_fees)

# student1.set_paid_fees(23000)
# reuslt = student1.get_paid_fees()
# reuslt = student1.paid_fees
# student1.paid_fees = 10000
# from dataclasses import dataclass

# @dataclass
# class Car:
#     engine_cap: str
#     model: str
    
    
# Car("600cc", "x model")

# "ram".upper() => "RAM"
# annual_fees = int(input("Enter annual fees: "))
# Student.update_annual_fees(annual_fees)

# student1.show_info()