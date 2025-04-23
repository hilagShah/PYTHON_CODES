def binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary(n//2) + str(n%2)

num = int(input("ENTER A NUMBER : "))
if num >= 0:
    print(f"THE BINARY OF {num} is {binary(num)}.")
else:
    print("ENTER A NON-NEGATIVE NUMBER.")
