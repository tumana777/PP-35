# def add(a, b, c):
#     return a + c
#
# print(add(5, 6, 8))

# def add(*args):
#
#     total = 0
#
#     for i in args:
#         total += i
#
#     return total
#
# print(add(4, 9, 6, 6, 1, 2, 3))

# def add(*args):
#
#     return sum(args)
#
# print(add(4, 9, 6, 6, 1, 2, 3))

# def add(a, b, *args):
#     return f"a = {a}, b = {b}, args = {args}"
#
# print(add("Otar", "Nino", "Mary", "Alex"))

# def add(b, a, *args):
#     return f"a = {a}, b = {b} args = {args}"
#
# print(add("Otar", "Nino", "Mary", "Alex"))

# *a, b, c = 1, 2, 6, 5
#
# print(a)

# def greet_user(greeting, user):
#     return f"{greeting}, {user}!"
#
# lst = ["Hi", "Otar"]
#
# print(greet_user(*lst))

# def add(a=6, b=7):
#     return a + b
#
# print(add(9, 6))

# def add(a, b=9):
#     return a + b
#
# print(add(5, 6))

# def add(a, *args, b=8):
#     return f"a = {a}, b = {b}, args = {args}"
#
# lst = [1, 2, 3, 4, 5]
#
# print(add(*lst))

# def add(a, b=8, *args):
#     return f"a = {a}, b = {b}, args = {args}"
#
# print(add(4, 7, 9, 1, 2))

# def greet(name, greeting, age):
#     return f"{greeting}, {name}, you are {age} years old!"
#
# print(greet(greeting="Hi", age=25, name="Otar"))

# def greet(name, greeting, age):
#     return f"{greeting}, {name}, you are {age} years old!"
#
# print(greet("Otar", greeting="Hi", age=33))


# def greet(name, greeting="Hi"):
#     return f"{greeting}, {name}!"
#
# print(greet(greeting="Hello", name="Otar"))


# def greet(a, b, *args, **kwargs):
#     return f"a = {a}, b = {b}, args = {args}, kwargs = {kwargs}"
#
# print(greet("Otar", "Tumanishvili", "Tbilisi",  message="Hello", age=33))


# def greet(**kwargs):
#     kwargs["city"] = "Tbilisi"
#
#     return kwargs
#
# print(greet(name="Otar", age=33, message="Hello", city="Poti"))

# x = 8 # Global
#
# def outer():
#     x = 10 # Enclosing
#
#     def inner():
#         x = 5 # Local
#
#         print(x)
#
#     inner()
#
# outer()


# __name__ = "Global"

# def outer():
#     # __name__ = "Enclosing"
#
#     def inner():
#         # __name__ = "Local"
#
#         print(__name__)
#
#     inner()
#
# outer()










