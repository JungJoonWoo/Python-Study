# s = list(input())
# s.sort()
#
# sum = 0
# count = 0
# for word in s:
#     if 0 < ord(word) - 48 < 10:
#         sum += int(word)
#         count += 1
# s = s[count:]
# s.append(str(sum))
# print("".join(s))

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print("".join(result))
