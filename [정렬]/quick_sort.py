import sys
arr = list(map(int, sys.stdin.readline().split()))

def quick_sort(arr, start, end):
    if start >= end: # start가 end보다 크거나 같다는 것은 원소가 1개라는 뜻
        return arr
    
    pivot = start
    i = start + 1 # 피봇 다음의 인덱스부터 검사하기 위함
    j = end

    while i<=j: #엇갈릴 떄까지 반복
        while arr[i] <= arr[pivot] and i < end: # 키 값보다 큰 값을 만날 때까지 이동
            i += 1
        while arr[j] >= arr[pivot] and j > start:
            j -= 1
        if i > j: # 현재 엇갈린 상태라면 교체
            arr[pivot], arr[j] = arr[j], arr[pivot]
        else:
            arr[i], arr[j] = arr[j], arr[i]
    
    #데이터가 엇갈려서 빠져나왔다면
    quick_sort(arr, start, j-1)
    quick_sort(arr, j+1, end)

quick_sort(arr, 0, len(arr)-1)
print(*arr)
