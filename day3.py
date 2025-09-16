# Operators
# 1. Arithmetic Operators ( +, -, /, *, %, //, **)

# x = 10
# y = 6
# result = x + y / 2 * 3
# result = x - y
# result = x * y
# result = x / y  # / it performs division
# result = x // y  # // it performs integer division
# result_round = round(result, 2)
# print(result_round)
# print(f"{result:.2f}")


# result = x % y  # it performs modulus, it returns remainder
# result = x**y  # it performs exponent, (power)
# print(result)

# Relational Operators ( >, <, >=, <=, ==, !=)

# x = 10
# y = 6
# result = x > y  # 10 > 6
# result = x < y
# result = x >= y
# result = x <= y
# result = x == y
# result = x != y


# 3. Logical Operators ( and, or, not)
# gender = "female"
# age = 17


# and operator
# decision = age >= 18 and gender == "male"
#  17 >= 18 rw "male" == "male"
#  False    rw   True  => final result False
# age 18 or 18 vanda thulo rw gender male hunu parne
# print(decision)

# male_citizenship_condition = gender == "male" and age >= 18
# female_citizenship_condition = gender == "female" and age >= 16
# print(female_citizenship_condition)


# Final Note: Final result for 'and' operator will be True (right) only if all the conditions are True


# or operator (if all are False then only final result will be False)

# math = 40
# science = 12
# nepali = 12
# pm = 32

# failed = math < pm or science < pm or nepali < pm
#         40  < 32 or 12  < 32
#          False   or  True  => Final result => True
# math maa 32 vanda less waa science maa 32 vanda less

# print(failed)
# passed = math >= pm and science >= pm and nepali >= pm
# print(passed)

# not operator
# raining = True  # (yes, right, ho)

# print(not raining)
# if not raining:
#     print("Don't Take an umbrella")

# if raining:
# print("Take an umbrella")

# print(result)
# age = 13
# print(age >= 18)

# 4. Membership operator (in, not in)
# picnic_group = "ram"

# # print("ma" in picnic_group)
# print("z" not in picnic_group)


# 4. Identity Operators (is, is not)
# name1 = "ram"
# name2 = "ram"
# print(name1 is name2)
# print(name1 is not name2)

# print(name1 == name2)

# == is used to compare values
# 'is' is used to compare objects, checks whether they are same or not


# . Assignment Operators ( =, +=, -=, *=, /=, %=, //=, **=)
