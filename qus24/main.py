#24. Write a class that represents a circle.The circle should have a radius, a diameter,
#and an area. It should also have a nice string representation.

import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.diameter=radius*2
        self.area = math.pi *radius**2
    def __str__(self):
        return f"Circle with radius {self.radius},diameter {self.diameter}, and area {self.area:.2f}"
my_circle=Circle(4)
print(my_circle)