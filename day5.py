# Data Structures

# 1. List

# list_of_numbers = [1, 2, 3, 4]
# mixed_list = [1, "ram", 5.5, "Kathmandu", True]

# participants = []

# print(participants)
# # print(type(participants))

# participants.append("Ram") # ["Ram"]
# participants.append("Hari") # ["Ram", "Hari"]
#                             #    0       1
                            
# print("Index of Ram is", participants.index("Ram"))


# participants.insert(0, "Shyam") # ["Shyam", "Ram", "Hari"]
#                                 #    0        1      2
                                
# # print("Index of Ram is", participants.index("Ram"))
# print(participants)


# participants.remove("Seeta") # Note: removes if exists, if doesn't exist, it gives error, ValueError, saying x is not in list


# participants.pop()
# print(participants)
# removed_value = participants.pop(0)

# print(participants)


# participants = ["ram", "hari", "shyam"]

# # 1, "ram"
# # 2, "hari"
# # 3, "shyam"
# for num, name in enumerate(participants, start=1):
#     print(num, name)


# participants = []

# while True:
#     new_name = input("Enter new participant's name (q for quit): ")
    
#     if new_name == 'q':
#         break
    
#     participants.append(new_name)

# print("List of participants ")
# # print(participants)
# for num, name in enumerate(participants, start=1):
#     print(num, name)



# participants = []

# MENU = """
#     ============MENU=================
#     1. Add new participant
#     2. Remove existing participant
#     3. Show all participants
#     Q. Quit
#     =================================
# """


# while True:
#     print(MENU)
    
#     user_choice = input("Enter your choice (1-3/Q) >>> ").upper()
#     # print("userchoice", user_choice)
    
#     if user_choice == "1":
#         new_name = input("Name of participant >>> ")
#         participants.append(new_name)
        
#     elif user_choice == "2":
#         remove_name = input("Name of participant to remove >>>  ")
#         if remove_name in participants:
#             participants.remove(remove_name)
#             print("Participant removed successfully")
#             continue

#         print("Participant not found in list")
        
#     elif user_choice == "3":
#         print("===============List of participants==============")
#         for num, name in enumerate(participants, start=1):
#             print(num, name)
#         print("=================================================")
#     # elif user_choice == "Q" or user_choice == "q":
#     elif user_choice == "Q":
#         print("Thank you for using our program")
#         break
#     else:
#         print("Please enter right choice. (1-3/Q)")
        
        
# # Tuple
# final_participants = tuple(participants)

# print("final", final_participants)


# ['ram', 'hari'] => list can be modified, mutable
# ('ram', 'hari') => tuple cannot be modified once created, immutable 

# final_participants = ("ram", "hari", "seeta", "geeta")

# # final_participants.append("Shyam")

# print(final_participants[1])
# final_participants[1] = "Shyam"
# print(final_participants[1])

# participants = ["ram", "hari"]

# for num, name in enumerate(participants, start=1):
#     print(num, name)


# a, *mids ,b = 1, 2, 3, 4, 5, 6, 7, 8

# print(a)
# print(mids)
# print(b)