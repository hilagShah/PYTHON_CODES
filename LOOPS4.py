# def primeOrNot(x):
#     y = int(x)
#     count = 0
#     for i in range(1,x+1):
#         if (x % i) == 0:
#             count = count +1
#     if x == 1:
#         print("THE NUMBER IS PRIME NUMBER.")
#     if count > 2:
#         print("THIS NUMBER NOT A PRIME NUMBER.")
#     else:
#         print("THIS NUMBER IS PRIME NUMBER.")

# def palindromeOrNot(n):
#     s = str(n)
#     if s == s[::-1]:
#         print("THE GIVEN NUMBER IS A PALINDROMIC NUMBER.")
#     else:
#         print("THE GIVEN NUMBER IS NOT A PALINDROMIC NUMBER.")


x = int(input("ENTER ANY NUMBER TO BE CHECKED : "))
# primeOrNot(x)
# palindromeOrNot(x)


sum = 0
for i in range(1,x):
    if x%i==0:
        sum= sum + i
if sum == x:
    print("THE NUMBER IS PERFECT")


