# 이진트리 순회
def pre(n):
    if n > 7:
        return
    else:
        print(n, end= " ")
        pre(n*2)
        pre(n*2+1)

def mid(n):
    if n > 7:
        return
    else:
        mid(n*2)
        print(n, end= " ")
        mid(n*2+1)
    

def post(n):
    if n > 7:
        return
    else:
        post(n*2)
        post(n*2+1)
        print(n, end= " ")

print(pre(1))
print(mid(1))
print(post(1))

# 전위순회 출력 : 1 2 4 5 3 6 7
# 중위순회 출력 : 4 2 5 1 6 3 7
# 후위순회 출력 : 4 5 2 6 7 3 1
