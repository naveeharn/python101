# keyword argument
# arguments preceded by an identifier when we pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives

def hello(first,middel,last):
    print("Hello "+first+" "+middel+" "+last+" Fuck you")

hello("mamacita","geogeo","john")
hello(last="mamacita",middel="geogeo",first="john")