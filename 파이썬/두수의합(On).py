from collections import defaultdict
def sol(nums, target):
    dix = defaultdict(int)
    ans = [0] * 2
    for i in nums:
        if target - i in dix:
            return sorted([target - i, i])
        dix[i] = 1   
    return ans

print(sol([7,3,2,12,13,9,15,8,11],12))
print(sol([21,12,30,15,6,2,9,19,14],24))
print(sol([12,18,5,8,21,27,22,25,16,2],28))
print(sol([11,17,6,8,21,9,19,12,25,16,2],26))
print(sol([7,5,12,-9,-12,22,-30,-35,-21],-14))
print(sol([7,5,12,20],15))