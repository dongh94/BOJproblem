import sys
from collections import deque
sys.stdin = open("나무재테크.txt")

# 1. 나무를 심는다.
# 2. 나무의 1년 주기를 만든다.

# arrFood = 양분데이터
# arrB = 나이데이터
# newTree = 새로운 나무 데이터
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
arrFoods =[list(map(int, input().split())) for _ in range(N)]
newTrees = [list(map(int, input().split())) for _ in range(M)]
arrInitFoods = [[5]*N for _ in range(N)]
trees = []
dead = deque()


def plantTree(newTrees):
    for tree in newTrees:
        r, c, age = tree[0]-1, tree[1]-1, tree[2]
        trees.append([r, c, age])


def timeSpring():
    #나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가,
    #하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
    i = 0
    while i < len(trees):
        r = trees[i][0]
        c = trees[i][1]
        age = trees[i][2]
        if arrFoods[r][c] < age :
            dead.append(trees[i])
            trees.pop(i)
        else:
            arrFoods[r][c] -= age
            trees[i][2] += 1
            i += 1


def timeSummer():
    # 봄에 죽은 나무가 양분으로 변하게 된다
    # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
    while dead:
        tree = dead.popleft()
        r = tree[0]
        c = tree[1]
        age = tree[2]
        arrFoods[r][c] += (age // 2)

def timeAutumn():
    global trees
    babyTrees = []
    for tree in trees:
        r = tree[0]
        c = tree[1]
        age = tree[2]
        if age % 5 != 0: continue
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                babyTrees.append((r, c, 1))
    #하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
    trees = babyTrees + trees

def timeWinter():
    for r in range(N):
        for c in range(N):
            arrFoods[r][c] += arrInitFoods[r][c]

def everyYear(s, k):
    global trees
    print(trees)
    while True:
        if s == k:
            return

        timeSpring()
        timeSummer()
        timeAutumn()
        timeWinter()
        s += 1

plantTree(newTrees)
everyYear(0, K)
print(len(trees))


