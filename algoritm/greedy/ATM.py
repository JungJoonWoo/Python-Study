import sys

n = int(sys.stdin.readline())

times = list(map(int, sys.stdin.readline().split()))

times.sort()

timeSum = 0
timeCurrent = 0
for time in times:
    timeCurrent += time
    timeSum += timeCurrent
print(timeSum)
