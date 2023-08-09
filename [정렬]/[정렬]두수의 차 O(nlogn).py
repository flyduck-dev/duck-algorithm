def sol(nums):
    ans = []
    minN = 10000000
    nums.sort()
    for i in range(1, len(nums)):
        minN = min(minN, nums[i]-nums[i-1])

    for i in range(1, len(nums)):
        if nums[i]-nums[i-1] == minN:
            ans.append([nums[i-1],nums[i]])
    return ans      

print(sol([3,8,1,5,12]))
print(sol([2,1,3,5,4]))
print(sol([5,10,15,20,25,11]))
print(sol([2,4,3,1,5,7,8,12,13,15,23]))
print(sol([100,200,300,400,120,130,135,121]))
