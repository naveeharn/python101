# super()
# Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        # super().__init__()

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)

    # def area(self):  //
    #     return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height) -> None:
        super().__init__(length, width)
        self.heigth = height

    def volume(self):
        return self.area() * self.heigth
        # return self.length * self.width * self.heigth //
    

square = Square(3, 3)
cube = Cube(4, 4, 4)

print(square.area())
print(cube.volume())