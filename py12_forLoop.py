# for loop 
# a statement that will execute it's block of code a limited amount of times
# 
# while loop    = unlimited
# for loop      =limited

for i in range(4):
    print(i+1)

print()

for i in range(110,112):
    print(i)

print()

for i in range(0,10,3):
    print(i)

print()

string = "wasd"
for i in string:
    print(i)

print()

import time

for seconds in range(3,0,-1):
    print(seconds)
    time.sleep(1)
print("TIME'S UP")
