# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except Exception as e:
#     # print(e)
#     print("Please enter a valid number")


# print("rest of the program")


# try:
#     dividend = int(input("Enter a dividend: "))
#     divisor = int(input("Enter a divisor: "))

#     div_result = dividend / divisor
#     print("result = ", div_result)
# except ZeroDivisionError:
#     # print(e)
#     print("Infinity")
# except ValueError:
#     print("Please enter valid numbers")
# except Exception as e:
#     print("Error: ", e)

# finally:
#     print("End of program")


# def test():
#     # try:
#     result = 5 / 1
#     return result


# except Exception:
#     pass
# finally:
#     print("finally")


# res = test()
# print(res)


# try:
#     res = 5 / 0
# except Exception:
#     pass
# else:
#     print(res)
# finally:
#     print("finally")


# for i in range(5):
#     if i == 2:
#         # break
#         continue
#     print(i)
# else:
#     print("else part")

# i = 0
# while i < 5:
#     i += 1
# else:
#     print("else")


# File Handling
# file = open("")
# file.close()

# with open("new.txt", "w") as file:
#     file.write("This is newly added text")
#     # more ops....
#     # more ops...

# with open("new.txt", "a") as file:
#     file.write("\nThi\ts is another line of text")
# # more ops....
# # more ops...

# with open("new.txt", "r") as file:
#     # content = file.read()
#     lines = file.readlines()
#     print(lines)
#     # print(content)
#     # print(len(content))
#     for line in lines:
#         print(line)

# st_content = "\tas\tdf\t".strip()
# print(st_content, len(st_content))


# import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)

#     for line in reader:
#         print(line)


# with open("students.csv", "a") as file:
#     writer = csv.writer(file)

#     # writer.writerow(["hari", 23, "btm"])
#     # writer.writerow(["ram", 23, "btm"])
#     rows = [["ram", 23, "btm"], ["hari", 34, "ktm"]]

#     writer.writerows(rows)
