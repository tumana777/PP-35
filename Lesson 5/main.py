# empty_list = []
# print(empty_list)
# print(type(empty_list))

# empty_list = list()
# print(empty_list)
# print(type(empty_list))

# integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(integer_list))

# names = ["Otar", "John", "Mary"]
# print(names)

# mixed_list = [1, "Otar", True, [1, 2, 3], 3.14, False, "Otar"]
# print(len(mixed_list))

# nested_list = [[1, 2, 3], [4, 5, 6]]
# print(len(nested_list))

# mixed_list = [1, "Otar", True, [1, 2, 3], 3.14, False, "Otar"]

# print(mixed_list[0])
# print(mixed_list[1])
# print(mixed_list[3])
# print(mixed_list[8])
# print(mixed_list[-1])
# print(mixed_list[1:5])
# print("Otar" in mixed_list)
# print(mixed_list[::-1])

# print(integer_list[1::2])


# mixed_list = [1, "Otar", True, [1, "Otar", [2], 3], 3.14, 1, False, "Otar"]
# mixed_list1 = [1, "Otar", True, [1, [2], 3], 3.14, False, "Otar"]
# print(mixed_list[3][1][0])
# mixed_list.append("Hello")
# mixed_list.append("Hello")

# mixed_list.clear()

# print(mixed_list.count("Otar"))
# print(mixed_list.count(1))

# counter = 0
#
# for item in mixed_list:
#     if type(item) == int and item == 1:
#         counter += 1
#
# print(counter)

# copied_list = mixed_list.copy()
# new_list = mixed_list
#
# mixed_list.append("Hello")
#
# print(mixed_list)
# print(copied_list)
# print(new_list)

# print(id(mixed_list), id(copied_list), id(new_list), sep='\n')
# print(mixed_list == copied_list)
# print(mixed_list is copied_list)
# print(mixed_list is new_list)

# mixed_list = [1, "Otar", True, [1, "Otar", [2], 3], 3.14, 1, False, "Otar"]
# mixed_list.extend([1, 2, 3])
# mixed_list.insert(3, "Nino")

# print(mixed_list.index("Otar"))

# popped_item = mixed_list.pop(1)
# mixed_list.pop()

# print(popped_item)

# mixed_list.remove("Otar")
# mixed_list.remove("Otar")
# mixed_list.remove("Otar")

# mixed_list.reverse()

# integer_list = [2, 3, 1, 4, 5, 10, 6, 7, 8, 9]

# sorted_list = sorted(integer_list)
# print(sorted_list)

# integer_list.sort(reverse=True)
# print(integer_list)


# names = ["John", "Otar", "nino", "Mary", "Nino"]
# names.sort()
#
# print(names)


# a = 5
# b = 10

# a, b = 5, 10

# names = ["John", "Otar", "Mary", "Nino", "Alex"]

# for i in range(len(names)):
#     print(f"index: {i}, name: {names[i]}")

# for a, b in enumerate(names):
#     print(f"index: {a}, name: {b}")


# nums = []
#
# for i in range(1, 21):
#     nums.append(i)

# nums = [i for i in range(1, 21)]

# print(nums)

# names = ["John", "Otar", "Mary", "Nino", "Alex"]
#
# new_names = [name.lower() for name in names]
#
# print(new_names)

# nums = []
#
# for i in range(1, 21):
#     if i % 2 == 0:
#         nums.append(i * i)
#
# nums = [i * i for i in range(1, 21) if i % 2 == 0]
#
# print(nums)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[1][1])




