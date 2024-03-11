n = int(input())
a = list(map(int, input().split(" ")))
m = int(input())

a.sort()

data = map(int, input().split())

for i in data:
    if i in a:
        print(1)
    else:
        print(0)
