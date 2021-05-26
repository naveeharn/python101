# zip(*iterables)
# aggregate elements from two or more iterables (list, tuples, sets, etc.)
# creates a zip object with paired elements stored in tuples for each element

username = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(username, passwords)
print(users)

users = zip(username, passwords, login_date)
print(users)

for i in users:
    print(i)

print(type(users)) 

users = dict(zip(username, passwords))

print(type(users))

for key, value in users.items():
    print(key+" : "+value)

