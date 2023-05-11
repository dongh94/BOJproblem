n = 5
arr = [[0]*5 for _ in range(5)]
for r in range(n):
    for c in range(n):
        arr[r][c] = 1

print(arr)
test = [(1,2)]
for r, c in test:
    print(r, c)

arr= [[1]*n for _ in range(n)]
print(arr)