n = input()

fearLevel = list(map(int, input().split(" ")))

fearLevel.sort()

result = 0
count = 0

dictionary = {}

# for i in range(len(fearLevel)):
#
#     if fearLevel[i] not in dictionary:
#         dictionary[fearLevel[i]] = 0
#
#     dictionary[fearLevel[i]] += 1
#
#     if dictionary[fearLevel[i]] == fearLevel[i]:
#         result += 1
#         dictionary[fearLevel[i]] = 0

for i in fearLevel:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
