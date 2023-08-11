import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    c = find(a)
    d = find(b)
    if c != d:
        parent[d] = c

def check_same(a,b):
    c = find(a)
    d = find(b)
    if c == d:
        return True
    return False

# 출력부 
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b,c)
    else:
        if check_same(b,c) == True:
            print('YES')
        else:
            print('NO')