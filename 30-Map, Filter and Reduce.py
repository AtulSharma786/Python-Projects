numbers = ["3", "34", "64"]

print(numbers)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers = list(map(int, numbers))


numbers[2] = numbers[2]+1

print(numbers)

num = [2, 54, 56, 876, 76]
square = list(map(lambda a: a*a, num))
print(square)

square = lambda a: a*a
cube = lambda a: a*a*a

func = [square, cube]

for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

# -----------------------------------------------------------filter
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5


gr_than_5  = list(filter(is_greater_5, list1))
print(gr_than_5)

# --------------------------------------------------------------reduce

from functools import reduce

list1 = [1, 2, 3, 4, 5]
num = reduce(lambda a, b: a+b, list1)

# num=0
# for i in list1:
#     num = num+i
# print(num)

print(num)
