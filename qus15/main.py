#15. Write a function get_hypotenuse that returns the hypotenuse of a right triangle
#given the other two sides.
#>>> get_hypotenuse(0, 0)
#0.0
#>>> get_hypotenuse(3, 4)
#5.0
def get_hypotenuse(side1, side2):
    hypotenuse = (side1**2 + side2**2)**0.5
    return hypotenuse


side1 = int(input("Enter the value os side 1: "))
side2 = int(input("Enter the value os side 2: "))
print(f'hypotenuse is {get_hypotenuse(side1,side2)}')

