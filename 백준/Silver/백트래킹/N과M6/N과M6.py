import sys
sys.stdin=open("N과M6.txt")
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = [0] * M
check = [False] * (N+1)
arr.sort()

def dfs(dept, cnt):
    if dept == M:
        print(*result)
        return

    for i in range(N):
        if not check[i] and cnt < arr[i]:
            check[i] = True
            result[dept] = arr[i]
            dfs(dept + 1, arr[i])
            check[i] = False

dfs(0, 0)