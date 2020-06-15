# -------------------------------------------Reason Behind Decorators
#
#
# def function1():
#     print("Subscibe now")
#
#
# func2 = function1
# del function1
# func2()
#
#
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
#
# a = funcret(1)
# print(a)
#
#
# def executor(func):
#     func("this")
#
#
# executor(print)
# -------------------------------------------------------------------


def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec


@dec1
def who_is_atulsharma():
    print("atul sharma is a good boy")


# who_is_atulsharma = dec1(who_is_atulsharma)
who_is_atulsharma()
# dec1(who_is_atulsharma)
