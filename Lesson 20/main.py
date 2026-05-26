import json
#
# student = {
#     "name": "John",
#     "age": 30,
#     "grades": [85, 90, 75],
#     "is_student": True,
#     "address": {
#         "street": "Main Street",
#         "city": "New York",
#     },
#     "pay": 1000.00,
#     "courses": ("Math", "English", "History")
# }
#
# student2 = {
#     "name": "Bob",
#     "age": 35,
#     "grades": [85, 90, 75],
#     "is_student": True,
#     "address": {
#         "street": "Main Street",
#         "city": "New Orleans",
#     },
#     "pay": 1000.00,
#     "courses": ("Math", "English", "History")
# }
#
# students = {
#     "students": [student, student2],
#     "total_students": 2
# }

# students = [student, student2]


# with open("student.json", "w") as f:
#     json.dump(students, f, indent=4)


# import json
#
# with open("student.json", "r") as f:
#     data = json.load(f)
#
# print(data)

# student = {
#     "name": "John",
#     "age": 30,
#     "grades": [85, 90, 75],
#     "is_student": True,
#     "address": {
#         "street": "Main Street",
#         "city": "New York",
#     },
#     "pay": 1000.00,
#     "courses": ("Math", "English", "History")
# }


# serialized_student = json.dumps(student, indent=4)

# print(type(serialized_student))

# deserialized_student = json.loads(serialized_student)
#
# print(type(deserialized_student))


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"

# student = Student("John", 35)
#
# def student_serializer(obj):
#     return {
#         "name": obj.name,
#         "age": obj.age
#     }

# serialized_student = student_serializer(student)
#
# print(serialized_student)

# with open("student1.json", "w") as f:
#     json.dump(student, f, default=student_serializer, indent=4)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"
#
# def student_deserializer(data):
#     return Student(data["name"], data["age"])
#
# with open("student1.json", "r") as f:
#     student = json.load(f, object_hook=student_deserializer)
#
# print(student)

import pickle

# student = {
#     "name": "John",
#     "age": 30,
#     "grades": [85, 90, 75],
#     "is_student": True,
#     "address": {
#         "street": "Main Street",
#         "city": "New York",
#     },
#     "pay": 1000.00,
#     "courses": ("Math", "English", "History")
# }


# with open("student.pickle", "wb") as f:
#     pickle.dump(student, f)

# with open("student.pkl", "rb") as f:
#     data = pickle.load(f)
#
# print(data)

# student = {
#     "name": "John",
#     "age": 30,
#     "grades": [85, 90, 75],
#     "is_student": True,
#     "address": {
#         "street": "Main Street",
#         "city": "New York",
#     },
#     "pay": 1000.00,
#     "courses": ("Math", "English", "History")
# }
#
# serialized_student = pickle.dumps(student)
#
# deserialized_student = pickle.loads(serialized_student)

# print(deserialized_student)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"

# student = Student("John", 35)

# with open("student.pkl", "wb") as f:
#     pickle.dump(student, f)


# with open("student.pkl", "rb") as f:
#     student = pickle.load(f)
#
# print(student)


import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
#
# data = response.json()
#
# for post in data:
#     print(post)

student = {
    "name": "John",
    "age": 30,
    "grades": [85, 90, 75],
    "is_student": True,
    "address": {
        "street": "Main Street",
        "city": "New York",
    },
    "pay": 1000.00,
}

if response.status_code == 200:
    requests.post(url, json=student)
    print("Post successful")





































