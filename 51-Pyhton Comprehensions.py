# ls = []
# for i in range (100):
#     if i%3 == 0 :
#         ls.append(i)

# ls = [i for i in range(100) if i %3 == 0 ]
#
# print(ls)

# dict = {i:f"item{i}" for i in range(90,100)}

# dict = {i:f"item{i}" for i in range(5)}
# dict = {value:key for key,value in dict.items()}
# print(dict)


# dresses = {dress for dress in ["dress 1","dress2","dress 1","dress2","dress 1","dress2"]}
#
# print(dresses)

evens = (i for i in range(100) if i % 2 == 0)

# print (evens)
# print (type(evens))

# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

for item in evens:
    print(item)
