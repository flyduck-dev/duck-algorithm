def dfs(n, g, ch, num):
    ch[n] = 1
    for z in g[n]:
        if ch[z] == 0:
            dfs(z, g, ch, num)

def sol(num, arr):
    ans = 0
    g = [[] for _ in range(num+1)]
    for [x,y] in arr:
        g[x].append(y)
        g[y].append(x)
    ch = [0] * (num+1)
    for i in range(1, num+1):
        if ch[i] == 0:
            ans += 1
            dfs(i, g, ch, num)

    return ans

print(sol(10,[[1,2],[2,3],[1,4],[1,5],[6,8],[7,8],[9,10]])) # 3
print(sol(20,[[1,2],[2,5],[5,7],[9,7],[5,13],[15,13],[3,4],[4,6],[6,8],[8,10],[11,12],[14,16],[16,17],[17,18],[19,20]])) # 5
print(sol(7,[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # 1
print(sol(30,[[5,6],[6,7]])) # 28