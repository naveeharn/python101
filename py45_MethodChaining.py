# method chaining
# calling multiple methods sequentially
# each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self #add return for chaining method

    def drive(self):
        print("You drive a car")
        return self #add return for chaining method

    def brake(self):
        print("You step on the breaks")
        return self #add return for chaining method

    def turn_off(self):
        print("You turn off the engine")
        return self #add return for chaining method

car = Car()

car.turn_on()
car.drive()
car.brake()
car.turn_off()
print()

car.turn_on().drive().brake().turn_off()
print()

car.turn_on()\
    .drive()\
        .brake()\
            .turn_off()
print()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
print()