# for -> for loop
# if  -> if
# while -> while

# for i in range(3):
#     for j in range(3):
#         print("i  = ", i, "j = ", j)
#     print("End of inner for loop")


# print("End of outer for loop")

# remove countries that starts with C
# step 1: pick one country name
# step 2: check if country name starts with 'C'
# step 3: if starts with 'C' -> then remove it
# step 4: Follow step 1 to 3 until all country names are picked

# countries = ["America", "Canada", "Australia", "China", "India", "Chile"]
# # countries = ["America", "Australia"]
# #   "China"

# new_countries = [
#     "America",
# ]
# for country in countries:
#     if not country.startswith("C"):
#         new_countries.append(country)
#         # print(country)

# print(new_countries)

# set_a = {1, 2, 3}
# set_b = {2, 3, 4}

# print(set_b - set_a)


# Guess a secret number
"""
1. Ask user to guess the secret number
2. Check if user's guess is correct
3. If user's guess is correct, then show "WIN", and end the gameloop
4. If user's guess is wrong, repeat from step 1
"""
secret_number = 10
LIFE = 5
# WIN = False

# while not WIN:
#     # Ask user to guess the secret number
#     user_guess = int(input("Try to guess the secret number : "))

#     # Check if user's guess is correct
#     if user_guess == secret_number:
#         WIN = True
#         print("Congrats, you won !!")
#     else:
#         print("Uff, wrong guess. Please try again")

# print("Game ended successfully")


# while True:  # Run infinitly
#     # Ask user to guess the secret number
#     user_guess = int(input("Try to guess the secret number : "))

#     # Check if user's guess is correct
#     if user_guess == secret_number:
#         print("Congrats, you won !!")
#         break  # break means, go out of the loop
#     else:
#         print("Uff, wrong guess. Please try again")

# print("Game ended successfully")


# Check if user's guess is correct
# if user_guess == secret_number:
#     print("Congrats, you won !!")
#     break  # break means, go out of the loop
def user_guess_is_correct(user_guess):
    if user_guess == secret_number:
        return True
    else:
        return False


def show_congrats_message():
    print(
        """
         ################################# 
                        😊
                  Congratulations
                       You Won
          
        ################################
          """
    )


def show_try_again_message():
    if LIFE == 1:
        print(
            f"""
            ################################# 
                            😔
                Sorry, your guess is wrong
                    Please Try Again !!!
                     LAST ATTEMPT LEFT
            
            ################################
            """
        )
    else:
        print(
            f"""
            ################################# 
                            😔
                Sorry, your guess is wrong
                    Please Try Again !!!
                    LIFE remaining : {LIFE}
            
            ################################
            """
        )


while LIFE > 0:
    user_guess = int(input("Try to guess the secret number : "))

    if user_guess_is_correct(user_guess):
        show_congrats_message()
        break
    else:
        LIFE = LIFE - 1
        show_try_again_message()


if LIFE == 0:
    print("You lost the game")
