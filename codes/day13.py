# import os


# products = [
#     {"name": "watch", "price": 899},
#     {"name": "laptop", "price": 89999},
#     {"name": "mobile", "price": 9990},
#     {"name": "t-shirt", "price": 999},
# ]

# [
#     "watch",
#     "laptop",
#     "mobile",
#     "t-shirt"
# ]

# def show_products(products):
#     os.system("clear")
#     print("Products Table".center(30, "-"))
    
#     for sn, product in enumerate(products, start=1):
#         print(f"{sn}. {product["name"]} -> {product["price"]}")
        
#     print("-"*30)

# 1. Display all product names using map().
# product_names = list(map(lambda product : product["name"], products))
# print(product_names)

# 2. Search for a product by name using filter().
# Exact search
# search_result = list(filter(lambda product: product["name"]==search_input , products))
# def search_by_name():
#     search_input = input("Enter a product name to search: ")
#     search_result = list(filter(lambda product: search_input in product["name"] , products))
#     show_products(search_result)

# if len(search_result) == 0:
#     print("No product found ! ")
# else:
#     show_products(search_result)


# # 3. Sort products by price from low to high.
# def low_to_high():
#     low_to_high = sorted(products, key=lambda product: product["price"])
#     show_products(low_to_high)

# 4. Sort products by price from low to high.
# def high_to_low():
#     high_to_low = sorted(products, key=lambda product: product["price"], reverse=True)
#     show_products(high_to_low)

# 5. Filter products whose price is less than or equal to a given value.
# def show_by_max_price():
#     input_price = float(input("Enter price: "))
#     results = filter(lambda product: product["price"]<=input_price , products)

#     show_products(results)


# MENU = """
#     1) Show all products
#     2) Search product by name
#     3) Sort products by price from low to high
#     4) Sort products by price from high to low
#     5) Filter products by max_price
#     6) Exit
# """

# while True:
#     print(MENU)
    
#     user_choice = input("Enter your choice: ")
    
#     if user_choice == "6":
#         break
#     elif user_choice == "1":
#         show_products(products)
#     elif user_choice == "2":
#         search_by_name()
#     elif user_choice == "3":
#         low_to_high()
#     elif user_choice == "4":
#         high_to_low()
#     elif user_choice == "5":
#         show_by_max_price()
#     else:
#         print("Please enter a correct choice")



# File Handling
# Data stored in variables are temporary, because they are stored in RAM.
# Permanent storage using different files
# Text file (.txt), CSV file, (comma separated value),
# ram, 56, 98000000, kathmandu

# basic file modes
# 1. Read -> "r"
# 2. Write -> "w"
# 3. Append -> "a"

# Writing to a file
# with open("demo.txt", "w") as file:
#     file.write("Welcome guys, this is our new content, updated")


# with open("/home/prakash/Desktop/demo.txt", "w") as file:
#     file.write("""
# Welcome guys, 
# this is our new content, 
# updated
# """)


# Reading from a file
# with open("/home/prakash/Desktop/demo.txt", "r") as file:
#     # content = file.read()
#     # print(repr(content))
#     # print(file.readlines())
#     for line in file.readlines():
#         # print(repr(line))
#         print(line)
# with open("demo.txt", "a") as file:
#     file.write("\nThis is another added content")    



# search_pass = input("Enter your password to test: ")

# with open("passwords.txt", "r") as file:
#     for line in file.readlines():
#         if search_pass == line.strip():
#             print("Your password is in the list, please update it to the newer one")
#             break
#     else:
#         print("Congrats, your password is kind of safe")


# import sys

# def clear_last_line(n=1):
#     # Move up to the previous line and clear it
#     for _ in range(n):
#         sys.stdout.write('\033[A\033[2K')
#     sys.stdout.flush()

# # Your print output
# print("""
#    asdf
#    asd
#    f
#    asd
#    f
#    asd
#    f
#    yaha samma
#    """)

# # Clear the last actual line of text (need to go up past empty lines)
# clear_last_line(4)  # clears empty line