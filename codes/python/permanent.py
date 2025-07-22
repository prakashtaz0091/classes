import csv


def load_students(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        students = []
        for student in reader:
            students.append(student)

    return students


def add_student(file_name, student):
    with open(file_name, "a") as file:
        writer = csv.writer(file)
        writer.writerow(student)
