n = int(input("Please enter an integer "))


def factorial_of(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial_of(n-1)


print(factorial_of(n))
