import sys
from collections import deque
# sys.stdin = open('boj_7576_토마토.txt', 'r')
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def BFS(start):
    Q = deque(start)
    for s1, s2 in Q:
        visited[s1][s2] = 1
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if arr[ni][nj] == -1:
                    continue
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

def find(N, M, visited):
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] != -1:
                return -1
            if max_cnt < visited[i][j]:
                max_cnt = visited[i][j]
    return max_cnt -1

start = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start.append((i, j))

BFS(start)
print(find(N, M, visited))
