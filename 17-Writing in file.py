f = open("atul.txt", "r+")  # give a insted of r+ to only append in the file

f.write("Atul is very intelligent\n")

print(f.read())

f.write("thank you\n")

f.close()
