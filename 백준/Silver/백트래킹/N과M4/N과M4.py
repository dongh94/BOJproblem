import sys
sys.stdin=open("N과M4.txt")
sys.setrecursionlimit(5000)
n, m = map(int, sys.stdin.readline().split())

result = [0] * m

def dfs(dept, cut):
    if dept == m:
        print(*result)
        return

    for i in range(1, n+1):
        if cut <= i:
            result[dept] = i
            dfs(dept+1, i)

dfs(0, 0)