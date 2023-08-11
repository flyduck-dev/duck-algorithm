def sol(text):
    ans = []
    for i in text:
        if i != '#':
            ans.append(i)
        else:
            if len(ans) != 0:
                ans.pop()
    return "".join(ans)

print(sol("abc##ec#ab"))
print(sol("kefd#ef##s##"))
print(sol("teac#cher##er"))
