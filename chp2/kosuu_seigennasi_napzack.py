n = 3
W = 7
w = [3, 4, 2]
v = [4, 5, 3]

dp = [[0 for i in range(10001)] for j in range(10001)]

for i in range(n):
    for j in range(W + 1):
        # k = 0
        # while k * w[i] <= j:
        #     dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - k * w[i]] + k * v[i])
        #     k += 1
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])

print dp[n][W]
