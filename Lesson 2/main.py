
# a = 9
# a = a + 8

# a = 8
# a += 9

# a = 7
# a = a - 2
#
# a = 7
# a -= 2
#
# a = 7
# a *= 2
#
# a = 9
# a /= 2


# print(a)

# a = 5
# b = 5
# c = a
#
# a += 6
#
# print(a)
# print(c)


# a = 5
# b = 5
# c = a
#
# a += 6
#
# print(id(a))
# print(id(b))
# print(id(c))


# print(True and True)
# print(True and False)
# print(False and False)
# print(False and True)
# #
# print()
#
# print(True or True)
# print(True or False)
# print(False or False)
# print(False or True)

# print(not True and True)
# print(not True and False)
# print(not False and False)
# print(not False and True)


# print(not (True and True))
# print(not (True and False))
# print(not (False and False))
# print(not (False and True))


# print(True and not True and False and not False)


# print(True and True and False and False)
# print(True and True and True and False)
# print(True and True and True and True)

# print(True or True or False or False)
# print(True or True or True and False)

# print(5 > 4 or 3 > 4)

# print(5 or 6)
# print(0 or 6)

# print(5 and 6)
# print(0 and 6)

# print("" or "hello")
# print("" and "hello")

# a = 5
# b = 5
#
# print(a is b)
# print(a == b)


# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
#
# print(id(a))
# print(id(b))

#
# print(a == b)
# print(a is b)



# name = "Otar"
# n = "Otar"
#
# print(name is n)
# print(name is not n)

# print("i" in "Otar")
# print("a" in "Otar")
# print("o" in "Otar")
# print("mn" in "Tumanishvili")

# a = 5
# b = 578
#
# print(str(a) in str(b))

# a = 5
# b = 8
#
# print(a == b)
# print(a != b)
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)


# name = input("Enter your name: ")
#
# if name == "Otar":
#     print("Hello Otar")
#
# print("End of program")


# name = input("Enter your name: ")
#
# if name == "Otar":
#     print("Hello Otar")
# else:
#     print("Hello stranger")
#
# print("End of program")


# name = input("Enter your name: ")
#
# if name == "otar":
#     print("Hello Otar")
# elif name == "alex":
#     print("Hello Alex")
# else:
#     print("Hello stranger")
#
# print("End of program")

# name1 = input("Enter name 1: ")
# name2 = input("Enter name 2: ")
#
# if name1 == "otar":
#     print("Hello Otar")
# elif name2 == "alex":
#     print("Hello Alex")
# else:
#     print("Hello stranger")
#
# print("End of program")


# name1 = input("Enter name 1: ")
# name2 = input("Enter name 2: ")
#
# if name1 == "otar":
#     print("Hello Otar")
#
# if name2 == "alex":
#     print("Hello Alex")
# else:
#     print("Hello stranger")
#
# print("End of program")


# username = "admin"
# password = "admin123"
#
# user_username = input("Enter username: ")
# user_password = input("Enter password: ")
#
#
# if user_username == username and user_password == password:
#     print("Login successful")
# else:
#     print("username or password is incorrect")


username = "admin"
password = "admin123"
phone = 123

user_username = input("Enter username: ")

if user_username == username:
    user_password = input("Enter password: ")

    if user_password == password:
        user_phone = int(input("Enter phone number: "))

        if user_phone == phone:
            print("Login successful")
        else:
            print("phone number is incorrect")
    else:
        print("password is incorrect")
else:
    print("username incorrect")

