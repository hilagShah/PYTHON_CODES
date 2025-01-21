string = input("ENTER THE STRING : ")

def switch_case(input_string):
    output_string = ''
    
    for char in input_string:
        if 'a' <= char <= 'z': 
            output_string += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  
            output_string += chr(ord(char) + 32)
        else:
           
            output_string += char

    return output_string


result = switch_case(string)
print(f"The converted version is: {result}")

