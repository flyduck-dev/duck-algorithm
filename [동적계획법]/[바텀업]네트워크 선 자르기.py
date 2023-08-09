def sol(num):
    dp = [0] * (num+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, num+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[num]
print(sol(7))