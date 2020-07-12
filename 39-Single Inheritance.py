class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary} and rile is {self.role} and no of leaves is {self.no_of_leaves}."

    @classmethod # it changes class attribute not for only instance
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good", string)
        # return "ok bye"
        # return print("this is good", string)

class Programmer(Employee):
    
    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages

    def printprog(self):
        return f"the programmer's name is {self.name}. salary is {self.salary} and role is {self.role} and knows {self.languages}"

atul = Employee.from_dash("atul sharma-99999999-instructor")
rohan = Employee.from_dash("rohan-1111111-student")

shubham = Programmer ("shubham", 555, "programmer",["python"])
karan = Programmer ("karan", 777, "programmer",["python"])

print(karan.printprog())
