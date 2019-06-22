from sys import maxsize

INT_MAX = maxsize
INT_MIN = -maxsize - 1


def array_manipulation(n, queries):
    arr = [0 for _ in range(n + 1)]
    for row in queries:
        begin, end, value = row
        arr[begin - 1] += value
        arr[end] -= value

    result = INT_MIN
    cur = 0
    for num in arr:
        cur += num
        result = max(result, cur)

    return result
