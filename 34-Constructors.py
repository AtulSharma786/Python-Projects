class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary} and rile is {self.role}."


atul = Employee("atul sharma", 99999999, "instructor")
rohan = Employee("rohan", 1111111, "student")

print(rohan.printdetails())
print(atul.printdetails())
