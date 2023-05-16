import sys
sys.stdin = open("연구소.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(wallCnt):
    global maxSafeZone
    # 벽이 3개가 설치된 경우 bfs 탐색 시작
    if wallCnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if originalMap[i][j] == 0:
                originalMap[i][j] = 1
                dfs(wallCnt + 1)
                originalMap[i][j] = 0


def bfs():
    global maxSafeZone
    q = deque()

    for i in range(n):
        for j in range(m):
            if originalMap[i][j] == 2:
                q.append((i, j))

    # 원본 연구소를 바꾸지 않기 위한 카피맵 사용
    copyMap = [originalMap[i].copy() for i in range(n)]

    # BFS 탐색 시작
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 연구소 범위 밖이 아니고 빈칸일 경우에만 바이러스를 퍼트린다.
            if 0 <= nx < n and 0 <= ny < m:
                if copyMap[nx][ny] == 0:
                    q.append((nx, ny))
                    copyMap[nx][ny] = 2

    # SafeZone 확인
    safeZone = sum([copyMap[i].count(0) for i in range(n)])
    maxSafeZone = max(maxSafeZone, safeZone)


n, m = map(int, input().split())
originalMap = []

for _ in range(n):
    originalMap.append(list(map(int, input().split())))

maxSafeZone = float('-inf')  # 최대값을 찾기 위한 초기값 설정

dfs(0)

print(maxSafeZone)
