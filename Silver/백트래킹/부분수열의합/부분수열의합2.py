import sys;
sys.stdin=open("부분수열의합.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
used = [False] * 20
result = 0
def dfs(k, sum_v):
    global result

    if k == n:기
        if sum_v == s:
            result += 1
        return

    dfs(k + 1, sum_v)
    dfs(k + 1, sum_v + arr[k])

dfs(0, 0)
# 아무것도 안골랐을때.
if s == 0:
    result -= 1
print(result)