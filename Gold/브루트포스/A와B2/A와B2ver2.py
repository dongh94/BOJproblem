import sys

sys.stdin = open("A와B2.txt")
sys.setrecursionlimit(100)

a = input()
b = input()
def dfs(cur, target):
    if len(cur) == len(target):
        if cur == target:
            return 1
        return 0


    ret = 0
    # 빼고 돌리고
    if cur[0] == 'B':
        ret += dfs(cur[1:][::-1], target)
    # 빼고
    if cur[-1] == 'A':
        ret += dfs(cur[:-1], target)

    return 1 if ret > 0 else 0

print(dfs(b, a))
