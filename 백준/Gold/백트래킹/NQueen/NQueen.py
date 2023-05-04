import sys
sys.stdin = open("NQueen.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
RrefC = [0]*15
answer = 0

def dfs(dept):
    global answer

    if dept == n:
        answer += 1
        return

    for i in range(n): # 열
        RrefC[dept] = i # 행, 열

        No = False
        for j in range(dept): # 그 전까지 행, 열 비교
            if RrefC[dept] == RrefC[j] or abs(dept - j) == abs(RrefC[dept] - RrefC[j]):
                No = True
                break

        if not No: dfs(dept + 1);

dfs(0)
print(answer)