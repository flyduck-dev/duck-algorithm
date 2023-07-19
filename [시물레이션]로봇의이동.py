def sol(s):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = 1
    for z in s:
        if z == 'G':
            x = x + dx[d]
            y = y + dy[d]
        elif z == 'R':
            d = (d + 1) % 4
        elif z == 'L':
            d = (d - 1) % 4 
    return [x,y] 



print(sol('GGGRGGG')) # 3 3
print(sol('GGRGGG')) # 3 2
print(sol('GGGGGGGRGGGRGGRGGGLGGG')) # 0 2
print(sol('GGLLLGLGGG')) # 1 5
