def atul():
    x = 20

    def harry():
        global x
        x = 88

    print("before calling harry()", x)
    harry()
    print("after calling harry()", x)


atul()
print(x)
