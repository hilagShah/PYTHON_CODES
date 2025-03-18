def avgMarks(i,j,k,l,m):
    avgMarks = (i+j+k+l+m) / 5
    return avgMarks
i = int(input("ENTER MARKS OF SUBJECT 1: "))
j= int(input("ENTER MARKS OF SUBJECT 2: "))
k= int(input("ENTER MARKS OF SUBJECT 3: "))
l= int(input("ENTER MARKS OF SUBJECT 4: "))
m= int(input("ENTER MARKS OF SUBJECT 5: "))
print("AVERAGE MARKS OF ALL 5 SUBJECTS : ",avgMarks(i,j,k,l,m))
