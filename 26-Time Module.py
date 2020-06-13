import time

initial = time.time()

k = 0
while (k < 45):
    print("this is atul sharma")
    time.sleep(1)
    k += 1

print(f"while loop ran in ", time.time()-initial, "seconds")


initial2 = time.time()

for i in range(45):
    print("this is atul sharma")

print(f"for loop ran in ", time.time()-initial2, "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
