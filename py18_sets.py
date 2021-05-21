# set 
# collection witch is unordered, unindexed
# No duplicate values

utensils ={"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

for x in utensils:
    print(x)
print()

utensils.add("knife")
for x in utensils:
    print(x)
print()

utensils.remove("fork")
utensils.add("napkin")
for x in utensils:
    print(x)
print()

# utensils.update(dishes) //add all sets
# for x in utensils:
#     print(x)
# print()

dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)
print()

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(utensils))
