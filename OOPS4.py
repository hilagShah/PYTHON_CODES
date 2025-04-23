import math

class Polygon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length
    
    def perimeter(self):
        if self.sides < 3:
            return "Invalid polygon! A polygon must have at least 3 sides."
        return self.sides * self.length
    
    def area(self):
        if self.sides < 3:
            return "Invalid polygon! A polygon must have at least 3 sides."
        return (self.sides * self.length**2) / (4 * math.tan(math.pi / self.sides))

n = int(input("ENTER NUMBER OF SIDES (>=3): "))
if n < 3:
    print("Invalid input! A polygon must have at least 3 sides.")
else:
    s = float(input("ENTER THE LENGTH OF SIDE: "))

    polygon = Polygon(n, s)
    per = polygon.perimeter()
    are = polygon.area()

    print(f"\nPerimeter: {per:.2f}")
    if isinstance(are, str):
        print(are)
    else:
        print(f"Area: {are:.2f}")
