# modes,
# w -> write ( write new data )
# r -> read ( get existing data)
# a -> append (thapnu)


# new_file = open("new.txt", "w")

# new_file.write("This is new content.\n This is another line")
# new_file.write("This is new content\n")
# new_file.write("This is new content\n")
# new_file.write("This is new content\n")
# new_file.write("This is new content")
# lines = ["This is first line\t", "This is second line", "This is third line"]
# new_file.writelines(lines)

# new_file = open("new.txt", "r")

# file_content = new_file.read()
# file_content = new_file.read(10)  # read first 10 characters
# file_content = new_file.readline()
# file_content = new_file.readlines()
# print(file_content)
# for line in new_file:
#     print(line)

# new_file = open("new.txt", "a")

# new_file.write("\nThis is new content")


# new_file.close()


# with open("new.txt", "a") as new_file:
#     new_file.write("\nThis is new content")
#     new_file.write("\nThis is new content")
#     new_file.write("\nThis is new content")
#     new_file.write("\nThis is new content")


# open("n.txt", "r") # gives FileNotFound Error if file does not exist


# csv module
# import csv

# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Alice", 25, "New York"])
#     writer.writerow(["Bob", 30, "London"])
# with open("people.csv", "r", newline="") as file:
#     reader = csv.reader(file)
#     heading = next(reader)
#     # result = reader.next()  # skip header
#     for row in reader:
#         print(row)
