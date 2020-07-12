class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        print( f"name is {self.name}. salary is {self.salary} and rile is {self.role} and no of leaves is {self.no_of_leaves}.")

    @classmethod  # it changes class attribute not for only instance
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good", string)


atul = Employee.from_dash("atul sharma-99999999-instructor")
rohan = Employee.from_dash("rohan-1111111-student")


class Player:
    no_of_games = 4
    var = 9

    def __init__(self, name, game):
        self.name = name
        self.game = game


class CoolProgrammer(Employee, Player):
    language = "c++"

    def printlanguage(self):
        print(self.language)


shubham = Player("shubham", ["cricket"])
karan = CoolProgrammer("karan", 8999, "coolprogrammer")

print(karan.var)
