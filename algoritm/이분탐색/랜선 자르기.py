# 처음 대입할 숫자 입력
# 나누고 더한 값이
# 가장 큰 값으로 나누고 갑을 다 더하기
# 줄의 갯수보다 적으면 2^31 - 1 // 2
# 만약 줄의 갯수가 더 많다면 +1

n, m = map(int, input().split(" "))

data = []

for i in range(n):
    data.append(int(input()))
start, end = 1, max(data)

while start <= end:
    lineCount = 0
    mid = (start + end) // 2
    for i in data:
        lineCount += i // mid

    if lineCount >= m:
        start = mid + 1
    elif lineCount < m:
        end = mid - 1

print(end)
