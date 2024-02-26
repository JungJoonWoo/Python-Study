input = list(input())

# 편의를 위해 a -> 1로 바꿈
x = ord(input[0]) - 96
y = int(input[1])

dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]
# -2 +1
moveTypes = ["LD", "LU", "RD", "RU", "UL", "UR", "DL", "DR"]

count = 0

for i in range(len(moveTypes)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1
print(count)
