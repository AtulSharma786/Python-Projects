f = open("atul.txt", "rt")

content = f.read()

for line in content:
    print(line)

print(content)

content = f.read(4)  # ------- for next 4 characters
print("2", content)

f.close()
