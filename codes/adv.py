# Comprehensions

# Comprehensions are a concise way to create lists in Python. They consist of a single expression inside square brackets [], which includes an iterable, a loop variable, and an optional condition. The expression is evaluated for each item in the iterable, and if the condition is met, the item is added to the resulting list.

# l = [1, 2, 3, 4]

# sq_list = []

# for number in l:
        #something complex
#     sq_list.append(number**2)

# map()
# sq_list = [number**2 for number in l]
#      keep square of number from each number in list 'l'

# print(sq_list)

# filter()
# l = [1, 2, 3, 4]
# odd_list = []

# for number in l:
#     # something complex
#     if number % 2 == 1:
#         odd_list.append(number)

#  ? keep | where does it come from | which value to keep
# odd_list = [number for number in l if number % 2 == 1]

# print(odd_list)


# Set comprehension


# s = {1, 2, 3, 4}

# odd_s = {number for number in s if number % 2 == 1}

# print(odd_s)
# import pprint


# Dictionary comprehension

# english_to_nepali_days = {
#     "sunday": "आइतबार",
#     "monday": "सोमबार",
#     "tuesday": "मंगलबार",
#     "wednesday": "बुधबार",
#     "thursday": "बिहीबार",
#     "friday": "शुक्रबार",
#     "saturday": "शनिबार"
# }

# nepali_to_english_days = {
#     value : key
#     for key, value in english_to_nepali_days.items()
# }

# print(nepali_to_english_days)
# pprint.pprint(nepali_to_english_days)

# print(d["friday"])


# life_to_emoji = {
#     10: "🤩", # Peak happiness / Over the moon
#     9:  "😄", # Very happy
#     8:  "😊", # Content / Smiling
#     7:  "🙂", # Doing well
#     6:  "😐", # Neutral / "It's a day"
#     5:  "😕", # Slightly bummed
#     4:  "😟", # Worried / Unhappy
#     3:  "☹️", # Sad
#     2:  "😢", # Crying
#     1:  "😭"  # Maximum sadness / Heartbroken
# }

# emoji_to_life = {
#     emoji : life
#     for life, emoji in life_to_emoji.items()
# }

# print(emoji_to_life)


# pprint.pprint(emoji_to_life)

#--------------------------------------------------------------
# Iterators and Generators


# l = [1, 2, 3, 4]

# for num in l:
#     print(num)

# l = [1, 2, 3, 4]

# li = iter(l)

# print(li)
# print(next(li)) # 1
# print(next(li)) # 2
# print(next(li)) # 3
# print(next(li)) # 4
# print(next(li)) # no value

# for num in li:
#     print(num)

# products = [
#     {
#         "name": "iphone",
#         "images": [
#             "https://example/image.png", 
#             "https://example/image1.png",
#             "https://example/image2.png",
#             "https://example/image3.png",
#         ]
#     },
#     {
#         "name": "jphone",
#         "images": [
#             "https://example/jmage.png", 
#             "https://example/jmage1.png",
#             "https://example/jmage2.png",
#             "https://example/jmage3.png",
#         ]
#     }   
# ]

# product_images = [
#     image
#     for product in products
#     for image in product["images"]
# ]

# print(product_images)


#  Generator
# def natural_number():
#     num = 1
    
#     while True:
#         yield num   # num deu and wait
#         num = num + 1
        
        
# nat_num = natural_number()

# print(next(nat_num))
# print(next(nat_num))
# print(next(nat_num))
# print(next(nat_num))
# print(next(nat_num))
# print(next(nat_num))
# print(next(nat_num))
# print(next(nat_num))
# StopIteration

# for num in nat_num:
#     print(num)

# for _ in range(100000):
#     print(next(nat_num))

# def c_range(*args):
#     step = 1
    
#     if len(args) == 1:
#         start = 0
#         stop = args[0]
        
#     elif len(args) == 2:
#         start = args[0]
#         stop = args[1]
        
#     elif len(args) == 3:
#         start = args[0]
#         stop = args[1]
#         step = args[2]
        
#     while start < stop:
#         yield start
#         start = start + step
        
        
# for num in c_range(2, 10, 2):
#     print(num)


# Decorator
# def decorator_dai(gift_func):
#     def wrapper_func():
#         print("sticker")
#         print("Wrapping paper at top")
#         gift_func()
#         print("Wrapping paper at bottom")
    
#     return wrapper_func
        

# @decorator_dai
# def gift():
#     print("Cup set")
    

# @decorator_dai
# def flowers():
#     print("Flowers")
    
# gift()
import time

def check_exe_time(func):
    def wrapper_func():
        start_time = time.time()
        func() 
        end_time = time.time()
        exe_time = end_time-start_time
        print(f"Execution time, approx. {exe_time:.2f}", )

    return wrapper_func


@check_exe_time
def highly_complex():
        time.sleep(5)
        print("this is time consuming task")
        
        

highly_complex()