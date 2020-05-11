def solution(l):
    num_neg = 0
    greatest_neg = float('-inf')
    if len(l) == 1 and l[0] < 0:
        return str(l[0])
    l = filter(lambda a: a != 0, l)
    for num in l:
        if num < 0:
            greatest_neg = max(greatest_neg, num)
            num_neg += 1
    if (num_neg == len(l) and num_neg < 2):
        return "0"
    res = reduce(lambda x, y: x * y, l)
    if res < 0:
        res /= greatest_neg
    return str(res)