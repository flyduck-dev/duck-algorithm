def sol(m, nums):
    nums.sort(key = lambda x : x[0])
    start = end = ans = i = 0
    n = len(nums)
    while i < n:
        while i < n and nums[i][0] <= start:
            end = max(end, nums[i][1])
            i += 1
        ans += 1
        start = end
        if end >= m:
            return ans

print(sol(12,[[5,10],[1,8],[0,2],[0,3],[2,5],[2,6],[10,12],[7,12]])) # 3

print(sol(15,[[1,10],[0,8],[0,7],[0,10],[12,5],[0,12],[8,15],[5,14]])) # 2