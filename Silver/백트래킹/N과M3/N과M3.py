import sys
sys.stdin=open("N과M3.txt")
sys.setrecursionlimit(5000)
n, m = map(int, sys.stdin.readline().split())

result = [0]*m
# check = [False] * (n+1)

def dfs(dept):
    if dept == m:
        print(*result)
        return

    for i in range(1, n+1):
        # if not check[i]:
            # check[i] = True
            result[dept] = i
            dfs(dept + 1)
            # check[i] = False

dfs(0)