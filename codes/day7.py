from bill import show_bill_summary

user_bag = {}

MENU = """
    1. Add item to cart
    2. Show bill summary
    3. Quit

"""

while True:
    print(MENU)
    
    user_choice = input("choice >>> ")
    
    if user_choice == "1":
        item_name = input("Item name: ")
        item_price = float(input("Item price: "))
        item_quantity = int(input("Item quantity: "))
        user_bag[item_name] = {
            "label": item_name.capitalize(),
            "price": item_price,
            "quantity": item_quantity
        }
        
    elif user_choice == "2":
        show_bill_summary(cart=user_bag)
    elif user_choice == "3":
        break
    else:
        print("Invalid choice. Please enter [1-3]")
        
        
