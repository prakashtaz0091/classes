# class Player:
#     pass



# player1 = Player()

# # print(player1)
# print(type(player1))

# print(type(5))

# l = [1, 2, 3]

# l.append()

# s = {1, 2}

# s.add(5)


# def add():
#     pass


# print(type(add))
    
# from bill import show_bill_summary
# import bill


# # print(type(show_bill_summary))
# print(type(bill))


# class User: # defining a class
#     pass


# user = User() # creating new object of class User

# user.name = "Ram"
# user.email = "ram@gmail.com"
# user.password = "**********"

# user2 = User()
# user2.name = "Hari"
# user2.email = "hari@gmail.com"
# user2.password = "ASDFQEWRQWER"

# user3 = User()


# print(user.name)

# print(user2.name)

# print(user3.name)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        
        if User.check_password(password, name): 
            self.password = password
    
        
    def show_info(self):
        print("Name : ", self.name)
        print("Email : ", self.email)
        print("Password : ", self.password)
        
    def save(self):
        print("Saving to database")
        print("Saved to database")
        
    @staticmethod
    def check_password(password, name):
        if len(password) < 8:
            raise Exception("Password must be at least 8 chars long")
    
        has_special_chars = any(not char.isalnum() for char in password)
        
        if password.isalpha() or password.isdigit() or not has_special_chars:
            raise Exception("Password must be alphanumeric + special chars ")

        if name.lower() in password.lower():
            raise Exception("Password must not contain personal info")
        
        return True
        
        
    


user1 = User("Ram", "ram@gmail.com", "User@.123")
# user2 = User("Ram", "ram@gmail.com")
# user3 = User("Ram", "ram@gmail.com", "password123")
# user4 = User("Ram", "ram@gmail.com", "password123")

# print(user1.__dir__())
# print(dir(user1))
# print(user1.name)
# print(user1.email)
# print(user1.password)
# print(user1.address)

# students.append()
# user1.show_info()

User.show_info(user1)

user1.save()


# Start from encapsulation (Data protecting)
# Inheritance
# ######214
