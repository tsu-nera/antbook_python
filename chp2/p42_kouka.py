V = [1, 5, 10, 50, 100, 500]
C = [3, 2, 1, 3, 0, 2]
A = 620

ans = 0

for i in range(5, 0, -1):
    t = min(A / V[i], C[i])
    A -= t * V[i]
    ans += t

print ans
