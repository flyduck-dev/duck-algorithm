n = 0
def dfs(num, ch):
    if num == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end= " ")
        print()
    else:
        ch[num] = 1
        dfs(num+1, ch)
        ch[num] = 0
        dfs(num+1, ch)

def sol(num):
    global n
    n = num
    ch = [0] * (n+1)
    return dfs(1, ch)

print(sol(3))
# 출력
# 1 2 3 
# 1 2 
# 1 3 
# 1 
# 2 3 
# 2 
# 3