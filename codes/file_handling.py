# CSV file, (comma seperated value)

# ram,12,ktm
# ram|12|ktm

import csv

# with open("students.csv", "w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["ram", 12, "kathmandu"])
    
#     students = [
#         ["hari", 14, "pokhara"],
#         ["ramesh", 14, "biratnagar"],
#         ["roshan", 18, "birtamode"],
#         ["shrawan", 22, "butwal"],
#     ]
#     csv_writer.writerows(students)

# students = {
#     ["hari", 14, "pokhara"],
# }

# Without HEAder

# with open("students.csv", "r") as file:
#     # students = list(csv.reader(file, delimiter="|"))
#     students = list(csv.reader(file))

# while True:
#     print("""
#           1) New student
#           2) Show all student
#           #) Exit
#           """)
    
#     user_choice = input("Enter your choice: ")
    
#     if user_choice == "1":
#         print("New Student Entry".center(40, "-"))
#         new_name = input("Name: ")
#         new_age = int(input("Age: "))
#         new_address = input("Address: ")
        
#         new_student = [new_name, new_age, new_address]
#         students.append(new_student)
        
#     elif user_choice == "2":
#         print("Show all students")
#         for student in students:
#             print(student)
            
#     elif user_choice == "#":
#         print("Exit")
#         print("Wait....saving data for long term use")
        
#         with open("students.csv", "w") as file:
#             # csv_writer = csv.writer(file, delimiter="|")
#             csv_writer = csv.writer(file)
#             csv_writer.writerows(students)
        
#         break

# string = "qwer|123|qwer"
# print(string.split("|"))

##########################################################
##########################################################
# With header (Manual)
##########################################################
##########################################################

# HEADERS = ["Full Name", "Age", "Address"]

# with open("students.csv", "r") as file:
#     # students = list(csv.reader(file, delimiter="|"))
#     # students = list(csv.reader(file))
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)
    

# while True:
#     print("""
#           1) New student
#           2) Show all student
#           #) Exit
#           """)
    
#     user_choice = input("Enter your choice: ")
    
#     if user_choice == "1":
#         print("New Student Entry".center(40, "-"))
#         new_name = input("Name: ")
#         new_age = int(input("Age: "))
#         new_address = input("Address: ")
        
#         new_student = [new_name, new_age, new_address]
#         with open("students.csv", "a") as file:
#             # csv_writer = csv.writer(file, delimiter="|")
#             csv_writer = csv.writer(file)
#             csv_writer.writerow(new_student)
        
#     elif user_choice == "2":
#         with open("students.csv", "r") as file:
#             print("Show all students")
#             reader = csv.reader(file)
#             for line in reader:
#                 print(line)
            
#     elif user_choice == "#":
#         print("Exit")    
        
#         break


##########################################################
##########################################################
# With header (using dictionary)
##########################################################
##########################################################
HEADERS = ["Full Name", "Age", "Address"]

def create_header_if_not_exist():
    with open("students.csv", "r+") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
        if header is None:
            csv_writer = csv.writer(file)
            csv_writer.writerow(HEADERS)

create_header_if_not_exist()

while True:
    print("""
          1) New student
          2) Show all student
          #) Exit
          """)
    
    user_choice = input("Enter your choice: ")
    
    if user_choice == "1":
        print("New Student Entry".center(40, "-"))
        new_name = input("Name: ")
        new_age = int(input("Age: "))
        new_address = input("Address: ")
        
        new_student = {
            "Full Name": new_name,
            "Age": new_age,
            "Address": new_address
        }
        
        with open("students.csv", "a") as file:
            csv_writer = csv.DictWriter(file, fieldnames=HEADERS)
            csv_writer.writerow(new_student)
        
    elif user_choice == "2":
        with open("students.csv", "r") as file:
            print("Show all students")
            reader = csv.reader(file)
            for line in reader:
                print(line)
            
    elif user_choice == "#":
        print("Exit")    
        
        break
