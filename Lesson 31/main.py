from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")
client = MongoClient('localhost', 27017)

db = client["PP-35"]

# print(db.list_collection_names())

students = db["students"]

# print(students.find_one())

# for student in students.find():
#     print(student)

# print(students.count_documents({}))

# print(students.count_documents({"first_name": "Otar"}))
# print(students.count_documents({"first_name": "Gio"}))

# student1 = {
#     "first_name": "Leri",
#     "last_name": "Niazashvili",
#     "age": 21
# }
#
# students.insert_one(student1)

# students_list = [
#     {"first_name": "Alex", "last_name": "Dovlatov", "age": 22},
#     {"first_name": "Luka", "last_name": "Mosiashvili", "age": 25},
#     {"first_name": "Nodar", "last_name": "Akhvlediani", "age": 21},
#     {"first_name": "Vako", "last_name": "Lagvilava", "age": 32},
# ]
#
# students.insert_many(students_list)

# for student in students.find():
#     print(student)

# print(students.find_one({"first_name": "Gio"}))

# for student in students.find({"first_name": "Gio"}):
#     print(student)

# for student in students.find({"age": 21}):
#     print(student)

# for student in students.find({"age": {"$gt": 21}}):
#     print(student)

# for student in students.find({"age": {"$gte": 21}}):
#     print(student)

# for student in students.find({"age": {"$lt": 25}}):
#     print(student)

# for student in students.find({"age": {"$gt": 21, "$lt": 25}}):
#     print(student)

# for student in students.find({"age": {"$in": [21, 25, 32]}}):
#     print(student)

# for student in students.find({"saxeli": "Otar"}):
#     print(student)

# for student in students.find({"$or": [{"first_name": "Alex"}, {"first_name": "Gio"}]}):
#     print(student)

# for student in students.find({"$and": [{"first_name": "Gio"}, {"last_name": "Kabanashvili"}]}):
#     print(student)

# students.update_one({"first_name": "Alex"}, {"$set": {"age": 23}})

# students.update_many({"first_name": "Gio"}, {"$set": {"age": 25}})

# students.update_many({}, {"$set": {"status": True}})

# students.delete_one({"first_name": "Alex"})

# students.delete_many({"first_name": "Gio"})

# students.delete_many({})

# students.drop()