import sys
sys.stdin=open("연산자끼워넣기.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
max_v = -1000000000
min_v = 1000000000

def dfs(dept, calc, plus, minus, multi, divi):
    global max_v, min_v
    if dept == n:
        max_v = max(max_v, calc)
        min_v = min(min_v, calc)
        return

    if plus:
        dfs(dept + 1, calc + number[dept], plus - 1, minus, multi, divi)
    if minus:
        dfs(dept + 1, calc - number[dept], plus, minus - 1, multi, divi)
    if multi:
        dfs(dept + 1, calc * number[dept], plus, minus, multi - 1, divi)
    if divi:
        dfs(dept + 1, int(calc/ number[dept]), plus, minus, multi, divi - 1)


dfs(1, number[0], oper[0], oper[1], oper[2], oper[3])
print(max_v, min_v)