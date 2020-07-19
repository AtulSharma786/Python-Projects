import os

print(dir(os))

print(os.getcwd())

os.chdir("E://")
print(os.getcwd())

f = open("atul.txt")

print(os.listdir("d://"))
print(type(os.listdir("d://")))

os.mkdir("this")
os.mkdir("this/that")
os.makedirs("this/that")


os.rename("atul1.txt", "atulsharma.txt")

print(os.environ.get('path'))

print(os.path.join("e://", "atul.txt"))

print(os.path.exists("e://movie"))
print(os.path.isfile("atul1.txt"))
print(os.path.isdir("e:"))
