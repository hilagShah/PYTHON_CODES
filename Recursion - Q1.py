def prime_factors(n,divisor = 2):
    if n == 1:
        return []
    
    if n % divisor == 0:
        return [divisor] + prime_factors(n//divisor,divisor)
    else:
        return prime_factors(n,divisor+1)



num = int(input("ENTER A NUMBER : "))

if num>1:
    print("PRIME FACTORS : ", prime_factors(num))
else:
    print("ENTER A NUMBER GREATER THAN 1")
