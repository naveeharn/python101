# exception   
# events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter some number to divide : "))
    denominator = int(input("Enter some number to divide by : "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can not divide by zero! idiot! ")
except ValueError as e:
    print(e)
    print("Enter only number IDIOT! ")
except Exception as e:
    print(e)
    print("Exception I don't know")
else:
    print(result)
finally:
    print("This is always execute")

