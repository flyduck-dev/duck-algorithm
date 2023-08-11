def dfs(L,sum,a):
    global result
    if L == len(a):
        if sum > result:
            result = sum
    else:
        dfs(L+1, sum+a[L],a)
        dfs(L+1, sum,a)

def sol():
    c, n = map(int, input().split())
    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    dfs(0,0,a)
    print(result)