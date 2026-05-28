# Lambda function, (anon function)

# def cube(x):
#     return x**3

# cube = lambda x:x**3

# Higher order function like, map and filter

# len, int, str 
# marks = ['45', '34', '78', '86', 89]

# int_marks = list(map(int, marks))
# int_marks = tuple(map(int, marks))

# print(int_marks)
# int_marks = map(int, marks)
# print(int_marks)

# for mark in int_marks:
#     print(mark)

# print(next(int_marks)) #lazy evaluation
# print(next(int_marks)) #lazy evaluation

# marks = ['45', '34', '29', '86', 89]
# int_marks = list(map(int, marks))

# print(int_marks)

# def pass_or_fail(mark):
#     if mark >= 30:
#         return 'P'
#     else:
#         return 'F'
    

# marks_to_pass_fail = map(pass_or_fail, int_marks) 

# print(list(marks_to_pass_fail))

# marks_to_pass_fail = map(lambda mark:'P' if mark>=30 else 'F', int_marks)

# print(list(marks_to_pass_fail))
# int_marks.sort()
# print(int_marks)

# sorted_marks = sorted(int_marks, reverse=True)

# print(sorted_marks)

# stu_marks = {
#     "ram": 89,
#     "hari": 78,
#     "seeta": 99,
#     "geeta": 80
# }

                # ("geeta", 80)
# def return_value(item):
#     return item[1]

# sorted_marks = sorted(stu_marks.items())
# sorted_marks = sorted(stu_marks.items(), key=lambda item:item[1], reverse=True)
# # print(sorted_marks)
# ranked_stu_marks = dict(sorted_marks)
# print(ranked_stu_marks)


# Iterator

# marks = ['45', '34', '29', '86', 89]

# print(marks.__iter__)
# print(marks.__next__)
# mi = iter(marks)
# # print(mi.__next__)
# print(next(mi))
# print(next(mi))
# print(next(mi))

# print(type(mi))
# for mark in marks:

# marks = ['45', '34', '29', '86', 89]

# mi = iter(marks)
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# while True:
#     try:
#         value = next(mi)
#     except StopIteration:
#         print("End of list")
#         break
#     else:
#         print(value)

# print("End of while loop")

# Generator
# def num_gen():
#     yield 1   # freeze plus return
#     yield 2   # freeze plus return
#     yield 3   # freeze plus return
#     yield 4   # freeze plus return
#     yield 5   # freeze plus return
    
    
# nums = num_gen()

# # print(nums.__next__)

# # print(list(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


# def even_num_generator():
#     start = 2
#     while True:
#         yield start
#         start += 2
        
        
# # 2, 4, 6

# even_nums = even_num_generator()

# print(next(even_nums))
# print(next(even_nums))


# def range(stop):
#     start = 0
#     while start<stop:
#         yield start
#         start += 1
        
#         # [0,2,3,,,4]
# r = range(100)

# for num in r:
#     print(num)
# r = range(10)
# ri = iter(r)
# print(r.__iter__)
# print(ri.__next__)

