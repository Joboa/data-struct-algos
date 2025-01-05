from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.__PI = pi 

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def area(self):
        return self.__PI*self.radius**2
    
    def perimeter(self):
        return 2*self.__PI*self.radius
    
    def __str__(self):
        return f'Cirle with radius: {self.radius} has area of {self.area()}'
    

my_cirle = Circle(7)
print(my_cirle.get_radius())
my_cirle.set_radius(14)
print(my_cirle.get_radius())   
print("Area:", my_cirle.area())
print("Perimeter", my_cirle.perimeter())
