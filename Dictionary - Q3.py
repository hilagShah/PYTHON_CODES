employees = [
    (101, 'E001', 50000),
    (102, 'E002', 60000),
    (101, 'E003', 55000),
    (103, 'E004', 70000),
    (102, 'E005', 58000),
    (103, 'E006', 72000),
    (101, 'E007', 53000),
    (102, 'E008', 62000),
]

dept_salaries = {}

for dept, emp, salary in employees:
    if dept not in dept_salaries:
        dept_salaries[dept] = []  
    dept_salaries[dept].append(salary) 
for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")
