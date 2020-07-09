class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary} and rile is {self.role} and no of leaves is {self.no_of_leaves}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


atul = Employee("atul sharma", 99999999, "instructor")
rohan = Employee("rohan", 1111111, "student")

atul.change_leaves(89)
rohan.change_leaves(34)

print(rohan.printdetails())
print(atul.printdetails())
print(atul.salary)
