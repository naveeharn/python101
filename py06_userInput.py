message = input("Enter some message : ")
print("message is " + message)

number = input("add some number : ")
# number+=1 //Syntax Error :: because type input is string
number = int(number)
number += 1

print(number)
number = str(number)
print("number + 1 is : "+number)

decimal = float(input("Enter some decimal : "))
decimal += 3.14
print("decimal + 3.14 is " + str(decimal))
