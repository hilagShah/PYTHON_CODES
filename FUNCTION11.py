def create_lst(list1,list2):
    return list(set(list1) & set(list2))

list1 = [1,6,8,5,2,9,10]
list2 = [6,7,3,2,9,10]

print(create_lst(list1,list2))
