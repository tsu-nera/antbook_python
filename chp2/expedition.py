from heapq import heappush, heappop

N = 4
L = 25

P = 10

A = [10, 14, 20, 21]
B = [10, 5, 2, 4]


def solve():
    A.append(L)
    B.append(0)

    heap = []

    ans = 0
    pos = 0
    tank = P

    for i in range(N):
        d = A[i] - pos

        while tank - d < 0:
            if len(heap) == 0:
                print "-1"
                return

            tank += heappop(heap)
            ans += 1

        tank -= d
        pos = A[i]
        heappush(heap, B[i])

    print ans

solve()
