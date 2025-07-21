# import time

# CACHE = {}


# def heavy_task(a):
#     if a in CACHE.keys():  # if res of a already exists in CACHE
#         print("Result already calculated...")
#         return CACHE[a]

#     print("Calculating...")
#     time.sleep(5)  # just to represent time consuming task

#     res = a**2

#     CACHE[a] = res

#     return res


# print("first time", heavy_task(5))
# print("second time", heavy_task(5))
# print("third time", heavy_task(5))
# print(CACHE)
