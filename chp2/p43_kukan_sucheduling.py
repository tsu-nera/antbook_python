n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]

pair = zip(t, s)

sorted(pair)

ans = 0
t = 0

for i in range(n):
    if t < pair[i][1]:
        ans += 1
        t = pair[i][0]

print ans
