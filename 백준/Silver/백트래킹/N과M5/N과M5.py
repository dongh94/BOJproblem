import sys
sys.stdin = open("N과M5.txt")
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = [0]*M
check = [False]*(N+1)

def dfs(dept):
    if dept == M:
        print(*result)
        return

    for i in range(N):
        if not check[i]:
            check[i] = True
            result[dept] = arr[i]
            dfs(dept + 1)
            check[i] = False

dfs(0)
