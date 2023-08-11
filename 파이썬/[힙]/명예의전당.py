import heapq
def solution(k, score):
    score_arr = []
    today_score = []
    heapq.heapify(score_arr)
    for i in range(len(score)):
        heapq.heappush(score_arr, score[i])
        if len(score_arr) > k:
            heapq.heappop(score_arr)
        today_score.append(score_arr[0])
    return today_score