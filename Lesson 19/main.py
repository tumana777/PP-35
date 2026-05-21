# def commission_decorator(func):
#     def wrapper(balance, amount):
#         commission = 1
#
#         total_amount = amount + commission
#
#
#         print(f"Balance: {balance}.")
#         print(f"Commission: {commission}.")
#         print(f"Total Amount: {total_amount}.")
#
#         if total_amount > balance:
#             return "Insufficient funds."
#
#         return func(balance, total_amount)
#
#     return wrapper
#
# @commission_decorator
# def withdraw(balance, amount):
#     return f"Transaction successful. New balance: {balance - amount}."
# print(withdraw(100, 100))


# nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = []
#
# for num in nums_list:
#     new_list.append(str(num))

# new_list = [str(num) for num in nums_list]
#
# nums = ", ".join(new_list)

# print(nums)

# with open("numbers.txt", "w") as file:
#     file.write(str(nums))


# with open("numbers.txt", "r") as file:
#     data = file.read()
#
# my_list = data.split(", ")
#
# new_list = [int(i) for i in my_list]
#
# print(new_list)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

p1 = Person("John", 30)

def person_serializer(obj):
    return {
        "name": obj.name,
        "age": obj.age
    }

serialized_person = person_serializer(p1)

def person_deserializer(data):
    return Person(data["name"], data["age"])

deserialized_person = person_deserializer(serialized_person)

print(deserialized_person)












