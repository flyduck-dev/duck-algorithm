dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(board, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx <5 and ny < 5 and board[nx][ny]==1:
            board[nx][ny] = 0
            DFS(board, nx, ny)
def sol(board):
    ans = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                ans += 1
                board[i][j] = 0
                DFS(board, i, j)
    return ans

print(sol([[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,1,1,0]])) # 2
print(sol([[1,1,1,0,1],[1,1,1,0,1],[0,0,1,0,0],[1,1,0,1,0],[1,0,1,0,0]])) # 5
print(sol([[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[1,0,0,1,0],[0,0,1,1,0]])) # 3
print(sol([[0,0,0,0,1],[0,0,1,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,0,1,0,0]])) # 5