
def sol(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(sol([-3, -2, 0, 1, 3, 5, 8, 9, 12])) # 5

print(sol([-10, -5, -2, 3, 4, 6, 7, 8])) # 3