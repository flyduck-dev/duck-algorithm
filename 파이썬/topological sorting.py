# 위상 정렬
# 백준 2252 줄 세우기

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
connection = [[] for i in range(N+1)] #1~N까지 범위
income_edge = [0 for i in range(N+1)]
for i in range(M):
    A,B = map(int,input().split())
    connection[A].append(B)
    income_edge[B] += 1
answer = []
q = []
for node in range(1, N+1):
    if income_edge[node] == 0:
        q.append(node)
        #for nextNode in connection[node]:
        #    income_edge[nextNode] -= 1
while q:
    node = q.pop(0)
    answer.append(node)
    for next_node in connection[node]:
        income_edge[next_node]-=1
        if income_edge[next_node] == 0:
            q.append(next_node)

for i in answer:
    print(i, end=' ')