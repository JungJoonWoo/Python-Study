import sys

s = sys.stdin.readline().strip()

if "-" in s:
    s = s.split("-")
    result = sum(map(int, s[0].split("+")))
    for i in range(1, len(s)):
        result -= sum(map(int, s[i].split("+")))

else:
    result = eval(s)

print(result)
