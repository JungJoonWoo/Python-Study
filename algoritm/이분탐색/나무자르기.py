n, m = map(int, input().split())

treeLen = list(map(int, input().split()))
start, end = 0, max(treeLen)

while start <= end:
    mid = (start + end) // 2
    len = 0
    for i in treeLen:
        if i >= mid:
            len += i - mid

    if len >= m:
        start = mid + 1
    elif len < m:
        end = mid - 1

print(end)
