""" race condision example """

# import threading


# # global variable x
# x = 0


# def increment():
#     global x
#     x += 1


# def thread_task():
#     for _ in range(100000):
#         # lock.acquire()
#         increment()
#         # lock.release()


# def main_task():
#     global x
#     x = 0
#     # lock = threading.Lock()

#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()


# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print("Iteration {}: x = {}".format(i, x))


# import time
# import threading
# """mutex example"""

# # Python create mutex
# my_mutex = threading.Lock()


# class thread_one(threading.Thread):
#     def run(self):
#         # Python mutex global
#         global my_mutex
#         print("The first thread is now sleeping")
#         time.sleep(10)
#         print("First thread is finished")
#         # Python release mutex: once the first thread
#         # is done, we release the lock
#         my_mutex.release()


# class thread_two(threading.Thread):
#     def run(self):
#         # Python mutex global
#         global my_mutex
#         print("The second thread is now sleeping")
#         time.sleep(1)
#         # Python mutex acquire: second thread has to
#         # to keep waiting until the lock is released
#         my_mutex.acquire()
#         print("Second thread is finished")


# # Python mutex acquire: main thread is acquiring the lock
# my_mutex.acquire()
# t1 = thread_one()
# t2 = thread_two()
# t1.start()
# t2.start()


# from threading import Semaphore, Thread
# import time

# obj = Semaphore()


# def display():
#     obj.acquire()
#     print('Hello, ')
#     time.sleep(5)
#     print("end hello")
#     obj.release()


# def display1():
#     obj.acquire()
#     print('Hello1, ')
#     time.sleep(1)
#     print("end hello 1")
#     obj.release()


# t1 = Thread(target=display)
# t2 = Thread(target=display1)


# t1.start()
# t2.start()


from multiprocessing import Pool


def func(x):
    return x*x


if __name__ == "__main__":
    res = []
    with Pool() as pool:
        res.append(pool.map(func, [1, 2, 3]))
        print(res)
    print(res)
