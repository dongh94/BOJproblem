import sys
sys.stdin = open("퇴사.txt")
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
# 연속된 N일의 기간 중에서 연속되어 선택할 때 더 큰값으로 갱신
# 작은 공식이 큰 공식으로 = > 갱신되어 가는 과정이 필요한 것.
for i in range(N):
    for j in range(i + schedule[i][0], N + 1):
        dp[j] = max(dp[j], dp[i] + schedule[i][1])
print(dp[-1])

