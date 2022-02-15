import sys
n, m = map(int,(sys.stdin.readline().split()))
array = list(map(int,sys.stdin.readline().split()))
start = 0
end = max(array)
result = 0
while start <= end:
    total = 0 
    mid = (start + end) // 2
    for v in array:
        if v > mid:
            total += v - mid
    if total < m :
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)