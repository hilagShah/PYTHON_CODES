import math
def sine(x,terms):
    value = 0
    for n in range(terms):
      value += (-1)**n *(x**(2*n+1)) / math.factorial(2*n+1)
    return value



a = float(input("ENTER VALUE OF DEGREE (IN RADIANS) : "))
b = int(input("ENTER NUMBER OF TERMS OF APPROXIMATION : "))

approx_sine = sine(a,b)
print("sin(",a,")=",approx_sine)
