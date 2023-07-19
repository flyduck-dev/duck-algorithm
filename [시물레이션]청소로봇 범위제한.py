def sol(n,s):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U','R','D','L']
    for z in s:
        for k in range(4):
            if z == dir[k]:
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and ny >=0 and nx < n and ny < n:
                    x = nx
                    y = ny 

    return [x,y]
    

print(sol(5,"RRRDDDUUUUUUL")) # 0 2
print(sol(7,"DDDRRRDDLL")) # 5 1
print(sol(5,"RRRRRDDDDDU")) # 3 4
print(sol(6,"RRRRDDDRRDDLLUU")) # 33