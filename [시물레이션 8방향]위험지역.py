def sol(board):
    x = y = 0
    ans = 0
    h = len(board)
    w = len(board[0])
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and ny >= 0 and nx < h and ny < w:
                        if board[nx][ny] == 0:
                            board[nx][ny] = 2
                            ans += 1
    return ans
print(sol([[0,0,0,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]])) # 14
print(sol([[1,0,0,1,0],[0,1,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,1,0,0,0]])) # 17