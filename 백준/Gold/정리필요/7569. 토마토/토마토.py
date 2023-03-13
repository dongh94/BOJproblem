import sys
from collections import deque
# sys.stdin = open('boj_7569_토마토2.txt')
input = sys.stdin.readline

M, N, Z = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)]for _ in range(Z)]
visited = [[[0]*M for _ in range(N)]for _ in range(Z)]

# 우 하 좌 상 앞 뒤
di = [0, 1, 0, -1, 0, 0]
dj = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
def BFS(Q):
    for z, i, j  in Q:
        visited[z][i][j] = 1
    while Q:
        z, i, j = Q.popleft()
        for k in range(6):
            nz, ni, nj = z + dz[k] ,i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and 0<= nz < Z and not visited[nz][ni][nj]:
                if arr[nz][ni][nj] == -1:
                    continue
                Q.append((nz, ni, nj))
                visited[nz][ni][nj] = visited[z][i][j] + 1

def find(N, M, visited):
    max_cnt = 0
    for z in range(Z):
        for i in range(N):
            for j in range(M):
                if visited[z][i][j] == 0 and arr[z][i][j] != -1:
                    return -1
                if max_cnt < visited[z][i][j]:
                    max_cnt = visited[z][i][j]
    return max_cnt -1

Q = deque()
for z in range(Z):
    for i in range(N):
        for j in range(M):
            if arr[z][i][j] == 1:
                Q.append((z, i, j))

BFS(Q)
print(find(N, M, visited))
