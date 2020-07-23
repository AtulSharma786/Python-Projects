# == value equality - two objects have the same value
# is reference equality - two references refer to the same object

a = [6, 4, "43"]
b = [6, 4, "43"]
print(b == a)
print(a is b)


b = a
print(a is b)
print(b is a)
