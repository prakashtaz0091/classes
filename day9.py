# Functions
# def add(a, b, c):
#     print(a + b + c)


# add(5, 4, 5)


# *args -> * means any, args means arguments
# *numbers  -> numbers is just a parameter name. No different than previous. But, the * symbol we see here, it represents that this parameter can take any number of positional arguments
# def add(*numbers):
#     print(numbers)
# print(type(numbers))
# print(sum(numbers))


# add(0, 3, 4, 5, "ram") # here we are just passing data/values, these type of arguments are called positional arguments
# print(sum((0, 3, 4, 5)))


# def show_details(*data):
#     print(data)


# here name="ram", name is keyword and "ram" is value/data to be passed. These type of arguments are called keyword arguments
# In short, we say kwargs
# show_details(name="ram")


# **kwargs
# def show_details(**data):
#     # print(data)
#     for key, value in data.items():
#         print(key, " => ", value)


# show_details(name="ram", phone="9800000", address="KTM", postal_code=52000)


###############################
###############################
###############################
###############################
###############################
###############################
# Mini Student Tracker
MENU = """
    1. Add Student Data
    2. Show all students data
    3. Remove student data
    Q. Quit
"""
students = []


def show_menu():
    print(MENU)


def show_all_students_data():
    print("###############################")
    print("###-----STUDENTS DATA ----####")
    for student in students:
        print(f"##  Name: {student["name"]} ")
        print(f"##  Age : {student["age"]} ")
        print("----------------------------")

    print("####  -----  END -------  #####")
    print("###############################")


def add_student():
    name_input = input("Enter name: ")
    age_input = input("Enter age: ")

    new_student = {"name": name_input, "age": age_input}
    students.append(new_student)


def remove_student():
    name_to_remove = input("Enter student name to remove: ")
    for student in students:
        # check if student name is stu_name_to_remove
        if student["name"] == name_to_remove:
            students.remove(student)
            break


# Main loop
while True:
    # 1. Show menu to the user
    show_menu()

    # 2. Take input from user
    user_choice = input("Enter your choice (1/2/3/Q) >>> ")

    # if user_choice == "Q" or user_choice == "q":
    if user_choice in ("Q", "q"):
        print("Thank you for using our program")
        break

    elif user_choice == "1":
        add_student()
        # ask if user wants to enter another student data
        # if yes=> run add_student() again. Hint, use while loop

    elif user_choice == "2":
        show_all_students_data()

    elif user_choice == "3":
        remove_student()

    else:
        print("Invalid input ! Please read the instructions carefully ")


"""
# Structure of students list
[
    {
        "name":"Ram",
        "age": "23"
    },
    {
        "name":"Ram",
        "age": "23"
    },
    {
        "name":"Ram",
        "age": "23"
    },
    {
        "name":"Ram",
        "age": "23"
    }
    
]


[s1, s2, s3, s3, s4, s5]
for -> 5
if s1["name"] == name_to_remove:
    students.remove(student)
    break

s1 = {
        "name":"Ram",
        "age": "23"
    }
    
s2 = {
        "name":"Ram",
        "age": "23"
    }
    
 students =    ["ram", "hari"]
    
    students.remove({
        "name":"Ram",
        "age": "23"
    })
    
"""
