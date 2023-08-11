import heapq
def solution(no, works):
    result = 0
    temp = [i * -1 for i in works]
    heapq.heapify(temp)
    for j in range(no):
        tmp = heapq.heappop(temp)
        if tmp == 0: # 작업량이 0이면 더 이상 감소시킬 수 없으므로 종료
            break
        tmp = (tmp * -1) - 1
        heapq.heappush(temp, tmp* -1)
    
    result = sum([(i*-1)**2 for i in temp])
    return result