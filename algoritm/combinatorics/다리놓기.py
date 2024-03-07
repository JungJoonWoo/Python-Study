# 4 5


def factorial(param):
    result = 1
    if param == 0 or param == 1:
        return 1
    for i in range(1, param + 1):
        result *= i

    return result


num = int(input())

for i in range(num):
    r, n = map(int, input().split())
    combination = factorial(n) // (factorial(r) * factorial(n - r))
    print(combination)
# nCr -> 4 C 2
#
# 4!
# --
# 2!*2!
