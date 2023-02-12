n = 4
s = 5

frames = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
cnt = 0


def dfs(x, y):
    global cnt

    if y > s - 1 or y < 0 or x > n - 1 or x < 0:
        return 1

    if frames[x][y] == 0:
        frames[x][y] = 1
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
        return 0


for i in range(n):
    for j in range(s):
        if frames[i][j] == 0:
           if dfs(i, j) == 0:
            cnt += 1


print(cnt)
