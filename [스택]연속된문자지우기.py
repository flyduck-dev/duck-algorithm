def sol(text):
    stack = []
    for i in text:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

print(sol("acbbcaa"))
print(sol("bacccaba"))
print(sol("aabaababbaa"))