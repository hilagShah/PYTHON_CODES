def fun():
    print("THIS IS FUNCTION fun().")
def disp():
    print("THIS IS FUNCTION disp().")
def msg():
    print("THIS IS FUNCTION msg().")

lst = [fun,disp,msg]
for el in lst:
    el()
