import sys
sys.stdin=open("스타트와링크.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [False] * 21
ans = 1e9
# i번과 j번 + j번과 i번 => 다른 i, j 와의 비교

def dfs(dept, cnt):
    global ans

    if dept == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    start += arr[i][j]
                elif not check[i] and not check[j]:
                    link += arr[i][j]
        result = abs(start - link)
        ans = min(ans, result)
        return

    for i in range(cnt, n):
        check[i] = True
        dfs(dept + 1, i + 1)
        check[i] = False

dfs(0, 0)
print(ans)