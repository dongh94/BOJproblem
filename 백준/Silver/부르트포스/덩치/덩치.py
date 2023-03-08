import sys; sys.stdin=open("덩치.txt")

n = int(input())

arr = [[0,0] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr[i][0] = a
    arr[i][1] = b


for i in range(n):
    rank = 1

    for j in range(n):
        if i == j: continue;
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1

    print(rank, end=' ')