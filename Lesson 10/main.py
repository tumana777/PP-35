# import string
#
# def word_counter(text):
#     new_text = text.lower().split()
#
#     punctuations = string.punctuation
#
#     my_dict = {}
#
#     for word in new_text:
#         if word.strip(punctuations) not in my_dict:
#             my_dict[word.strip(punctuations)] = 1
#         else:
#             my_dict[word.strip(punctuations)] += 1
#
#     return my_dict
#
#
#
# print(word_counter("This is a test. this, test is fun."))


# def add(a, b):
#     return a + b
#
# result = add(5, 6)
# result = add(result, 7)
#
# print(result)

# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#     return a / b
#
# def test(func, y, z):
#     if callable(func):
#         return func(y, z)
#     return "Not a function"

# print(test(add, 5, 6))
# print(test(sub, 5, 6))
# print(test(mul, 5, 6))
# print(test(div, 8, 4))


# func_list = [add, sub, mul, div, 8]
#
# for func in func_list:
#     print(test(func, 5, 6))


# print(callable(input))
# print(callable(print))
# print(callable(type))
# print(callable(id))
# print(callable(list))
# print(callable("Otar"))


# def get_multiplier(a):
#
#     def multiply(b):
#         return a * b
#
#     return multiply

# print(get_multiplier(2)(5))

# multiply_by_2 = get_multiplier(2)
# multiply_by_3 = get_multiplier(3)

# print(x.__name__)

# print(multiply_by_2(5))
# print(multiply_by_2(9))
#
# print(multiply_by_3(5))
# print(multiply_by_3(9))


# def test():
#     return test()
#
# test()

# def find_factorial(n):
#     if n == 1 or n == 0:
#         return 1
#
#     return n * find_factorial(n - 1) # 5 * 4 * 3 * 2 * 1
#
# print(find_factorial(5))


# x = lambda a: a * 2
#
# print(x(5))


# x = lambda a, b: a + b
#
# print(x(5, 6))


# x = lambda a: a * 2 if a > 0 else "Negative number not allowed"
#
# print(x(0))


# names = ["johny", "otar", "nodar", "nino", "erekle"]

# empty_list = []
#
# for name in names:
#     empty_list.append(len(name))
#
# print(empty_list)

# def get_length(name):
#     return len(name)

# names_length = map(lambda x: len(x), names)
#
# print(list(names_length))


# names = ["johny", "oTar", "nodar", "nino", "erekle"]

# upper_names = map(lambda x: x.capitalize(), names)
#
# print(list(upper_names))

# long_names = filter(lambda x: len(x) > 4, names)
#
# print(list(long_names))


# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5, 8, 9, 14]
#
# print(reduce(lambda x, y: x + y, numbers))


# names = ["johny", "oto", "nodar", "nino", "erekle"]
#
#
# sorted_names = sorted(names, key=lambda x: len(x))
#
# print(sorted_names)

# try:
#     num1 = int(input("Please enter a number: "))
#     num2 = int(input("Please enter another number: "))
#
#     print(num1 / num2)
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except Exception as e:
#     print(e)
#
# print("Hello world")