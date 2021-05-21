# index operator [] 
# gives access to a sequence's element (str,list,tuples)

name = "geogeo mamaCita"
print(name)

if name[0].islower():
    name = name.capitalize()
print(name)

firstname = name[:6].upper()
print(firstname)

lastname = name[7:].lower()
print(lastname)

lastChracter = name[-1]
print(lastChracter)
lastChracter = name[-2]
print(lastChracter)