# Control Flow statement
# 1. Conditional statement
# age = int(input("Enter your age: "))

# # Whenever we see/use this (:, colon) symbol, the line right after this statement should be indented. That gap is called indentation
# if age >= 18:  # : this called as colon
#     print(f"You are {age} years old.")
#     print("so you can apply for Nepali citizenship")
# else:
#     print("You are under 18.")
#     print("Please try after few years")


# marks = int(input("Enter the marks: "))
"""
marks >= 90 => A+
marks >= 80 and marks < 90 => A
marks >= 70 and marks < 80 => B+
marks >= 60 and marks < 70 => B
marks >= 50 and marks < 60 => C+
marks >= 40 and marks < 50 => C
marks >= 30 and marks < 40 => D
marks < 30 => E
"""

# if marks >= 90 and marks <= 100:
#     print("A+")
# elif marks >= 80 and marks < 90:
#     print("A")
# elif marks >= 70 and marks < 80:
#     print("B+")
# elif marks >= 60 and marks < 70:
#     print("B")
# elif marks >= 50 and marks < 60:
#     print("C+")
# elif marks >= 40 and marks < 50:
#     print("C")
# elif marks >= 30 and marks < 40:
#     print("D")
# elif marks >= 0 and marks < 30:
#     print("E")
# else:
#     print("Invalid marks entered")
#     print("Marks should be in range of (0-100)")


# marks = int(input("Enter the marks: "))


# if marks >= 90 and marks <= 100:
#     print("A+")
# if marks >= 80 and marks < 90:
#     print("A")
# if marks >= 70 and marks < 80:
#     print("B+")
# if marks >= 60 and marks < 70:
#     print("B")
# if marks >= 50 and marks < 60:
#     print("C+")
# if marks >= 40 and marks < 50:
#     print("C")
# if marks >= 30 and marks < 40:
#     print("D")
# if marks >= 0 and marks < 30:
#     print("E")
# else:
#     print("Invalid marks entered")
#     print("Marks should be in range of (0-100)")


# 2. Looping Statement, (Loop means repeat)
# a. for in  Loop, (finite loop)
# b. while loop, (infinite loop)


# for n in range(10):
#     print("Welcome")

"""
In above for in loop, example, range(10) means generate a range of numbers from 0 to 10 (but 10 is not included). So basically we can say, 0-9. Here, 10 is called as stopping value, 

n in "0,1,2,3,4,5,6,7,8,9"
"""


# Whenever we provide two values to range, first smaller and second one must be greater. First value is start value and second value is stopping value
# for n in range(1, 10):
#     print(f"Welcome {n}")


# When we provide 3 values to range, first is called starting, second is called stopping, third/last is called step value
# for n in range(1, 10, 3):
#     print(f"Welcome {n}")


# Generate odd numbers from 0-20
# for number in range(1, 20, 2):
#     print(number)
# Generate even numbers from 0-20
# for number in range(2, 21, 2):
#     print(number)

# Generate multiplication table for 3
"""
eg.
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
"""
# number = int(input("Multiplication table for ?? : "))

# for n in range(1, 11):
#     print(f"{number} x {n} = {number*n}")


# while loop, (infinite)
# while condition:
#     # task to repeat
# here while loop will repeat the task given, till the condition is True

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1


# sad = True

#


"""
start game
-----playing game-----
-----end------

start game
end game

-----playing game-----
-----end------

start game
end game


-----playing game-----
-----end------

End game
Application close
"""
