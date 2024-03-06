n, m = map(int, input().split())
data = [[] * j for j in range(n)]

for i in range(n):
    data[i] = input()

# print(data)
list = []

for i in range(n):
    count = 0
    # for j in range(m, m - 7):
