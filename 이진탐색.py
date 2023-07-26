def sol(nums, target):
    start = 0
    end = len(nums)-1
    while(start <= end):
        mid = start + end // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
print(sol([2,5,7,8,10,15,20,24,25,30], 8))
print(sol([-3,0,2,5,8,9,12,15], 0))