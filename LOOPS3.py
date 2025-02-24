def countAlphabets(str):
    count1 = 0
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(str)):
        if str[i] in string:
            count1 = count1 +1
    return count1
def countNumbers(str):
    count2 = 0
    string = '1234567890'
    for i in range(len(str)):
        if str[i] in string:
            count2 = count2 +1
    return count2
str = input("ENTER THE STRING : ")
print("THE NUMBER OF ALPHABETS IN STRING = ", countAlphabets(str))
print("THE NUMBER OF ALPHABETS IN STRING = ", countNumbers(str))
