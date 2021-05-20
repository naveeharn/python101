# logical operators (and,or not)
# used to check if two or more conditional statements

temp = int(input("What is the Temperature outside : "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today! \nGo outside ")
elif not(temp >= 0 and temp <= 30):
    print("the temperature is bad today! \nStay inside")
