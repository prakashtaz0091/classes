# basic otp generation
# import random

# # Generate 6-digit OTP
# otp = random.randint(100000, 999999)

# print("Your OTP is:", otp)



# number guessing game
# import random

# # Generate random number between 1 and 100
# secret_number = random.randint(1, 100) # 20

# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100")

# while True: # Game loop
#     guess = int(input("Enter your guess: "))

#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break


# number guessing game with max-life
# import random

# # Generate random number between 1 and 100
# secret_number = random.randint(1, 100)

# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100")

# life = 5

# life_to_emotion = {
#     5: "😊",
#     4: "😃",
#     3: "😐",
#     2: "😔",
#     1: "😢"
# }


# while life>0: # Game loop
    
#     print("LIFE :: ", life, life_to_emotion[life])
    
#     guess = int(input("Enter your guess: "))

#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break
    
#     life -= 1


# Cards shuffler
# import random

# Deck of cards using emojis
# suits = ["♠️", "♥️", "♦️", "♣️"]
# ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# def get_random_card():
#     return f"{random.choice(suits)} {random.choice(ranks)}"

# first_card = get_random_card()
# second_card = get_random_card()
# third_card = get_random_card()

# print(first_card, second_card, third_card)

# import random

# suits = ["♠️", "♥️", "♦️", "♣️"]
# ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# all_cards = []
# for suit in suits:
#     print("===================================")
#     for rank in ranks:
#         card = f"{suit} {rank}"
#         print(card)
#         all_cards.append(card)
#     print("===================================")

# # print(all_cards)
# random.shuffle(all_cards)
# random.shuffle(all_cards)
# random.shuffle(all_cards)
# # print(all_cards)

# print("Prakash =>", all_cards[0]) # top
# print("Hari =>", all_cards[1]) # second
# print("Ramesh =>", all_cards[2]) # third


# Birthday calculator
# from datetime import datetime, date
# from dateutil.relativedelta import relativedelta

# # Single input from user
# dob_input = input("Enter your birthdate (YYYY-MM-DD): ")
# # "2000-01-01" -> date type 

# # Convert string to date
# # birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
# # print(birth_date, type(birth_date))
# birth_date = datetime.strptime(dob_input, "%Y-%m-%d").date()
# # print(birth_date, type(birth_date))

# # Today's date
# today = date.today()

# # Calculate difference
# age = relativedelta(today, birth_date)

# # Display result
# print(f"Age: {age.years} years, {age.months} months, {age.days} days")

# if age.years >= 18:
#     print("Yes you can apply for citizenship")
# else:
#     print("No, you can't apply for citizenship. Reason: under age")


    
# Measure execution time
# import time

# start = time.time()

# # some task
# # for i in range(1000000):
# #     pass
# time.sleep(5)

# end = time.time()

# print("Time taken:", end - start, "seconds")

# import time
# import os

# GREEN = '\033[92m'
# num = 10
# while num>0:
#     os.system("clear")
#     print(f"{GREEN} {num}")
#     time.sleep(1)
#     num -= 1




# file organizer
import os

# Folder to organize (change this path)
folder_path = "/home/prakash/Downloads"

# Get all files in folder
files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)
    print("file path ", file_path)

    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file)
    ext = ext[1:]  # remove dot (e.g. ".txt" → "txt")

    if ext == "":
        ext = "no_extension"
        continue
    
    # Create folder for this extension
    target_folder = os.path.join(folder_path, ext)
    print("target folder ", target_folder)

    # check if ext folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Move file
    # "test_folder/new.txt"
    # "test_folder/txt/new.txt"
    
    new_path = os.path.join(target_folder, file)
    print("new path ", new_path)
    
    os.rename(file_path, new_path)

print("Files organized successfully!")

"""
os.listdir() → list files
os.path.join() → safe path building
os.path.exists() → check folder exists
os.makedirs() → create folders
os.rename() → move files
"""


