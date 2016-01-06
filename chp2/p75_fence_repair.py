from heapq import heappush, heappop

N = 3
L = [8, 5, 8]


def solve():
    ans = 0
    que = []

    for i in range(N):
        heappush(que, L[i])

    while len(que) > 1:
        l1 = heappop(que)
        l2 = heappop(que)

        ans += l1 + l2
        heappush(que, l1 + l2)

    print ans

solve()
