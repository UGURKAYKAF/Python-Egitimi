# class Employee():
#     employee_name = "Ben"
#     department  = "sales"
#     starting_year  = 2020
#     salary = 5000

# myObject  = Employee()

# print("Employee name: " + myObject.employee_name)
# print("Department: " + myObject.department)
# print("Starting Year: " + myObject.starting_year)
# print("Salary: " + myObject.salary)

# --------------------------------------------------------

class Employee ():
    def __init__(self, employee_name, department, starting_year, salary):
        self.employee_name = employee_name
        self.department = department
        self.starting_year = starting_year
        self.salary = salary

employee_1 = Employee("Ben", "sales", 2020, 5000)

print("Employee name: " + employee_1.employee_name)
print("Department: " + employee_1.department)
print("Starting Year: " + employee_1.starting_year)
print("Salary: " + employee_1.salary)