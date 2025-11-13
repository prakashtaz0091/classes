# Relational Operators
# <, >, >=, <=,!=, ==
# a = 5 # this is not relational operator, this assigns 5 to variable a, so it's called as assignment operator
# for eg. 5 < 3 -> False
# for eg. age > 18 -> False

# print(5 > 3)
# print(2 < 5 > 3)
# print(5 == 3)
# englishmarks = 23
# "ram" == "ram"

# 20 - 40 -> D
# print(20 < englishmarks < 40)


# Logical Operators
# and, or, not
# and -> Sabai relation True huda matrai result True hunxa

# englishmarks > 20
# englishmarks < 40


# englishmarks > 20 and englishmarks < 40  # ... and more relations
# englishmarks should be greater than 20 and englishmarks should be less than 40
# englishmarks = 50
# print(englishmarks > 20 and englishmarks < 40)
#           50 > 20    and   50 < 40
#            True     and     False
#                   False


# or case maa , kunai euta relation True vayo vane, final result True hunxa
# marks = 101
# FM = 100
# # marks 0  , marks < 100
# marks < 0  # that means, if marks is in -ve, it's invalid
# marks > FM  # that means, if marks is great FM, again it's invalid

# marks < 0 or marks > FM  # and much more
# # 101 < 0 or 101 > 100
# #  False  or    True


# not, reverts the relation. For eg. True relation to False and False to True

# 5 > 3  # -> True
# not 5 > 3  # -> False
# not True  # -> False

# raining = True
"""
multi line comment
if raining -> then do something

if not raining -> then do no thing

"""

# Rules for naming variables
# 1. variable name must start with a letter or an underscore _
# marks = 40  # right
# Marks = 40  # right, but not recommended, it has seperate usecase
# 1marks = 40 # wrong, it gives syntax error
# _1marks = 40 # right, but not recommended, it has seperate usecase


# 2. variable name must be meaningful (convention)
# a = 5 # this variable a, doesn't convey any meaning to understand the value
# age = 5 # now we know 5 is someone's age
# no_of_students = 50 # now we clearly know 50 is the number of students

# 3. variable name must be a single word
# englishmarksofram = 40 # wrong, variable name must be a single word
# english marks of ram = 40 # wrong, variable name must be a single word
# english_marks_of_ram = 40  # this correct way to write descriptive variable names, this style is called snake_case, (convention)
# englishMarksOfRam = 40  # right, this is called as camelCase


# 4. Resevered words cannot be used as a variable name
# if, while, not, and , or
# or = 5 # this is not allowed, because, or has special meaning in context to python language


# String operators
# + -> concatenation operator -> it combines two strings
# * -> repeatation operator -> it repeats string n number of times

# first_name = "Ram "
# last_name = "Poudel"

# full_name = first_name + last_name
# print(full_name)
# result = first_name * 3  # "Ram Ram Ram "
# print(result, type(result))


# Length operator, (len)
# it provides length of any sequence
# first_name = "Ram "
# no_of_characters = len(first_name)
# print(no_of_characters)


# Membership operator, (in)
# shareholders = "ram hari geeta"

# check = "ram" in shareholders # it looks for full sequence, or say search a sub sequence in a full sequence
# check = "ramri" in shareholders # it gives False
# check = "ram geeta" in shareholders  # it gives False

# print(check)

# Identity operator, (is)

# a = 5
# b = 5

# print(a is b)
# Mutable and Immutable,


# name1 = """
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# """
# name2 = """
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# Ram is a very good student. He reads in class 5
# """

# print(name1 is name2)

# fullname = "Ram Poudel"

# first_name = "Ram "
# last_name = "Poudel"
# first_plus_last = first_name + last_name

# print(fullname)
# print(first_plus_last)
# print(first_plus_last is fullname)

# a = None
# b = None

# print(a is b)

# result = None  # This value comes from different code

# if result is not None:
#     print("result", result)

# if result == None:
