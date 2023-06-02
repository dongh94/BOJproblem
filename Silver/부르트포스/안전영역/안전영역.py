import sys
sys.stdin = open("안전영역.txt")
from collections import deque
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# 1 ~ 9 까지 0, 1 로 나눈다음에
# 그때마다 bfs 돌려서 수를 세고 max값과 비교하면서 몇을 지웠는지 알아야 한다.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_i = max(max(arr))

def bfs(r, c, i):
    global cnt
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        sr, sc = Q.popleft()

        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] <= i or visited[nr][nc] == 1: continue;
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                Q.append((nr,nc))


for i in range(max_i):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > i and visited[r][c] == 0:
                bfs(r, c, i)
                cnt += 1
    answer = max(answer, cnt)
print(answer)

