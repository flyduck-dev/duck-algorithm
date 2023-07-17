# 재배치 후 팰린드롬을 만들 수 있는지 확인
from collections import Counter
def sol(s):
    sH = Counter(s)
    # 빈도수가 홀수인 키가 몇개인지 센다
    odd = 0
    for key in sH:
        if sH[key] % 2 !=0:
            odd += 1
    return odd <= 1

print(sol("abacbaa"))
print(sol("abaccbaa"))
print(sol("abacccbaa"))

