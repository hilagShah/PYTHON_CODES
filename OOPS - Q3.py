import math

class Solid:
    def __init__(self, shape):
        self.shape = shape.lower()
        self.dimensions = {}
        
    def accept_data(self):
        if self.shape == "sphere":
            self.dimensions["radius"] = float(input("ENTER RADIUS : "))
        elif self.shape == "Cylinder":
            self.dimensions["radius"] = float(input("ENTER RADIUS : "))
            self.dimensions["height"] = float(input("ENTER HEIGHT : "))
        elif self.shape == "cube":
            self.dimensions["side"] = float(input("ENTER SIDE : "))
        else:
            print("INVALID SOLID! SUPPORTED SHAPES ARE CUBE,SPHERE,CYLINDER")
    
    def volume(self):
        if self.shape == "sphere":
            r = self.dimensions.get("radius", 0)
            return (4/3)*(math.pi)*(r**3)
        elif self.shape == "cylinder":
            r = self.dimensions.get("radius", 0)
            h= self.dimensions.get("height", 0)
            return (math.pi)*(r**2)*(h)
        elif self.shape == "cube":
            s = self.dimensions.get("side", 0)
            return s**3
        else:
            return None
    
    def surface_area(self):
        if self.shape == "sphere":
            r = self.dimensions.get("radius", 0)
            return (4)*(math.pi)*(r**2)
        elif self.shape == "cylinder":
            r = self.dimensions.get("radius", 0)
            h= self.dimensions.get("height", 0)
            return 2*(math.pi)*(r)*(h)
        elif self.shape == "cube":
            s = self.dimensions.get("side", 0)
            return (6)*(s**2)
        else:
            return None
        
    
shape_type = input("Enter the type of Solid (Sphere, Cylinder, Cube) : ")
solid = Solid(shape_type)

solid.accept_data()
volume = solid.volume()
surface_area = solid.surface_area()

if surface_area is not None and volume is not None:
    print(f"Surface area is : {surface_area:.2f}")
    print(f"Volume is : {volume:.2f}")
