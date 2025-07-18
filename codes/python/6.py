# LIST => mutable data type

# fruits = [
#     "apple",
#     "grapes",
#     "coconut",
# ]  # fruits => collection of fruits (string data) , fruits => single list type data

# print(type(fruits))

# hc = [
#     "ram",  # index = 0 or -6
#     5,  # index = 1 or -5
#     5.5,  # index = 2 or -4
#     True,  # index = 3 or -3
#     None,  # index = 4 or -2
#     ["another list data", "another list 2nd item"],  # index = 5  or -1
# ]

# # print(hc[0])
# # print(hc[1])
# # print(hc[2])
# # print(hc[6])

# # print(hc[5])
# # print(hc[-1])
# # last_item = hc[-1]
# # last_item = hc[-1][0]

# # print(last_item[0])
# # print(last_item[-1])

# # print(hc)

# # hc[0] = "Shyam"
# # hc[-1] = "new item"
# print(hc)
# # hc.append("new item added")
# # del hc[0]
# hc.remove("")

# print(hc)


# players_list = ["ram", "hari", "ramesh", "rajesh", "hari"]
# players_list.append("roshan")
# print(players_list)
# players_list.remove("hari") # removes specific value/item
# players_list.remove("hari")  # removes specific value/item
# players_list.pop()  # removed last item
# popped_player1 = players_list.pop(1)
# popped_player2 = players_list.pop(-1)

# print(players_list)
# print(popped_player1, popped_player2)
# players_list_copy = players_list
# players_list_copy = players_list.copy()

# players_list.pop()

# print(players_list)
# print(players_list_copy)
# print(players_list_copy is players_list)


# print(players_list.count("hari"))
# players_list.insert(0, "new player at first")
# print(players_list.index("hari", 2))
# print(players_list)

# for count, player in enumerate(players_list, start=1):
#     # print(count, player)
#     print(f"Player No. [{count}] : {player}")
# def show_players_info(player_list):
#     for count, player in enumerate(player_list, start=1):
#         # print(count, player)
#         print(f"Player No. [{count}] : {player}")


# player_list = []  # empty list

# while True:
#     new_player_name = input("Enter the player name (q to quit) : ")

#     if new_player_name == "q":
#         break

#     player_list.append(new_player_name)


# # once the entry is done i.e. when while loop ends

# show_players_info(player_list)

# players_list = ["ram", "hari", "ramesh", "rajesh", "hari"]

# players_list.pop()
# Tuple
# players_list_final = tuple(players_list)
# print(players_list)
# print(players_list_final)
# players_final_list = ("ram", "hari")  # if need to intialize empty tuple, ()


# DAYS = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
# print(DAYS[0])
# print(DAYS[-1])
# print(DAYS.index("monday"))
# print(DAYS.count("monday"))

# *args => (1,2,3,4)
# enumerate(players_list, start=1) => (1, "ram")
# return result1, result2 => (1, 2)

# r1, r2 = (1, 2)
# count, player = (1, "ram")

# a, *middles, b = [1, 2, 3, 4]
# print(a, middles, b)


# Set
# ram_likes = {"football", "volleyball", "chess", "football"}

# print(ram_likes)

# p_list = ["hari", "shyam", "hari", "geeta", "ram"]
# unique_p_list = set(p_list)

# print(unique_p_list)

# empty_set = {} => wrong, since python treats {} as a empty dictionary
# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# a = {1, 2, 3, 4, 5}
# b = {2, 3, 4, 7, 8}

# result = a.union(b)
# result = a | b  # we can simply use pipe '|' symbol to represent union operation

# result = a.intersection(b)
# result = a & b  # we can simply use pipe '&' symbol to represent intersection operation
# print(result)
# print(result)
# print(a)
# print(b)
# a_minus_b = a.difference(b)
# a_minus_b = a - b
# print(a_minus_b)
# b_minus_a = b - a
# print(b_minus_a)

# sym_diff_a_b = a.symmetric_difference(b)
# print(sym_diff_a_b)
