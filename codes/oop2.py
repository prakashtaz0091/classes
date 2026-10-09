# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
        
#         if User.check_password(password, name): 
#             # self.password = password   # it's public access
#             # self._password = password   # it's protected access
#             self.__password = password   # it's private access
#             # __password => _User__password
            
    
#     @property
#     def password(self):
#         return "*"*len(self.__password)
    
#     @password.setter
#     def password(self, new_value):
#         if User.check_password(new_value, self.name):
#             self.__password = new_value
    
        
#     def show_info(self):
#         print("Name : ", self.name)
#         print("Email : ", self.email)
#         # print("Password : ", self.password)
#         # print("Password : ", self._password)
#         print("Password : ", self.__password)
        
#     def save(self):
#         print("Saving to database")
#         print("Saved to database")
        
#     @staticmethod
#     def check_password(password, name):
#         if len(password) < 8:
#             raise Exception("Password must be at least 8 chars long")
    
#         has_special_chars = any(not char.isalnum() for char in password)
        
#         if password.isalpha() or password.isdigit() or not has_special_chars:
#             raise Exception("Password must be alphanumeric + special chars ")

#         if name.lower() in password.lower():
#             raise Exception("Password must not contain personal info")
        
#         return True
    
#     def __str__(self): # Override
#         return self.name
    
#     def __add__(self, other):
#         print("Adding two users")
#         return f"{self.name} + {other.name}"
    
#     def __sub__(self, other):
#         print("Sub two users")
#         return f"{self.name} - {other.name}"
        

# user1 = User("ram", "ram@gmail.com", "ASDF@1234")
# user2 = User("hari", "ram@gmail.com", "ASDF@1234")


# print(user1 - user2)

# special, magic, dunder 
# print(dir(user1))
# print(user2)
# 90 => str(90) => "90"
# print(90)

# print("AFter creation")
# user1.show_info()

# # print(user1.name)
# # print(user1.email)
# # print(user1.__password)
# # user1.__password = "New password"

# print("AFter __password change")
# print(user1._User__password)

# print(dir(user1))

# print(user1.password)
# user1.password = "laksdfjlksdf123@"

# user1.show_info()
# "ram"*2 => "ramram"
# "hari"*3 => "hariharihari"

# "*"*8 => "*********"


# Inheritance
# models.py
# class Model:
#     def save()
#     def delete()


# class Profile(models.Model):
#      birthdate
#      address
#      bio
#      profile_pic
#      created_at
#      updated_at 
     
     
# class Booking(models.Model):
#     user 
#     date
#     created_at
#     payment_status



# p = Profile("asdlkf", "lkasdjf")

# p.save()

# b = Booking("alsdkfj", kajsdlfkj)
# b.save()


# Override

# print(5+2)
# print("ram"+" thapa")
# print([1, 2, 3] + [4, 5])
# print({1, 2, 3} - {3, 5})





