import random
list1 = []
for i in range(10):
    list1.append(random.randrange(-15,15))
print(list1)
new_list=list(map(lambda x : x**2,list1))
print(new_list)
    
