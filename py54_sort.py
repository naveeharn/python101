# sort() method     = used with lists
# sort() function   =used with iterables

students = ["He", "Sb", "Na", "Xe", "Fr"]
print(students)
students.sort()
print(students)
print()

students = ["He", "Sb", "Na", "Xe", "Fr"]
print(students)
students.sort(reverse=True)
print(students)
print()

students = ("He", "Sb", "Na", "Xe", "Fr")
print(students)
sorted_students = sorted(students) #iterables
print(students)
print(sorted_students)
print()

students = ("He", "Sb", "Na", "Xe", "Fr")
print(students)
sorted_students = sorted(students, reverse=True) #iterables
print(students)
print(sorted_students)
print()


students = [
    ("He", "F", 40),
    ("Sb", "A", 21),
    ("Na", "D", 52),
    ("Xe", "B", 18),
    ("Fr", "C", 58)
]
students.sort()
for i in students:
    print(i)
print()


students = [
    ("He", "F", 40),
    ("Sb", "A", 21),
    ("Na", "D", 52),
    ("Xe", "B", 18),
    ("Fr", "C", 58)
]
grade = lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print(i)
print()


students = [
    ("He", "F", 40),
    ("Sb", "A", 21),
    ("Na", "D", 52),
    ("Xe", "B", 18),
    ("Fr", "C", 58)
]
age = lambda grades:grades[2]
students.sort(key=age)
for i in students:
    print(i)
print()


students = [
    ("He", "F", 40),
    ("Sb", "A", 21),
    ("Na", "D", 52),
    ("Xe", "B", 18),
    ("Fr", "C", 58)
]
age = lambda grades:grades[2]
students.sort(key=age,reverse=True)
for i in students:
    print(i)
print()


students = [
    ("He", "F", 40),
    ("Sb", "A", 21),
    ("Na", "D", 52),
    ("Xe", "B", 18),
    ("Fr", "C", 58)
]
age = lambda grades:grades[2]
sorted_students = sorted(students,key=age,reverse=True) #iterables
for i in sorted_students:
    print(i)
print()

