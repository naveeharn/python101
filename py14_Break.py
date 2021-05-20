#  Loop Control statments
# change a loop execution from its normal sequence

# break     used to terminate the loop entirely
# continue  skips to the next iteration of the loop
# pass      does nothing, acts as a placeholder

name = "kuy"

while True:
    name = input("Enter your name : ")
    if name != "":
        break
print("Hello "+str(name))

print()

phoneNumber = "112-044-0112"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

print()

for i in range(1, 9):
    if i == 4:
        pass
    else:
        print(i)
