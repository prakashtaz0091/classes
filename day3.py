# a = 5
# b = 10

# Arthmetic operators
# print("addition result", a+b)
# print("sub result", a-b)
# print("mul result", a*b)
# print("div result", a/b)
# print(a//b) # quotient # int division
# print(a%b) # modulo -> Remainder
# print(a**b)
# print(a+b/2+4-3)

# Relational operators or Comparision operators

# print(5>2)
# print(5<2)
# print(5>=2) # greater than or equals to
# print(5<=2) # less than or equals to
# print(5==2)
# print(5!=2)

# print(2<5<3)
# print(2<5<10)


# Logical Operators, and, or , not

# print(5>2 and 5<3 and 5>10) # 1st comp and 2nd comp and 3rd comp => finally True
#     True    False   False
# print(5>2 and 5>3 and 5<10) # 1st comp and 2nd comp and 3rd comp => finally True

# print(5>2 or 5>3) # 1st comp and 2nd comp
# print(5<2 or 5<3) # 1st comp and 2nd comp

# print(not 5>2) # => not True => False


# 1st Example - find if student has passed the exam
# "45" -> 45
# english_marks = int(input("Enter marks obtained in English: "))
# english_pass_marks = 32

# english_passed = english_marks >= english_pass_marks
# # True                     # 34    >=       32 => True
# # print(english_passed)


# # The gap we see in line 52 and 54 before print statement, is called indentation

# if english_passed:   # : is called as colon
#     print("This student has passed english subject")
#     print("Congrats ")
# else:
#     print("This student has failed english subject")
#     print("Sorry, please try again next time")



# english_pass_marks = 32
# Rules for naming variables
# 1. Starting character of variable name must be a letter or an underscore
# rollno1 = 
# 1rollno # wrong
# _1rollno # right

# 2. variable name must be a single word
# english_marks = 45 # snake_case
# englishMarks = 45 # camelCase
# EnglishMarks = 45 # PascalCase

# 3. variable name must not be a reserved keyword
# if = 5
# and = 4
# or = 3
# not = 2

# Ternary operator
# print("Pass" if english_marks > 32 else "fail")

# 2nd example - Compute grade
english_marks = int(input("Enter marks obtained in English: "))

if english_marks>100:
    print("Marks greater than 100 not allowed")
if english_marks > 90:
    print("A+")
elif english_marks > 80:
    print("A")
elif english_marks > 70:
    print("B+")
elif english_marks > 60:
    print("B")
elif english_marks > 50:
    print("C+")
elif english_marks > 40:
    print("C")
elif english_marks > 30:
    print("D")
elif english_marks > 20:
    print("E")
elif english_marks > 0:
    print("NG")
else:
    print("Negative marks not allowed")
