from collections import deque
# 세로 N, 가로 M
N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
# 우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs(sr, sc, sz):
    queue = deque([(sr, sc, sz)])
    visited[sr][sc][sz] = 1
    while queue:
        r, c, z = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if r == N - 1 and c == M - 1:
            return visited[r][c][z]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue;
            # 벽, 부쉈을 때, 안가
            if arr[nr][nc] and visited[nr][nc][z]: continue;
            # 벽, 부수지 않았을 때,
            if arr[nr][nc] and not z and not visited[nr][nc][z] :
                visited[nr][nc][z+1] = visited[r][c][z] + 1
                queue.append((nr, nc, z+1))
            # 벽 아닐때, (부수든 안부스든 그 표시 그대로 가야함.)
            elif not arr[nr][nc] and not visited[nr][nc][z]:
                visited[nr][nc][z] = visited[r][c][z] + 1
                queue.append((nr, nc, z))

    return -1

print(bfs(0, 0, 0))