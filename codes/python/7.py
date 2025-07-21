# test_dict = {}  # empty dictionary represent garxa
# person1 = {"name": "ram", "age": 20, "college": "KMC"}

# print(type(person1))
# print(person1["name"])
# print(person1["age"])
# print(person1["college"])
# print(person1)
# # person1["name"] = "Hari"
# # del person1["college"]
# # person1.pop("name")
# # person1.popitem()

# # person1["ph no"] = "98**********"

# print(person1)

# print(person1.keys())
# print(person1.values())
# print(person1.items())

# for item in person1:
#     # print(item)
#     print(person1[item])
# for key, value in person1.items():
#     print(key, value)

# print("ph no" in person1.keys())
# print("hari" in person1.values())
# for num, letter in enumerate("apple"):
#     print(num, letter)
# seq = "apple"
# seq[0] = "b"
# print(seq[1])


person1 = {
    "name": {"first": "Ram", "last": "Poudel"},
    "age": 20,
    "address": {
        "temp": "Kathmandu",
        "perm": {
            "province": "Koshi",
            "district": "Jhapa",
            "city": {"name": "Damak", "street": "Himalaya marga", "house no": "202"},
        },
    },
}

# person_info = person1.keys()
# # print(person_info)

# person_address = person1["address"]
# person_address_info = person_address.keys()
# # print(person_address_info)

# person_perm_address = person_address["perm"]
# # print(person_perm_address.keys())

# person_perm_address_city = person_perm_address["city"]

# # print(person_perm_address_city.keys())

# person_prem_address_city_street = person_perm_address_city["street"]
# print(person_prem_address_city_street)

# street = person1["address"]["perm"]["city"]["street"]
# print(street)
