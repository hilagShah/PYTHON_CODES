def ispallindrome(string):
    cleaned_string = "".join(string.lower().split()) 
    
    return cleaned_string == cleaned_string[::-1]

data = input("ENTER STRING : ")
if ispallindrome(data):
    print("YES, THE STRING IS PALLINDROME.")
else:
    print("NO, THE STRING IS NOT PALLINDROME.")
