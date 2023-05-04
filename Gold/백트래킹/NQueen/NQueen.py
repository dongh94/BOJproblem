import sys
sys.stdin = open("NQueen.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
RrefC = [0]*15
answer = 0
def check(row):
    for j in range(row):  # 그 전까지 행, 열 비교
        if RrefC[row] == RrefC[j] or abs(row - j) == abs(RrefC[row] - RrefC[j]):
            return False
    return True

def dfs(k):
    global answer

    if k == n:
        answer += 1
        return

    for i in range(n): # 열
        RrefC[k] = i # 행, 열

        if check(k):
            dfs(k + 1)

dfs(0)
print(answer)