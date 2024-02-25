
a = 0;
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()

print((lambda a,b: a*b)(4, 5))