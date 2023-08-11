arr = [7,3,2,9] # 합계 : 21
def recur_sum(arr, result):
    if len(arr) < 1:return result
    return recur_sum(arr, result + arr.pop())

print(recur_sum(arr,0))