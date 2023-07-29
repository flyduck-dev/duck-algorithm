def sol(num):
    if num == 1:
        return num
    else:
        ans = num * sol(num-1)
    return ans 
print(sol(5)) #120
print(sol(6)) #720
print(sol(7)) #5040
print(sol(8)) #40320