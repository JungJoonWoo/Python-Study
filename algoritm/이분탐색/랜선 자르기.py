# 처음 대입할 숫자 입력
# 나누고 더한 값이
# 가장 큰 값으로 나누고 갑을 다 더하기
# 줄의 갯수보다 적으면 2^31 - 1 // 2
# 만약 줄의 갯수가 더 많다면 +1

n, m = map(int, input().split(" "))

data = []

for i in range(n):
    data.append(int(input()))

data.sort()
count = 0
divNum = data[len(data) // 2]

while True:
    count = 0
    for i in data:
        count += i // divNum
    if count == m:
        print(int(divNum))
        break
    elif count < m:
        divNum -= divNum / 2
    elif count > m:
        divNum += divNum / 2

# divNum = data[len(data) - 1]
# while count != m:
#     count = 0
#     for i in data:
#         count += i // divNum
#
#     if count == m:
#         print(int(divNum))
#         break
#     elif count < m:
#         divNum //= 2
#     elif count > m:
#         divNum += divNum // 2
# divNum = sum(data) // m
# while True:
#     count = 0
#     for i in data:
#         count += i // divNum
#     if count == m:
#         print(int(divNum))
#         break
#     elif count < m:
#         divNum /= 2
#     elif count > m:
#         divNum += divNum / 2
