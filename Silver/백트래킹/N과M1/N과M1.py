import sys
sys.stdin = open("N과M1.txt")
sys.setrecursionlimit(5000)
n, m = map(int, sys.stdin.readline().split())
result = [0] * m
used = [False] * (n + 1)

def dfs(dept):
    if dept == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not used[i]:
            result[dept] = i
            used[i] = True
            dfs(dept + 1)
            used[i] = False

dfs(0)