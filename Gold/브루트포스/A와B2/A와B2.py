import sys
sys.stdin = open("A와B2.txt")
sys.setrecursionlimit(100)
S = list(input())
T = list(input())
s_length = len(S)
t_length = len(T)
ans = 0

def dfs(k):
    global S, ans
    if k == t_length:
        print(S, T)
        if S == T:
            ans = 1
        return

    if ans == 1:
        return

    for i in range(2):
        if i == 1:
            S.append('B')
            S.reverse()
            dfs(k + 1)
            S.reverse()
            S.pop()
        S.append('A')
        dfs(k + 1)
        S.pop()

dfs(s_length)
print(ans)
