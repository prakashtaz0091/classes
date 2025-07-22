balance = 5000


def withdraw(amount):
    global balance
    if amount > balance:
        raise Exception("Insufficient balance to withdraw")

    balance = balance - amount
    print("Withdraw successful")


try:
    withdraw(6000)
except Exception as e:
    print(e)
