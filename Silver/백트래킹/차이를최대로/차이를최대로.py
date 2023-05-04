import sys
sys.stdin=open("차이를최대로.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
used = [False] * 8
result = []
answer = 0
def dfs(k):
    global result, answer

    if k == n:
        temp = 0
        for i in range(n-1):
            temp += abs(result[i] - result[i+1])
        answer = max(answer, temp)
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            result.append(number[i])
            dfs(k + 1)
            result.pop()
            used[i] = False

dfs(0)
print(answer)