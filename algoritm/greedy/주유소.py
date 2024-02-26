import sys

n = int(sys.stdin.readline().rstrip())

cities = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0

minPrice = price[0]

for i in range(n - 1):
    if price[i] < minPrice:
        minPrice = price[i]

    result += minPrice * cities[i]

print(result)
