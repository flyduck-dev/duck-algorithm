def sol(nums, k):
    ans = 0
    n = len(nums)
    for i in range(k+1):
        sumN = 0
        for j in range(i):
            sumN += nums[j]
        for j in range(n-k+i,n):
            sumN += nums[j]
        ans = max(ans, sumN)
    return ans
        
print(sol([2,3,7,1,2,1,5],4)) # 17

print(sol([1,2,3,5,6,7,1,3,9],5)) # 26

print(sol([1,30,3,5,6,7],3)) # 38