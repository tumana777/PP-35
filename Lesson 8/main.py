# a = int(input("Enter a number 1: "))
# b = int(input("Enter a number 2: "))
#
# print(a + b)
#
# print("Code execution finished")
# print("Hello world")
#
# a = int(input("Enter a number 1: "))
# b = int(input("Enter a number 2: "))
#
# print(a + b)
#
# print("Another code execution")
# print("Hello world")


# def add_numbers():
#     a = int(input("Enter a number 1: "))
#     b = int(input("Enter a number 2: "))
#
#     print(a + b)

# from my_module import add_numbers
#
# print("Code execution finished")
# print("Hello world")
#
# add_numbers()
#
# print("Another code execution")
# print("Hello world")
#
# add_numbers()

# from my_module import add_numbers

# num = 8

# def print_number(num):
#     print(f"The number is {num}")
#
#
# print_number(7)


# def print_number(num):
#     print("Hello world")
#
#
# print_number("Python")

# def greeting(name):
#     print(f"Hello {name}")
#
# greeting("Otar")
# greeting("John")

# def greeting(name, age):
#     print(f"Hello {name}, you are {age} years old")
#
# greeting("Otar", 35)

# def sum_numbers(a, b):
#     result = a + b
#     print(result)
#
# sum_numbers(5, 6)


# def sub_numbers(a, b):
#     print(b - a)
#
# sub_numbers(8, 6)


# def sum_numbers(a, b):
#     print("Hello world")
#     print(a + b)
#     print("Goodbye world")
#
# sum_numbers(5, 6)


# def sum_numbers(a, b):
#     return a + b
#
# result1 = sum_numbers(5, 6)
# result2 = sum_numbers(8, 9)
#
# print(result1 * result2)

# def sum_numbers(a, b):
#     print("Function execution started")
#     return a + b
#     print("Function execution finished")
#
# result1 = sum_numbers(5, 6)
# print(result1)

def test_function(text):
    length = len(text)
    reversed_text = text[::-1]
    return length, reversed_text, "Test"

result = test_function("Hello")

a, b, c = result

print(a)
print(b)
print(c)