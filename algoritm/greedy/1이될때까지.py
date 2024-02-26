#
# def case1():
#     global n
#     n = n - 1
#
# def case2():
#     global n, k
#     n = n // k
#
#
# n, k = map(int, input().split())
# count = 0
# while n != 1:
#     if(n % k == 0):
#         case2()
#     else:
#         case1()
#     count+=1
#
# print(count)

n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k
    count += n - target
    n = target

    if n < k:
        break

    count += 1
    n //= k

count += n-1
print(count)

