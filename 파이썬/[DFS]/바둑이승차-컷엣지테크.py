def dfs(L,sum,tsum):
    global total, a, total, result
    if sum + (total - tsum) < result:
        return
    if sum > a:
        return
    if L == b:
        if sum > result:
            result = sum
    else:
        dfs(L+1, sum + arr[L], tsum + arr[L])
        dfs(L+1, sum, tsum + arr[L])

a, b = map(int, input().split())
arr = []
result = -2147000000
for i in range(b):
    arr.append(int(input()))
total = sum(arr)
dfs(0,0,0)
print(result)

# def dfs():
#     print()
# def sol():
#     print()

# print(sol([1,2,3,4]))