def solution(n):
    n = int(n)
    res = 0
    while n != 1:
        if n & 1 == 0:
            n >>= 1
        elif n == 3  or ((n + 1) & n) > ((n - 1) & (n - 2)):
            n -= 1
        else:
            n += 1
        res += 1
    return res