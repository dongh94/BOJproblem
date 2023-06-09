from collections import deque
import sys
sys.stdin = open("나무재테크.txt")

class Tree:
    def __init__(self, x, y, age):
        self.x = x
        self.y = y
        self.age = age

    def __str__(self):
        return (self.x, self.y, self.age)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
n, m, k = map(int, input().split())
foodStart = [[0] * (n + 1) for _ in range(n + 1)] # 처음 양분
foodInit = [[0] * (n + 1) for _ in range(n + 1)] # 추가 양분
trees = [] # 나무(나이로) 정보
dead = deque()
year = 0

for i in range(1, n + 1):
    foodInit[i] = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        foodStart[i][j] = 5

for _ in range(m):
    x, y, age = map(int, input().split())
    trees.append(Tree(x, y, age))



def simulate():
    global year, trees
    while True:
        if year == k:
            return

        # 봄
        i = 0
        while i < len(trees):
            tree = trees[i]
            r = tree.x
            c = tree.y
            age = tree.age
            if foodStart[r][c] < age:
                # 먹지 못하고 즉시 죽음
                dead.append(tree)
                trees.pop(i)
            else:
                foodStart[r][c] -= age
                tree.age += 1
                i += 1
        # 여름
        while dead:
            tree = dead.popleft()
            foodStart[tree.x][tree.y] += tree.age // 2

        # 가을
        babyTrees = []
        for tree in trees:
            r = tree.x
            c = tree.y
            if tree.age % 5 != 0:
                continue
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 1 or nc < 1 or nr > n or nc > n:
                    continue
                babyTrees.append(Tree(nr, nc, 1))
        trees = babyTrees + trees

        # 겨울
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                foodStart[i][j] += foodInit[i][j]

        year += 1



simulate()


print(len(trees))