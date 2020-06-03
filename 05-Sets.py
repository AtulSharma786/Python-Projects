s = {1,2}

print(s)

s.add(1)
s.add(7)

s1 = s.union({1, 2, 3, 4, 5, 6, 7, 7})

s1 = s.intersection({1, 2, 3, 4, 5, 6, 7, 7})

print(s1)
s.remove(2)

s1 = {4, 6}

print(s1)
print(s)
print(s1.isdisjoint(s))
