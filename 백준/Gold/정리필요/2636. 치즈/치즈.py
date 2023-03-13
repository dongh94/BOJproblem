def BFS(sr, sc):
    q = [(sr, sc)]
    cnt = 0
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if nr<0 or nr>=N or nc<0 or nc>=M: continue;

            if not visit[nr][nc] and not arr[nr][nc]:
                q.append((nr,nc))
                visit[nr][nc] = 1

            elif not visit[nr][nc] and arr[nr][nc]:
                visit[nr][nc] = 1
                arr[nr][nc] = 0
                cnt += 1
    return cnt


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

#우하좌상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
t = -1
ans = count = 1

while count > 0:
    t += 1
    visit = [[0] * M for _ in range(N)]
    ans = count
    count = BFS(0,0)
print(t)
print(ans)