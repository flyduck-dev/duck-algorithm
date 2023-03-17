import sys
a = int(sys.stdin.readline().strip())
w_map = [list(map(int,sys.stdin.readline().strip())) for i in range(a)]
check = [[False]*a for i in range(a)]

result = []

cnt = 0

dy = [0, 1, 0 ,-1]
dx = [1, 0, -1, 0]

def dfs(i,j):
    global cnt
    cnt += 1
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if 0 <= ny < a and 0 <= nx < a:
            if w_map[ny][nx] == 1 and check[ny][nx] == False:
                check[ny][nx] = True
                dfs(ny, nx)

for i in range(a):
    for j in range(a):
        if w_map[i][j] == 1 and check[i][j] == False:
            check[i][j] = True
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)