# class Student:
#     status = True
#     pay = 1000
#     total_students = 0
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Student.total_students += 1
#
#     def get_email(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"

# class Student:
#     status = True
#     pay = 1000
#     total_students = 0
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Student.total_students += 1
#
#     def get_email(self, domain):
#         return f"{self.first_name}.{self.last_name}{self.age}@{domain}"
#
#     def get_full_name(test):
#         return f"{test.first_name} {test.last_name}"
#
# student1 = Student("otar", "tumanishvili", 35)
# student2 = Student("alex", "ninidze", 21)

# print(student1.get_email("yahoo.com"))
# print(student2.get_email("mail.com"))

# print(student1.get_full_name())
# print(student2.get_full_name())


# class Suv:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, speed):
#         self.speed += speed
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, speed):
#         self.speed -= speed
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return "Speed is now 0"
#
#     def off_road(self):
#         return "This Vehicle can off-roading"
#
#
# class Motorcycle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, speed):
#         self.speed += speed
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, speed):
#         self.speed -= speed
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return "Speed is now 0"
#
#     def wheelie(self):
#         return "This Vehicle can wheelie"
#
#
# subaru = Suv("Subaru", "WRX", 2015)
# ktm = Motorcycle("KTM", "X-Bow", 2019)

# print(subaru.speed)
# subaru.accelerate(10)
# subaru.accelerate(15)
# subaru.slow_down(10)
# subaru.accelerate(5)
# print(subaru.speed)
# subaru.brake()
# print(subaru.speed)
# print(subaru.off_road())

# print(ktm.speed)
# ktm.accelerate(10)
# ktm.accelerate(15)
# ktm.slow_down(10)
# ktm.accelerate(5)
# print(ktm.speed)
# ktm.brake()
# print(ktm.speed)
# print(ktm.wheelie())



# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, speed):
#         self.speed += speed
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, speed):
#         self.speed -= speed
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return "Speed is now 0"
#
# class Suv(Vehicle):
#
#     def __init__(self, make, model, year, clearance):
#         super().__init__(make, model, year)
#         self.clearance = clearance
#
#     def off_road(self):
#         return f"This Vehicle can off-roading and clearance is {self.clearance}."
#
# class Motorcycle(Vehicle):
#     def wheelie(self):
#         return "This Vehicle can wheelie"
#
# subaru = Suv("Subaru", "Forester", 2015, 200)
# ktm = Motorcycle("KTM", "X-Bow", 2019)
#
# print(subaru.off_road())
# print(subaru.speed)

# print(subaru.speed)
# print(subaru.accelerate(10))
# print(subaru.accelerate(15))
# print(subaru.slow_down(10))
# print(subaru.accelerate(5))
# print(subaru.brake())
# print(subaru.off_road())

# print(ktm.speed)
# print(ktm.accelerate(10))
# print(ktm.accelerate(15))
# print(ktm.slow_down(10))
# print(ktm.accelerate(5))
# print(ktm.brake())
# print(ktm.wheelie())


# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, speed):
#         self.speed += speed
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, speed):
#         self.speed -= speed
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return "Speed is now 0"
#
# class ElectricVehicle:
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity
#         self.battery_level = 100
#
#     def charge(self, amount):
#         self.battery_level = min(self.battery_level + amount, 100)
#         return f"Battery level is now {self.battery_level}."
#
#     def discharge(self, amount):
#         self.battery_level = max(self.battery_level - amount, 0)
#         return f"Battery level is now {self.battery_level}."
#
#
# class ElectricSuv(Vehicle, ElectricVehicle):
#     def __init__(self, make, model, year, battery_capacity):
#         Vehicle.__init__(self, make, model, year)
#         ElectricVehicle.__init__(self, battery_capacity)
#
#     def info(self):
#         return f"This is an electric SUV with a battery capacity of {self.battery_capacity} and a battery level of {self.battery_level}%"
#
#
# tesla = ElectricSuv("Tesla", "Model X", 2020, "100KW")
#
# print(tesla.make)
# print(tesla.model)
# print(tesla.year)
# print(tesla.charge(10))
# print(tesla.discharge(100))
# print(tesla.discharge(10))
# print(tesla.info())
# print(tesla.accelerate(10))
# print(tesla.brake())
# print(tesla.slow_down(10))


# class Shape:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
# class Rectangle(Shape):
#     def calculate_perimeter(self):
#         return f"Rectangle perimeter is {2 * (self.length + self.width)}"
#
#     def calculate_area(self):
#         return f"Rectangle area is {super().calculate_area()}"

# rec = Rectangle(5, 10)
# print(rec.calculate_area())
# print(rec.calculate_perimeter())

# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def calculate_perimeter(self):
#         return f"Square perimeter is {4 * self.length}"
#
#     def calculate_area(self):
#         return f"Square area is {super().calculate_area()}"
#
#
# sq = Square(5)
# print(sq.calculate_perimeter())
# print(sq.calculate_area())
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__(base, height)
#
#     def calculate_area(self):
#         return f"Triangle area is {0.5 * self.length * self.width}"
#
# triang = Triangle(5, 10)
# print(triang.calculate_area())

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#     def test(self):
#         return "Test"
#
# class Rectangle(Shape):
#     def calculate_perimeter(self):
#         return f"Rectangle perimeter is {2 * (self.length + self.width)}"
#
#     def calculate_area(self):
#         return f"Rectangle area is {super().calculate_area()}"
#
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def calculate_area(self):
#         return f"Square area is {self.length * self.width}"
#
#     def __str__(self):
#         return "This is a square"
#
# sq = Square(5)
# print(sq)

# print(sq.calculate_area())

# rec = Rectangle(5, 10)
# print(rec.calculate_area())








