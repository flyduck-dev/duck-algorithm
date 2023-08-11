def sol(text):
    stack = []
    for i in text:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0 :
                return "NO"
            else:
                stack.pop()
    if len(stack)==0:
        return "YES"
    else:
        return "NO"
    
print(sol("((()))()")) # YES
print(sol("(()((")) # NO