import sys
from collections import defaultdict
N, M = map(int,input().split())
ans = []
names = defaultdict(int)
for i in range(N):
    s = input()
    names[s] = 1
for i in range(M):
    s = input()
    print('chack ',s)
    if s in names:
        ans.append(s)
    
ans.sort()
print()
for i in ans:
    print(ans[i])