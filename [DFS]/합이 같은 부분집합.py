import sys
def dfs(L, dfs_sum, arr):
    if sum(arr) // 2 < dfs_sum:
        return
    if L == len(arr):
        if dfs_sum == sum(arr) - dfs_sum:
            print("YES")
            sys.exit()
    else:
        dfs(L+1, dfs_sum+arr[L], arr)
        dfs(L+1, dfs_sum, arr)

def sol(arr):
    dfs(0,0, arr)
    print("NO")

print(sol([1,3,5,6,7,10]))