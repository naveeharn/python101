# *args
# parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add_1(number_1, number_2):
    sumation = number_1 + number_2
    return sumation
print(add_1(3, 4))
# print(1,1,1) // Syntax Error :: parameters in function have 2 parameter
print()

def add_2(*args):
    sumation = 0
    # args[0] = 0 // Syntax Error :: 'tuple' object doesn't support item assignment
    args = list(args)
    args[0] = 0
    for i in args:
        sumation += i
    return sumation
print(add_2(1, 2, 3, 4, 5))
