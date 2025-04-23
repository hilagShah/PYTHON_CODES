def power(a,b):
    if b == 0:
        return 1
    else:
        return a * power(a,b-1)

x = int(input("ENTER BASE : "))
y = int(input("ENTER POWER : "))
print(power(x,y))
