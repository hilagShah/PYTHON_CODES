def convert(s):
    cleaned_s = "".join(s.lower().split())
    set_ = sorted(set(cleaned_s))
    print(set_)

data = input("ENTER A STRING : ")
convert(data)
    
