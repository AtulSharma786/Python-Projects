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

    @classmethod
    def from_dash(cls, string):
        # details = string.split("-")
        # return cls(details[0], details[1],details[2])
        return cls(*string.split("-"))


atul = Employee.from_dash("atul sharma-99999999-instructor")
rohan = Employee.from_dash("rohan-1111111-student")

print(rohan.printdetails())
print(atul.printdetails())
print(atul.salary)
