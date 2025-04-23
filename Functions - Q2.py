def compute(n, terms=4):
    total = 0
    num_str = str(n)
    
    for i in range(1, terms + 1):  
        total += int(num_str * i)  
    
    return total

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")
