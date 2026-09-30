# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# for i in range(10):
#     print("Good morning", i)
    

# print("2 x 1 = 2")
# print("2 x 2 = 4")
# print("2 x 3 = 6")
# print("2 x 4 = 8")
# print("2 x 5 = 10")
# print("2 x 6 = 12")
# print("2 x 7 = 14")
# print("2 x 8 = 16")
# print("2 x 9 = 18")
# print("2 x 10 = 20")

# num = int(input("Which multiplication table? ")) # 10

# for i in range(1, 11):
#     print(f"{num} x {i}  = {num*i}")

# example = "This is example data"

# for char in example:
#     print("character ", char)

# While loop

# for i in range(1000):
#     print("Sorry")

# happy = False

# while not happy:
#     print("Sorry")
    
#     answer = input("Is he/she happy now?? [yes/no] ")
    
#     if answer == "yes":
#         happy = True
#     else:
#         print("Let's try once again")



# sad = True

# while sad:
    
#     answer = input("Is he/she happy now?? [yes/no] ")
    
#     if answer == "yes":
#         sad = False
#     else:
#         print("Sorry")
    
    
# happy = True

# while not happy:
    
#     answer = input("Is he/she happy now?? [yes/no] ")
    
#     if answer == "yes":
#         happy = False
#     else:
#         print("Sorry")


# Data structures
# 1. List
# participants = ["ram", "sita", "geeta", "hari", "saugat", "uttam"]


# for name in participants:
#     print(name.capitalize())


# print(participants)

#                0       1        2       3      4          5
participants = ["ram", "sita", "geeta", "hari", "saugat", "uttam"]
# print(participants)

participants.insert(2, "Kushal")
participants.append("Priya")
participants.append("uttam")
participants.extend(["Ramesh", "Roshan"])

# participants.remove("uttam")



# print(participants)

# while "uttam" in participants:
#     participants.remove("uttam")

# # print(participants)
# # \n -> New line
# for name in participants:
#     print(name.capitalize(), end=" ")

# Ram Sita Hari 
num = 10
while True:
    print("Some task")
    
    if num == 10:
        break
    