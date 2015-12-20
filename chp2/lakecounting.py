# http://poj.org/problem?id=2386
N = 10
M = 12

fields = ["W........WW.",
          ".WWW.....WWW",
          "....WW...WW.",
          ".........WW.",
          ".........W..",
          "..W......W..",
          ".W.W.....WW.",
          "W.W.W.....W.",
          ".W.W......W.",
          "..W.......W."]

vx = [1, -1, 0, 0, 1, 1, -1, -1]
vy = [0, 0, 1, -1, 1, -1, 1, -1]

cnt = 0
memo = [[False for i in range(M)] for j in range(N)]


def dfs(i, j):
    memo[i][j] = True

    for x, y in zip(vx, vy):
        nx = i + x
        ny = j + y
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if fields[nx][ny] == "W" and not memo[nx][ny]:
            dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if fields[i][j] == "W" and not memo[i][j]:
            cnt += 1
            dfs(i, j)

print cnt
