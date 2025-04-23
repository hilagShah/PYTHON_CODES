import math

def permutation(n,r):
  return math.factorial(n) // math.factorial(n-r)
def combination(n,r):
  return math.factorial(n) // (math.factorial(n-r)*math.factorial(r))

x = int(input("ENTER VALUE OF n : "))
y = int(input("ENTER VALUE OF r : "))
print("nCr = ",combination(x,y))
print("nPr = ",permutation(x,y))
