def dfs(num, dp):
    if dp[num]:
        return dp[num]
    if num == 1 or num ==2:
        return num
    else:
        dp[num] = dfs(num-1,dp) + dfs(num-2,dp)
        return dp[num]

def sol(n):
    dp = [0] * (n+1)
    ans = dfs(n, dp)
    return ans

print(sol(7))