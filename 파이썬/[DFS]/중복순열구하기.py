import sys
sys.setrecursionlimit(10**6)
a, b, = map(int, input().split())
idx = []
ans = 0
def dfs(n):
    global idx, b, ans
    idx.append(n)
    if len(idx) == b:
        print(*idx)
        ans += 1
        idx.pop()
        return
    else:
        for i in range(1, a+1):
            dfs(i)

def sol():
    global a, b, idx 
    for i in range(1, a+1):
        idx = []
        dfs(i)

sol()
print(ans)