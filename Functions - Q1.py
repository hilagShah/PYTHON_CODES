def count_lower_upper(str1):
    lower=0
    upper=0
    for char in str1:
        if char.islower():
            lower+=1
        elif char.isupper():
            upper+=1
    return {"lower_case":lower,"upper_case":upper}

str1=input("Enter the string : ")
result=count_lower_upper(str1)
print(result)

    
