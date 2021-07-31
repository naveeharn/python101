
from py39_Car import Car

listCar = []

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

listCar.append(car_1)
listCar.append(car_2)

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

for i in listCar:
    print(i.make)
    print(i.model)
    print(i.year)
    print(i.color)
    i.drive()
    i.stop()
