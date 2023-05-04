import sys
sys.stdin=open("N과M7.txt")
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = [0]*m
arr.sort()
def dfs(dept):
    if dept == m:
        print(*result)
        return

    for i in range(n):
        result[dept] = arr[i]
        dfs(dept + 1)

dfs(0)