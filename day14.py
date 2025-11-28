# Attributes types according to access level
# 1. Public
# 2. Protected
# 3. Private

# data -> saman
# Class -> Ghar
# water tap -> public
# Flowers -> protected
# Impt documents, -> private


# class BankAccount:
#     bank_name = "ABC Bank"

#     def __init__(self, account_no, deposit_balance):
#         self.account_no = account_no
#         self.balance = deposit_balance

#     def show_info(self):
#         print("Account No: ", self.account_no)
#         print("Balance: ", self.balance)


# account1 = BankAccount("0123", 1000)

# print(account1.account_no)
# account1.account_no = "012345"

# account1.show_info()
"""
In above example, account_no (data member) can be accessed directly outside the class, so these types of data members are called as public data attributes

"""


# class BankAccount:
#     bank_name = "ABC Bank"

#     def __init__(self, account_no, deposit_balance):
#         self._account_no = account_no
#         self.balance = deposit_balance

#     def show_info(self):
#         print("Account No: ", self._account_no)
#         print("Balance: ", self.balance)


# account1 = BankAccount("0123", 1000)

# print(account1._account_no)
# account1._account_no = "012345"

# account1.show_info()
"""
Here above, now we changed 'account_no' to '_account_no', which gives python developers a hint, saying that its protected, it shouldn't be used outside the class directly, or at least be careful.
"""

############################################


class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, account_no, deposit_balance):
        self.__account_no = account_no
        self.__balance = deposit_balance

    # getter
    @property  # property is just a variable, and it's dynamic
    def account_no(self):
        return f"XXXXXXXX{self.__account_no[-2:]}"

    # getter
    @property  # property is just a variable, and it's dynamic
    def balance(self):
        return f"Rs. {self.__balance}"

    @balance.setter
    def balance(self, new_balance):
        # if isinstance(new_balance, int):
        #     self.__balance = new_balance
        #     print("balance set")
        # else:
        #     print("new_balance is inappropriate data")
        if not isinstance(new_balance, (int, float)):
            raise Exception("Got inappropriate value for balance")

        # self.__balance = self.__balance + new_balance
        self.__balance += new_balance

    def show_info(self):
        print("Account No: ", self.__account_no)
        print("Balance: ", self.__balance)


account1 = BankAccount("1234567867", 1000)
"""
Here to maintain strict no access, python changes the name '__account_no' to '_BankAccount__account_no'. This process of renaming private attributes/data members is called as name mangling
"""

# Never ever access private variables like below.
# print(account1._BankAccount__account_no)
# account1.__account_no = "012345"

# account1.show_info()

# print(account1.account_no)


# account1.account_no = "laksdjlk"


# print(account1.account_no)


while True:
    try:
        balance = float(input("Enter balance to deposit: "))
        account1.balance = balance
    except Exception:
        print("Invalid value")
    else:
        print("balance deposited successfuly")
        print("Your new balance is: ")
        print(account1.balance)
        break

"""
      01234
ac = "1234567867"
             -3 -2 -1

ac[start_index:stop_index]
ac[2:4] => "34"
ac[2:] => 2 index to end => "34567867"
ac[:4] => start to 3rd index => "1234"
ac[:] => start to end => make new copy

ac[-2:]

f"XXXXXXXX{ac[-2:]}"

"""
