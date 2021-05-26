# list comprehension
# a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

squares = []                # create an empty list
for i in range(1, 11):      # create a for loop ( 10 elemets )
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

print()

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students)) # list = [expression for item in iterable] //
print(passed_students)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = [i for i in students if i >= 60]          # list = [expression for item in iterable if conditional] //
print(passed_students)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = [i if i>= 60 else "FAILED" for i in students]          # list = [expression (if/else) for item in iterable] //
print(passed_students)
