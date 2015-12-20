N = 10
M = 10
field = ["#S######.#",
         "......#..#",
         ".#.##.##.#",
         ".#........",
         "##.##.####",
         "....#....#",
         ".#######.#",
         "....#.....",
         ".####.###.",
         "....#...G#"]

vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]
memo = [[float('inf') for j in range(M)] for i in range(N)]


def bfs(i, j):
    queue = []
    queue.append((i, j))

    while len(queue) > 0:
        p, q = queue.pop()

        if field[p][q] == "G":
            continue

        for x, y in zip(vx, vy):
            nx = p + x
            ny = q + y
            if nx < 0 or ny < 0 or nx >= N or ny >= M or field[nx][ny] == "#":
                continue
            if memo[nx][ny] > memo[p][q] + 1:
                queue.append((nx, ny))
                memo[nx][ny] = memo[p][q] + 1

for i in range(N):
    for j in range(M):
        if field[i][j] == "S":
            memo[i][j] = 0
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if field[i][j] == "G":
            print memo[i][j]
            break
