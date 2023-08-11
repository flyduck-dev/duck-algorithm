def sol(nums):
    ans = 0
    cnt = 0
    for i in range(len(nums)):
        if nums[i] != 1:
            if ans < cnt:
                ans = cnt
            cnt = 0
        elif nums[i] == 1:
            cnt += 1
    if ans < cnt:
        ans = cnt
    return ans 
    

print(sol([-1,1,1,1,0,1,1,1,1,1,0])) #5
print(sol([0,1,0,1,0,1])) # 1
print(sol([1,1,1,1,1])) # 5
print(sol([-1,0,1,1,0,1,1,1,0,1,1,1])) # 3