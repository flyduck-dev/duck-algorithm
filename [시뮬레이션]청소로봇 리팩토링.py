def sol(s):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U','R','D','L']
    for z in s:
        for k in range(4):
            if z == dir[k]:
                x = x + dx[k]
                y = y + dy[k]

    return [x,y]
    

print(sol("RRRDDDLU"))
print(sol("DDDRRRDDLL"))