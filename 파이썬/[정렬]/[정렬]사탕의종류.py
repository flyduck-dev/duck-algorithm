def sol(nums):
    amount = len(nums) // 2
    nums.sort()
    cnt = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            cnt += 1
    return min(amount, cnt)

print(sol([2,1,1,3,2,3,1,2])) # 3
print(sol([1,3,5,7,2,3,7,5,3,2,5,7,9,12])) # 7
print(sol([5,5,5,5,5,5])) # 1 
print(sol([12,23,11,3,5,23,23,23,23,23,23,23])) # 5
print(sol([100,200,300,400,500,600,700,800])) # 4