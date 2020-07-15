class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary} and rile is {self.role} and no of leaves is {self.no_of_leaves}."
        # print(f"name is {var.name}. salary is {var.salary} and rile is {var.role}.")

    @classmethod # it changes class attribute not for only instance
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return self.printdetails()


emp1 = Employee("atul sharma",345, "programmer")
# emp2 = Employee("rohan",5, "cleaner")

print(emp1)
print(repr(emp1))
print(str(emp1))
