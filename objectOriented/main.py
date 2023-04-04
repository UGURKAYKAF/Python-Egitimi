# class Employee():
#     employee_name = "uğur"
#     department = "departmant"
#     startingYear = 2021
#     salary = 5000

# myObject = Employee()

# print(myObject.employee_name)
# print(myObject.department)
# print(myObject.startingYear)
# print(myObject.salary)

# *************************************************

class Employee():
    def __init__(self,employee_name,department,startingYear,salary):
        self.employee_name = employee_name 
        self.department = department
        self.startingYear = startingYear
        self.salary = salary 

employee1 = Employee("ben","sales",2020,5000)

print(employee1.employee_name)
print(employee1.department)
print(employee1.startingYear)
print(employee1.salary)
