# Special/Dunder/Magic methods

# int, float, str 
# matrix

# [1, 2] [3, 4]

# class Matrix:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __str__(self):
#         matrix_str_format = f""" 
#         | {self.a} | 
#         | {self.b} |
#         """
#         return matrix_str_format
    
#     def __add__(self, other):
#         if not isinstance(other, Matrix):
#             raise Exception("Second operand must be a valid matrix")
        
#         new_a = self.a + other.a
#         new_b = self.b + other.b
#         new_matrix = Matrix(new_a, new_b)
#         return new_matrix
    
#     def __sub__(self, other):
#         if not isinstance(other, Matrix):
#             raise Exception("Second operand must be a valid matrix")
        
#         return Matrix(self.a - other.a, self.b - other.b)
    
#     def __mul__(self, other):
#         return Matrix(self.a*other, self.b*other)    
    
    

# a1 = Matrix(5, 20)
# a2 = Matrix(3, 4)

# print(a1)
# print(a2)
# print(5) -> '5'
# print(5.5) -> '5.5'
# print(a1 + a2)

# a3 = a1 + a2

# a4 = Matrix(1,1)

# print(a3+a4)

# print(a1+2)

# print(a1-a2)
# print(a1*6)


# Inheritance
# class User:
#     def __init__(self, username, password, email="example@ex.com"):
#         self.username = username
        
#         if len(password) < 6:
#             raise Exception("Password must be at least 6 chars long")
#         if username in password:
#             raise Exception("Password cannot contain username")
        
#         self.password = password
         
#     def __str__(self):
#         return f"{self.username}'s account"


# u1 = User("ram", "ram@123")
# str(u1)
# print(u1)

# Here, User is copied by Student class, so 
# User class is called as Parent/Super class
# Student class is called as Child/Sub class
# class Student(User):
#     # def __init__ # copied from User class
#     def __init__(self, username, password, father_name, email="opt@opt.com"):
#         # method overriding
#         super().__init__(username, password, email)
#         self.father_name = father_name




# s1 = Student("ram", "ram@123", "ram's father")

# print(s1)       
    
# class Teacher(User):
#     def __init__(self, username, password, salary, email="opt@opt.com"):
#         # method overriding
#         super().__init__(username, password, email)
#         self.salary = salary


# t1 = Teacher("hari", "ASDF@123", 45000)
# print(t1)

# Common uses of inheritance in django
# class Student(models.Model):
    # name = models.Charfield
    # address = models.Charfield
    # father_name = models.Charfield
    # mother_name = models.Charfield


# forms
# Student.objects.create(
#     name = name,
#     name = name,
#     name = name,
# )

# s1.address = "BTM"
# s1.save()

# Forms
# class StudentForm(forms.ModelForm):
    # fields
    
    
# form_obj = StudentForm()

# {{form_obj}}
# form_obj.is_valid()
# form_obj.save()

# ORM -> Object Relational Mapping

# Virtual Environment

