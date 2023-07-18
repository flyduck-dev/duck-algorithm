from collections import defaultdict

def sol(n,m,arr):
    ans = []
    dix = defaultdict(int)
    for i in range(0, n):
        dix[arr[i]] = 1
    for i in range(n, n+m):
        if dix[arr[i]] == 1:
            ans.append(arr[i])
    print(len(ans))
    ans.sort()
    for i in ans:
        print(i)
    
n,m = map(int, input().split())
arr = []
for i in range(n+m):
    arr.append(input())
sol(n,m,arr)