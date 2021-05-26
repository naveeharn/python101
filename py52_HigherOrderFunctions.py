#  Higher Order Function
# a function that either:

# 1. accepts a function as an argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
print()

# or

# 2. returns a function
# (In python, functions are also treated as objects)

def divistor(x):
    print("1")
    def dividend(y):
        print("2")
        return y/x
    print("3")
    return dividend

print("-4-")
divide = divistor(2)
print("-5-")
print(divide(10))
print("-6-")