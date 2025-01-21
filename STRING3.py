# STRING IN STRING
def stringInString(STRING1,STRING2):
    if STRING1 in STRING2:
        print("THE STRING IS PRESENT")
    else:
        print("THE STRING IS NOT PRESENT")

string1 = input("ENTER THE STRING : ")
string2 = input("ENTER THE STRING TO BE SEARCHED : ")
stringInString(string1,string2)