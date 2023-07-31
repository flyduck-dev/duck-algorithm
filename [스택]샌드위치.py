def sol(ele):
    stack = []
    ans = 0
    for i in ele:
        if i == 1:
            if len(stack) >= 2 and stack[-1] == 2 and stack[-2] == 1:
                stack.pop()
                stack.pop()
                ans += 1
            else:
                stack.append(1)
        else:
            stack.append(i)
    return ans

print(sol([1,1,1,2,1,1,2,1,2,1])) # 3

print(sol([2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1])) # 6

print(sol([1,1,1,1,1,2,1,2,1,1,1])) # 2

print(sol([2,1,1,1,2,1,2])) # 1