import sys
sys.stdin=open("스도쿠.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
n = 9
loc = []
for r in range(n):
    for c in range(n):
        if not arr[r][c]:
            loc.append((r, c))

def check(r, c):
    checked = [False] * 10
    for i in range(9):
        checked[arr[r][i]] = True

    for j in range(9):
        checked[arr[j][c]] = True

    sr = (r // 3) * 3
    sc = (c // 3) * 3
    for nr in range(sr, sr + 3):
        for nc in range(sc, sc + 3):
            checked[arr[nr][nc]] = True

    return checked

def dfs(k):
    global flag

    if flag:
        return

    if k == len(loc):
        for r in range(n):
            print(*arr[r])
            flag = True
        return

    r, c = loc[k]
    checked = check(r, c)

    for i in range(1, 10):
        if not checked[i]:
            arr[r][c] = i
            dfs(k + 1)
            arr[r][c] = 0

flag = False
dfs(0)

