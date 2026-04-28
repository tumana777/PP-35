import os

# print(os.getcwd())
# print(os.listdir())

# os.mkdir("test")

# print(os.listdir())

# print(os.path.exists("test.txt"))

# if not os.path.exists("test"):
#     os.mkdir("test")
# else:
#     print("Folder already exists")

# if os.path.exists("test"):
#     os.rmdir("test")
# else:
#     print("Folder does not exist")


# print(os.path.abspath("test.txt"))

# print(os.path.isfile("test.txt"))
# print(os.path.isfile("test"))

# print(os.path.isdir("test.txt"))
# print(os.path.isdir("test"))


# if os.path.exists("test.txt"):
#     os.remove("test.txt")
# else:
#     print("File does not exist")

# import shutil
#
# shutil.rmtree("test")

# name = "ოთარ"
# name = "Otar"

# encoded_name = name.encode()

# print(type(encoded_name))

# with open("test.txt", "wb") as file:
#     file.write(encoded_name)

# with open("test.txt", "rb") as file:
#     print(file.read())


# with open("img.webp", "rb") as file:
#     img = file.read()
#
#     with open("img4.jpg", "wb") as f:
#         f.write(img)

import csv

# with open("companies.csv", "r") as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

# headers = ["Name", "Age", "City"]
# person1 = ["Nodar", 30, "Tbilisi"]

# data = [
#     ["Otar", 25, "Tbilisi"],
#     ["Nino", 22, "Tbilisi"],
#     ["Alex", 26, "Tbilisi"],
#     ["John", 27, "Tbilisi"],
#     ["Mary", 28, "Tbilisi"]
# ]

# with open("persons.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)
#     writer.writerows(data)


# with open("companies.csv", "r") as file:
#     reader = csv.reader(file)
#
#     with open("companies2.csv", "w") as f:
#         writer = csv.writer(f)
#
#
#         for row in reader:
#             new = [elem.strip() for elem in row]
#             writer.writerow(new)


# with open("companies.csv", "r") as file:
#     dict_reader = csv.DictReader(file)
#
#     for row in dict_reader:
#         print(row)


# persons = [
#     {"name": "Otar", "age": 25, "city": "Tbilisi"},
#     {"name": "Nino", "age": 22, "city": "Tbilisi"},
#     {"name": "Alex", "age": 26, "city": "Tbilisi"},
#     {"name": "John", "age": 27, "city": "Tbilisi"},
#     {"name": "Mary", "age": 28, "city": "Tbilisi"}
# ]
#
# headers = persons[0].keys()
#
# with open("persons1.csv", "w") as file:
#     dict_writer = csv.DictWriter(file, fieldnames=headers)
#     dict_writer.writeheader()
#     dict_writer.writerows(persons)


# from faker import Faker
#
# fake = Faker()
#
# print(fake.first_name())
# print(fake.last_name())
# print(fake.name())
# print(fake.address())
# print(fake.email())
# print(fake.phone_number())


















