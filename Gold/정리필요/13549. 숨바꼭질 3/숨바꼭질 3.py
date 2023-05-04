from collections import deque

def bfs(N, K):
    Q = deque([N])
    visit = [-1] * 100001
    visit[N] = 0
    while Q:
        n = Q.popleft()

        if n == K:
            return visit[n]

        for m in (2*n, n-1, n+1):
            if 0<= m <100001 and visit[m] == -1:
                if m == 2*n:
                    visit[m] = visit[n] + 0
                    Q.append(m)
                else:
                    visit[m] = visit[n] + 1
                    Q.append(m)


N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)