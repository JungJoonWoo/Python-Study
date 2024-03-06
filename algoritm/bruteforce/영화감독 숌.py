n = int(input())

data = [0]
i = 0
count = 666

while i < n:
    if str(count).__contains__("666"):
        data.append(count)
        i += 1
    count += 1

print(data[n])
