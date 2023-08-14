import sys
sys.setrecursionlimit(10**6)
a, b, = map(int, input().split())
idx = []
ans = 0
def dfs(L):
    global idx, b, ans
    if L == b:
        for i in range(b):
            print(idx[i],end =' ')
        print()
        ans += 1
    else:
        for i in range(1, a+1):
            idx[L] = i
            dfs(L+1)

def sol():
    global a, b, idx 
    idx = [0] * b
    dfs(0)

sol()
print(ans)