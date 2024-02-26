# n = int(input())
#
# list = list(input())
#
# array = [[i for i in range(n + 1)] for j in range(n + 1)]
#
# x, y = 1, 1
#
# for i in range(len(list)):
#     if list[i] == "R":
#         if y + 1 > len(list):
#             continue
#         y += 1
#     elif list[i] == "L":
#         if y - 1 < 1:
#             continue
#         y -= 1
#     elif list[i] == "U":
#         if x - 1 < 1:
#             continue
#         x -= 1
#     elif list[i] == "D":
#         if x + 1 > len(list):
#             continue
#         x += 1
#
# print(x, y)

n = int(input())

x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x = nx
    y = ny
print(nx, ny)
