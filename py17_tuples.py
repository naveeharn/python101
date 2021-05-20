# tuple
# collection which is orderd and unchangeable
# used to group together related data

student = ("asdf",112,"male")

print("count "+ str(student.count("asdf")))
print("index "+ str(student.index("male")))

for i in student:
    print(i)

if 112 in student:
    print("student have 112")
   
# tuples