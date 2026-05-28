# import time
#
# def task1():
#     print("Task 1 started")
#     time.sleep(3)
#     print("Task 1 finished")
#
# def task2():
#     print("Task 2 started")
#     time.sleep(5)
#     print("Task 2 finished")
#
# def task3():
#     print("Task 3 started")
#     time.sleep(4)
#     print("Task 3 finished")
#
# start = time.time()
#
# task1()
# task2()
# task3()
#
# end = time.time()
#
# print(f"Total time: {end - start:.2f} seconds")

# import time, threading
#
# def task1():
#     print("Task 1 started")
#     time.sleep(3)
#     print("Task 1 finished")
#
# def task2():
#     print("Task 2 started")
#     time.sleep(5)
#     print("Task 2 finished")
#
# def task3():
#     print("Task 3 started")
#     time.sleep(4)
#     print("Task 3 finished")
#
# start = time.time()
#
# thread1 = threading.Thread(target=task1)
# thread2 = threading.Thread(target=task2)
# thread3 = threading.Thread(target=task3)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# end = time.time()
#
# print(f"Total time: {end - start:.2f} seconds")


# import time, threading
#
# def task(name):
#     print(f"Task {name} started...")
#     time.sleep(2)
#     print(f"Task {name} finished!")
#
# threads = []
#
# start = time.time()
#
# for i in range(1, 5001):
#     thread = threading.Thread(target=task, args=(i, ))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# end = time.time()
#
#
# print(f"Total time: {end - start:.2f} seconds")


# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def task(name):
#     print(f"Task {name} started...")
#     time.sleep(2)
#     print(f"Task {name} finished!")
#
# start = time.time()
#
# with ThreadPoolExecutor(max_workers=5000) as executor:
#     for i in range(1, 10001):
#         executor.submit(task, i)
#
# end = time.time()
#
# print(f"Total time: {end - start:.2f} seconds")


# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def task(name):
#     time.sleep(2)
#     return f"Task {name} finished!"
#
# start = time.time()
#
# with ThreadPoolExecutor(max_workers=100) as executor:
#     threads = [executor.submit(task, i) for i in range(1, 101)]
#
#     for thread in threads:
#         print(thread.result())
#
# end = time.time()
#
# print(f"Total time: {end - start:.2f} seconds")










