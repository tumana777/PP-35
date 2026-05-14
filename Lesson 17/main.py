# decorators

# def change_value(func):
#     def wrapper(x, y):
#         x += 10
#         y += 10
#         return func(x, y)
#     return wrapper
#
# def satesto(a, b):
#     print(f"a = {a}, b = {b}")
#
# @change_value
# def test(a, b):
#     print(f"a = {a}, b = {b}")
#
# test(1, 2)
#
# @change_value
# def another_test(a, b):
#     print(f"a = {a}, b = {b}")
#
# another_test(8, 6)

# import time

# def test():
#     print("Function Execution Started...")
#     start_time = time.time()
#     time.sleep(2)
#     end_time = time.time()
#     print("Function Execution Finished.")
#     print(f"Execution Time: {end_time - start_time:.2f} seconds")
#
# test()

# def time_counter(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution Time: {end_time - start_time:.2f} seconds")
#     return wrapper
#
# @time_counter
# def test():
#     print("Function Execution Started...")
#     for _ in range(3):
#         input("Press Enter to continue...")
#     print("Function Execution Finished.")

# t = time_counter(test)
# t()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def print_list(self):

        current = self.head

        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# 7 -> 8 -> 6 -> 4

ll = LinkedList()
ll.append(8)
ll.append(6)
ll.append(4)
ll.append(10)
ll.prepend(7)
ll.prepend(5)

ll.print_list()

ll.delete(8)

ll.print_list()


# ll.delete(8)






