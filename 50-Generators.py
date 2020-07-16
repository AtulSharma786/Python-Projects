def gen(n):
    for i in range(n):
        yield i


g = gen(4)
# print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# print(g.__next__())

# for i in g:
#     print(i)

h = "harry"
# h = 53436

# print(h[0])

# print(iter(h))

iter = iter(h)

print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())

# print(iter.__next__())

# for i in h:
#     print(i)
