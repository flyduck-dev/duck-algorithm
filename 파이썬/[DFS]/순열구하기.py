a, b = map(int, input().split())
ch = [0] * (a+1)
print_arr = [0] * b
ans = 0
def dfs(L):
    global a, b, ch, ans
    if L == b:
        print(*print_arr)
        ans += 1
    else:
        for i in range(1,a+1):
            if ch[i] == 0:
                ch[i] = 1
                print_arr[L] = i
                dfs(L+1)
                ch[i] = 0

def sol():
    dfs(0)
    print(ans)

sol()