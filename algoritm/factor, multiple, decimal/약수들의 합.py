data = 0
while True:
    data = int(input())
    if data == -1:
        break
    list = []

    for i in range(1, data):
        if data % i == 0:
            list.append(i)

    if data == sum(list):
        print(f"{data} =", end=" ")
        print(" + ".join(map(str, list)))

    else:
        print(f"{data} is NOT Perfect.")
