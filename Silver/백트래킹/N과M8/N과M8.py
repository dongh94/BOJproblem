import sys
sys.stdin=open("N과M8.txt")
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = [0] * m
def dfs(dept, prior):
    if dept == m:
        print(*result)
        return

    for i in range(n):
        if arr[i] >= prior:
            result[dept] = arr[i]
            dfs(dept+1, arr[i])

dfs(0, 0)
