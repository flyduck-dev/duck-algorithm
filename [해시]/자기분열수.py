from collections import defaultdict, Counter
# 자기 분열수란 배열의 원소 중 자기 자신의 숫자만큼 빈도수를 갖는 숫자를 의미한다.
def sol(nums):
    ans = 10000000
    dix = defaultdict(int)
    dix = Counter(nums)
    for key in dix:
        if dix[key] == key:
            ans = min(ans, key)
    return -1 if ans == 10000000 else ans

print(sol([1,2,3,1,3,3,2,4]))