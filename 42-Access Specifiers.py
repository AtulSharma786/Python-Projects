class Employee:
    no_of_leaves = 8
    _protected = 9
    __private = 89


atul = Employee()

print(atul._protected)

# print(atul._private)

print(atul._Employee__private)
