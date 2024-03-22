# m을 입력받음
# 처음에 9 - 1 -> 8
# for문 처음부터 8을 더해서

n, m = map(int, input().split())

list = []
mid = 0
for i in range(n):
    list.append(int(input()))
list.sort()
result = 0
first, end = 1, list[len(list) - 1] - list[0]  # 1,8

while first <= end:
    count = 0
    mid = (first + end) // 2
    current = list[0]

    for i in list:
        if i >= current:
            count += 1
            current = i + mid

    if count < m:
        end = mid - 1
    elif count >= m:
        result = mid
        first = mid + 1

print(result)
