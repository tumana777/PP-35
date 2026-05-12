# class Student:
#     status = True
#     pay = 1000
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def get_email(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"
#
#     def __add__(self, other):
#         return f"This is Student __add__ method"
#
#     def __repr__(self):
#         return f"Student({self.first_name}, {self.last_name}, {self.age})"
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age} years old"
#
# student1 = Student("otar", "tumanishvili", 35)
# student2 = Student("alex", "ninidze", 21)
#
# print(student1 + student2)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return f"{other} is not a Vector object"
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return f"{other} is not a Vector object"
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return Vector(self.x * other, self.y * other)
#         return f"{other} is not a number"
#
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return Vector(self.x / other, self.y / other)
#         return f"{other} is not a number"
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# v1 = Vector(7, 2)
# v2 = Vector(3, 4)

# print(v1 + v2)
# print(v1 - v2)
# print(v1 * 2)


# print(isinstance(1, int))
# print(isinstance(1.0, float))
# print(isinstance("Hello", str))


# class Student:
#     pay = 1000
#     discount = 0.8
#
#     def __init__(self, first_name, last_name, pay, discount):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         self.discount = discount
#
#     @classmethod
#     def get_pay(cls):
#         return cls.pay * cls.discount
#
#     @staticmethod
#     def get_rest(day):
#         # day = input("Enter weekday: ").lower()
#
#         if day == "sunday":
#             return "You can rest today"
#         return "You can't rest today"
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
# student1 = Student("otar", "tumanishvili", 700, 0.9)
#
# # print(student1.get_pay())
# print(student1.get_rest("sunday"))



# class Student:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self._last_name = last_name
#         self.__age = age

    # def get_last_name(self):
    #     return self._last_name
    #
    # def get_age(self):
    #     return self.__age

#     def __str__(self):
#         return f"{self.first_name} {self._last_name} is {self.__age} years old"
#
# student1 = Student("otar", "tumanishvili", 35)

# print(student1.get_age())

# student1.age = 36
# print(student1.age)

# student1._last_name = "ninidze"
#
# print(student1._last_name)



# class Student:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self._last_name = last_name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 10:
#             raise ValueError("Age must be greater than 10")
#         self.__age = value
#
#     def __call__(self):
#         return f"I am callable object"
#
# student1 = Student("otar", "tumanishvili", 35)

# print(student1())

# print(callable(student1))

# print(student1.age)
#
# student1.age = 20
#
# print(student1.age)

# def test():
#     return "Hello World"
#
# print(test())


# class Multiplier:
#     def __init__(self, x):
#         self.x = x
#
#     def __call__(self, y):
#         return self.x * y
#
#     def __str__(self):
#         return f"Multiplier({self.x})"
#
# double = Multiplier(2)
# triple = Multiplier(3)
#
# print(double(9))
# print(triple(9))


# class Student:
#
#     def __init__(self):
#         print("__init__ method called")
#
#     def __new__(cls):
#         print("__new__ method called")
#         return super().__new__(cls)
#
# student1 = Student()


# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#         print(f"name: {name}")
#         print(f"bases: {bases}")
#         attrs["created_by"] = "Admin"
#         print(f"attrs: {attrs}")
#         return super().__new__(cls, name, bases, attrs)
#
# class Parent:
#     pass
#
# class MyClass(Parent, metaclass=MyMeta):
#     test = 58
#
#     def get_test(self):
#         return self.test
#
#
# test = MyClass()
#
# print(test.created_by)








