import json


empcode = input("Enter employee code: ")
empname = input("Enter employee name: ")
doj = input("Enter date of joining (DD-MM-YYYY): ")
salary = float(input("Enter salary: "))


employee = {
    "empcode": empcode,
    "empname": empname,
    "doj": doj,
    "salary": salary
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)
print("\nEmployee data saved to 'employee.json' successfully!")


with open("employee.json", "r") as file:
    loaded_employee = json.load(file)


print("\nDeserialized Employee Data from JSON:")
print(f"Emp Code : {loaded_employee['empcode']}")
print(f"Name     : {loaded_employee['empname']}")
print(f"DOJ      : {loaded_employee['doj']}")
print(f"Salary   : {loaded_employee['salary']}")
