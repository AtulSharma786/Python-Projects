# Use of emumerate functions
l1 = ["bhindi", "potato", "tomato", "chocolate"]

# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f"buy {item}")
#     i+=1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"buy {item}")
