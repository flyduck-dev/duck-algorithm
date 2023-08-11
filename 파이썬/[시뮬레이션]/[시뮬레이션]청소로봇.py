def sol(s):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for z in s:
        if z == 'U':
            x = x + dx[0]
            y = y + dy[0]

        if z == 'R':
            x = x + dx[1]
            y = y + dy[1]
            
        if z == 'D':
            x = x + dx[2]
            y = y + dy[2]
        
        if z == 'L':
            x = x + dx[3]
            y = y + dy[3]
    return [x,y]
    

print(sol("RRRDDDLU"))
print(sol("DDDRRRDDLL"))