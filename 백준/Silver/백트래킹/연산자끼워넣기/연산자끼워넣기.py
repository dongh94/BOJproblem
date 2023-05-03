import sys
sys.stdin=open("연산자끼워넣기.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
max_v = -1000000000
min_v = 1000000000

def calc(i, num1, num2):
    if i == 0:
        return num1 + num2
    elif i == 1:
        return num1 - num2
    elif i == 2:
        return num1 * num2
    else:
        return int(num1 / num2)

        # if num1 >= 0:
        #     return num1 // num2
        # else:
        #     return (-num1 // num2) * -1

def dfs(dept, calcur):
    global max_v, min_v

    if dept == n:
        max_v = max(max_v, calcur)
        min_v = min(min_v, calcur)
        return

    # 숫자 먼저 선택 dept , 연산자 선택 i
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            dfs(dept+1, calc(i, calcur, number[dept]))
            oper[i] += 1


dfs(1, number[0])
print(max_v, min_v)