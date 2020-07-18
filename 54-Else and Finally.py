f1 = open("atul.txt")

try:
    f = open("file.txt")

except EOFError as e:
    print(e)
    
except Exception as e:
    print(e)

else:
    print("this will run only if except is not running")

finally:
    print("run this anyway")
    f.close()
    f1.close()

print("important stuff")
