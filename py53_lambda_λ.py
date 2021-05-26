# lambda function
# function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lambda parameters:expression

def triple(x):
    return x*3
print(triple(5))
print()


def triple(x): return x*3
print(triple(5))
print()

multiply = lambda x,y : x*y
print(multiply(4,5))
print()

add = lambda x,y,z:x+y+z
print(add(1,2,3))
print()

fullname = lambda firstname,lastname:firstname + " "+lastname
print(fullname("john","mamacita"))
print()

age_check = lambda age:"Adult" if age>=18 else "DekD"
print(age_check(17))
print(age_check(18))
