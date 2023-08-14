a, b = map(int, input().split())
arr_c = list(map(int, input().split()))
print_arr = [0] * b
ch = [0] * (b+1)
ans = 0
def dfs(L):
    global a, b, arr_c, ans, print_arr
    if L == b:
        print(*print_arr)
        ans += 1
    else:
        for i in range(a):
            if ch[i] == 0:
                ch[i] = 1
                print_arr[L] = arr_c[i]
                dfs(L+1)
                ch[i] = 0

def sol():
    dfs(0)

sol()