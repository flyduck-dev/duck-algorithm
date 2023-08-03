from collections import deque
def BFS(n):
    q = deque()
    q.append(n)
    level = 1
    while q:
        length = len(q)
        print(level, end = " : ")
        for i in range(length):
            ele = q.popleft()
            print(ele, end = " ")
            for j in [ele*2, ele*2+1]:
                if j > 7:
                    continue
                q.append(j)
        print()
        level += 1

BFS(1)

# 1 : 1 
# 2 : 2 3 
# 3 : 4 5 6 7 