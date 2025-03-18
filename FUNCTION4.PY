def avgMarks(i,j,k,l,m):
    avgMarks = (i+j+k+l+m) / 5
    totalMarks = i+j+k+l+m
    return avgMarks,totalMarks
i = int(input("ENTER MARKS OF SUBJECT 1: "))
j= int(input("ENTER MARKS OF SUBJECT 2: "))
k= int(input("ENTER MARKS OF SUBJECT 3: "))
l= int(input("ENTER MARKS OF SUBJECT 4: "))
m= int(input("ENTER MARKS OF SUBJECT 5: "))
print("AVERAGE MARKS OF ALL 5 SUBJECTS , TOTAL OF ALL SUBJECTS ",avgMarks(i,j,k,l,m))
