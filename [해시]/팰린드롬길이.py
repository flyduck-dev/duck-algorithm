#문자열이 주어지면 해당 문자열의 문자들을 가지고 만들 수 있는 팰린드롬의 최대길이
from collections import Counter
def sol(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 != 0:
            odd += 1
    
    #홀수 갯수만큼 빼주고, +1
    #홀수가 없을 경우에는 그냥 return
    if odd == 0 or odd == 1:
        return len(s)
    else:
        return len(s) - odd + 1

print(sol("abcbbbccaaeee"))
print(sol("aabbccddee"))
