# Exception handling

# def ex():
#     print("this is function")
#     print("This is second line")



# Exception ?? 
# An exception is an event, which occurs during the execution of a program, that disrupts the normal flow of the program's instructions.

# user_input = int(input("Enter a number: "))

# print(user_input)
# print("End of program normally")

# Above code crashes/terminates when user inputs other than numbers like abc or special characters

# Same code with exception handling

# try:
#     user_input = int(input("Enter a number: "))
#     print(user_input)
# except ValueError:
#     print("Please enter numbers only")

# print("End of program normally")

# Write a program (WAP) in python to ask number as input. Ask the user to input number again and again if user enters garbage value

# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#         print(user_input)
#         break
#     except ValueError: # handle value error
#         print("Please enter numbers only")

# print("End of program normally")


# WAP in python to perform division operation

# while True:
#     try:
#         num1 = int(input("Enter a number: "))
#         num2 = int(input("Enter another number: "))

#         div_result = num1/num2
        
#         print("Division result is ", div_result)
#         print("Division result is ", div_result+"jpt")
#         break
#     except ValueError: # handle value error
#         print("Please enter numbers only")
#     except ZeroDivisionError:
#         print("Sorry, you can't divide something by zero")
#         print("Please enter another number")
#     except Exception as e:
#         # print("Unexpected error occured", e)
#         print("Something went wrong", e)

# print("End of program normally")

#
# try:
#     # write code/instructions which may lead to error
#     print("asdfs")
# except Exception:
#     # handle any exception
#     print("Exception handled")
# else:
#     # this block will run if no exception raised
#     print("else block")
# finally:
#     # this block doesn't care whether exception occured or not
#     # this will always run

# try:
#     file = open("dem.txt")
# except FileNotFoundError:
#     print("The file you are trying to open doesn't exist")
# else:
#     content = file.read()
#     print(content)
#     file.close()
# finally:
#     print("Thanks for using our program")

# l = [1,2,4]

# print(l[5])

# d = {
#     "name": "ram",
#     "age": 12
# }

# print(d["phone"])

# def 
# AMOUNT = 5000
# try:
#     withdraw_amount = int(input("Enter withdraw amount: "))
    
#     if withdraw_amount > AMOUNT:
#         raise Exception("Insufficient balance !!!")
# except Exception as e:
#     print(e)
# else:
#     AMOUNT = AMOUNT - withdraw_amount
#     print("Please collect your cash")
#     print(f"""
#           ------------------------------------
#           Receipt:
          
#             Date: xxxxxx
#             withdraw amount: {withdraw_amount}
#             remaining balance: {AMOUNT}
#           ------------------------------------
#           """)
# finally:
#     print("Thank you for banking with us")