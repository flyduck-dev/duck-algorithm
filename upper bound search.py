# 찾고자 하는 값보다 큰 것 중에서 가장 작은 값을 찾아주는 이분검색방법
def sol(nums, target):
    start = 0
    end = len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return -1 if end == len(nums) else end 
    
print(sol([100,120,150,160,165,170,175,180,190,200],175))