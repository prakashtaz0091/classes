# MENU = """
# ============================
# Student Result System
# 1. Calculate Total
# 2. Calculate Percentage
# 3. Check Pass / Fail
# 4. Exit
# ============================
# """
# PASS_MARKS = 40

# def display_choices():
#     print(MENU)

# def ask_marks():
#     m1 = int(input(" Math : "))
#     m2 = int(input(" Science : "))
#     m3 = int(input(" English : "))
#     m4 = int(input(" Computer : "))
#     m5 = int(input(" Nepali : "))
#     return m1, m2, m3, m4, m5

# def show_pass_fail(all_marks):
#     for marks in all_marks:
#         if marks < PASS_MARKS:
#             print("Failed the exam")
#             break
#     else:
#         print("Passed the exam")



# while True:
#     display_choices()
#     choice = input(" Choice >>> ")

#     if choice == "1":
#         all_marks = ask_marks()
#         print(" Total :", sum(all_marks))

#     elif choice == "2":
#         all_marks = ask_marks()
#         print(" Percentage :", sum(all_marks) / len(all_marks))

#     elif choice == "3":
#         all_marks = ask_marks()
#         show_pass_fail(all_marks)

        
#     elif choice == "4":
#         break
#     else:
#         print(" Invalid choice ")




