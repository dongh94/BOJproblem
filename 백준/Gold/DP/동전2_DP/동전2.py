import sys; sys.stdin=open("동전2.txt")

N, K = map(int, input().split())
value_list_a = [int(input()) for _ in range(N)]
answer = 0
# 최솟값이니 dp값 최대치 수
INF = 10001
dp = [INF]*(K+1)
# 초기값 0으로 value 값들을 K까지 돌려주며 min값을 dp[v-value] + 1(Counting) 값으로 갱신 dp[0] = 0
dp[0] = 0
for value in value_list_a:
    for v in range(value, K+1):
        dp[v] = min(dp[v], dp[v-value]+1)
answer = dp[K]

if dp[K] == INF:
    answer = -1

print(answer)




