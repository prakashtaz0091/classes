# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"P({self.x}, {self.y})"  # P(1,1)

#     def __add__(self, other):
#         new_x = self.x + other.x
#         new_y = self.y + other.y

#         new_point = Point(new_x, new_y)

#         return new_point

#     def __sub__(self, other):
#         a = (self.x - other.x) ** 2
#         b = (self.y - other.y) ** 2

#         d = (a + b) ** 0.5
#         return d

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# # dunder -> d-> double, under-> underscore
# # special methods
# # magic methods

# p1 = Point(1, 0)
# p2 = Point(1, 1)

# # result = p1 + p2
# # print(result)
# # distance = p1 - p2
# # print(distance, "sq. units")

# print(p1 == p2)

# # 1 - 3
# # 2 + 3
# # [1,2,3] + [2,3,4] => [1,2,3,2,3,4]
# # "ram" + "hari" => "ramhari"
# # "ram"*3 => "ramramram"

# # print(p1)
# # print(p2)
# # s1 = {1,2,3}
# # s2 = {2,3}
# # s1 - s2 -> set difference

# # len("ram") -> 3
