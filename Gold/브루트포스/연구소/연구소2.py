import sys
sys.stdin = open("연구소.txt")
sys.setrecursionlimit(1000)

input = sys.stdin.readline


from collections import deque

def check(graph):
    global answer
    zero = 0
    for r in range(n):
        for c in range(m):
            if not graph[r][c]:
                zero += 1
    answer = max(answer, zero)

def bfs():
    Q = deque()

    for r in range(n):
        for c in range(m):
            if graph[r][c] == 2:
                Q.append((r,c))

    each_graph = [graph[i].copy() for i in range(n)]

    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= n or nc < 0 or nc >= m or each_graph[nr][nc] == 1: continue;
            if each_graph[nr][nc] == 0:
                each_graph[nr][nc] = 2
                Q.append((nr, nc))

    check(each_graph)
# 3개 골라서 bfs
def dfs(k):
    if k == 3:
        bfs()
        return

    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:
                graph[r][c] = 1
                dfs(k + 1)
                graph[r][c] = 0



n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dfs(0)
print(answer)
