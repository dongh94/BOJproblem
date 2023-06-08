import sys
sys.stdin=open("N과M2.txt")
sys.setrecursionlimit(5000)
n, m = map(int, sys.stdin.readline().split())

result = [0] * m
used = [False] * (n + 1)

def dfs(dept, cut):
    if dept == m:
        print(*result)
        return

#     for i in range(1, n + 1):
#         if not used[i] and cut < i:
#             used[i] = True
#             result[dept] = i
#             dfs(dept + 1, i)
#             used[i] = False
#
# dfs(0, 0)

    for i in range(cut, n+1):
        if not used[i]:
            used[i] = True
            result[dept] = i
            dfs(dept + 1, i + 1)
            used[i] = False

dfs(0, 1)