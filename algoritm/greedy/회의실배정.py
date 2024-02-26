n = int(input())

useTimes = [list(map(int, input().split())) for _ in range(n)]

useTimes.sort(key=lambda x: (x[1], x[0]))

endTime = 0
count = 0
for start, end in useTimes:
    if endTime <= start:
        count += 1
        endTime = end
print(count)

# 시간초과
# n = int(input())
#
# useTimes = [[0 for i in range(2)] for j in range(n)]
#
# for i in range(n):
#     useTimes[i][0], useTimes[i][1] = map(int, input().split())
#
# useTimes.sort()
#
# possibleTime = []
# for i in range(n):
#     count = 1
#     endTime = useTimes[i][1]
#     for j in range(i, n):
#         if useTimes[j][0] >= endTime:
#             count += 1
#             endTime = useTimes[j][1]
#     possibleTime.append(count)
#
# possibleTime.sort(reverse=True)
# print(possibleTime[0])
