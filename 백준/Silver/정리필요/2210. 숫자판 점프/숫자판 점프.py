#우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(n, r, c, num):
    num += arr[r][c]
    if n == 6:
        set_num.add(num)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(n+1,nr,nc,num)

N = 5
arr = [list(input().split()) for _ in range(N)]
set_num = set()

for r in range(5):
    for c in range(5):
        dfs(1, r, c, '')

print(len(set_num))