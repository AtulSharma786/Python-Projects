def function(a, b, c, d, e):
    print(a, b, c, d, e)


function("atul","harsh","sharma","harry","faltu")


def fun(normal, *argsatul, **kwargsatul):
    print(normal)
    for item in argsatul:
        print(item)

    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargsatul.items():
        print(f"{key} is a {value}")


kw = {"atul": "monitor", "sharma": "Fitness instructor", "harsh": "student"}
normal = "I am a normal Argument and the students are:"
atul = ["atul", "sharma", "harsh"]
fun(normal, *atul, **kw)
