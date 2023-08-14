ans = 0
def dfs(n):
    global ans
    ans += 1
    ch[n] = 1
    if n > a:
        return
    else:
        for i in graph[n]:
            if ch[i] != 1:
                dfs(i)

a = int(input())
b = int(input())
ch = [0] * (a+1)
graph = [[] for _ in range(a+1)]
for i in range(b):
    c, d = map(int, input.split())
    graph[c] = d
    graph[d] = c

dfs(1)
print(ans)

