# 백준 문제 '그림'

import sys
from collections import deque

n,m = map(int, input().split())
w_map = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
check = [[False] * m for i in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y,x):
    result = 1
    q= deque()
    q.append((y,x))
    while q:
        ey,ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if check[ny][nx] == False and w_map[ny][nx] == 1:
                    check[ny][nx] = True
                    result += 1
                    q.append((ny,nx))
    return result

cnt = 0
max_val = 0
for i in range(n):
    for j in range(m):
        if check[i][j] == False and w_map[i][j] ==1:
            check[i][j] = True
            cnt += 1
            max_val = max(max_val, bfs(i,j))
print(cnt)
print(max_val)