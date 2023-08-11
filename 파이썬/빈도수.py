def sol(nums):
    ans = 0
    arr = [0] * 1001
    for x in nums:
        arr[x] += 1
    for i in range(1000, 0, -1):
        if arr[i] == 1:
            return i

    return ans

print(sol([3,9,2,12,9,12,8,7,9,12]))