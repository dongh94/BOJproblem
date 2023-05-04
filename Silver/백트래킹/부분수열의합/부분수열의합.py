import sys;
sys.stdin=open("부분수열의합.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
used = [False] * 20
sum_v = 0
result = 0
def dfs(k, cut):
    global sum_v, result

    if sum_v == s and k > 0:
        print(sum_v)
        result += 1

    for i in range(cut, n):
        if not used[i]:
            used[i] = True
            sum_v += arr[i]
            dfs(k + 1, i + 1)
            sum_v -= arr[i]
            used[i] = False

dfs(0, 0)
print(result)
