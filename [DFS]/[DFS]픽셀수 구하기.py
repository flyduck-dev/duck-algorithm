dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def DFS(board, x, y):
    global cnt
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx >=0 and ny >=0 and nx < 5 and ny < 5 and board[nx][ny] == 1:
            board[nx][ny] = 0
            DFS(board, nx, ny)
    
def sol(board):
    global cnt
    ans = []
    for i in range(5):
        for j in range(5):
            cnt = 0
            if board[i][j] == 1:
                board[i][j] = 0
                DFS(board, i, j)
                ans.append(cnt)
    return ans

print(sol([[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,1,1,0]])) # [5,3]
print(sol([[1,1,1,0,1],[1,1,1,0,1],[0,0,1,0,0],[1,1,0,1,0],[1,0,1,0,0]])) # [7,2,3,1,1]
print(sol([[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[1,0,0,1,0],[0,0,1,1,0]])) # [4,1,3]