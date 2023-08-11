def sol(arrs):
    hole = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    h = len(arrs)
    w = len(arrs[0])

    for i in range(h):
        for j in range(w):
            
            flag = True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and ny >=0 and nx < h and ny < w:
                    if arrs[i][j] >= arrs[nx][ny]:
                        flag = False
                        break
            if flag == True:
                hole += 1

    return hole

print(sol([[10,20,50,30,20],[20,30,50,70,90],[10,15,25,80,35],[25,35,40,55,80],[30,20,35,40,90]])) #5
print(sol([[80,25,10,65,100],[20,10,32,70,33],[45,10,88,9,90],[10,35,10,55,66],[10,84,65,88,99]])) #4
print(sol([[33,22,55,65,55],[55,88,99,12,19],[18,33,25,57,77],[46,78,54,55,99],[33,25,47,85,17]])) #6