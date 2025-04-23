import csv

students = {}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        rollno = row['RollNo']
        name = row['Name']
        marks1 = int(row['Subject1'])
        marks2 = int(row['Subject2'])
        marks3 = int(row['Subject3'])
        total = marks1 + marks2 + marks3
        
        students[rollno] = {
            'name': name,
            'subject1': marks1,
            'subject2': marks2,
            'subject3': marks3,
            'total': total
        }


print("\nStudent Data with Total Marks:\n")
for rollno, info in students.items():
    print(f"Roll No: {rollno}")
    print(f"Name   : {info['name']}")
    print(f"Marks  : {info['subject1']}, {info['subject2']}, {info['subject3']}")
    print(f"Total  : {info['total']}")
    print("-" * 30)
