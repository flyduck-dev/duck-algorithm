from collections import defaultdict

def sol(nums):
    ans = -1
    dic = defaultdict(int)
    for i in nums:
        dic[i] += 1
    for key in dic:
        if dic[key] == 1:
            ans = max(ans, key)

    return ans
print(sol([3,9,2,12,9,12,8,7,9,12]))
    
