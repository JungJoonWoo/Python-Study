n = int(input())
list = list(map(int, input().split()))
result = 0
for i in range(n):
    count = 0

    for j in range(1, list[i] + 1):
        if list[i] % j == 0:
            count += 1

    if count == 2:
        result += 1

print(result)
