def sol(nums, target):
    ans = [0] * 2
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return sorted([nums[i],nums[j]])
    return ans
    

print(sol([7,9,2,13,3,15,8,11],12))