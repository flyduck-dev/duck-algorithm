# 풀이방법 1
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    mid_index = len(s) // 2
    for k in range(mid_index-1):
        if s[k] != s[-1-k]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))

# 파이썬 문법을 활용한 풀이방법2

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print('#%d YES' %(i+1))
    else:        
        print('#%d NO' %(i+1))
        
