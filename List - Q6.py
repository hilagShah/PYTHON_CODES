import random

random_int = [random.randint(1,50) for _ in range (1,6)]
print(f"CELCIUS TEMP : {random_int}")
fareh = []
for num in random_int:
    far = (9*num)/5 + 32
    fareh.append(far)
print(f"FARENHEIT TEMP : {fareh}")
