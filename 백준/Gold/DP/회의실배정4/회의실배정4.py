import sys; sys.stdin = open("회의실배정4.txt")

class Meet:
    def __init__(self, s, e, p):
        self.s = s
        self.e = e
        self.p = p

n = int(input())
meets = [None] * n
for i in range(n):
    s, e, p = map(int, input().split())
    meets[i] = Meet(s, e, p)

meets.sort(key=lambda m: (m.e, m.s))

dp = [0] * n
dp[0] = meets[0].p

for i in range(1, n):
    t = 0
    for j in range(i):
        if meets[j].e <= meets[i].s:
            t = j + 1
    print(dp)
    dp[i] = max(dp[i-1], (dp[t-1] if t > 0 else 0) + meets[i].p)

print(dp[n-1])