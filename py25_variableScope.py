# scope
# The region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created

name = "mamacita" # global scope (available inside and outside functons)

def display_name():
    name = "qwert" # local scope (available only inside thid function)
    print(name)

def display_global_name():
    print(name)

print(name)
display_name()
display_global_name()
 