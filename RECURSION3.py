def count_vowels(n,index =0 ):
    vowels = "aeiouAEIOU"
    if index == len(n):
        return 0
    else:
        return(n[index] in vowels) + count_vowels(n,index+1)

data = input("ENTER A STRING : ")
print(count_vowels(data))
