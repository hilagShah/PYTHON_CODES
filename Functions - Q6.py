def values(x):
    list_1 = []
    for i in range(1,x+1):
        if i<x and i**2<x and i**3<x:
            list_1.append((i,i**2,i**3))
    return list_1

data = int(input("ENTER x = "))
print(values(data))

            
    
