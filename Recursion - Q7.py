def recursive_sum(lst,n):
    if n == 0:
        return 0
    return lst[n-1] + recursive_sum(lst,n-1)
def recursive_avg(lst):
    if not lst:
        return 0
    return recursive_sum(lst, len(lst)) / len(lst)
data = list(map(int, input("ENTER NUMBER WITH SPACE : ").split()))
print(recursive_avg(data))
