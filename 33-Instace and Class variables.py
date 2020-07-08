class Employee:
    no_of_leaves = 8
    pass


atul = Employee()
rohan = Employee()

atul.name = "atul sharma"
atul.salary = "9999999"
atul.role = "instructor"

Employee.no_of_leavesl = 8

rohan.name = "rohan"
rohan.salary = "1111111"
rohan.role = "student"

print(atul.__dict__)
print(Employee.__dict__)
print(atul.name)