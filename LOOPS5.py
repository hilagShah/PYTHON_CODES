#### print all pythagorea triplets
for k in range(1,31):
    for i in range(1,31):
        for j in range(1,31):
            if (i**2 + j**2) == ((k)**2):
                if i<j:
                    print(i,j,k)