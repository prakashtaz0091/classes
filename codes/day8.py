# from datetime import datetime

# # calulate age

# today = datetime.today()
# today_date = today.date()

# birth_date = input("Enter your birth-date [yyyy-mm-dd]: ")
# actual_birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()


# date_diff = today_date - actual_birth_date

# print(date_diff)

# years = date_diff.days//365
# remaining_days = date_diff.days%365

# months = remaining_days//30

# days = remaining_days%30

# print(years)
# print(months)
# print(days)


# print(type(today_date))
# print(type(birth_date))
# print(type(actual_birth_date))

# print(actual_birth_date)

# age = today_date - birth_date

# print(age)

# print(birth_date)

# print(today_date)


# from dateutil.relativedelta import relativedelta
# from datetime import datetime

# # calulate age

# today = datetime.today()
# today_date = today.date()

# birth_date = input("Enter your birth-date [yyyy-mm-dd]: ")
# actual_birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()


# date_diff = relativedelta(today_date, actual_birth_date)

# print(date_diff.years)
# print(date_diff.months)
# print(date_diff.days)


# OTPs -> expiry time
# otp = {
#     "value": "123789",
#     "created_at": datetime,
#     "expires_at": datetime
# }

# from datetime import datetime, timedelta
# import time

# otp = {
#     "value": "123456"
# }

# now = datetime.now()
# # print(now)

# otp["created_at"] = now

# expiry_time = now + timedelta(seconds=2)

# otp["expires_at"] = expiry_time

# print(otp)


# time.sleep(5)


# # otp verification
# if otp["expires_at"] < datetime.now():
#     print("Expired")
        # message()
# else:
#     print("Verified")


import random

# print(random.randint(1,10))

# secret_number = random.randint(1,10)

# life = 5

# while True:
#     print("Life: ", life)
#     user_guess = int(input("Guess the secret: "))

#     if user_guess == secret_number:
#         print("You won the game")
#         break
#     else:
#         life -= 1
#         if life == 0:
#             print("You lost the game")
#             break
#         print("Wrong guess, please try again")


# coupons = ["120312392394", "19284792834", "1982739182", "29837983745"]

# winner = random.choice(coupons)
# print(winner)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q"]

random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)
random.shuffle(cards)
print(cards)


ram = cards[0:3]
hari = cards[3:6]
ramesh = cards[6:9]

print(ram)
print(hari)
print(ramesh)

