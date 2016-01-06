n = 4
W = 5
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]


def rec(i, j):

    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i + 1, j)
    else:
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])

    return res

print rec(0, W)
