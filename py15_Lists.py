# list 
# used to store multiple items in a single variable

food = ["pizza","steak","hotdog"]

print(food)
print(food[0])

food[0] = "hamburge"

print(food[0])

food.append("kebab")
print()

for i in food:
    print(i)
print()

print(food)
print()

food.remove("steak")
print(food)
print()

food.pop()
print(food)
print()

food.insert(1,"overice")
print(food)
print()

food.sort()
print(food)
print()

food.clear()
print(food)
print()

