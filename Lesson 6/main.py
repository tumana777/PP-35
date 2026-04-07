# empty_dict = {}
#
# print(type(empty_dict))

# names = ["John", "Otar", "Nino", "Mary"]
# ages = [25, 26, 27, 52]
# cities = ["Beijing", "New York", "London", "Paris"]
#
# for i in range(len(names)):
#     print(f"{names[i]} is {ages[i]} years old and lives in {cities[i]}")

# person1 = {"name": "John", "age": 25, "city": "Beijing"}
# person2 = {"name": "Otar", "age": 26, "city": "New York"}
# person3 = {"name": "Nino", "age": 27, "city": "London"}
# person4 = {"name": "Mary", "age": 52, "city": "Paris"}

# persons = {
#     "John": 25,
#     "Otar": 26,
#     "Nino": 27,
#     "Mary": 52,
#     "Alex": 25,
#     "Nina": 26
# }

# print(persons["Nino"])
# print(persons["Alex"])

# print(persons["nino"])

# persons["Nino"] = 30
#
# print(persons["Nino"])

# persons["nino"] = 36
#
# print(persons['nino'])

# persons = {
#     "John": 25,
#     "Otar": 26,
#     "Nino": 27,
#     "Mary": 52,
#     "Alex": 25,
#     "John": 33,
#     "Nina": 26
# }
#
# print(persons)

# my_dict = {
#     "names": ["John", "Otar", "Nino", "Mary"],
#     1: 25,
#     3.14: 6.25,
#     False: True,
#     None: None,
#     [1, 2]: 5
# }
#
# print(my_dict)

# persons = {
#     "John": 25,
#     "Otar": 26,
#     "Nino": 27,
#     "Mary": 52,
#     "Alex": 25,
#     "Nina": 26
# }

# for i in persons:
#     print(f"{i} is {persons[i]} years old")


# print(persons.get("john", "Not found"))
# print(list(persons.keys()))
# print(list(persons.values()))
# print(list(persons.items()))

# persons.update({"Walter": 33, "Jessie": 29})

# popped_item = persons.pop("John")
# persons.popitem()

# persons.setdefault("John", 33)

# print(persons)

# names = ["John", "Otar", "Nino", "Mary"]
# ages = 5
#
# my_dict = dict.fromkeys(names, ages)
#
# print(my_dict)

# my_dict = {i:i for i in range(1, 6)}
#
# print(my_dict)


# products = {
#     "Electronics": {
#         "Laptops": {"name": "Dell", "price": 1000},
#         "Smartphones": {"name": "Apple", "price": 500},
#         "Tablets": {"name": "Samsung", "price": 200}
#     }
# }
#
# print(products["Electronics"]["Smartphones"]["price"])




