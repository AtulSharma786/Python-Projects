f = open("atul.txt", "rt")

print(f.readline())  # Read only one line in the file
print(f.readlines())  # Read all the lines in the file

f.close()
