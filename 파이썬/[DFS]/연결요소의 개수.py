import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
ans = 0
def dfs(n):
    ch[n] = 1
    for j in g[n]:
        if ch[j] == 0:
            dfs(j)

n,m = map(int, input().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a, b= map(int, input().split())
    g[a].append(b)
    g[b].append(a)
ch = [0] * (n+1)
for k in range(1, len(ch)):
    if ch[k] == 0:
        ans += 1
        dfs(k)
print(ans)