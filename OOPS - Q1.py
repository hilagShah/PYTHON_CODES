class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def shownumber(self):
        print(self.real,"+",self.img,"i")
    
    def __add__(self, num2):
        NewReal = self.real + num2.real
        NewImg = self.img + num2.img
        return Complex(NewReal, NewImg)
    
    def __sub__(self, num2):
        NewReal = self.real - num2.real
        NewImg = self.img - num2.img
        return Complex(NewReal, NewImg)
    
    def __mul__(self, num2):
        NewReal = (self.real * num2.real) - (self.img * num2.img)
        NewImg = (self.real * num2.img) + (self.img * num2.real)
        return Complex(NewReal, NewImg)
    
    def __truediv__(self, num2):
        NewReal = ((self.real * num2.real) + (self.img * num2.img))/(num2.real**2+num2.img**2)
        NewImg = ((self.img * num2.real) - (self.real * num2.img))/(num2.real**2+num2.img**2) 
        return Complex(NewReal, NewImg)

num1 = Complex(1,5)
num1.shownumber()
num2 = Complex(3,8)
num2.shownumber()
print(f"Addition Result : ")
num3 = num1 + num2
num3.shownumber()
print(f"Subtraction Result : ")
num4 = num1 - num2
num4.shownumber()
print(f"Multiplication Result : ")
num5 = num1 * num2
num5.shownumber()
print(f"Division Result : ")
num6 = num1 / num2
num6.shownumber()
