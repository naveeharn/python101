# Python threading tutorial

# thread
# a flow of execution. Like a separate order of instructions.
# However each thread takes a turn running to achieve concurrency
# GIL = (global interpreter lock),
# allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound
# program/task spends most of it's time waiting for internal events (CPU intensive)
# use multiprocessing

# io bound
# program/task spends most of it's time waiting for external events (user input, web scraping)
# use multithreading

import threading
import time

for i in range(1,5):
    print(time.perf_counter())
    time.sleep(1)


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


def eat_breakfast():
    time.sleep(1)
    print(str(time.ctime(time.time())) + " -> You eat breakfast")


def drink_coffee():
    time.sleep(2)
    print(str(time.ctime(time.time())) + " -> You drank coffee")


def study():
    time.sleep(3)
    print(str(time.ctime(time.time())) + " -> You finish studying")


eat_breakfast()
drink_coffee()
study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

time.sleep(5)

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

eat_breakfast()
drink_coffee()
study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
