# OOP continued

class BankAccount:
    currency_options = [
        ("NPR", "Rs.", 1),
        ("USD", "$", 0.006), # 
        ("INR", "Re.", 1/1.6), # 
    ]
    bank_name = "XYZ Bank Pvt. Ltd."
    
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        
        # if balance is not an integer
        if not isinstance(balance, (int)):
            raise Exception("Balance must be a valid positive integer value")

        # if balance is negative value
        if balance < 0:
            raise Exception("Balance must be a valid positive integer value")        

        # Note: single underscore in front of attribute name -> protected
        # Note: double underscore in front of attribute name -> private
        self.__balance = balance # always in NPR        
        self.display_currency = BankAccount.currency_options[0]
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_value):
        # if balance is not an integer
        if not isinstance(new_value, (int)):
            raise Exception("Balance must be a valid positive integer value")

        # if balance is negative value
        if new_value < 0:
            raise Exception("Balance must be a valid positive integer value") 
        
        self.__balance = new_value 
        
    def get_currency_display(self):
        # ("NPR", "Rs.")
        # ("USD", "$")
        return self.display_currency[1]
    
    def get_balance_display(self):
        return self.__balance * self.display_currency[2]
    
    def show_account_details(self):
        print(f"""
            ====================================  
              Bank Name   : {self.bank_name}
              Account Name: {self.owner_name}
              Balance     : {self.get_currency_display()} {self.get_balance_display()}
            ====================================
              """)
   
   
   
    
a1 = BankAccount("Ram", 1500)
# a2 = BankAccount("Hari", 1500)
# a3 = BankAccount("Shyam", 1500)

# print("Balance of account a1 ", a1.balance)
# print("Balance of account a2 ", a2.balance)

# a1.display_currency = BankAccount.currency_options[1] # USD
# a1.show_account_details()

# a2.show_account_details()

# a3.display_currency = BankAccount.currency_options[2] # INR
# a3.show_account_details()
# BankAccount.show_account_details(a1)

# Access (public, protected, private)
# a1.balance = -1500 # public attribute
# a1._balance

# a1.show_account_details()

# a1.__balance = -1500
# a1.new_var = 60000

# print(a1.__balance, a1.new_var)


# a1.show_account_details()

# print(a1.__balance)
# Name Mangling
# _BankAccount__balance
# a1._BankAccount__balance = -1500
# print(a1._BankAccount__balance)
# a1.show_account_details()
# a1.balance = "abc"
# print(a1.balance)
# a1.set_new_balance(1500)

# l1.append()
# l2.append()
# l.remove()

# Encapsulation - Data protection as well as data and method bundling
# Abstraction - Hiding complexity, and giving easy access outside the class
# Inheritance - Copying properties of a class
# Polymorphism - Single code, but many forms, (according to object)

# len("alsdkfj l") -> 9
# len(["ram", "shyam", "hari"]) -> 3

# +, -, / , *
