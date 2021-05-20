# If Statement
# a block of code that will execute if it's condition is true

age = int(input("Enter some number : "))

if age >= 112:
    print("You are a century old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You have not been born yet")
else:
    print("You are a Child")
