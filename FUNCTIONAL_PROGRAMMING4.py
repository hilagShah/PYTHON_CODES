lst = ["madam","python","malayalam",12321]

pallindrome = list(filter(lambda x : str(x) == str(x)[::-1],lst))
print("List", lst)
print("Pallindrome : ", pallindrome)
