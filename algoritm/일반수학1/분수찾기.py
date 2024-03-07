n = int(input())

x = 1
y = 1
count = 1
direction = -1
# 방향이 1이면 왼쪽 아래로 방향이 -1이면 오른쪽 위로
while count != n:
    if x == 1:
        direction *= -1
        y += 1
        count += 1
    elif y == 1:
        direction *= -1
        x += 1
        count += 1

    if count == n:
        break

    if direction == 1:
        x += 1
        y -= 1
    elif direction == -1:
        x -= 1
        y += 1
    count += 1
print(f"{x}/{y}")
