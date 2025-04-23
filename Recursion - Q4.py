def reverse_list(lst):
    if len(lst) == 0:
        return []
    
    return [lst[-1]] + reverse_list(lst[:-1])

data = list(map(int, input("ENTER NUMBERS SEPERATED BY SPACE : ").split()))
print(reverse_list(data))
