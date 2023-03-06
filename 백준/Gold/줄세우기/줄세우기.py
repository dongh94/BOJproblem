import sys; sys.stdin = open('줄세우기.txt')
N = int(input())
list_a = [int(input()) for _ in range(N)]
# 오름차순으로 이전 값이 나보다 작은 거 카운팅(나포함) / 카운팅 수가 나보다 하나라도 크면 해당 X(간선확인)
dp = [0]*N
max_v = 0
# 3 7 5 2 6 1 4
# 1 2 2 1 3 1 2
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if list_a[j] < list_a[i] and dp[i] < dp[j] + 1:
            dp[i] += 1
    if max_v < dp[i]:
        max_v = dp[i]
# 나머지 다 바꿔
print(N - max_v)
