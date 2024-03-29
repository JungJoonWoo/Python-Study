# 1 2 3 4 5 6 7 -> 4 5 6 7 1 2
# 4 5 6 7 1 2
# 7 1 2 4 5
# 4 5 7 1
# 1 4 5
# 1 4

import time
from collections import deque

startTime = time.time()

n, k = map(int, input().split())

n = [i for i in range(1, n + 1)]
deque = deque(n)

result = []

for i in range(0, len(n)):
    for j in range(0, k - 1):
        deque.append(deque.popleft())
    result.append(deque.popleft())
print("<" + ", ".join(map(str, result)) + ">")

endTime = time.time()

print(endTime - startTime)
