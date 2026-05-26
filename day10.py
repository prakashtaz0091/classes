# 1. Reading a Text File
# with open("mytext.txt", "r") as file:
#     content = file.read()

# print(content)

# EOF 
# with open("/home/prakash/Desktop/demo texts/new.txt", "r") as file:
#     # content = file.read()
#     for line in file.readlines():
#         print('line sep------------------')
#         print(line)  

# print(content)
# 1 -> aa 

# 1 -> aa

# WPA/WPS tester
# admin123 -> 2123efa02364 ? kun tariya? algorithm
# wifi_password = "2123efa02364"  # hash

# with open("/home/prakash/Desktop/demo texts/passwords.txt", "r") as passwords_file:
    # print(type(passwords_file))
    
    # for password in passwords_file:
    #     cleaned_pass = password.strip()
    #     # hash_value = caculate_hash(cleaned_pass) -> 2123efa02364
    #     if cleaned_pass == wifi_password:
    #         print("password found", password)
        

# # number guessing game
# import random

# # Generate random number between 1 and 100
# secret_number = random.randint(1, 100) # 20

# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100")

# with open("guess_game_record.txt", "r") as file:
#     current_min_guess = file.read()
        

# if current_min_guess.strip() == "0":
#     print("No players till now. be the first to score")
# else:
#     print("Minimum guess till now: ", current_min_guess)

# counter = 0
# while True: # Game loop
#     guess = int(input("Enter your guess: "))

#     counter += 1
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break


# print("You made successful guess after ", counter, " times")
# print("Minimum guess till now ", current_min_guess)

# if int(current_min_guess) == 0 or counter < int(current_min_guess):
#     with open("guess_game_record.txt", "w") as file:
#         file.write(str(counter))


# with open("web_logs.txt", "a") as file:
#     user_inputs = []
#     while True:
#         user_input = input("(q for quit)>>> ").lower()
#         if user_input == 'q':
#             break
#         user_inputs.append(f"{user_input}\n")
        
#     file.writelines(user_inputs)



# import csv

# with open("class6_marks.csv", "r") as file:
#     reader = csv.reader(file, delimiter="|")
#     header = next(reader) # reader will return first row
#     for row in reader:
#         # print(row)
#         name = row[0]
#         marks = row[1:]
        
#         print("student ", name)
#         print("marks ", marks)
        
#         total = 0
#         no_of_sub = len(marks)
#         for mark in marks:
#             int_mark = int(mark)
#             total += int_mark
        
#         percentage = total/no_of_sub
#         print(name, percentage, "%")
         

# print(0 & 0)   
# print(0 & 1)   
# print(1 & 0)   
# print(1 & 1)   
# print(2 & 2)   
# print(5 & 5)   101 & 101 
# print(5 & 2)   101 
#                010
# print(5 & 3)   #  101 * 011
#                  011
#                  001
    # #101 => 1*2^2 + 0*2^1 + 1*2^0
    #         4   +   0    + 1 => 5     1   0
        # 64    32    16    8    4     2     1
        #                        1     0      1  => 5
        #                        0     1      1  => 3
        #                        0     0      1                         1    1      1
                        1    0    0    1      1
        
# 5 -> 101
# 3 -> 011
#      001
# AND -> ? All must be true => True         


# print(5 & 5)
# 101
# 101
# 101
# print(5 | 3) # OR
# 101
# 011
# 111

# print(5>>1)
# 101 -> 1
# 10
# 111 
# 001

# 7 % 2 == 0 # => even

# 9 & 1
# 1001
# 0001
# 0001 => Ans 

# res = 7 & 1
# print(res)

