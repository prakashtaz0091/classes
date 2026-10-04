DISCOUNT_PERCENTAGE = 5 
TAX_PERCENTAGE = 13 

def calculate_item_total(item_name, cart):
    price = cart[item_name]["price"]  
    quantity = cart[item_name]["quantity"]  

    return price*quantity
    

def calculate_subtotal(cart):
    subtotal = 0 
    for item in cart.keys():
        item_total = calculate_item_total(item, cart)
        subtotal += item_total
    
    return subtotal

def calculate_discount(cart):
    subtotal = calculate_subtotal(cart)
    discount_amount = subtotal * DISCOUNT_PERCENTAGE/100
    return discount_amount

def calculate_amount_after_discount(cart):
    return calculate_subtotal(cart) - calculate_discount(cart)
        
def calculate_tax(cart):
    tax_amount = calculate_amount_after_discount(cart) * TAX_PERCENTAGE/100
    
    return round(tax_amount, 2)
    
    
def calculate_final_amount(cart):
    tax_amount = calculate_tax(cart)
    
    final_amount = calculate_amount_after_discount(cart) + tax_amount
    
    return round(final_amount, 2)

def show_bill_summary(cart):
    
    cart = {}

    bill_draft = """
    ==============================
        BILL SUMMARY
    ==============================

    """

    for item_key in cart.keys():
        item_summary = f"""
        Product: {cart[item_key]["label"]}
        Price: Rs. {cart[item_key]["price"]}
        Quantity: {cart[item_key]["quantity"]}
        Total: Rs. {calculate_item_total(item_key, cart)}
        """
        
        bill_draft += item_summary    


    bill_draft += f"""
    ------------------------------
        Subtotal: Rs. {calculate_subtotal(cart)}
        Discount ({DISCOUNT_PERCENTAGE}%): Rs. {calculate_discount(cart)}
        Tax ({TAX_PERCENTAGE}%) : Rs. {calculate_tax(cart)}
    ------------------------------
        Final Amount: Rs. {calculate_final_amount(cart)}
    ==============================

    """
    
    print(bill_draft)

