# slicing
# create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "john mamacita"

firstname = name[:4]
lastname = name[5:]
funckyName = name[::3]

# print(firstname)

print(name)
print(name[0:4])
print(name[:4])

print(name[5:13])
print(name[5:])

print(name[0:13:3])
print(name[::2])

print(name[::-1])
print(name[::-3])

print("")

website_01 = "https://google.com"
website_02 = "https://pornhub.com"

slice = slice(8, -4)


print(website_01[slice])
print(website_02[slice])
