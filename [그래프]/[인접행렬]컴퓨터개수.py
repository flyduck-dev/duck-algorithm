import sys
sys.setrecursionlimit(10**6)
cnt = 0
def DFS(v, ch, g, num):
    global cnt
    cnt += 1
    ch[v] = 1
    for i in range(1, num+1):
        if g[v][i] == 1 and ch[i] == 0:
            DFS(i, ch, g, num)

def sol(num, board):
    global cnt
    cnt = 0
    ch = [0] * (num+1)
    g = [[0] * (num+1) for _ in range(num+1)]
    for [x,y] in board:
        g[x][y] = 1
        g[y][x] = 1
    DFS(1, ch, g, num)
    return num - cnt

print(sol(11, [[1,2],[1,4],[2,3],[4,5],[5,6],[7,8],[7,10],[8,9],[10,11]])) # 5
print(sol(12, [[1,2],[1,7],[1,8],[1,6],[8,11],[11,12]])) # 5 
print(sol(14, [[1,6],[1,5],[6,7],[7,8],[9,8],[3,4],[4,14]])) # 8
print(sol(15, [[1,4],[1,5],[9,5],[9,6],[7,9],[7,14]])) # 8