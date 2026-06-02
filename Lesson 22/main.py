# Single Responsibility Principle
# Bad Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Generating report for '{self.data}'"
#
#     def write_to_file(self, filename):
#         with open(filename, "w") as f:
#             f.write(self.generate_report())
#
# r = Report("This is a report")
# r.write_to_file("report.txt")

# Good Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Generating report for '{self.data}'"
#
# class ReportWriter:
#     @staticmethod
#     def write_to_file(report:Report, filename):
#         with open(filename, "w") as f:
#             f.write(report.generate_report())
#
# r = Report("This is a report")
# rw = ReportWriter()
#
# rw.write_to_file(r, "new_report.txt")


# Open/Closed Principle
# Bad Example

# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def get_discount(self, discount_type):
#         if discount_type == "VIP":
#             return self.price * 0.9
#         elif discount_type == "Gold":
#             return self.price * 0.8
#         else:
#             return self.price
#
# discount = Discount(100)
#
# print(discount.get_discount("Vip+"))


# Good Example

# from abc import ABC, abstractmethod
#
# class Discount(ABC):
#     def __init__(self, price):
#         self.price = price
#
#     @abstractmethod
#     def get_discount(self):
#         pass
#
# class VIPDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.9
#
# class GoldDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.8
#
# class PlatinumDiscount(Discount):
#     def get_discount(self):
#         return self.price * 0.7
#
# vipdiscount = VIPDiscount(100)
# golddiscount = GoldDiscount(100)
# platinumdiscount = PlatinumDiscount(100)
#
# print(vipdiscount.get_discount())
# print(golddiscount.get_discount())
# print(platinumdiscount.get_discount())


# Liskov Substitution Principle
# Bad Example

# class Bird:
#     @staticmethod
#     def fly():
#         return "I can fly"
#
#     @staticmethod
#     def eat():
#         return "I can eat"
#
# class Sparrow(Bird):
#     @staticmethod
#     def fly():
#         return "Sparrow can fly"
#
#     @staticmethod
#     def eat():
#         return "Sparrow can eat"
#
# class Penguin(Bird):
#     @staticmethod
#     def eat():
#         return "Penguin can eat"
#
#     @staticmethod
#     def fly():
#         raise Exception("Penguin can't fly")


# Good Example

# class Bird:
#     @staticmethod
#     def eat():
#         return "I can eat"
#
#     @staticmethod
#     def move():
#         return "I can move"
#
# class FlyingBird(Bird):
#     @staticmethod
#     def fly():
#         return "I can fly"
#
# class SwimmingBird(Bird):
#     @staticmethod
#     def swim():
#         return "I can swim"
#
# class Penguin(SwimmingBird):
#     pass
#
# class Sparrow(FlyingBird):
#     pass

# Interface Segregation Principle
# Bad Example

# class Worker:
#     @staticmethod
#     def work():
#         return "I am working"
#
#     @staticmethod
#     def eat():
#         return "I am eating"
#
# class Manager(Worker):
#     @staticmethod
#     def manage():
#         return "I am managing"
#
#
# class Robot(Worker):
#     @staticmethod
#     def program():
#         return "I am programming"
#
#     @staticmethod
#     def charge():
#         return "I am charging"


# Good Example
# from abc import ABC, abstractmethod
#
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Eatable(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Chargeable(ABC):
#     @abstractmethod
#     def charge(self):
#         pass
#
# class Manager(Workable, Eatable):
#     def work(self):
#         return "I am working"
#
#     def eat(self):
#         return "I am eating"
#
# class Robot(Workable, Chargeable):
#     def work(self):
#         return "I am working"
#
#     def charge(self):
#         return "I am charging"



# Dependency Inversion Principle
# Bad Example

# class MySQLDatabase:
#     @staticmethod
#     def connect():
#         return "Connected to MySQL database"
#
# class Application:
#     def __init__(self):
#         self.database = MySQLDatabase()
#
#     def run(self):
#         return self.database.connect()
#
# app = Application()
#
# print(app.run())

# Good Example
# from abc import ABC, abstractmethod
#
# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
# class MySQLDatabase(Database):
#     def connect(self):
#         return "Connected to MySQL database"
#
# class PostgreSQLDatabase(Database):
#     def connect(self):
#         return "Connected to PostgreSQL database"
#
# class MongoDBDatabase(Database):
#     def connect(self):
#         return "Connected to MongoDB database"
#
# class Application:
#     def __init__(self, db:Database):
#         self.db = db
#
#     def run(self):
#         return self.db.connect()
#
# mysql_db = MySQLDatabase()
# postgres_db = PostgreSQLDatabase()
# mongo_db = MongoDBDatabase()
#
# app = Application(mysql_db)
# app2 = Application(postgres_db)
# app3 = Application(mongo_db)
#
# print(app.run())
# print(app2.run())
# print(app3.run())


# print(isinstance(mysql_db, Database))