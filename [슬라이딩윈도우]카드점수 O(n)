def sol(nums, num):
    left = right = ans = window = 0
    for i in range(len(nums)-num):
        window += nums[i]
    ans = window
    for right in range(len(nums)-num, len(nums)):
        window += nums[right] - nums[left]
        left += 1
        ans = min(ans, window)
    return sum(nums)-ans

print(sol([2,3,7,1,2,1,5],4)) # 17

print(sol([1,2,3,5,6,7,1,3,9],5)) # 26

print(sol([1,30,3,5,6,7],3)) # 38