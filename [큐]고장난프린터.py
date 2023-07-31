from collections import deque
def sol(nums):
    q = deque(nums)
    while len(q)>1:
        for i in range(2):
            if len(q)>1:
                q.popleft()
            elif len(q)==1:
                return q[0]
        q.append(q.popleft())
    return q[0]

print(sol([3,1,4,5,2,6,7])) # 6
print(sol([10,8,3,1,4,5,2,6,7,9])) # 5
print(sol([10,8,3,11,12,1,4,5,2,6,7,9])) # 2
print(sol([10,8,3,1,4,5,2,11,13,6,7,12,9,14])) # 12