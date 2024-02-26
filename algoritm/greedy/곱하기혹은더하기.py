s = list(map(int, input()))

result = 0

for i in range(len(s)):

    if result <= 1 or s[i] <= 1:
        result += s[i]
    else:
        result *= s[i]

print(result)
