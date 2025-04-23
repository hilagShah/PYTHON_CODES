import random
data = list(random.randint(-15,15) for _ in range(10))
new_list = list(map(lambda x : x**2,data))
print("LIST OF NUMBERS : ", data)
print("LIST OF SQUARED NUMBERS : ", new_list)
