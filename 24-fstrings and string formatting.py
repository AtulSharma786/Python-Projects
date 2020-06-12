me = "atul"
a = "this is %s" % me
print(a)

a1 = 3
a = "this is {} {}"
b = a.format(me, a1)
print(b)

a1 = 3
a = "this is {1} {0}"
b = a.format(me, a1)
print(b)

a = f"this is {me} {a1} {4*60}"
print(a)
