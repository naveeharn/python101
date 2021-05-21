# Dictionary
# a changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {
    "USA": "New York City",
    "india": "New Dehli",
    'China': 'Beijing',
    'Russia': "Moscow"
}

print(capitals["USA"])
print(capitals["China"])
print(capitals['Russia'])
print()

# print(capitals['Germany']) //Syn tax Error :: Germany not member in captitals

print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())  # For Loop Syntax
print()

for key, value in capitals.items():
    print(key, value)
print()

capitals.update({"Germany":"Berlin"})
for key, value in capitals.items():
    print(key, value)
print()

capitals.update({'USA':'Seatle'})
for key, value in capitals.items():
    print(key, value)
print()

capitals.update({'usa':'Texas'})
for key, value in capitals.items():
    print(key, value)
print()

capitals.pop('China')
for key, value in capitals.items():
    print(key, value)
print()

capitals.clear()
for key, value in capitals.items():
    print(key, value)
print()