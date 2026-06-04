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
#     if b == 0:
#         raise ZeroDivisionError("Division by zero is not allowed")
#     return a / b
#
# def is_even(num):
#     return num % 2 == 0

class Student:
    discount = 0.9

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self, domain):
        return f"{self.first_name}.{self.last_name}@{domain}"

    def get_pay(self):
        self.pay *= self.discount
