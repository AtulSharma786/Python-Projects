a = input("what is your name")
b = int(input("how much do you earn"))

if b == 0:
    raise ZeroDivisionError("b is 0 so stopping programme")

if a.isnumeric():
    raise Exception("numbers are not allowed")

print(f"hello {a}")

c = input("enter your name")
try:
    print(a)

except Exception as e:

    if c == "atul sharma":
        raise ValueError("atul sharma is blocked")

    print("Exception handled")
