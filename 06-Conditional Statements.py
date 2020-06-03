"""var1=6
var2=56
var3=int(input("please enter a number : "))

if var3>var2:
    print("greater than 56")
elif var3==var2:
    print("equal to 56")
else:
    print("lesser than 56")
    """

list=[5,6,7]

item=input("search : ")

print(item in list)
print(item not in list)

if item in list :
    print(item,"is in the list")
else :
    print(item,"is not in list")
