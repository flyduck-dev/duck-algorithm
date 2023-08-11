n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
minN = arr[-1]
ans = 1
for i in range(len(arr)-2,-1, -1):
    if arr[i] > minN:
        minN = arr[i]
        ans += 1
print(ans)