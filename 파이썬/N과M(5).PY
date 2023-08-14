a, b = map(int, input().split())
number_arr = list(map(int, input().split()))
number_arr.sort()
print_arr = [0] * b
ch = [0] * a 

def dfs(L):
    global a, b, number_arr, print_arr, ch
    if L == b:
        print(*print_arr)
    else:
        for idx, value in enumerate(number_arr):
            if ch[idx] == 0:
                ch[idx] = 1
                print_arr[L] = value
                dfs(L+1)
                ch[idx] = 0

def sol():
    dfs(0)

sol()
# 필요함 : LEVEL, PRINTARR, CNT, CH