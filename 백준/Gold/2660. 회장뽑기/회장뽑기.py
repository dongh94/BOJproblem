N = int(input())
graph = [[] for _ in range(N+1)]
visit = [[0] for _ in range(N+1)]
while True:
    a, b = map(int,input().split())
    if a == -1 and b == -1: break;
    graph[a].append(b)
    graph[b].append(a)

def BFS(c):
    q = [c]
    visit = [-1]*(N+1)
    visit[c] = 0
    while q:
        n = q.pop(0)
        for g in graph[n]:
            if visit[g]==-1:
                q.append(g)
                visit[g] = visit[n] + 1

    return max(visit)

ans = []
for i in range(1,N+1):
    ans.append(BFS(i))
min_v = min(ans)
print(min_v, ans.count(min_v))

result = []
for i in range(N):
    if min_v == ans[i]:
        result.append(i+1)
print(*result)