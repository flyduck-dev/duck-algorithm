def sol(nums, limit):
    ans = 0
    nums.sort(key = lambda x : -x[1])
    for arr in nums:
        cnt = min(limit, arr[0])
        ans += cnt * arr[1]
        limit -= cnt
        if limit == 0:
            break
    return ans
print(sol([[2,20],[2,10],[3,15],[2,30]],5))
print(sol([[2,70],[5,100],[3,90],[1,95]],8))