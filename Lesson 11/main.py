# file = open("test.txt", "r")
#
# print(file.readable())
# print(file.writable())
#
# data = file.read()
#
# file.close()

# file = open("../Lesson 9/main.py", "r")
#
# print(file.read())
#
# file.close()

# file = open("../.gitignore", "r")
#
# print(file.read())
#
# file.close()

# file = open("test.txt", "r")
#
# data1 = file.read()
#
# file.close()
#
# print(data1)
#
# file = open("test.txt", "r")
# data2 = file.read()
# file.close()
#
# print(data2)

# file = open("test.txt", "r")
#
# data1 = file.read()
# file.seek(5)
# data2 = file.read()
#
# file.close()
#
# print(data2)

# file = open("test.txt", "r")
#
# data1 = file.read(16)
# data2 = file.read()
#
# file.close()
#
# print(data2)

# file = open("test.txt", "r")
#
# data = file.read()
#
# file.close()
#
# print(type(data))

# file = open("test.txt", "r")
#
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# line4 = file.readline()
#
# file.close()
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)

# file = open("test.txt", "r")
#
# lines = file.readlines()
#
# file.close()
#
# print(lines)

# file = open("test1.txt", "w")
#
# file.write("Hello World")
# file.write("\n")
# file.write("Hello Python")
#
# file.close()


# file = open("test1.txt", "a")
#
# file.write("\nHello World")
#
# file.close()

# file = open("test1.txt", "w")
#
# file.write("Otar\n")
# file.write("Nodar\n")
# file.write("Alex\n")
#
# file.close()


# file = open("test3.txt", "x")
#
# file.write("Hello Leri")
#
# file.close()

# names_list = ["Otar", "Nino", "Alex", "Mary", "John", "Nina", "Nino"]
#
# file = open("names.txt", "w")
#
# for name in names_list:
#     file.write(f"{name}\n")
#
# file.close()


# names_list = ["Otar", "Nino", "Alex", "Mary", "John", "Nina", "Nino"]
#
# new_names_list = [f"{name}\n" for name in names_list]
#
# file = open("names.txt", "w")
#
# file.writelines(new_names_list)
#
# file.close()

# file = open("names.txt", "r+")
#
# print(file.readable())
# print(file.writable())
#
# file.close()


# with open("test.txt", "r") as file:
#     data = file.read()
#     file.seek(0)
#     data1 = file.read()
#
# print(data1)