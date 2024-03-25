# k번째로 큰 수 찾기
# 행마다 갯수 찾기
def count(mid):
    return sum(min(mid // i, n) for i in range(1, 1 + n))


def binary_search():
    first, last = 1, n * n
    while first <= last:
        mid = (first + last) // 2
        if count(mid) < k:
            first = mid + 1
        else:
            last = mid - 1
    return first


n = int(input())
k = int(input())
print(binary_search())
