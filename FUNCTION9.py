def count_alpha_num(s):
    count_dict = {"alphabets": 0, "digits": 0}
    for char in s:
        if char.isalpha():
            count_dict["alphabets"] += 1
        elif char.isdigit():
            count_dict["digits"] += 1
    
    return count_dict

data = input("ENTER A STRING : ")
print(count_alpha_num(data))
        
