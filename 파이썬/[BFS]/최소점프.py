from collections import deque
def sol(num):
    board = [0] * 10001
    q = deque()
    q.append(0)
    board[0] == 1
    L = 0
    while q:
        n = len(q)
        for i in range(n):
            point = q.popleft()
            if point == num:
                return L
            else:
                for j in [point-1, point+1, point+5]:
                    if 0 <= j and 10001 > j and board[j] == 0:
                      board[j] == 1
                      q.append(j)
        L += 1
                    
print(sol(10))
print(sol(14))
print(sol(25))
print(sol(24))