# Counting Sort
import sys
n = int(sys.stdin.readline())
# [0] 을 n+1 까지!
# 그자리에 +1 채워
lst = [0]*10001
for _ in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1

# 그럼 1부터 n+1 까지 합쳐진걸 풀어서 세. 1,1,2,2,3,3, 이렇게 되겠쥐?
for i in range(1, 10001):
    count = lst[i]
    for _ in range(count):
        print(i)