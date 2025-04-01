def fun():
    print("fun is called")
    return 1
def disp():
    print("disp is called")
    return 2
    
def msg():
    print("msg is called")
    return 3
    
list = [fun , disp , msg]
for i in list:
    i()
    #print(i())
