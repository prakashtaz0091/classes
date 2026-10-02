# Repeated/ Reusable
# a = 10

# DRY -> Don't Repeat Yourself
# def send_mail(): # function defination
#     print("finding user from db")
#     print("check if user email is verified")
#     print("check if user email is active/online")
#     print("Prepare mail message")
#     print("Mail sending")
#     print("Mail sent")



# send_mail() # function call






# send_mail() # function call









# print("finding user from db")
# print("check if user email is verified")
# print("Prepare mail message")
# print("Mail sending")
# print("Mail sent")








# print("finding user from db")
# print("check if user email is verified")
# print("Prepare mail message")
# print("Mail sending")
# print("Mail sent")




# def send_mail(name, order_status): # function defination
#     print(f"Sending email to {name}, status '{order_status}'")



# value we pass/send to function is called as argument
# send_mail("Hari", "order placed") # function call
# send_mail("Reeta") # function call

# in above example, the arguments are based on position, therefore these type of arguments are called as positional arguments

# send_mail("Hari", "in-transit") # function call
# send_mail("in-transit", "Hari") # function call

#
# send_mail(order_status="in-transit", name="Hari") # function call
# in above example, the arguments are based on parameter name, therefore these type of arguments are called as keyword arguments



# greeting="Hello", here it is called as default argument
# def send_mail(name, order_status, greeting="Hello"): # function defination
#     print(f"{greeting}, {name}")
#     print(f"Your order status : '{order_status}'")
    
    

# send_mail(
#     name="Hari",
#     order_status="delivered",
#     # greeting="Good morning"
#     )


# def send_mail(name, order_status, greeting="Hello"): # function defination
#     print(f"{greeting}, {name}")
#     print(f"Your order status : '{order_status}'")
    
#     return "Your task has started"

    

# response = send_mail(
#         name="Hari",
#         order_status="delivered",
#         greeting="Good morning"
#     )

# print("Response:", response)

# def add(a, b):
#     result = a+b
#     # print(result)
#     return result
#     # return None
    
# add_result = add(5,60)

# x = add_result * 70
# print(x)


# def add_sub(a,b):
#     a_result = a+b
#     s_result = a-b
#     m_result = a*b
    
#     return a_result, s_result, m_result


# result = add_sub(5,6)
# a, s, m = add_sub(5,6)

# a, s = (11, -1)
# a, s, m = result

# print(result)


# def send_mail(name, order_status, greeting="Hello", a = "1", b="5"): # function defination
#     print(f"{greeting}, {name}")
#     print(f"Your order status : '{order_status}'")
    
#     return "Your task has started"


# send_mail(
#     "hari",
#     "placed",
#     greeting="Good moring",
#     b="6"
# )