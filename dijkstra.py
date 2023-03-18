# 꼭짓점 간의 최단 경로를 찾는 알고리즘
# 백준 1916
import sys
import heapq

city = int(sys.stdin.readline().strip())
bus = int(sys.stdin.readline().strip())
graph = [[] for i in range(city+1)]

for i in range(bus):
    start_city, end_city, cost = map(int, sys.stdin.readline().split())
    graph[start_city].append((cost, end_city))

start, target = map(int, sys.stdin.readline().split())

distance = [float('inf') for _ in range(city+1)]
distance[start] = 0

heap = []
heapq.heappush(heap,(0, start))
while heap:
    cost, node = heapq.heappop(heap)
    if distance[node] < cost:
        continue
    for i in graph[node]:
        next_cost, next_node =i[0], i[1]
        if distance[next_node] > cost + next_cost:
            distance[next_node] = cost + next_cost
            heapq.heappush(heap, (distance[next_node],next_node))

print(distance[target])