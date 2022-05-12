from collections import deque


def bfs(N, M):
    q = deque([N])
    visited = [-1] * 1000001
    visited[N] = 0
    while q:
        n = q.popleft()
        if n == M:
            return visited[n]
        if 0 <= n - 1 < 100001 and visited[n - 1] == -1:
            visited[n - 1] = visited[n] + 1
            q.append(n - 1)
        if 0 < n * 2 < 100001 and visited[n * 2] == -1:
            visited[n * 2] = visited[n]
            q.appendleft(n * 2)
        if 0 <= n+1 < 100001 and visited[n + 1] == -1:
            visited[n+1] = visited[n] + 1
            q.append(n+1)

N, M = map(int, input().split())
ans = bfs(N, M)
print(ans)