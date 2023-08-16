def dfs(L):
    global a, b, print_arr
    if L == b:
        print(*print_arr)
        return
    else:
        for i in range(1, a+1):
            print_arr.append(i)
            dfs(L+1)
            print_arr.pop()
a, b = map(int,input().split())
print_arr = []
dfs(0)
